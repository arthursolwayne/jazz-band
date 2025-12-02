"""
Ensemble Reward: Multiplicative bonus based on dynamic coherence.

Measures how well sax and piano velocity contours correlate over time.
Higher correlation = better ensemble awareness = bonus multiplier.

Returns a multiplier (1.0-1.1) applied to base instrument rewards.
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
# Dynamic Coherence (sole ensemble feature)
# =============================================================================

def dynamic_coherence(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Correlation between sax and piano velocity contours.

    Rationale: Good ensemble playing has dynamic coherence.
    When sax plays loud, piano should respond accordingly.
    Completely random dynamics = poor ensemble awareness.

    Direction: Higher is better (more coherent dynamics)
    """
    sax = get_sax_notes(midi)
    piano = get_piano_notes(midi)

    if len(sax) < 2 or len(piano) < 2:
        return 0.5  # Neutral if insufficient data

    # Divide time into windows and compute average velocity per window
    all_notes = sax + piano
    max_time = max(n.end for n in all_notes)
    n_windows = 8
    window_size = max_time / n_windows

    sax_vel = []
    piano_vel = []

    for i in range(n_windows):
        win_start = i * window_size
        win_end = (i + 1) * window_size

        sax_in_win = [n.velocity for n in sax if win_start <= n.start < win_end]
        piano_in_win = [n.velocity for n in piano if win_start <= n.start < win_end]

        sax_vel.append(sum(sax_in_win) / len(sax_in_win) if sax_in_win else 0)
        piano_vel.append(sum(piano_in_win) / len(piano_in_win) if piano_in_win else 0)

    # Compute Pearson correlation
    n = len(sax_vel)
    mean_sax = sum(sax_vel) / n
    mean_piano = sum(piano_vel) / n

    cov = sum((sax_vel[i] - mean_sax) * (piano_vel[i] - mean_piano) for i in range(n))
    std_sax = math.sqrt(sum((v - mean_sax)**2 for v in sax_vel))
    std_piano = math.sqrt(sum((v - mean_piano)**2 for v in piano_vel))

    if std_sax < 0.01 or std_piano < 0.01:
        return 0.5  # Can't compute correlation with no variance

    r = cov / (std_sax * std_piano)
    return (r + 1) / 2  # Normalize to [0, 1]


# =============================================================================
# Ensemble Reward Function (Multiplicative)
# =============================================================================

def compute_ensemble_reward(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Compute ensemble multiplier based on dynamic coherence.

    Returns a multiplier (1.0-1.1) to apply to base instrument rewards.
    Higher dynamic coherence = sax and piano move together dynamically = bonus.

    Validated on n=29 human-scored tracks: r=0.47 with GEPA_best_balance at #5.
    """
    dc = dynamic_coherence(midi)
    # dc ranges 0-1, bonus kicks in above 0.5
    # 1.0 + max(0, dc - 0.5) * 0.2 gives range 1.0-1.1
    return 1.0 + max(0, dc - 0.5) * 0.2


def compute_ensemble_reward_detailed(midi: "pretty_midi.PrettyMIDI") -> dict:
    """
    Compute ensemble reward with breakdown.

    Returns dict with:
        - total: multiplier (1.0-1.1)
        - dynamic_coherence: raw dc value (0-1)
    """
    dc = dynamic_coherence(midi)
    mult = 1.0 + max(0, dc - 0.5) * 0.2

    return {
        "total": mult,
        "dynamic_coherence": dc,
    }
