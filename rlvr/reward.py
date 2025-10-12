"""
RLVR Reward Function

Implements weighted reward calculation with curriculum learning, annealing,
exploration bonuses, and penalty hooks.

Strategy:
- Phase A (steps 0-5): Focus on rhythm (syncopation + groove = 60% weight)
- Phase B (steps 6-10): Add harmony and activation metrics
- Phase C (steps 11+): Anneal Judge score weight from 0.10 → 0.30

Exploration bonuses reward first-time achievements (e.g., first time hitting
trumpet_activation ≥ 0.5).

Penalty hooks punish invalid outputs and rule violations.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Set, Optional


class CurriculumPhase(Enum):
    """Training curriculum phases."""
    PHASE_A = "rhythm_focus"      # Steps 0-5
    PHASE_B = "harmony_added"     # Steps 6-10
    PHASE_C = "full_training"     # Steps 11+


@dataclass
class RewardWeights:
    """
    Weights for each metric in the reward function.

    Total should sum to 1.0 for interpretability.
    Rhythm section (syncopation + groove) gets ≥40% weight in all phases.
    """
    # Rhythm section (≥40% total)
    upbeat_syncopation: float
    groove_alignment: float

    # Harmony & activation
    seventh_chords: float
    trumpet_activation: float
    space_density: float

    # Baseline stability
    consonance: float
    density_regularity: float

    # Judge score (annealed over time)
    judge_score: float

    def validate(self) -> None:
        """Check that weights sum to approximately 1.0."""
        total = (
            self.upbeat_syncopation +
            self.groove_alignment +
            self.seventh_chords +
            self.trumpet_activation +
            self.space_density +
            self.consonance +
            self.density_regularity +
            self.judge_score
        )
        assert abs(total - 1.0) < 0.01, f"Weights must sum to 1.0, got {total}"


def get_curriculum_weights(step: int) -> RewardWeights:
    """
    Get reward weights for current training step based on curriculum phase.

    Args:
        step: Current training step (0-indexed)

    Returns:
        RewardWeights for this phase
    """
    if step <= 5:
        # Phase A: Rhythm focus (syncopation + groove = 60%)
        return RewardWeights(
            upbeat_syncopation=0.35,    # PRIMARY FOCUS
            groove_alignment=0.25,      # SECONDARY FOCUS
            seventh_chords=0.10,        # Low weight
            trumpet_activation=0.05,    # Low weight
            space_density=0.05,         # Low weight
            consonance=0.10,            # Baseline stability
            density_regularity=0.05,    # Baseline stability
            judge_score=0.05,           # Minimal Judge influence early
        )

    elif step <= 10:
        # Phase B: Add harmony and activation (rhythm still 40%)
        return RewardWeights(
            upbeat_syncopation=0.25,    # Still important
            groove_alignment=0.15,      # Still important
            seventh_chords=0.15,        # INCREASED
            trumpet_activation=0.10,    # INCREASED
            space_density=0.10,         # INCREASED
            consonance=0.10,            # Baseline stability
            density_regularity=0.05,    # Baseline stability
            judge_score=0.10,           # Moderate Judge influence
        )

    else:
        # Phase C: Full training with annealed Judge score
        # Judge weight increases from 0.10 → 0.30 over steps 11-20
        judge_weight = min(0.30, 0.10 + (step - 11) * 0.02)

        # Rebalance other weights proportionally
        base_weights = 1.0 - judge_weight

        return RewardWeights(
            upbeat_syncopation=0.25 * base_weights / 0.90,
            groove_alignment=0.15 * base_weights / 0.90,
            seventh_chords=0.15 * base_weights / 0.90,
            trumpet_activation=0.10 * base_weights / 0.90,
            space_density=0.10 * base_weights / 0.90,
            consonance=0.10 * base_weights / 0.90,
            density_regularity=0.05 * base_weights / 0.90,
            judge_score=judge_weight,
        )


# Track exploration bonuses granted (per-session)
# Key: (achievement_name, session_id) -> bool
_exploration_bonuses_granted: Set[str] = set()


def reset_exploration_bonuses():
    """Reset exploration bonus tracking (call at start of training)."""
    global _exploration_bonuses_granted
    _exploration_bonuses_granted = set()


def check_exploration_bonuses(
    metrics: Dict[str, float],
    session_id: str
) -> float:
    """
    Check if any first-time achievement bonuses should be awarded.

    Exploration bonuses are ONE-TIME rewards for hitting thresholds for the first time.
    This encourages exploration of the solution space.

    Args:
        metrics: Dict of metric values
        session_id: Unique identifier for this training session

    Returns:
        Total exploration bonus (additive)
    """
    bonus = 0.0

    # Bonus 1: First time hitting upbeat_syncopation ≥ 0.6
    if metrics["upbeat_syncopation"] >= 0.6:
        key = f"upbeat_syncopation_60_{session_id}"
        if key not in _exploration_bonuses_granted:
            bonus += 0.2
            _exploration_bonuses_granted.add(key)

    # Bonus 2: First time hitting trumpet_activation ≥ 0.5
    if metrics["trumpet_activation"] >= 0.5:
        key = f"trumpet_activation_50_{session_id}"
        if key not in _exploration_bonuses_granted:
            bonus += 0.2
            _exploration_bonuses_granted.add(key)

    # Bonus 3: First time hitting seventh_chord_usage ≥ 0.75
    if metrics["seventh_chord_usage"] >= 0.75:
        key = f"seventh_chords_75_{session_id}"
        if key not in _exploration_bonuses_granted:
            bonus += 0.15
            _exploration_bonuses_granted.add(key)

    # Bonus 4: First time hitting space_density ≥ 0.5
    if metrics["space_density"] >= 0.5:
        key = f"space_density_50_{session_id}"
        if key not in _exploration_bonuses_granted:
            bonus += 0.15
            _exploration_bonuses_granted.add(key)

    return bonus


def apply_penalty_hooks(
    jam_json: Optional[Dict],
    metrics: Dict[str, float],
    is_valid: bool
) -> float:
    """
    Apply penalties for invalid outputs and rule violations.

    Args:
        jam_json: JamJSON dictionary (None if invalid/failed to parse)
        metrics: Dict of metric values
        is_valid: Whether JamJSON passed validation

    Returns:
        Total penalty (negative value to subtract from reward)
    """
    penalty = 0.0

    # Penalty 1: Invalid JamJSON (terminal failure)
    if not is_valid or jam_json is None:
        return -1.0  # Maximum penalty

    # Penalty 2: Trumpet plays < 3 bars (severe violation)
    # trumpet_activation < 0.375 means < 3 bars out of 8
    if metrics["trumpet_activation"] < 0.375:
        penalty += 0.5

    # Penalty 3: No 7th chords at all (harmony violation)
    if metrics["seventh_chord_usage"] == 0.0:
        penalty += 0.3

    # Penalty 4: No upbeat syncopation (rhythm violation)
    if metrics["upbeat_syncopation"] < 0.1:
        penalty += 0.3

    return -penalty


def calculate_reward(
    step: int,
    metrics: Dict[str, float],
    judge_score: float,
    jam_json: Optional[Dict] = None,
    is_valid: bool = True,
    session_id: str = "default",
) -> Dict:
    """
    Calculate total reward with curriculum weights, bonuses, and penalties.

    Args:
        step: Current training step
        metrics: Dict of metric values (all 0.0-1.0)
        judge_score: Judge overall score (0.0-10.0)
        jam_json: Optional JamJSON dict (for penalty checks)
        is_valid: Whether JamJSON passed validation
        session_id: Unique session ID for exploration bonuses

    Returns:
        Dict with:
            - total_reward: Final scalar reward
            - base_reward: Weighted sum before bonuses/penalties
            - exploration_bonus: First-time achievement bonuses
            - penalty: Rule violation penalties
            - weights: RewardWeights used
            - breakdown: Per-metric contributions
    """
    # Get curriculum weights
    weights = get_curriculum_weights(step)
    weights.validate()

    # Calculate weighted sum of metrics
    # Normalize judge_score to 0-1 range for consistent weighting
    normalized_judge = judge_score / 10.0

    base_reward = (
        weights.upbeat_syncopation * metrics["upbeat_syncopation"] +
        weights.groove_alignment * metrics["groove_alignment"] +
        weights.seventh_chords * metrics["seventh_chord_usage"] +
        weights.trumpet_activation * metrics["trumpet_activation"] +
        weights.space_density * metrics["space_density"] +
        weights.consonance * metrics["consonance"] +
        weights.density_regularity * metrics["density_regularity"] +
        weights.judge_score * normalized_judge
    )

    # Check exploration bonuses
    exploration_bonus = check_exploration_bonuses(metrics, session_id)

    # Apply penalty hooks
    penalty = apply_penalty_hooks(jam_json, metrics, is_valid)

    # Total reward
    total_reward = base_reward + exploration_bonus + penalty

    # Per-metric breakdown for logging
    breakdown = {
        "upbeat_syncopation": weights.upbeat_syncopation * metrics["upbeat_syncopation"],
        "groove_alignment": weights.groove_alignment * metrics["groove_alignment"],
        "seventh_chords": weights.seventh_chords * metrics["seventh_chord_usage"],
        "trumpet_activation": weights.trumpet_activation * metrics["trumpet_activation"],
        "space_density": weights.space_density * metrics["space_density"],
        "consonance": weights.consonance * metrics["consonance"],
        "density_regularity": weights.density_regularity * metrics["density_regularity"],
        "judge_score": weights.judge_score * normalized_judge,
    }

    return {
        "total_reward": total_reward,
        "base_reward": base_reward,
        "exploration_bonus": exploration_bonus,
        "penalty": penalty,
        "weights": weights,
        "breakdown": breakdown,
    }
