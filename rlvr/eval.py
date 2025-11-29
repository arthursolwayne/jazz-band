"""
RLVR Evaluation: Weighted sum of metrics → scalar reward.
"""

from typing import Dict

# Fixed weights (sum to 1.0)
WEIGHTS = {
    "upbeat_syncopation": 0.25,
    "groove_alignment": 0.15,
    "seventh_chord_usage": 0.10,
    "textural_arc": 0.10,
    "rhythmic_variety": 0.10,
    "dynamic_contrast": 0.10,
    "melodic_exploration": 0.10,
    "harmonic_movement": 0.05,
    "consonance": 0.05,
}


def compute_reward(metrics: Dict[str, float], is_valid: bool = True) -> float:
    """
    Weighted sum of metrics → scalar reward.

    Args:
        metrics: Dict from metrics.compute_all()
        is_valid: False if generation failed

    Returns:
        Scalar reward (can be negative if invalid)
    """
    if not is_valid:
        return -1.0

    reward = sum(WEIGHTS[k] * metrics[k] for k in WEIGHTS)

    # Penalties
    if metrics["seventh_chord_usage"] == 0.0:
        reward -= 0.3
    if metrics["upbeat_syncopation"] < 0.1:
        reward -= 0.3

    return reward
