"""
GEPA Main Loop

Runs genetic-Pareto reflective prompt evolution across generations.
Logs everything to W&B Weave using only WANDBAPIKEY (following 2048.py pattern).
"""

import os
import sys
import random
import argparse
import asyncio
import logging
from pathlib import Path
from typing import Dict, List, Optional
from dotenv import load_dotenv

import weave
import wandb
import yaml

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from jazz_band.memory import ChemistryMemory
from jazz_band.agents.llm import init_model

from .population import Individual, Population, create_initial_population
from .evaluate import evaluate_individual, ObjectiveVector
from .pareto import compute_pareto_front, archive_elites, select_survivors
from .mutate import mutate_individual

# Suppress weave logs (following 2048.py pattern)
logging.getLogger("weave").setLevel(logging.CRITICAL)

# Load environment variables
load_dotenv()


@weave.op
async def evaluate_population(
    model,
    population: Population,
    generation: int,
    project_root: Path,
) -> Dict:
    """
    Evaluate all individuals in population.

    Args:
        model: ART model (or None for dry-run)
        population: Population to evaluate
        generation: Current generation number
        project_root: Project root path

    Returns:
        Dict with evaluation results
    """
    print(f"\n{'='*60}")
    print(f"Generation {generation}: Evaluating {len(population.individuals)} individuals")
    print(f"{'='*60}")

    # Storage for artifacts
    jam_jsons = {}
    memories = {}
    critiques = {}

    # Evaluate each individual
    for i, individual in enumerate(population.individuals):
        print(f"\n[{i+1}/{len(population.individuals)}] Evaluating individual {individual.id}...")

        # Create fresh memory for this individual
        memory = ChemistryMemory()

        # Set up jam state
        jam_state = {
            "key": "C",
            "tempo": 120,
            "time_sig": "4/4",
            "last_n_bars": [],
            "form_position": "opening",
        }

        # Evaluate
        try:
            jam_json, objectives, critique = await evaluate_individual(
                model=model,
                individual_prompt=individual.prompt_text,
                individual_genes=individual.genes.to_dict(),
                jam_state=jam_state,
                memory=memory,
                bars_to_generate=8,  # Reduced from 16 based on user feedback
            )

            # Store objectives
            individual.objectives = objectives.to_list()

            # Store artifacts
            jam_jsons[individual.id] = jam_json
            memories[individual.id] = memory
            critiques[individual.id] = critique

            # Print summary
            print(f"  Objectives: {objectives.to_dict()}")
            print(f"  Judge Score: {objectives.judge_score:.2f}/10")

        except Exception as e:
            print(f"  ERROR evaluating individual {individual.id}: {e}")
            # Assign poor objectives
            individual.objectives = [0.0] * 6

    # Calculate population statistics for logging
    valid_individuals = [ind for ind in population.individuals if ind.objectives is not None]
    stats = {}
    if valid_individuals:
        # Extract objectives (assuming index 5 is judge_score normalized to 0-1)
        judge_scores = [ind.objectives[5] * 10 for ind in valid_individuals if len(ind.objectives) > 5]
        groove_scores = [ind.objectives[0] for ind in valid_individuals if len(ind.objectives) > 0]

        if judge_scores:
            stats["avg_judge_score"] = sum(judge_scores) / len(judge_scores)
            stats["max_judge_score"] = max(judge_scores)
            stats["min_judge_score"] = min(judge_scores)

        if groove_scores:
            stats["avg_groove_alignment"] = sum(groove_scores) / len(groove_scores)
            stats["max_groove_alignment"] = max(groove_scores)

    print()
    return {
        "jam_jsons": jam_jsons,
        "memories": memories,
        "critiques": critiques,
        "stats": stats,
    }


