"""
GEPA Evolution Loop

Rollout → metrics → Pareto select → mutate prompt.
"""

import os
import json
import asyncio
import random
import logging
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict, List
from datetime import datetime

from tqdm.asyncio import tqdm_asyncio

from dotenv import load_dotenv

load_dotenv()

# ART imports (for inference)
try:
    import art
    from art.serverless.backend import ServerlessBackend
    HAS_ART = True
except ImportError:
    art = None
    HAS_ART = False

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from .pareto import Individual, compute_pareto_fronts, select_survivors, mutate_prompt
from jazz_band.symbol_engine import (
    SYSTEM_PROMPT as BASE_PROMPT,
    execute_midi_code,
    compute_reward_breakdown,
    get_sax_notes,
    unique_durations,
    has_rests,
)

# Jazz keys from reference standards
JAZZ_KEYS = ["Dm", "Fm", "F", "D"]

# Artifacts directory
ARTIFACTS_DIR = Path(__file__).parent.parent / "artifacts" / "gepa"


def sanitize_midi(midi):
    """Ensure all MIDI note pitches and velocities are integers."""
    if midi is None:
        return None
    for inst in midi.instruments:
        for note in inst.notes:
            note.pitch = int(note.pitch)
            note.velocity = int(note.velocity)
    return midi


def save_individual(individual: Individual, gen: int, midi, code: str, run_id: str, breakdown: dict = None, error: str = None):
    """Save individual artifacts: code, MIDI, metadata."""
    ind_dir = ARTIFACTS_DIR / run_id / f"gen_{gen:03d}" / f"ind_{individual.id:03d}"
    ind_dir.mkdir(parents=True, exist_ok=True)

    # Save code
    (ind_dir / "code.py").write_text(code)

    # Save prompt
    (ind_dir / "prompt.txt").write_text(individual.prompt)

    # Save MIDI if valid (sanitize to ensure int values)
    if midi is not None:
        midi_path = ind_dir / "output.mid"
        sanitize_midi(midi)
        midi.write(str(midi_path))

    # Save metadata with per-instrument breakdown
    meta = {
        "id": individual.id,
        "generation": gen,
        "reward": individual.reward,
        "breakdown": breakdown,
        "metrics": individual.metrics,
        "has_midi": midi is not None,
        "error": error,
        "timestamp": datetime.now().isoformat(),
    }
    (ind_dir / "meta.json").write_text(json.dumps(meta, indent=2))

    return ind_dir


def open_midi_in_garageband(midi_path: Path):
    """Open MIDI file in GarageBand (macOS)."""
    subprocess.run(["open", "-a", "GarageBand", str(midi_path)])


async def evaluate_individual(
    client,
    model_name: str,
    individual: Individual,
    gen: int,
    run_id: str,
    key: str = "C",
    tempo: int = 160,  # Must match composer.md timing
) -> Individual:
    """Evaluate one individual: prompt → code → execute → reward."""

    user_prompt = f"Compose a 4-bar jazz piece in {key} at {tempo} BPM."

    breakdown = None
    try:
        completion = await client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": individual.prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_completion_tokens=12000,
            temperature=0.75,
        )
        code = completion.choices[0].message.content
        midi, cleaned_code, error = execute_midi_code(code)
        code = cleaned_code

        # Compute reward breakdown (all instruments)
        breakdown = compute_reward_breakdown(midi) if midi else None
        reward = breakdown["combined"] if breakdown else 0.0
        individual.reward = reward

        # Extract trace info for reflection
        sax_notes = get_sax_notes(midi) if midi else []
        ud = unique_durations(sax_notes)
        hr = has_rests(sax_notes)

        # Per-instrument scores for Pareto selection
        individual.metrics = {
            "sax": breakdown.get("sax_sig", 0) if breakdown else 0,
            "bass": breakdown.get("bass_sig", 0) if breakdown else 0,
            "piano": breakdown.get("piano_sig", 0) if breakdown else 0,
            "drums": breakdown.get("drums_sig", 0) if breakdown else 0,
            "valid_midi": 1.0 if midi else 0.0,
        }

        # Rich trace for reflective mutation - include per-instrument breakdown
        individual.traces.append({
            "reward": reward,
            "sax": breakdown.get("sax_sig", 0) if breakdown else 0,
            "bass": breakdown.get("bass_sig", 0) if breakdown else 0,
            "piano": breakdown.get("piano_sig", 0) if breakdown else 0,
            "drums": breakdown.get("drums_sig", 0) if breakdown else 0,
            "unique_durs": ud,
            "has_rests": hr,
            "error": error,
            "code": code,
        })

    except Exception as e:
        error = str(e)
        midi = None
        individual.reward = 0.0  # was -1.0
        individual.metrics = {"reward": 0.0, "valid_midi": 0.0}
        individual.traces.append({
            "reward": 0.0,
            "unique_durs": 0,
            "has_rests": False,
            "error": error,
            "code": code if code else "",
        })

    # Save artifacts
    save_individual(individual, gen, midi, code, run_id, breakdown, error)

    return individual


