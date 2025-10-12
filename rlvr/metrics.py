"""
RLVR Metrics Module

Computes verifiable metrics for RLVR training with focus on rhythm-first objectives.

Metrics (all return 0.0-1.0 with smooth gradients):
1. Upbeat syncopation - % hihat hits on upbeats (target > 0.6)
2. 7th chord usage - fraction of bars with 7th chords (target > 0.75)
3. Trumpet activation - fraction of bars with trumpet notes (target ≥ 0.5)
4. Space density - fraction of bars with ≥1 non-rhythm instrument resting (target ≥ 0.5)
5. Consonance (baseline) - % notes in key scale
6. Groove alignment (baseline) - bass-drum downbeat correlation
7. Density regularity (baseline) - inverse variance of note counts

All metrics return values between 0.0 and 1.0 for consistent reward weighting.
"""

import sys
from pathlib import Path
from typing import Dict, List
from collections import Counter
import statistics

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from jazz_band.memory import ChemistryMemory


# ============================================================================
# NEW RHYTHM-FIRST METRICS (Priority for RLVR)
# ============================================================================

def compute_upbeat_syncopation(jam_json: Dict) -> float:
    """
    Metric 1: Upbeat Syncopation (MOST IMPORTANT FOR LATIN JAZZ)

    Measures the percentage of hihat hits that occur on upbeats ("and"s)
    rather than downbeats. Latin jazz requires strong upbeat emphasis.

    Think of each bar in 4/4 as 8 eighth notes:
    - Downbeats: positions 0, 2, 4, 6 (beats 1, 2, 3, 4)
    - Upbeats: positions 1, 3, 5, 7 (the "and"s)

    Target: >60% of hihat hits on upbeats for authentic Latin feel.

    Args:
        jam_json: JamJSON dictionary

    Returns:
        Float 0.0 to 1.0 (proportion of hihat hits on upbeats)
    """
    total_hihat_hits = 0
    upbeat_hihat_hits = 0

    for bar in jam_json["bars"]:
        hihat_events = bar["parts"].get("hihat", [])

        # Track position in bar (in eighth note units)
        position = 0  # 0-7 for eight eighth notes in 4/4

        for event in hihat_events:
            pitch = event.get("pitch", "rest")
            dur = event.get("dur", "q")

            # Convert duration to eighth note units
            dur_map = {"e": 1, "q": 2, "h": 4, "w": 8}
            dur_units = dur_map.get(dur, 2)

            # Check if this is a hihat hit (not a rest)
            if pitch == "hihat":
                total_hihat_hits += 1

                # Check if current position is an upbeat (odd positions: 1, 3, 5, 7)
                if position % 2 == 1:
                    upbeat_hihat_hits += 1

            # Advance position
            position += dur_units
            position = position % 8  # Wrap at bar boundary

    if total_hihat_hits == 0:
        return 0.5  # Neutral score if no hihat

    return upbeat_hihat_hits / total_hihat_hits


def compute_seventh_chord_usage(jam_json: Dict) -> float:
    """
    Metric 2: 7th Chord Usage

    Measures the fraction of bars where piano uses 7th chords (4 notes)
    rather than simple triads (3 notes). Jazz harmony requires 7th chords minimum.

    Target: >75% of bars should contain 7th chords.

    Args:
        jam_json: JamJSON dictionary

    Returns:
        Float 0.0 to 1.0 (proportion of bars with 7th chords)
    """
    bars_with_7th_chords = 0
    total_bars = len(jam_json["bars"])

    for bar in jam_json["bars"]:
        piano_events = bar["parts"].get("piano", [])

        # Collect unique pitches in this bar (excluding rests)
        unique_pitches = set()
        for event in piano_events:
            pitch = event.get("pitch", "rest")
            if pitch != "rest":
                # Extract pitch class (remove octave number)
                pitch_class = pitch.rstrip("0123456789")
                unique_pitches.add(pitch_class)

        # Check if we have 4+ unique pitch classes (indicates 7th chord)
        # This is a simple heuristic - could be improved with chord detection
        if len(unique_pitches) >= 4:
            bars_with_7th_chords += 1

    if total_bars == 0:
        return 0.5

    return bars_with_7th_chords / total_bars



def compute_space_density(jam_json: Dict) -> float:
    """
    Metric 4: Space Density

    Measures the fraction of bars where at least one non-rhythm instrument
    (piano, sax, or trumpet) rests for the entire bar. Space creates depth
    and prevents muddy, crowded arrangements.

    Target: ≥50% of bars should have space (i.e., 4+ bars out of 8).

    Args:
        jam_json: JamJSON dictionary

    Returns:
        Float 0.0 to 1.0 (proportion of bars with space)
    """
    bars_with_space = 0
    total_bars = len(jam_json["bars"])

    non_rhythm_instruments = ["piano", "sax", "trumpet"]

    for bar in jam_json["bars"]:
        # Check if at least one non-rhythm instrument rests the entire bar
        has_space = False

        for inst in non_rhythm_instruments:
            events = bar["parts"].get(inst, [])

            # Check if all events are rests OR if there's only one whole note rest
            all_rests = all(
                event.get("pitch", "rest") == "rest"
                for event in events
            )

            if all_rests:
                has_space = True
                break

        if has_space:
            bars_with_space += 1

    if total_bars == 0:
        return 0.5

    return bars_with_space / total_bars


