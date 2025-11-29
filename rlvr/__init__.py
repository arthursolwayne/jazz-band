"""
RLVR (Reinforcement Learning with Verifiable Rewards) Training Infrastructure

This package implements ART-based RL training for the Jazz Band Composer agent.
Uses 100% verifiable, deterministic metrics with fixed weights (no curriculum, no judge in reward).
"""

from .metrics import (
    compute_all_metrics,
    compute_upbeat_syncopation,
    compute_seventh_chord_usage,
    compute_textural_arc,
    compute_rhythmic_variety,
    compute_dynamic_contrast,
    compute_melodic_exploration,
    compute_harmonic_movement,
)
from .reward import calculate_reward, RewardWeights, FIXED_WEIGHTS

__all__ = [
    "compute_all_metrics",
    "compute_upbeat_syncopation",
    "compute_seventh_chord_usage",
    "compute_textural_arc",
    "compute_rhythmic_variety",
    "compute_dynamic_contrast",
    "compute_melodic_exploration",
    "compute_harmonic_movement",
    "calculate_reward",
    "RewardWeights",
    "FIXED_WEIGHTS",
]