def load_population_from_run(run_id: str, population_size: int) -> tuple[List[Individual], int]:
    """Load population state from a previous run's last generation."""
    run_dir = ARTIFACTS_DIR / run_id
    if not run_dir.exists():
        raise ValueError(f"Run directory not found: {run_dir}")

    # Find the last generation
    gen_dirs = sorted(run_dir.glob("gen_*"))
    if not gen_dirs:
        raise ValueError(f"No generations found in {run_dir}")

    last_gen_dir = gen_dirs[-1]
    last_gen = int(last_gen_dir.name.split("_")[1])

    # Load individuals from last generation
    population = []
    for ind_dir in sorted(last_gen_dir.glob("ind_*")):
        prompt_file = ind_dir / "prompt.txt"
        meta_file = ind_dir / "meta.json"

        if prompt_file.exists() and meta_file.exists():
            prompt = prompt_file.read_text()
            meta = json.loads(meta_file.read_text())
            ind = Individual(
                id=meta["id"],
                prompt=prompt,
                reward=meta.get("reward", 0.0),
                metrics=meta.get("metrics", {}),
            )
            population.append(ind)

    # Pad if needed
    while len(population) < population_size:
        population.append(Individual(id=len(population), prompt=BASE_PROMPT))

    return population[:population_size], last_gen + 1