@weave.op
async def evolve_generation(
    model,
    population: Population,
    generation: int,
    project_root: Path,
    archive_dir: Path,
    schema_path: Path,
    mutation_rate: float = 0.8,
) -> Population:
    """
    Run one generation of evolution.

    Args:
        model: ART model (or None for dry-run)
        population: Current population
        generation: Generation number
        project_root: Project root path
        archive_dir: Elite archive directory
        schema_path: Path to genes_schema.yaml
        mutation_rate: Mutation rate

    Returns:
        Tuple of (new population for next generation, Pareto fronts of evaluated population)
    """
    # Step 1: Evaluate population
    eval_results = await evaluate_population(model, population, generation, project_root)

    # Step 2: Compute Pareto fronts
    print(f"Computing Pareto fronts...")
    fronts = compute_pareto_front(population.individuals)

    print(f"  Front sizes: {[len(f) for f in fronts]}")
    print(f"  First front ({len(fronts[0])} individuals):")
    for ind in fronts[0]:
        obj_str = ", ".join([f"{o:.3f}" for o in ind.objectives[:5]])  # First 5 objs
        print(f"    Ind {ind.id}: [{obj_str}, J={ind.objectives[5]*10:.1f}]")

    # Step 3: Archive elites
    print(f"\nArchiving top elites...")
    archive_elites(
        individuals=population.individuals,
        generation=generation,
        archive_dir=archive_dir,
        top_k=3,
        jam_jsons=eval_results["jam_jsons"],
        memories=eval_results["memories"],
        critiques=eval_results["critiques"],
    )

    # Step 4: Select survivors
    print(f"\nSelecting survivors for next generation...")
    survivors = select_survivors(population.individuals, target_size=population.size)
    print(f"  Selected {len(survivors)} survivors (target: {population.size})")

    # Step 5: Mutate to create next generation
    print(f"\nMutating survivors...")
    next_generation = []

    for ind in survivors:
        # Get critique if available
        critique = eval_results["critiques"].get(ind.id)

        # Mutate
        use_reflective = random.random() < 0.5  # 50% chance of reflective mutation
        mutated = mutate_individual(
            individual=ind,
            schema_path=schema_path,
            critique=critique,
            use_reflective=use_reflective,
            mutation_rate=mutation_rate,
        )

        next_generation.append(mutated)

    # Create new population
    new_pop = Population(population.population_dir, schema_path, size=population.size)
    new_pop.replace_with(next_generation)

    print(f"  Created {len(next_generation)} individuals for generation {generation+1}")

    return new_pop, fronts, eval_results


