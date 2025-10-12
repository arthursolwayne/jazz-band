"""
Pareto Optimization Utilities

Implements non-dominated sorting (NSGA-II style) and elite archiving.
All objectives are maximized (higher is better).
"""

import json
import yaml
import shutil
from pathlib import Path
from typing import List, Tuple, Dict, Any
from .population import Individual


def dominates(obj1: List[float], obj2: List[float]) -> bool:
    """
    Check if obj1 Pareto-dominates obj2 (maximization).

    Args:
        obj1: Objective vector 1
        obj2: Objective vector 2

    Returns:
        True if obj1 dominates obj2
    """
    # obj1 dominates obj2 if:
    # - obj1 >= obj2 for all objectives
    # - obj1 > obj2 for at least one objective

    at_least_one_better = False
    for v1, v2 in zip(obj1, obj2):
        if v1 < v2:
            return False  # obj1 worse in this objective
        if v1 > v2:
            at_least_one_better = True

    return at_least_one_better


def fast_non_dominated_sort(individuals: List[Individual]) -> List[List[Individual]]:
    """
    Fast non-dominated sorting (NSGA-II algorithm).

    Args:
        individuals: List of individuals with objectives

    Returns:
        List of fronts (each front is a list of individuals)
    """
    # Track domination relationships
    domination_count = {ind.id: 0 for ind in individuals}  # how many dominate this individual
    dominated_by = {ind.id: [] for ind in individuals}  # which individuals this one dominates

    fronts = [[]]

    for i, ind_p in enumerate(individuals):
        for ind_q in individuals[i+1:]:
            if ind_p.objectives is None or ind_q.objectives is None:
                continue

            if dominates(ind_p.objectives, ind_q.objectives):
                dominated_by[ind_p.id].append(ind_q)
                domination_count[ind_q.id] += 1
            elif dominates(ind_q.objectives, ind_p.objectives):
                dominated_by[ind_q.id].append(ind_p)
                domination_count[ind_p.id] += 1

    # First front: individuals with domination count = 0
    for ind in individuals:
        if domination_count[ind.id] == 0:
            ind.rank = 0
            fronts[0].append(ind)

    # Subsequent fronts
    current_front = 0
    while len(fronts[current_front]) > 0:
        next_front = []
        for ind_p in fronts[current_front]:
            for ind_q in dominated_by[ind_p.id]:
                domination_count[ind_q.id] -= 1
                if domination_count[ind_q.id] == 0:
                    ind_q.rank = current_front + 1
                    next_front.append(ind_q)
        current_front += 1
        fronts.append(next_front)

    # Remove empty last front
    if len(fronts[-1]) == 0:
        fronts.pop()

    return fronts


def compute_crowding_distance(individuals: List[Individual]) -> None:
    """
    Compute crowding distance for individuals in the same front.
    Modifies individuals in-place.

    Args:
        individuals: List of individuals in the same front
    """
    n = len(individuals)
    if n == 0:
        return

    # Number of objectives
    n_obj = len(individuals[0].objectives) if individuals[0].objectives else 0

    # Initialize distances
    for ind in individuals:
        ind.crowding_distance = 0.0

    # For each objective
    for obj_idx in range(n_obj):
        # Sort by this objective
        individuals.sort(key=lambda ind: ind.objectives[obj_idx])

        # Boundary points get infinite distance
        individuals[0].crowding_distance = float('inf')
        individuals[-1].crowding_distance = float('inf')

        # Compute range
        obj_range = individuals[-1].objectives[obj_idx] - individuals[0].objectives[obj_idx]
        if obj_range == 0:
            continue

        # Compute distance for interior points
        for i in range(1, n - 1):
            distance_contrib = (individuals[i+1].objectives[obj_idx] - individuals[i-1].objectives[obj_idx]) / obj_range
            individuals[i].crowding_distance += distance_contrib


