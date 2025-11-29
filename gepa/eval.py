"""
GEPA Evaluation: Pareto selection for multi-objective optimization.
"""

from typing import Dict, List
from dataclasses import dataclass, field


@dataclass
class Individual:
    """An individual in the population."""
    id: int
    prompt: str
    reward: float = 0.0
    metrics: Dict[str, float] = field(default_factory=dict)


def dominates(a: Individual, b: Individual) -> bool:
    """True if a dominates b (a >= b on all objectives, a > b on at least one)."""
    dominated = False
    for key in a.metrics:
        if key not in b.metrics:
            continue
        if a.metrics[key] < b.metrics[key]:
            return False
        if a.metrics[key] > b.metrics[key]:
            dominated = True
    return dominated


def compute_pareto_fronts(population: List[Individual]) -> List[List[Individual]]:
    """
    Compute Pareto fronts using non-dominated sorting.

    Returns list of fronts, where front[0] is the Pareto-optimal set.
    """
    remaining = list(population)
    fronts = []

    while remaining:
        front = []
        for ind in remaining:
            is_dominated = False
            for other in remaining:
                if other is not ind and dominates(other, ind):
                    is_dominated = True
                    break
            if not is_dominated:
                front.append(ind)

        fronts.append(front)
        remaining = [ind for ind in remaining if ind not in front]

    return fronts


def select_survivors(population: List[Individual], target_size: int) -> List[Individual]:
    """
    Select survivors using NSGA-II style selection.
    Fill from front 0, then front 1, etc. until target_size reached.
    """
    fronts = compute_pareto_fronts(population)
    survivors = []

    for front in fronts:
        if len(survivors) + len(front) <= target_size:
            survivors.extend(front)
        else:
            # Partial front - just take first N needed
            needed = target_size - len(survivors)
            survivors.extend(front[:needed])
            break

    return survivors


def mutate_prompt(prompt: str, feedback: str = None) -> str:
    """
    Mutate prompt based on feedback.

    TODO: Implement LLM-based reflection/mutation.
    For now, returns prompt unchanged.
    """
    return prompt
