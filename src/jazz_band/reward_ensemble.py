"""
Ensemble Reward: Multiplicative bonus based on sax-piano interaction.

Measures rhythmic independence and temporal overlap between sax and piano.
Poor interaction = 1.0 (no bonus).
Strong interaction = 1.1 (max bonus).

Returns a multiplier (1.0-1.1) applied to base instrument rewards.

Validated against human ratings: r = +0.458 (2-feature ablation-optimized)
"""

import math
from typing import TYPE_CHECKING, List, Dict

if TYPE_CHECKING:
    import pretty_midi


# =============================================================================
# Instrument Extraction Helpers
# =============================================================================

def get_sax_notes(midi: "pretty_midi.PrettyMIDI") -> List:
    """Extract sax track notes (program 66)."""
    for inst in midi.instruments:
        if not inst.is_drum and inst.program == 66:
            return sorted(inst.notes, key=lambda n: n.start)
    return []


def get_piano_notes(midi: "pretty_midi.PrettyMIDI") -> List:
    """Extract piano track notes (program 0, non-drum)."""
    for inst in midi.instruments:
        if not inst.is_drum and inst.program == 0:
            return sorted(inst.notes, key=lambda n: n.start)
    return []


# =============================================================================
# Ensemble Features
# =============================================================================

def rhythmic_independence(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Measure rhythmic independence between sax and piano.

    Higher = sax and piano NOT hitting same beat positions = better jazz interplay.
    Standards: 0.27-0.81 (varies by style)
    Human correlation: r = +0.364 (strongest predictor)

    Direction: Higher is better
    Returns: 0.0 (locked together) to 1.0 (independent)
    """
    sax = get_sax_notes(midi)
    piano = get_piano_notes(midi)

    if len(sax) < 2 or len(piano) < 2:
        return 0.5

    # Quantize onsets to 16th note grid
    grid = 0.125  # 16th at 120bpm
    sax_onsets = set(round(n.start / grid) * grid for n in sax)
    piano_onsets = set(round(n.start / grid) * grid for n in piano)

    coincident = len(sax_onsets & piano_onsets)
    total = len(sax_onsets | piano_onsets)

    if total == 0:
        return 0.5

    # Return 1 - overlap (higher = more independent)
    return 1.0 - (coincident / total)


def note_overlap_ratio(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Measure how much sax and piano play simultaneously.

    Good jazz: sax solo with piano comp = moderate overlap (30-70%)
    Too low: sparse, disconnected
    Too high: stepping on each other

    Standards: 0.28-0.74
    Human correlation: r = +0.318

    Direction: Higher is better (within reason)
    Returns: 0.0 (never overlap) to 1.0 (always overlap)
    """
    sax = get_sax_notes(midi)
    piano = get_piano_notes(midi)

    if not sax or not piano:
        return 0.5

    # Sample at 0.1s intervals
    max_time = max(max(n.end for n in sax), max(n.end for n in piano))
    step = 0.1
    both_playing = 0
    total_samples = 0

    t = 0
    while t < max_time:
        sax_active = any(n.start <= t < n.end for n in sax)
        piano_active = any(n.start <= t < n.end for n in piano)
        if sax_active and piano_active:
            both_playing += 1
        total_samples += 1
        t += step

    return both_playing / total_samples if total_samples > 0 else 0


def density_ratio(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Ratio of piano density to sax density.

    Good jazz: piano sparser than sax (comping vs melody)
    Piano density should be 30-70% of sax density.

    Standards: 0.46-0.54
    Human correlation: r = -0.213 (lower is better)

    Direction: Lower is better (piano should be sparser)
    Returns: 0.0 (piano silent) to 2.0+ (piano denser than sax)
    """
    sax = get_sax_notes(midi)
    piano = get_piano_notes(midi)

    if not sax or not piano:
        return 0.5

    max_time = max(max(n.end for n in sax), max(n.end for n in piano))
    if max_time <= 0:
        return 0.5

    sax_density = len(sax) / max_time
    piano_density = len(piano) / max_time

    if sax_density <= 0:
        return 0

    return piano_density / sax_density


# =============================================================================
# Ensemble Reward Function (Multiplicative)
# =============================================================================

def compute_ensemble_reward(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Compute ensemble multiplier based on validated features.

    Features (correlation with human ratings):
    - rhythmic_independence: r = +0.364
    - note_overlap_ratio:    r = +0.318
    Combined: r = +0.458 (ablation-optimized, 2-feature config)

    Old metric (velocity correlation): r = -0.08 (harmful)
    New metric (2-feature):             r = +0.458 (validated)

    Returns multiplier (1.0-1.1) to apply to base instrument rewards.
    """
    # Compute features
    ri = rhythmic_independence(midi)
    overlap = note_overlap_ratio(midi)

    # Z-score normalization (stats from human-rated tracks)
    # rhythmic_indep: mean=0.58, std=0.17
    # overlap:        mean=0.51, std=0.18

    z_ri = (ri - 0.58) / 0.17 if 0.17 > 0 else 0
    z_overlap = (overlap - 0.51) / 0.18 if 0.18 > 0 else 0

    # Clamp to ±3
    z_ri = max(-3, min(3, z_ri))
    z_overlap = max(-3, min(3, z_overlap))

    # Weight by correlation strength
    z_sum = z_ri * 0.364 + z_overlap * 0.318

    # Normalize z_sum to roughly 0-1 range (±3σ → ±0.9)
    score = (z_sum + 3) / 6  # Maps [-3, 3] to [0, 1]
    score = max(0, min(1, score))

    # Map to 1.0-1.1 multiplier
    return 1.0 + score * 0.1


def compute_ensemble_reward_detailed(midi: "pretty_midi.PrettyMIDI") -> dict:
    """
    Compute ensemble reward with breakdown.

    Returns dict with:
        - total: multiplier (1.0-1.1)
        - rhythmic_independence: raw value (0-1)
        - note_overlap_ratio: raw value (0-1)
        - density_ratio: raw value (0-2+)
    """
    ri = rhythmic_independence(midi)
    overlap = note_overlap_ratio(midi)
    dr = density_ratio(midi)
    mult = compute_ensemble_reward(midi)

    return {
        "total": mult,
        "rhythmic_independence": ri,
        "note_overlap_ratio": overlap,
        "density_ratio": dr,
    }
