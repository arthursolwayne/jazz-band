"""
GEPA Evaluation: Metrics → Pareto selection.
"""

from typing import Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    import pretty_midi


def dominates(a: List[float], b: List[float]) -> bool:
    """True if a dominates b (a >= b on all, a > b on at least one)."""
    dominated = False
    for ai, bi in zip(a, b):
        if ai < bi:
            return False
        if ai > bi:
            dominated = True
    return dominated


def compute_pareto_front(individuals: List[Dict]) -> List[List[Dict]]:
    """
    Compute Pareto fronts from individuals.

    Args:
        individuals: List of {id, metrics: {metric_name: value}}

    Returns:
        List of fronts (front 0 = best)
    """
    # TODO: Implement Pareto front computation
    raise NotImplementedError


def select_survivors(individuals: List[Dict], target_size: int) -> List[Dict]:
    """
    Select survivors using NSGA-II style selection.

    Args:
        individuals: All individuals with metrics
        target_size: How many to keep

    Returns:
        Selected individuals
    """
    # TODO: Implement selection
    raise NotImplementedError


def mutate_prompt(prompt: str, critique: Dict) -> str:
    """
    Mutate prompt text using LLM critique.

    Args:
        prompt: Current prompt
        critique: {suggestions, prompt_mutation}

    Returns:
        Mutated prompt
    """
    # TODO: Implement reflective mutation
    raise NotImplementedError