def compute_pareto_front(individuals: List[Individual]) -> List[List[Individual]]:
    """
    Compute Pareto fronts and assign ranks + crowding distances.

    Args:
        individuals: List of individuals to process

    Returns:
        List of fronts (sorted by rank)
    """
    fronts = fast_non_dominated_sort(individuals)

    # Compute crowding distance within each front
    for front in fronts:
        compute_crowding_distance(front)

    return fronts


def archive_elites(
    individuals: List[Individual],
    generation: int,
    archive_dir: Path,
    top_k: int = 3,
    jam_jsons: Dict[int, Dict] = None,
    memories: Dict[int, Any] = None,
    critiques: Dict[int, Dict] = None,
) -> None:
    """
    Archive top-k elite individuals with all artifacts.

    Args:
        individuals: List of individuals to consider
        generation: Current generation number
        archive_dir: Base archive directory (e.g., artifacts/elites/)
        top_k: Number of elites to archive
        jam_jsons: Dict mapping individual ID to JamJSON
        memories: Dict mapping individual ID to ChemistryMemory
        critiques: Dict mapping individual ID to critique result
    """
    # Sort by rank then crowding distance
    sorted_inds = sorted(
        individuals,
        key=lambda ind: (ind.rank if ind.rank is not None else float('inf'), -ind.crowding_distance)
    )

    elites = sorted_inds[:top_k]

    for elite in elites:
        # Create archive subdirectory
        elite_dir = archive_dir / f"gen_{generation:03d}_ind_{elite.id:04d}"
        elite_dir.mkdir(parents=True, exist_ok=True)

        # Save prompt and genes
        elite.save(elite_dir)

        # Save metrics
        metrics = {
            "generation": generation,
            "individual_id": elite.id,
            "rank": elite.rank,
            "crowding_distance": elite.crowding_distance,
            "objectives": {
                "consonance": elite.objectives[0] if elite.objectives else None,
                "groove_alignment": elite.objectives[1] if elite.objectives else None,
                "motif_coherence": elite.objectives[2] if elite.objectives else None,
                "interplay": elite.objectives[3] if elite.objectives else None,
                "density_regularity": elite.objectives[4] if elite.objectives else None,
                "judge_score": elite.objectives[5] * 10.0 if elite.objectives else None,  # Denormalize
            }
        }

        metrics_path = elite_dir / "metrics.json"
        with open(metrics_path, 'w') as f:
            json.dump(metrics, f, indent=2)

        # Save JamJSON if provided
        if jam_jsons and elite.id in jam_jsons:
            jam_path = elite_dir / "jam.json"
            with open(jam_path, 'w') as f:
                json.dump(jam_jsons[elite.id], f, indent=2)

            # Also export MIDI (requires ScoreBuilder)
            import sys
            from pathlib import Path as _Path
            sys.path.insert(0, str(_Path(__file__).parent.parent / "src"))
            from jazz_band.score_builder import ScoreBuilder

            builder = ScoreBuilder()
            score = builder.from_jam_json(jam_jsons[elite.id])
            midi_path = elite_dir / "jam.mid"
            builder.export_midi(score, midi_path)

        # Save memory if provided
        if memories and elite.id in memories:
            memory_path = elite_dir / "memory.json"
            memories[elite.id].save(memory_path)

        # Save critique if provided
        if critiques and elite.id in critiques:
            critique_path = elite_dir / "critique.json"
            with open(critique_path, 'w') as f:
                json.dump(critiques[elite.id], f, indent=2)


def select_survivors(
    individuals: List[Individual],
    target_size: int,
) -> List[Individual]:
    """
    Select survivors for next generation using Pareto rank + crowding distance.

    Args:
        individuals: Current population
        target_size: Target population size

    Returns:
        Selected individuals
    """
    # Compute fronts
    fronts = compute_pareto_front(individuals)

    survivors = []
    for front in fronts:
        if len(survivors) + len(front) <= target_size:
            # Add entire front
            survivors.extend(front)
        else:
            # Sort front by crowding distance (descending)
            front.sort(key=lambda ind: -ind.crowding_distance)
            # Add best from front until target size
            remaining = target_size - len(survivors)
            survivors.extend(front[:remaining])
            break

    return survivors