@weave.op
async def run_gepa(
    project_root: Path,
    generations: int = 10,
    population_size: int = 8,
    seed: Optional[int] = None,
    dry_run: bool = True,
    mutation_rate: float = 0.8,
    enable_early_stopping: bool = True,
) -> Dict:
    """
    Main GEPA loop.

    Args:
        project_root: Project root directory
        generations: Number of generations to run
        population_size: Population size
        seed: Random seed for reproducibility
        dry_run: If True, use dry-run mode (no LLM)
        mutation_rate: Mutation rate (0.0 to 1.0)
        enable_early_stopping: If True, stop early if judge score < 6.0 after gen 10

    Returns:
        Results dictionary with metrics and artifacts
    """
    print("=" * 60)
    print("GEPA - Genetic-Pareto Reflective Prompt Evolution")
    print("=" * 60)
    print(f"Generations: {generations}")
    print(f"Population Size: {population_size}")
    print(f"Seed: {seed}")
    print(f"Mode: {'DRY-RUN' if dry_run else 'LLM-ENABLED'}")
    print(f"Mutation Rate: {mutation_rate}")
    print(f"Early Stopping: {'ENABLED' if enable_early_stopping else 'DISABLED'}")
    print()

    # Set seed
    if seed is not None:
        random.seed(seed)

    # Initialize ART model (following 2048.py pattern)
    # Initialize wandb for tracking
    wandb.init(
        project="jazz-band-gepa",
        config={
            "generations": generations,
            "population_size": population_size,
            "seed": seed,
            "mutation_rate": mutation_rate,
            "mode": "dry-run" if dry_run else "llm",
        },
        tags=["gepa", "progressive-arrangement", "5-part-ensemble"],
    )

    print("Initializing model...")
    if dry_run:
        model = None
        print("  Using dry-run mode (no LLM)")
    else:
        model = await init_model(
            project="jazz-band-gepa",
            model_name="gepa-composer-001",
            dry_run=False
        )
        print(f"  Model initialized: {model.get_inference_name()}")
    print()

    # Create directories
    archive_dir = project_root / "artifacts" / "elites"
    archive_dir.mkdir(parents=True, exist_ok=True)

    schema_path = project_root / "gepa" / "genes_schema.yaml"

    # Initialize population
    print("Creating initial population...")
    population = create_initial_population(
        project_root=project_root,
        population_size=population_size,
        seed=seed,
    )
    print(f"  Created {len(population.individuals)} individuals")
    print()

    # Evolution loop
    results = {
        "generations": [],
        "population_size": population_size,
        "seed": seed,
        "mutation_rate": mutation_rate,
    }

    for gen in range(generations):
        print(f"\n{'#'*60}")
        print(f"# Generation {gen}/{generations-1}")
        print(f"{'#'*60}\n")

        # Evolve (returns new population, evaluated fronts, and eval results)
        population, fronts, eval_results = await evolve_generation(
            model=model,
            population=population,
            generation=gen,
            project_root=project_root,
            archive_dir=archive_dir,
            schema_path=schema_path,
            mutation_rate=mutation_rate,
        )

        # Record generation metrics
        gen_metrics = {
            "generation": gen,
            "front_sizes": [],
            "best_objectives": None,
        }

        # Use the evaluated fronts returned from evolve_generation
        gen_metrics["front_sizes"] = [len(f) for f in fronts]

        if len(fronts) > 0 and len(fronts[0]) > 0:
            best_ind = fronts[0][0]
            gen_metrics["best_objectives"] = best_ind.objectives

        results["generations"].append(gen_metrics)

        # Log to wandb
        log_dict = {
            "generation": gen,
            "front_sizes": len(fronts[0]) if len(fronts) > 0 else 0,
        }

        # Add stats from evaluation
        eval_stats = eval_results.get("stats", {})
        log_dict.update(eval_stats)

        # Log best individual objectives if available
        if len(fronts) > 0 and len(fronts[0]) > 0:
            best_ind = fronts[0][0]
            if best_ind.objectives and len(best_ind.objectives) > 5:
                log_dict["best_groove_alignment"] = best_ind.objectives[0]
                log_dict["best_judge_score"] = best_ind.objectives[5] * 10

                # Log MIDI of best individual
                best_midi_path = archive_dir / f"gen_{gen:03d}_ind_{best_ind.id:04d}" / "jam.mid"
                if best_midi_path.exists():
                    wandb.log({
                        **log_dict,
                        "best_midi": wandb.Audio(str(best_midi_path), sample_rate=44100)
                    })
                else:
                    wandb.log(log_dict)
            else:
                wandb.log(log_dict)
        else:
            wandb.log(log_dict)

        print(f"\nGeneration {gen} complete!")
        print(f"  Front sizes: {gen_metrics['front_sizes']}")

        # Early stopping: If after Gen 10, best judge score is < 6.0, stop evolution
        if enable_early_stopping and gen >= 10 and len(fronts) > 0 and len(fronts[0]) > 0:
            # Filter out individuals with None objectives
            valid_individuals = [ind for ind in fronts[0] if ind.objectives is not None and len(ind.objectives) > 5]
            if len(valid_individuals) > 0:
                best_judge_score = max(ind.objectives[5] for ind in valid_individuals) * 10  # Index 5 is judge_score (normalized to 0-1)
                print(f"  Best Judge Score: {best_judge_score:.1f}/10")
                if best_judge_score < 6.0:
                    print(f"\n{'!'*60}")
                    print(f"! EARLY STOPPING: Gen {gen} best score ({best_judge_score:.1f}/10) < 6.0")
                    print(f"! No significant improvement after Gen 10 - halting evolution")
                    print(f"{'!'*60}\n")
                    break

    print("\n" + "="*60)
    print("GEPA Evolution Complete!")
    print("="*60)
    print(f"Ran {generations} generations with population size {population_size}")
    print(f"Elites archived to: {archive_dir}")
    print()

    # Finish wandb run
    wandb.finish()

    return results


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="GEPA - Genetic-Pareto Prompt Evolution")
    parser.add_argument("--generations", "-g", type=int, default=10, help="Number of generations")
    parser.add_argument("--population-size", "-p", type=int, default=8, help="Population size")
    parser.add_argument("--seed", "-s", type=int, default=None, help="Random seed")
    parser.add_argument("--dry-run", action="store_true", help="Use dry-run mode (no LLM)")
    parser.add_argument("--use-llm", action="store_true", help="Enable LLM mode (requires WANDB_API_KEY)")
    parser.add_argument("--mutation-rate", "-m", type=float, default=0.8, help="Mutation rate (0.0-1.0)")
    parser.add_argument("--no-early-stopping", action="store_true", help="Disable early stopping (run all generations)")

    args = parser.parse_args()

    # Determine mode
    if args.use_llm:
        dry_run = False
        # Validate API key (following 2048.py pattern)
        if not (os.environ.get("WANDB_API_KEY") or os.environ.get("WANDBAPIKEY")):
            print("ERROR: WANDB_API_KEY required for --use-llm mode")
            print("Set it in .env file or environment, or use --dry-run mode")
            sys.exit(1)
    else:
        dry_run = True

    # Initialize Weave (following 2048.py pattern)
    api_key = os.environ.get("WANDB_API_KEY") or os.environ.get("WANDBAPIKEY", "")
    os.environ["WANDB_API_KEY"] = api_key
    weave.init("jazz-band-gepa")

    # Get project root
    project_root = Path(__file__).parent.parent

    # Run GEPA
    result = asyncio.run(run_gepa(
        project_root=project_root,
        generations=args.generations,
        population_size=args.population_size,
        seed=args.seed,
        dry_run=dry_run,
        mutation_rate=args.mutation_rate,
        enable_early_stopping=not args.no_early_stopping,
    ))

    print("\nResults summary:")
    print(f"  Total generations: {len(result['generations'])}")
    print(f"  Final front sizes: {result['generations'][-1]['front_sizes'] if result['generations'] else 'N/A'}")
    print()

    sys.exit(0)


if __name__ == "__main__":
    main()
