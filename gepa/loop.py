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

from dotenv import load_dotenv
import weave

load_dotenv()

# Suppress weave info logs (keep errors)
logging.getLogger("weave").setLevel(logging.ERROR)

# ART imports (for inference)
try:
    import art
    from art.serverless.backend import ServerlessBackend
    HAS_ART = True
except ImportError:
    art = None
    HAS_ART = False

from .eval import Individual, compute_pareto_fronts, select_survivors, mutate_prompt

# Artifacts directory
ARTIFACTS_DIR = Path(__file__).parent.parent / "artifacts" / "gepa"

# Base system prompt for generating pretty_midi code
BASE_PROMPT = """You are a jazz composer. Generate Python code using pretty_midi to create a 4-bar jazz composition.

Your code must:
1. Import pretty_midi
2. Create a PrettyMIDI object
3. Add instruments and notes
4. Assign the final PrettyMIDI object to a variable called `midi`

Example:
```python
import pretty_midi

midi = pretty_midi.PrettyMIDI()
piano = pretty_midi.Instrument(program=0)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=0.5))
midi.instruments.append(piano)
```

Only output Python code. No explanations."""


def execute_midi_code(code: str):
    """Execute LLM-generated code and return PrettyMIDI object."""
    import pretty_midi

    # Clean code (remove markdown fences if present)
    if "```python" in code:
        code = code.split("```python")[1].split("```")[0]
    elif "```" in code:
        code = code.split("```")[1].split("```")[0]

    # Execute in isolated namespace
    namespace = {"pretty_midi": pretty_midi}
    try:
        exec(code, namespace)
        return namespace.get("midi", None), code, None
    except Exception as e:
        return None, code, str(e)


def compute_reward(midi) -> float:
    """Dummy reward: 1.0 if MIDI has notes, -1.0 otherwise."""
    if midi is None:
        return -1.0
    total_notes = sum(len(inst.notes) for inst in midi.instruments)
    return 1.0 if total_notes > 0 else -1.0


def save_individual(individual: Individual, gen: int, midi, code: str, run_id: str, error: str = None):
    """Save individual artifacts: code, MIDI, metadata."""
    ind_dir = ARTIFACTS_DIR / run_id / f"gen_{gen:03d}" / f"ind_{individual.id:03d}"
    ind_dir.mkdir(parents=True, exist_ok=True)

    # Save code
    (ind_dir / "code.py").write_text(code)

    # Save prompt
    (ind_dir / "prompt.txt").write_text(individual.prompt)

    # Save MIDI if valid
    if midi is not None:
        midi_path = ind_dir / "output.mid"
        midi.write(str(midi_path))

    # Save metadata
    meta = {
        "id": individual.id,
        "generation": gen,
        "reward": individual.reward,
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


@weave.op
async def evaluate_individual(
    client,
    model_name: str,
    individual: Individual,
    gen: int,
    run_id: str,
    key: str = "C",
    tempo: int = 120,
) -> Individual:
    """Evaluate one individual: prompt → code → execute → reward."""

    user_prompt = f"Compose a 4-bar jazz piece in {key} at {tempo} BPM."

    try:
        completion = await client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": individual.prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_completion_tokens=1000,
            temperature=0.7,
        )
        code = completion.choices[0].message.content
        midi, cleaned_code, error = execute_midi_code(code)
        code = cleaned_code

        # Compute reward
        reward = compute_reward(midi)
        individual.reward = reward
        individual.metrics = {
            "reward": reward,
            "note_count": sum(len(inst.notes) for inst in midi.instruments) if midi else 0,
            "valid_midi": 1.0 if midi else 0.0,
        }

    except Exception as e:
        error = str(e)
        code = ""
        midi = None
        individual.reward = -1.0
        individual.metrics = {"reward": -1.0, "valid_midi": 0.0}

    # Save artifacts
    save_individual(individual, gen, midi, code, run_id, error)

    return individual


async def evolve(
    generations: int = 10,
    population_size: int = 8,
    dry_run: bool = False,
    project: str = "jazz-band-gepa",
    base_model: str = "OpenPipe/Qwen3-14B-Instruct",
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

    # Initialize weave for logging
    weave.init(project)

    # Generate unique run ID
    run_id = f"gepa_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    artifacts_path = ARTIFACTS_DIR / run_id
    artifacts_rel = f"artifacts/gepa/{run_id}"

    # Print header
    print()
    print("=" * 60)
    print(f"GEPA Evolution Run: {run_id}")
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

    # Initialize population
    population = [
        Individual(id=i, prompt=BASE_PROMPT)
        for i in range(population_size)
    ]

    # Evolution stats
    total_valid = 0
    total_evals = 0
    best_single_reward = float("-inf")

    for gen in range(generations):
        # Evaluate all individuals in parallel
        tasks = [
            evaluate_individual(client, model_name, ind, gen, run_id)
            for ind in population
        ]
        population = await asyncio.gather(*tasks)

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

            # Create next generation
            next_pop = []
            for i, survivor in enumerate(survivors):
                # Keep survivor
                child1 = Individual(id=i * 2, prompt=survivor.prompt)
                # Mutate copy (for now, just copy - mutation TODO)
                child2 = Individual(id=i * 2 + 1, prompt=mutate_prompt(survivor.prompt))
                next_pop.extend([child1, child2])

            population = next_pop[:population_size]

    # Find best MIDI
    best_midi_path = None
    for gen_dir in sorted(artifacts_path.glob("gen_*")):
        for ind_dir in sorted(gen_dir.glob("ind_*")):
            midi_file = ind_dir / "output.mid"
            if midi_file.exists():
                best_midi_path = midi_file

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

    if best_midi_path:
        print(f"\nOpening best MIDI in GarageBand...")
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
    parser.add_argument("--generations", type=int, default=10, help="Number of generations")
    parser.add_argument("--population", type=int, default=8, help="Population size")
    parser.add_argument("--dry-run", action="store_true", help="Use mock rewards")
    parser.add_argument("--project", default="jazz-band-gepa", help="W&B project")
    parser.add_argument("--base-model", default="OpenPipe/Qwen3-14B-Instruct", help="Base model")
    args = parser.parse_args()

    summary = asyncio.run(evolve(
        generations=args.generations,
        population_size=args.population,
        dry_run=args.dry_run,
        project=args.project,
        base_model=args.base_model,
    ))
    print(f"Done: {summary}")