# ============================================================================
# BASELINE METRICS (Reused from GEPA for stability)
# ============================================================================

# Musical scale definitions (for consonance calculation)
SCALES = {
    "C": ["C", "D", "E", "F", "G", "A", "B"],
    "Dm": ["D", "E", "F", "G", "A", "Bb", "C"],
    "F": ["F", "G", "A", "Bb", "C", "D", "E"],
    "G": ["G", "A", "B", "C", "D", "E", "F#"],
    "Am": ["A", "B", "C", "D", "E", "F", "G"],
    "Bb": ["Bb", "C", "D", "Eb", "F", "G", "A"],
    "D": ["D", "E", "F#", "G", "A", "B", "C#"],
    "Em": ["E", "F#", "G", "A", "B", "C", "D"],
    "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
}


def compute_consonance(jam_json: Dict) -> float:
    """
    Baseline Metric 5: Consonance

    Percentage of notes that fit in the key scale (avoid excessive chromatic tension).
    This is a stability metric - ensures output stays in key.

    Args:
        jam_json: JamJSON dictionary

    Returns:
        Consonance score 0.0 to 1.0
    """
    key = jam_json.get("key", "C")
    scale = SCALES.get(key, SCALES["C"])  # Default to C major

    # Extract pitch classes (remove octave numbers)
    total_notes = 0
    in_scale_notes = 0

    for bar in jam_json["bars"]:
        for part_name, events in bar["parts"].items():
            # Skip drums
            if part_name in ["snare", "hihat"]:
                continue

            for event in events:
                pitch = event.get("pitch", "rest")
                if pitch == "rest":
                    continue

                # Extract pitch class (remove octave)
                pitch_class = pitch.rstrip("0123456789")

                total_notes += 1
                if pitch_class in scale:
                    in_scale_notes += 1

    if total_notes == 0:
        return 0.5  # Neutral score for empty arrangements

    return in_scale_notes / total_notes


def compute_groove_alignment(jam_json: Dict) -> float:
    """
    Baseline Metric 6: Groove Alignment

    Correlation between bass and drum hits on downbeats (beat 1 of each bar).
    When rhythm section is aligned, it creates a solid foundation.

    Args:
        jam_json: JamJSON dictionary

    Returns:
        Groove alignment score 0.0 to 1.0
    """
    alignment_count = 0
    total_bars = len(jam_json["bars"])

    for bar in jam_json["bars"]:
        # Check if bass has a note on beat 1 (first event)
        bass_events = bar["parts"].get("bass", [])
        has_bass_downbeat = len(bass_events) > 0 and bass_events[0].get("pitch") != "rest"

        # Check if snare or hihat has a hit on beat 1
        snare_events = bar["parts"].get("snare", [])
        hihat_events = bar["parts"].get("hihat", [])
        has_drum_downbeat = (
            (len(snare_events) > 0 and snare_events[0].get("pitch") != "rest") or
            (len(hihat_events) > 0 and hihat_events[0].get("pitch") != "rest")
        )

        # Both hit on downbeat = aligned
        if has_bass_downbeat and has_drum_downbeat:
            alignment_count += 1

    if total_bars == 0:
        return 0.5

    return alignment_count / total_bars


def compute_density_regularity(jam_json: Dict) -> float:
    """
    Baseline Metric 7: Density Regularity

    Inverse of variance in note counts per bar per instrument.
    Regular density = consistent phrasing (not erratic).

    Args:
        jam_json: JamJSON dictionary

    Returns:
        Density regularity score 0.0 to 1.0
    """
    # Collect note counts per bar for each instrument
    instrument_densities = {
        "bass": [],
        "piano": [],
        "sax": [],
        "trumpet": [],
    }

    for bar in jam_json["bars"]:
        for inst in instrument_densities.keys():
            events = bar["parts"].get(inst, [])
            note_count = sum(1 for e in events if e.get("pitch") != "rest")
            instrument_densities[inst].append(note_count)

    # Compute variance for each instrument
    total_variance = 0.0
    inst_count = 0

    for inst, densities in instrument_densities.items():
        if len(densities) > 1:
            variance = statistics.variance(densities)
            total_variance += variance
            inst_count += 1

    if inst_count == 0:
        return 0.5

    avg_variance = total_variance / inst_count

    # Score: lower variance = higher regularity
    # Normalize by expected variance (~2.0 for typical jazz)
    expected_variance = 2.0
    score = max(0.0, 1.0 - (avg_variance / expected_variance))

    return score


# ============================================================================
# HELPER FUNCTION
# ============================================================================

def compute_all_metrics(jam_json: Dict, memory: ChemistryMemory = None) -> Dict[str, float]:
    """
    Compute all RLVR metrics at once.

    Args:
        jam_json: JamJSON dictionary
        memory: Optional ChemistryMemory (not used for current metrics)

    Returns:
        Dictionary mapping metric names to values (all 0.0-1.0)
    """
    return {
        # Rhythm-first metrics (priority)
        "upbeat_syncopation": compute_upbeat_syncopation(jam_json),
        "seventh_chord_usage": compute_seventh_chord_usage(jam_json),
        "space_density": compute_space_density(jam_json),

        # Baseline metrics (stability)
        "consonance": compute_consonance(jam_json),
        "groove_alignment": compute_groove_alignment(jam_json),
        "density_regularity": compute_density_regularity(jam_json),
    }
