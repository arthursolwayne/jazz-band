"""
RLVR (Reinforcement Learning with Verifiable Rewards) Training Infrastructure

This package implements ART-based RL training for the Jazz Band Composer agent.
Uses rhythm-first metrics, strict Judge calibration, and curriculum-based reward shaping.
"""

from .metrics import (
    compute_all_metrics,
    compute_upbeat_syncopation,
    compute_seventh_chord_usage,
    compute_trumpet_activation,
    compute_space_density,
)
from .reward import calculate_reward, RewardWeights, CurriculumPhase

__all__ = [
    "compute_all_metrics",
    "compute_upbeat_syncopation",
    "compute_seventh_chord_usage",
    "compute_trumpet_activation",
    "compute_space_density",
    "calculate_reward",
    "RewardWeights",
    "CurriculumPhase",
]