async def evolve(
    generations: int = 10,
    population_size: int = 8,
    dry_run: bool = False,
    project: str = "jazz-band-gepa",
    base_model: str = "OpenPipe/Qwen3-14B-Instruct",
    resume: str = None,  # Pass run_id to resume
) -> Dict:
    """
    Main evolution loop.
    """
    if dry_run:
        # Dry-run: mock rewards
        best_reward = float("-inf")
        for gen in range(generations):
            rewards = [random.choice([-1.0, 1.0]) for _ in range(population_size)]
            avg_reward = sum(rewards) / len(rewards)
            if max(rewards) > best_reward:
                best_reward = max(rewards)
            print(f"Gen {gen}: avg_reward={avg_reward:.3f}")
        return {"generations": generations, "best_reward": best_reward}

    # Real evolution with LLM
    if not HAS_ART:
        raise ImportError("openpipe-art required. Install with: pip install openpipe-art")

    # Set API key
    api_key = os.environ.get("WANDB_API_KEY") or os.environ.get("WANDBAPIKEY")
    if not api_key:
        raise ValueError("WANDB_API_KEY or WANDBAPIKEY required")
    os.environ["WANDB_API_KEY"] = api_key

    # Resume existing run or create new one
    if resume:
        run_id = resume
        population, start_gen = load_population_from_run(resume, population_size)
    else:
        run_id = f"gepa_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        population = [Individual(id=i, prompt=BASE_PROMPT) for i in range(population_size)]
        start_gen = 0

    artifacts_path = ARTIFACTS_DIR / run_id
    artifacts_rel = f"artifacts/gepa/{run_id}"

    # Print header
    print()
    print("=" * 60)
    print(f"GEPA Evolution Run: {run_id}")
    if resume:
        print(f"  (Resuming from generation {start_gen})")
    print("=" * 60)
    print(f"  Base model:   {base_model}")
    print(f"  Generations:  {generations}")
    print(f"  Population:   {population_size}")
    print(f"  Artifacts:    {artifacts_rel}")
    print("=" * 60)
    print()

    # Initialize model for inference (use TrainableModel but skip training)
    model = art.TrainableModel(
        name=run_id,
        project=project,
        base_model=base_model,
    )

    backend = ServerlessBackend()
    await model.register(backend)

    from openai import AsyncOpenAI
    client = AsyncOpenAI(
        base_url=model.inference_base_url,
        api_key=model.inference_api_key,
    )
    model_name = model.get_inference_name()

    # Evolution stats
    total_valid = 0
    total_evals = 0
    best_single_reward = float("-inf")

    for gen in range(start_gen, generations):
        # Evaluate all individuals in parallel (random key per individual)
        tasks = [
            evaluate_individual(client, model_name, ind, gen, run_id, key=random.choice(JAZZ_KEYS))
            for ind in population
        ]
        population = await tqdm_asyncio.gather(*tasks, desc=f"Gen {gen}/{generations}")

        # Stats
        gen_rewards = [ind.reward for ind in population]
        gen_valid = sum(1 for ind in population if ind.metrics.get("valid_midi", 0) > 0)
        total_valid += gen_valid
        total_evals += len(population)

        if max(gen_rewards) > best_single_reward:
            best_single_reward = max(gen_rewards)

        avg_reward = sum(gen_rewards) / len(gen_rewards)
        print(f"  Gen {gen}: reward={avg_reward:+.2f}  valid={gen_valid}/{len(population)}")

        # Selection + mutation for next generation (skip on last gen)
        if gen < generations - 1:
            survivors = select_survivors(population, population_size // 2)

            # Create next generation with acceptance-gated mutation
            # Like GEPA-Lite: mutant must produce valid MIDI and not regress to be accepted
            next_pop = []
            accepted_mutations = 0
            rejected_mutations = 0

            for i, survivor in enumerate(survivors):
                # Keep survivor as child1 (inherits traces)
                child1 = Individual(id=i * 2, prompt=survivor.prompt, traces=survivor.traces.copy())
                next_pop.append(child1)

                # Create mutant candidate for child2
                mutated_prompt = await mutate_prompt(client, model_name, survivor.prompt, survivor.traces)
                mutant = Individual(id=i * 2 + 1, prompt=mutated_prompt, traces=survivor.traces.copy())

                # Evaluate mutant to check acceptance (save to gen+1 since it's for next gen)
                mutant = await evaluate_individual(
                    client, model_name, mutant, gen + 1, run_id,
                    key=random.choice(JAZZ_KEYS)
                )

                # Relaxed acceptance: Pareto-based, not scalar reward
                # Accept if mutant is valid, OR with 30% exploration chance
                mutant_valid = mutant.metrics.get("valid_midi", 0) > 0

                # Check Pareto improvement (better on any objective without being worse on all)
                def pareto_dominated(a_metrics, b_metrics):
                    dominated = False
                    for key in ["sax", "bass", "piano", "drums"]:
                        if a_metrics.get(key, 0) < b_metrics.get(key, 0):
                            return False
                        if a_metrics.get(key, 0) > b_metrics.get(key, 0):
                            dominated = True
                    return dominated

                mutant_dominates = pareto_dominated(mutant.metrics, survivor.metrics)
                explore_accept = random.random() < 0.3  # 30% exploration

                if mutant_valid and mutant_dominates:
                    # Pareto improvement - accept
                    child2 = mutant
                    accepted_mutations += 1
                elif mutant_valid and explore_accept:
                    # Valid but not dominant - accept for diversity
                    child2 = mutant
                    accepted_mutations += 1
                elif explore_accept:
                    # Even invalid - accept for exploration (30% chance)
                    child2 = mutant
                    accepted_mutations += 1
                else:
                    # Reject - keep parent
                    child2 = Individual(id=i * 2 + 1, prompt=survivor.prompt, traces=survivor.traces.copy())
                    rejected_mutations += 1

                next_pop.append(child2)

            print(f"         mutations: {accepted_mutations} accepted, {rejected_mutations} rejected")
            population = next_pop[:population_size]

    # Find best MIDI by reward (scan meta.json files)
    best_midi_path = None
    best_midi_reward = float("-inf")
    best_midi_meta = None
    for gen_dir in sorted(artifacts_path.glob("gen_*")):
        for ind_dir in sorted(gen_dir.glob("ind_*")):
            midi_file = ind_dir / "output.mid"
            meta_file = ind_dir / "meta.json"
            if midi_file.exists() and meta_file.exists():
                meta = json.loads(meta_file.read_text())
                if meta.get("reward", 0) > best_midi_reward:
                    best_midi_reward = meta["reward"]
                    best_midi_path = midi_file
                    best_midi_meta = meta

    # Print final summary
    print()
    print("=" * 60)
    print("Evolution Complete")
    print("=" * 60)
    print(f"  Generations:        {generations}")
    print(f"  Total evaluations:  {total_evals}")
    print(f"  Valid MIDIs:        {total_valid}/{total_evals} ({100*total_valid/total_evals:.0f}%)")
    print(f"  Best single reward: {best_single_reward:+.2f}")
    print(f"  Artifacts:          {artifacts_rel}")
    print("=" * 60)

    if best_midi_path and best_midi_meta:
        print(f"\n  Best MIDI:")
        print(f"    Path:       {best_midi_path.relative_to(artifacts_path.parent.parent)}")
        print(f"    Reward:     {best_midi_meta['reward']:.3f}")
        print(f"    Generation: {best_midi_meta.get('generation', '?')}")
        print(f"    Individual: {best_midi_meta.get('id', '?')}")
        bd = best_midi_meta.get("breakdown")
        if bd:
            print(f"    ───────────────────────────")
            print(f"              z-score   sigmoid")
            print(f"    Sax:      {bd.get('sax', 0):+6.2f}    {bd.get('sax_sig', 0):.3f}")
            print(f"    Bass:     {bd.get('bass', 0):+6.2f}    {bd.get('bass_sig', 0):.3f}")
            print(f"    Piano:    {bd.get('piano', 0):+6.2f}    {bd.get('piano_sig', 0):.3f}")
            print(f"    Drums:    {bd.get('drums', 0):+6.2f}    {bd.get('drums_sig', 0):.3f}")
            print(f"    Ensemble: {bd.get('ensemble', 0):+6.2f}    {bd.get('ensemble_sig', 0):.3f}")
            print(f"    ───────────────────────────")
            print(f"    Total:    {bd.get('z_sum', 0):+6.2f}    {bd.get('combined', 0):.3f}")
        print(f"\nOpening in GarageBand...")
        open_midi_in_garageband(best_midi_path)
    print()

    return {
        "generations": generations,
        "total_evals": total_evals,
        "total_valid": total_valid,
        "best_reward": best_single_reward,
        "run_id": run_id,
    }


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="GEPA Evolution")
    parser.add_argument("--generations", type=int, default=20, help="Number of generations")
    parser.add_argument("--population", type=int, default=24, help="Population size")
    parser.add_argument("--dry-run", action="store_true", help="Use mock rewards")
    parser.add_argument("--project", default="jazz-band-gepa", help="W&B project")
    parser.add_argument("--base-model", default="OpenPipe/Qwen3-14B-Instruct", help="Base model")
    parser.add_argument("--resume", type=str, default=None, help="Run ID to resume")
    args = parser.parse_args()

    summary = asyncio.run(evolve(
        generations=args.generations,
        population_size=args.population,
        dry_run=args.dry_run,
        project=args.project,
        base_model=args.base_model,
        resume=args.resume,
    ))
    print(f"Done: {summary}")
