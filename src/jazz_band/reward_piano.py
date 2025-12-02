"""
Piano Comping Reward Features for Jazz MIDI Generation.

This module provides 12 features designed to correlate with human musicality
scores for jazz piano comping. Based on jazz pedagogy research:
- Voicings should be rich but not cluttered (3-6 notes typical)
- Rhythm should be sparse/syncopated, not on every beat
- Register should stay out of melody range (typically lower)
- Voice leading should be smooth between chords

Feature categories:
1. Voicing quality (chord size, spread, rootless detection)
2. Rhythm/sparseness (note density, syncopation, gaps)
3. Register separation (avoid melody range)
4. Voice leading (smooth motion between chords)

References:
- Jazz Library: https://jazz-library.com/articles/comping/
- The Jazz Piano Site: https://www.thejazzpianosite.com/jazz-piano-lessons/jazz-chord-voicings/how-to-comp/
"""

import math
from collections import Counter
from typing import TYPE_CHECKING, List, Dict, Tuple, Optional

from .symbol_engine import clamp_z

if TYPE_CHECKING:
    import pretty_midi


# =============================================================================
# Piano Note Extraction
# =============================================================================

def get_piano_notes(midi: "pretty_midi.PrettyMIDI") -> List:
    """
    Extract piano track notes (program 0) or fallback heuristics.

    Returns notes sorted by start time.
    """
    # Look for program 0 (Acoustic Grand Piano) non-drum track
    for inst in midi.instruments:
        if not inst.is_drum and inst.program == 0:
            # Check if it looks like a piano part (chordal, mid-low register)
            if len(inst.notes) > 0:
                pitches = [n.pitch for n in inst.notes]
                avg_pitch = sum(pitches) / len(pitches)
                # Piano comping usually in range 40-70 (E2 to Bb4)
                if 35 <= avg_pitch <= 75:
                    return sorted(inst.notes, key=lambda n: n.start)

    # Fallback: look for any non-drum track with chordal characteristics
    for inst in midi.instruments:
        if not inst.is_drum and inst.program in [0, 1, 2, 3, 4, 5]:  # Piano family
            if len(inst.notes) > 0:
                return sorted(inst.notes, key=lambda n: n.start)

    return []


def get_sax_notes(midi: "pretty_midi.PrettyMIDI") -> List:
    """Extract sax track notes for register comparison."""
    for inst in midi.instruments:
        if not inst.is_drum and inst.program == 66:
            return sorted(inst.notes, key=lambda n: n.start)
    # Fallback: first non-drum, non-piano track
    for inst in midi.instruments:
        if not inst.is_drum and inst.program not in [0, 1, 2, 3, 4, 5, 33]:
            return sorted(inst.notes, key=lambda n: n.start)
    return []


# =============================================================================
# Helper Functions
# =============================================================================

def group_simultaneous_notes(notes: List, threshold: float = 0.05) -> List[List]:
    """
    Group notes that start within threshold seconds of each other.
    Returns list of note groups (chords).
    """
    if not notes:
        return []

    groups = []
    current_group = [notes[0]]

    for note in notes[1:]:
        if note.start - current_group[0].start <= threshold:
            current_group.append(note)
        else:
            groups.append(current_group)
            current_group = [note]

    groups.append(current_group)
    return groups


def get_chord_intervals(chord_notes: List) -> List[int]:
    """Get sorted intervals (in semitones) within a chord."""
    if len(chord_notes) < 2:
        return []
    pitches = sorted(n.pitch for n in chord_notes)
    return [pitches[i+1] - pitches[i] for i in range(len(pitches) - 1)]


# =============================================================================
# Feature 1: Voicing Richness (avg notes per chord)
# =============================================================================

def voicing_richness(notes: List) -> float:
    """
    Average number of notes per chord voicing.

    Rationale: Good jazz voicings typically have 3-6 notes.
    Too few = thin sound, too many = muddy.
    Direction: Moderate is better (will need nonlinear mapping).

    For reward, we'll use distance from ideal (4 notes).
    """
    if not notes:
        return 0.0

    chords = group_simultaneous_notes(notes)
    if not chords:
        return 0.0

    avg_size = sum(len(c) for c in chords) / len(chords)
    return avg_size


def voicing_richness_penalty(notes: List) -> float:
    """
    Penalty for deviation from ideal chord size (4 notes).

    Returns: 0.0 (perfect) to 1.0 (very bad)
    Direction: Lower is better.
    """
    avg = voicing_richness(notes)
    ideal = 4.0
    # Quadratic penalty for deviation
    return min(1.0, ((avg - ideal) / 3.0) ** 2)


# =============================================================================
# Feature 2: Chord Spread (voicing width in semitones)
# =============================================================================

def avg_chord_spread(notes: List) -> float:
    """
    Average interval span of chords (highest - lowest pitch).

    Rationale: Open voicings (10-20 semitones) sound more professional
    than closed position (< 12 semitones).
    Direction: Higher is better (to a point).
    """
    if not notes:
        return 0.0

    chords = group_simultaneous_notes(notes)
    spreads = []

    for chord in chords:
        if len(chord) >= 2:
            pitches = [n.pitch for n in chord]
            spreads.append(max(pitches) - min(pitches))

    if not spreads:
        return 0.0

    return sum(spreads) / len(spreads)


# =============================================================================
# Feature 3: Rootless Voicing Ratio
# =============================================================================

def rootless_ratio(notes: List) -> float:
    """
    Estimate ratio of rootless voicings (no bass note doubling root).

    Rationale: Professional jazz comping uses rootless voicings
    to leave room for the bass player.
    Direction: Higher is better.

    Heuristic: If lowest note in chord is > 12 semitones above
    the overall bass, likely rootless.
    """
    if not notes:
        return 0.0

    chords = group_simultaneous_notes(notes)
    if not chords:
        return 0.0

    # Find overall bass range
    all_pitches = [n.pitch for n in notes]
    bass_threshold = min(all_pitches) + 12  # One octave above lowest note

    rootless_count = 0
    for chord in chords:
        if len(chord) >= 2:
            lowest = min(n.pitch for n in chord)
            if lowest > bass_threshold:
                rootless_count += 1

    return rootless_count / len(chords)


# =============================================================================
# Feature: Chord Variety (unique chords / total chords)
# =============================================================================

def chord_variety(notes: List) -> float:
    """
    Ratio of unique chords to total chords.

    Measures harmonic variety — are we hearing different chords or
    the same voicing repeated? Uses pitch-class sets (transposition-invariant).

    Direction: Higher = better (more variety)

    Example:
        3 unique chords out of 4 total = 0.75
        1 chord repeated 4 times = 0.25
    """
    if not notes:
        return 0.0

    chords = group_simultaneous_notes(notes)
    if len(chords) < 2:
        return 1.0  # Only one chord, trivially "unique"

    # Convert each chord to a pitch-class set (mod 12)
    def to_pc_set(chord_notes):
        pcs = frozenset(n.pitch % 12 for n in chord_notes)
        return pcs

    pc_sets = [to_pc_set(c) for c in chords]
    unique_count = len(set(pc_sets))

    return unique_count / len(chords)


# =============================================================================
# Feature: Total Chords (count of sustained chord attacks)
# =============================================================================

# Chord requirements to prevent gaming
MIN_CHORD_NOTES = 3      # Must have 3+ notes to count as chord
MIN_CHORD_DURATION = 0.1  # Must be held for 100ms+


def is_sustained_chord(chord_notes: List) -> bool:
    """
    Check if a note group is a real sustained chord.

    Requirements:
    - At least MIN_CHORD_NOTES notes (3+)
    - Average duration >= MIN_CHORD_DURATION (100ms+)

    Filters out single notes, intervals, and quick stabs.
    """
    if len(chord_notes) < MIN_CHORD_NOTES:
        return False

    avg_duration = sum(n.end - n.start for n in chord_notes) / len(chord_notes)
    return avg_duration >= MIN_CHORD_DURATION


def unique_chords(notes: List) -> int:
    """
    Count of unique sustained chord voicings in the piece.

    Only counts unique pitch-class sets from chords with 3+ notes held for 100ms+.
    Prevents gaming by repeating the same chord.

    Direction: Higher = better
    """
    if not notes:
        return 0

    chords = group_simultaneous_notes(notes)
    sustained = [c for c in chords if is_sustained_chord(c)]

    if not sustained:
        return 0

    pc_sets = [frozenset(n.pitch % 12 for n in c) for c in sustained]
    return len(set(pc_sets))


def unique_chords_per_bar(notes: List, num_bars: int = 4) -> float:
    """
    Unique sustained chords per bar.

    Direction: Higher = better
    """
    return unique_chords(notes) / num_bars


# =============================================================================
# Feature 4: Note Density (notes per second)
# =============================================================================

def note_density(notes: List) -> float:
    """
    Notes per second of comping.

    Rationale: Good comping is sparse - typically 1-3 notes/sec.
    Too dense = overplaying.
    Direction: Lower is often better (but not zero).
    """
    if len(notes) < 2:
        return 0.0

    duration = notes[-1].end - notes[0].start
    if duration <= 0:
        return 0.0

    return len(notes) / duration


# =============================================================================
# Feature 5: Syncopation Score
# =============================================================================

def syncopation_score(notes: List, beat_duration: float = 0.5) -> float:
    """
    Ratio of notes starting on off-beats.

    Rationale: Jazz comping emphasizes syncopation (off-beats).
    Playing on every downbeat is square/non-jazz.
    Direction: Higher is better.
    """
    if not notes:
        return 0.0

    chords = group_simultaneous_notes(notes)
    offbeat_count = 0

    for chord in chords:
        start = chord[0].start
        # Check if note is on an off-beat (between beats)
        beat_position = (start / beat_duration) % 1.0
        # Off-beat if not close to 0 or 1
        if 0.15 < beat_position < 0.85:
            offbeat_count += 1

    return offbeat_count / len(chords) if chords else 0.0


# =============================================================================
# Feature 6: Gap Ratio (rests between chords)
# =============================================================================

def gap_ratio(notes: List) -> float:
    """
    Ratio of time spent in silence between chord attacks.

    Rationale: Good comping has breathing room, not wall-to-wall chords.
    Direction: Moderate is better (0.3-0.6 ideal).
    """
    if len(notes) < 2:
        return 0.0

    chords = group_simultaneous_notes(notes)
    if len(chords) < 2:
        return 0.0

    total_duration = notes[-1].end - notes[0].start
    if total_duration <= 0:
        return 0.0

    # Calculate time between chord attacks
    gap_time = 0.0
    for i in range(len(chords) - 1):
        chord_end = max(n.end for n in chords[i])
        next_start = chords[i + 1][0].start
        if next_start > chord_end:
            gap_time += next_start - chord_end

    return gap_time / total_duration


# =============================================================================
# Feature 7: Chord Attack Variance
# =============================================================================

def attack_variance(notes: List) -> float:
    """
    Coefficient of variation in inter-onset intervals.

    Rationale: Mechanical comping has regular attacks.
    Good jazz comping varies the timing.
    Direction: Higher is better.
    """
    if len(notes) < 3:
        return 0.0

    chords = group_simultaneous_notes(notes)
    if len(chords) < 3:
        return 0.0

    # Get inter-onset intervals
    iois = []
    for i in range(len(chords) - 1):
        ioi = chords[i + 1][0].start - chords[i][0].start
        iois.append(ioi)

    mean_ioi = sum(iois) / len(iois)
    if mean_ioi <= 0:
        return 0.0

    variance = sum((ioi - mean_ioi) ** 2 for ioi in iois) / len(iois)
    return math.sqrt(variance) / mean_ioi  # CV


# =============================================================================
# Feature 8: Register Separation (from melody)
# =============================================================================

def register_separation(piano_notes: List, sax_notes: List) -> float:
    """
    Average pitch distance between piano and sax (melody).

    Rationale: Good comping stays out of the melody's register.
    Direction: Higher is better (within reason).
    """
    if not piano_notes or not sax_notes:
        return 0.0

    piano_avg = sum(n.pitch for n in piano_notes) / len(piano_notes)
    sax_avg = sum(n.pitch for n in sax_notes) / len(sax_notes)

    return abs(sax_avg - piano_avg)


def register_below_melody(piano_notes: List, sax_notes: List) -> float:
    """
    1.0 if piano is predominantly below melody, 0.0 otherwise.

    Rationale: Piano comping should be below the melody.
    Direction: Higher is better.
    """
    if not piano_notes or not sax_notes:
        return 0.0

    piano_avg = sum(n.pitch for n in piano_notes) / len(piano_notes)
    sax_avg = sum(n.pitch for n in sax_notes) / len(sax_notes)

    # Return how much lower piano is (normalized)
    diff = sax_avg - piano_avg
    return max(0.0, min(1.0, diff / 24.0))  # Normalize to ~2 octave range


# =============================================================================
# Feature 9: Voice Leading Smoothness
# =============================================================================

def voice_leading_smoothness(notes: List) -> float:
    """
    Inverse of average voice movement between consecutive chords.

    Rationale: Good voice leading minimizes jumps; notes move
    by step or stay the same.
    Direction: Higher is better.
    """
    if len(notes) < 4:
        return 0.0

    chords = group_simultaneous_notes(notes)
    if len(chords) < 2:
        return 0.0

    total_movement = 0.0
    comparisons = 0

    for i in range(len(chords) - 1):
        pitches1 = sorted(n.pitch for n in chords[i])
        pitches2 = sorted(n.pitch for n in chords[i + 1])

        # Compare each voice (min of the two chord sizes)
        min_voices = min(len(pitches1), len(pitches2))
        if min_voices > 0:
            movement = sum(abs(pitches2[j] - pitches1[j])
                          for j in range(min_voices))
            total_movement += movement / min_voices
            comparisons += 1

    if comparisons == 0:
        return 0.0

    avg_movement = total_movement / comparisons
    # Invert: 0 movement = 1.0, 12 semitones = ~0.0
    return max(0.0, 1.0 - avg_movement / 12.0)


# =============================================================================
# Feature 10: Interval Variety (within chords)
# =============================================================================

def interval_variety(notes: List) -> float:
    """
    Entropy of intervals used in voicings.

    Rationale: Professional voicings use varied intervals,
    not just stacked thirds.
    Direction: Higher is better.
    """
    if not notes:
        return 0.0

    chords = group_simultaneous_notes(notes)
    all_intervals = []

    for chord in chords:
        intervals = get_chord_intervals(chord)
        all_intervals.extend(intervals)

    if not all_intervals:
        return 0.0

    counts = Counter(all_intervals)
    total = len(all_intervals)
    entropy = -sum((c / total) * math.log2(c / total)
                   for c in counts.values() if c > 0)

    return entropy


# =============================================================================
# Feature 11: Rhythmic Pattern Repetition
# =============================================================================

def rhythmic_pattern_score(notes: List) -> float:
    """
    Score for repeated rhythmic patterns (motif consistency).

    Rationale: Good comping has recognizable rhythmic patterns
    but not monotonous.
    Direction: Moderate is better.
    """
    if len(notes) < 4:
        return 0.0

    chords = group_simultaneous_notes(notes)
    if len(chords) < 4:
        return 0.0

    # Quantize inter-onset intervals
    iois = []
    for i in range(len(chords) - 1):
        ioi = chords[i + 1][0].start - chords[i][0].start
        # Quantize to 16th notes (0.125 sec at 120 BPM)
        quantized = round(ioi / 0.125) * 0.125
        iois.append(quantized)

    # Count 2-grams
    if len(iois) < 2:
        return 0.0

    grams = [f"{iois[i]:.3f}_{iois[i+1]:.3f}" for i in range(len(iois) - 1)]
    counts = Counter(grams)

    # Score: ratio of repeated patterns
    repeated = sum(1 for c in counts.values() if c > 1)
    return repeated / len(counts) if counts else 0.0


# =============================================================================
# Feature 12: Dynamic Range (velocity variation)
# =============================================================================

def velocity_variance(notes: List) -> float:
    """
    Standard deviation of note velocities.

    Rationale: Good comping has dynamic expression,
    not constant velocity.
    Direction: Higher = better (more dynamics).

    Uses raw std to match drums/bass (not CV).
    """
    if len(notes) < 2:
        return 0.0

    velocities = [n.velocity for n in notes]
    mean_vel = sum(velocities) / len(velocities)
    variance = sum((v - mean_vel) ** 2 for v in velocities) / len(velocities)
    return math.sqrt(variance)


def duration_variety(notes: List) -> int:
    """
    Count of distinct note durations (quantized to 32nd notes).

    Varied note lengths = more expressive. Staccato chords, sustained pads.
    Direction: Higher = better.

    Matches drums/bass definition.
    """
    if not notes:
        return 0
    durations = [round((n.end - n.start) * 16) / 16 for n in notes]
    return len(set(durations))


# =============================================================================
# Aggregate Feature Extraction
# =============================================================================

def compute_piano_features(midi: "pretty_midi.PrettyMIDI") -> Dict[str, float]:
    """
    Compute all 12 piano comping features.

    Returns dict of feature_name -> value.
    """
    piano_notes = get_piano_notes(midi)
    sax_notes = get_sax_notes(midi)

    if len(piano_notes) < 4:
        return {}

    return {
        # Voicing quality
        'voicing_richness': voicing_richness(piano_notes),
        'avg_chord_spread': avg_chord_spread(piano_notes),
        'rootless_ratio': rootless_ratio(piano_notes),
        'chord_variety': chord_variety(piano_notes),

        # Rhythm/sparseness
        'note_density': note_density(piano_notes),
        'syncopation_score': syncopation_score(piano_notes),
        'gap_ratio': gap_ratio(piano_notes),
        'attack_variance': attack_variance(piano_notes),

        # Register
        'register_separation': register_separation(piano_notes, sax_notes),
        'register_below_melody': register_below_melody(piano_notes, sax_notes),

        # Voice leading
        'voice_leading_smoothness': voice_leading_smoothness(piano_notes),
        'interval_variety': interval_variety(piano_notes),

        # Rhythm patterns
        'rhythmic_pattern_score': rhythmic_pattern_score(piano_notes),

        # Dynamics
        'velocity_variance': velocity_variance(piano_notes),
    }


# =============================================================================
# Feature Metadata (for analysis)
# =============================================================================

FEATURE_METADATA = {
    'voicing_richness': {
        'description': 'Average notes per chord',
        'direction': 'optimal_4',  # 4 is ideal
        'category': 'voicing',
    },
    'avg_chord_spread': {
        'description': 'Average chord width in semitones',
        'direction': 'higher_better',
        'category': 'voicing',
    },
    'rootless_ratio': {
        'description': 'Ratio of rootless voicings',
        'direction': 'higher_better',
        'category': 'voicing',
    },
    'note_density': {
        'description': 'Notes per second',
        'direction': 'lower_better',  # Sparse comping is good
        'category': 'rhythm',
    },
    'syncopation_score': {
        'description': 'Ratio of off-beat attacks',
        'direction': 'higher_better',
        'category': 'rhythm',
    },
    'gap_ratio': {
        'description': 'Ratio of silence between chords',
        'direction': 'optimal_0.4',  # ~40% silence is good
        'category': 'rhythm',
    },
    'attack_variance': {
        'description': 'CV of inter-onset intervals',
        'direction': 'higher_better',
        'category': 'rhythm',
    },
    'register_separation': {
        'description': 'Pitch distance from melody',
        'direction': 'higher_better',
        'category': 'register',
    },
    'register_below_melody': {
        'description': 'Piano is below melody (0-1)',
        'direction': 'higher_better',
        'category': 'register',
    },
    'voice_leading_smoothness': {
        'description': 'Smooth voice motion (0-1)',
        'direction': 'higher_better',
        'category': 'voice_leading',
    },
    'interval_variety': {
        'description': 'Entropy of chord intervals',
        'direction': 'higher_better',
        'category': 'voicing',
    },
    'rhythmic_pattern_score': {
        'description': 'Ratio of repeated rhythm patterns',
        'direction': 'optimal_0.3',  # Some repetition, not too much
        'category': 'rhythm',
    },
    'velocity_variance': {
        'description': 'CV of note velocities',
        'direction': 'higher_better',
        'category': 'dynamics',
    },
}


# REVISED PIANO REWARD (2024-12 analysis on n=6 piano-mentioned subset)
# =============================================================================
#
# Validated features (Spearman correlation + standards holdout):
#   total_chords:    r=+1.00 (std=10.4, model=5.3) — more chords = better
#   chords_per_bar:  r=+0.77 (std=4.1, model=2.2)  — activity level
#
# Gates (50% penalty each):
#   cluster_gate:    any chord has adjacent semitones (minor 2nd)
#   out_of_key_gate: >10% of notes don't fit best diatonic key
#   robotic_gate:    velocity_variance=0 AND attack_variance=0 (keep)
#
# Removed (inverted or no signal):
#   repetition_gate (chord_variety was INVERTED: less variety = better in standards)
#   avg_chord_spread (conflicted with standards)
#   duration_variety (no signal on n=6)
#   velocity_variance as feature (keep only as gate input)

PIANO_REWARD_FEATURES = [
    "unique_chords",          # higher = better, capped at 3, weight 1.0
    "avg_chord_duration",     # higher = better, weight 1.5
    "cluster_ratio",          # lower = better (inverted)
    "out_of_key_ratio",       # lower = better (inverted)
    "chord_duration_variety", # higher = better
]

# Reference stats from n=101 MIDIs with unique chords
PIANO_REFERENCE_STATS = {
    'unique_chords': {'mean': 1.83, 'std': 1.16},
    'avg_chord_duration': {'mean': 0.307, 'std': 0.122},
    'cluster_ratio': {'mean': 0.278, 'std': 0.417},
    'out_of_key_ratio': {'mean': 0.061, 'std': 0.101},
    'chord_duration_variety': {'mean': 1.04, 'std': 0.20},
}

# Cap unique_chords contribution - diminishing returns after 3
UNIQUE_CHORDS_CAP = 3

# Weight for avg_chord_duration (more important than chord count)
AVG_CHORD_DURATION_WEIGHT = 1.5

# Bonus gate: +20% if final chord resolves to tonic (can only help, not hurt)
TONIC_BONUS = 1.2

# Register gate: 50% penalty if avg pitch below C3 (MIDI 48)
REGISTER_MIN_PITCH = 48  # C3 - floor of piano comping range
REGISTER_GATE_PENALTY = 0.5

# All 12 major scales (pitch classes)
MAJOR_SCALES = {
    0: {0, 2, 4, 5, 7, 9, 11},   # C major
    1: {1, 3, 5, 6, 8, 10, 0},   # Db major
    2: {2, 4, 6, 7, 9, 11, 1},   # D major
    3: {3, 5, 7, 8, 10, 0, 2},   # Eb major
    4: {4, 6, 8, 9, 11, 1, 3},   # E major
    5: {5, 7, 9, 10, 0, 2, 4},   # F major
    6: {6, 8, 10, 11, 1, 3, 5},  # F# major
    7: {7, 9, 11, 0, 2, 4, 6},   # G major
    8: {8, 10, 0, 1, 3, 5, 7},   # Ab major
    9: {9, 11, 1, 2, 4, 6, 8},   # A major
    10: {10, 0, 2, 3, 5, 7, 9},  # Bb major
    11: {11, 1, 3, 4, 6, 8, 10}, # B major
}

# Natural minor scales (relative minor of each major)
MINOR_SCALES = {
    0: {0, 2, 3, 5, 7, 8, 10},   # C minor
    1: {1, 3, 4, 6, 8, 9, 11},   # C# minor
    2: {2, 4, 5, 7, 9, 10, 0},   # D minor
    3: {3, 5, 6, 8, 10, 11, 1},  # Eb minor
    4: {4, 6, 7, 9, 11, 0, 2},   # E minor
    5: {5, 7, 8, 10, 0, 1, 3},   # F minor
    6: {6, 8, 9, 11, 1, 2, 4},   # F# minor
    7: {7, 9, 10, 0, 2, 3, 5},   # G minor
    8: {8, 10, 11, 1, 3, 4, 6},  # Ab minor
    9: {9, 11, 0, 2, 4, 5, 7},   # A minor
    10: {10, 0, 1, 3, 5, 6, 8},  # Bb minor
    11: {11, 1, 2, 4, 6, 7, 9},  # B minor
}


def has_cluster(chord_notes: List) -> bool:
    """
    Check if chord has cluster voicing (sounds like smashing keys).

    Catches:
    1. Adjacent semitones (minor 2nd interval) - e.g. [Db, D, F, B]
    2. Uniform small intervals (≤2 semitones, all same) - e.g. [Bb, C, D, Eb]
       This catches whole-tone stacks that sound atonal.
    """
    if len(chord_notes) < 2:
        return False
    pitches = sorted(n.pitch for n in chord_notes)
    intervals = [pitches[i + 1] - pitches[i] for i in range(len(pitches) - 1)]

    # Check for adjacent semitones
    if 1 in intervals:
        return True

    # Check for uniform small intervals (3+ notes, all intervals ≤2 and same)
    if len(intervals) >= 2:
        if all(i <= 2 for i in intervals) and len(set(intervals)) == 1:
            return True

    return False


def cluster_gate(notes: List) -> float:
    """
    Gate: 50% penalty if ANY chord has adjacent semitones.

    Catches: Track 4 "out of tune" (Db-D clash)
    Standards: 0% had clusters, Model: 8% had clusters
    """
    if not notes:
        return 1.0

    chords = group_simultaneous_notes(notes)
    for chord in chords:
        if has_cluster(chord):
            return CLUSTER_GATE_PENALTY
    return 1.0


def out_of_key_ratio(notes: List) -> float:
    """
    Ratio of notes that don't fit the best-matching diatonic scale.

    Tries all 24 major/minor keys, picks the one with highest fit,
    returns the ratio of notes that still don't fit.
    """
    if not notes:
        return 0.0

    pitch_classes = [n.pitch % 12 for n in notes]
    all_scales = list(MAJOR_SCALES.values()) + list(MINOR_SCALES.values())

    best_fit = 0
    for scale in all_scales:
        fit = sum(1 for pc in pitch_classes if pc in scale)
        best_fit = max(best_fit, fit)

    out_of_key = len(pitch_classes) - best_fit
    return out_of_key / len(pitch_classes)


def out_of_key_gate(notes: List) -> float:
    """
    Gate: 50% penalty if >10% of notes don't fit any diatonic scale.

    Catches: Track 5 (25% out-of-key), Track 4 (12% out-of-key)
    Standards: 0% out-of-key, Model: 6% out-of-key
    """
    ratio = out_of_key_ratio(notes)
    if ratio > OUT_OF_KEY_GATE_THRESHOLD:
        return OUT_OF_KEY_GATE_PENALTY
    return 1.0


def cluster_ratio(notes: List) -> float:
    """
    Ratio of chords containing adjacent semitones (clusters).

    Lower = better. Clusters sound dissonant/out-of-tune.
    """
    if not notes:
        return 0.0

    chords = group_simultaneous_notes(notes)
    sustained = [c for c in chords if is_sustained_chord(c)]

    if len(sustained) == 0:
        return 0.0

    clusters = sum(1 for c in sustained if has_cluster(c))
    return clusters / len(sustained)


def unique_chord_ratio(notes: List) -> float:
    """
    Ratio of unique chord voicings to total chords.

    Higher = better. More variety in voicings.
    """
    if not notes:
        return 0.0

    chords = group_simultaneous_notes(notes)
    sustained = [c for c in chords if is_sustained_chord(c)]

    if len(sustained) == 0:
        return 0.0

    pc_sets = [frozenset(n.pitch % 12 for n in c) for c in sustained]
    return len(set(pc_sets)) / len(sustained)


def avg_chord_duration(notes: List) -> float:
    """
    Average duration of sustained chords in seconds.

    Longer chords = more sustained comping. Higher = better.
    """
    if not notes:
        return 0.0

    chords = group_simultaneous_notes(notes)
    sustained = [c for c in chords if is_sustained_chord(c)]

    if not sustained:
        return 0.0

    durations = [sum(n.end - n.start for n in c) / len(c) for c in sustained]
    return sum(durations) / len(durations)


def chord_duration_variety(notes: List) -> int:
    """
    Count of unique chord durations (quantized to 50ms).

    Higher = better. Varied durations sound more musical.
    """
    if not notes:
        return 0

    chords = group_simultaneous_notes(notes)
    sustained = [c for c in chords if is_sustained_chord(c)]

    if len(sustained) == 0:
        return 0

    durations = []
    for chord in sustained:
        avg_dur = sum(n.end - n.start for n in chord) / len(chord)
        quantized = round(avg_dur * 20) / 20
        durations.append(quantized)

    return len(set(durations))


def detect_key(notes: List) -> tuple:
    """
    Detect the best-fit major or minor key for the notes.

    Returns (root_pitch_class, scale_set).
    """
    if not notes:
        return 0, set()

    pitch_classes = [n.pitch % 12 for n in notes]
    all_scales = list(MAJOR_SCALES.items()) + list(MINOR_SCALES.items())

    best_key, best_scale, best_fit = 0, set(), 0
    for key, scale in all_scales:
        fit = sum(1 for pc in pitch_classes if pc in scale)
        if fit > best_fit:
            best_key, best_scale, best_fit = key, scale, fit

    return best_key, best_scale


def tonic_resolution(notes: List) -> float:
    """
    Measure if final chord resolves to the tonic (key root).

    Returns 1.0 if:
        - There are 2+ unique chord voicings (actual movement)
        - Final chord contains the detected key's root

    Returns 0.0 if no movement or final doesn't have tonic.
    Can't "resolve" if you never left.
    """
    if not notes:
        return 0.0

    chords = group_simultaneous_notes(notes)
    sustained = [c for c in chords if is_sustained_chord(c)]

    if len(sustained) < 2:
        return 0.0

    # Must have actual harmonic movement to resolve
    pc_sets = [frozenset(n.pitch % 12 for n in c) for c in sustained]
    if len(set(pc_sets)) < 2:
        return 0.0  # No movement = no resolution

    key, scale = detect_key(notes)
    final_pcs = [n.pitch % 12 for n in sustained[-1]]

    return 1.0 if key in final_pcs else 0.0


def avg_pitch(notes: List) -> float:
    """Average MIDI pitch of all notes."""
    if not notes:
        return 0.0
    return sum(n.pitch for n in notes) / len(notes)


def register_gate(notes: List) -> float:
    """
    Gate: 50% penalty if average pitch below C3 (MIDI 48).

    Piano comping should be in the C3-C5 range (48-72).
    Below that is bass territory.
    """
    if not notes:
        return 1.0
    if avg_pitch(notes) < REGISTER_MIN_PITCH:
        return REGISTER_GATE_PENALTY
    return 1.0


def compute_piano_reward(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Compute piano comping reward using 5 features + tonic bonus.

    Features (z-sum):
        1. unique_chords: Count of unique voicings (capped at 3), weight 1.0
        2. avg_chord_duration: Sustained chords (higher = better), weight 1.5
        3. cluster_ratio: Chords with clusters (lower = better, inverted)
        4. out_of_key_ratio: Chromatic notes (lower = better, inverted)
        5. chord_duration_variety: Varied note lengths (higher = better)

    Bonus:
        +20% if final chord resolves to tonic (can only help)
    """
    piano_notes = get_piano_notes(midi)

    # Partial credit for outputs with few piano notes
    if len(piano_notes) < 4:
        if len(piano_notes) == 0:
            return -3.0
        return -2.0

    # Compute features
    uc = min(unique_chords(piano_notes), UNIQUE_CHORDS_CAP)  # Cap at 3
    acd = avg_chord_duration(piano_notes)
    cr = cluster_ratio(piano_notes)
    ook = out_of_key_ratio(piano_notes)
    cdv = chord_duration_variety(piano_notes)

    stats = PIANO_REFERENCE_STATS

    # Z-scores
    z_uc = clamp_z((uc - stats['unique_chords']['mean']) / stats['unique_chords']['std'])
    z_acd = clamp_z((acd - stats['avg_chord_duration']['mean']) / stats['avg_chord_duration']['std'])
    z_cr = clamp_z(-(cr - stats['cluster_ratio']['mean']) / stats['cluster_ratio']['std'])
    z_ook = clamp_z(-(ook - stats['out_of_key_ratio']['mean']) / stats['out_of_key_ratio']['std'])
    z_cdv = clamp_z((cdv - stats['chord_duration_variety']['mean']) / stats['chord_duration_variety']['std'])

    # Weighted sum (avg_chord_duration gets 1.5x)
    z_sum = z_uc + (z_acd * AVG_CHORD_DURATION_WEIGHT) + z_cr + z_ook + z_cdv

    # Tonic bonus (can only help, not hurt)
    if tonic_resolution(piano_notes) > 0:
        z_sum *= TONIC_BONUS

    # Register gate (penalty if avg pitch < C3)
    # If positive: halve it. If negative: make 1.5x worse.
    if register_gate(piano_notes) < 1.0:
        if z_sum > 0:
            z_sum *= REGISTER_GATE_PENALTY
        else:
            z_sum *= 1.5  # Make negative scores worse

    return z_sum


def compute_piano_reward_detailed(midi: "pretty_midi.PrettyMIDI") -> dict:
    """
    Compute piano reward with per-feature breakdown.

    Returns dict with:
        - total: final reward (z-sum × tonic_bonus)
        - tonic_bonus: 1.2 if resolved to tonic, 1.0 otherwise
        - features: {name: {raw, z_score, weight}} for each feature
    """
    piano_notes = get_piano_notes(midi)

    if len(piano_notes) < 4:
        partial = -3.0 if len(piano_notes) == 0 else -2.0
        return {
            "total": partial,
            "tonic_bonus": 1.0,
            "features": {},
        }

    # Compute features
    uc_raw = unique_chords(piano_notes)
    uc = min(uc_raw, UNIQUE_CHORDS_CAP)  # Cap at 3
    acd = avg_chord_duration(piano_notes)
    cr = cluster_ratio(piano_notes)
    ook = out_of_key_ratio(piano_notes)
    cdv = chord_duration_variety(piano_notes)
    tr = tonic_resolution(piano_notes)

    stats = PIANO_REFERENCE_STATS

    # Z-scores
    z_uc = clamp_z((uc - stats['unique_chords']['mean']) / stats['unique_chords']['std'])
    z_acd = clamp_z((acd - stats['avg_chord_duration']['mean']) / stats['avg_chord_duration']['std'])
    z_cr = clamp_z(-(cr - stats['cluster_ratio']['mean']) / stats['cluster_ratio']['std'])
    z_ook = clamp_z(-(ook - stats['out_of_key_ratio']['mean']) / stats['out_of_key_ratio']['std'])
    z_cdv = clamp_z((cdv - stats['chord_duration_variety']['mean']) / stats['chord_duration_variety']['std'])

    # Weighted sum
    z_sum = z_uc + (z_acd * AVG_CHORD_DURATION_WEIGHT) + z_cr + z_ook + z_cdv

    # Gates
    tonic_mult = TONIC_BONUS if tr > 0 else 1.0
    reg_failed = register_gate(piano_notes) < 1.0
    ap = avg_pitch(piano_notes)

    total = z_sum * tonic_mult
    if reg_failed:
        if total > 0:
            total *= REGISTER_GATE_PENALTY
        else:
            total *= 1.5  # Make negative scores worse

    return {
        "total": total,
        "tonic_bonus": tonic_mult,
        "register_failed": reg_failed,
        "avg_pitch": ap,
        "features": {
            "unique_chords": {"raw": uc_raw, "capped": uc, "z_score": z_uc, "weight": 1.0},
            "avg_chord_duration": {"raw": acd, "z_score": z_acd, "weight": AVG_CHORD_DURATION_WEIGHT},
            "cluster_ratio": {"raw": cr, "z_score": z_cr, "weight": 1.0},
            "out_of_key_ratio": {"raw": ook, "z_score": z_ook, "weight": 1.0},
            "chord_duration_variety": {"raw": cdv, "z_score": z_cdv, "weight": 1.0},
        },
    }


def compute_recommended_features(midi: "pretty_midi.PrettyMIDI") -> Dict[str, float]:
    """
    Compute the 2 reward features plus gate inputs for analysis.

    Returns the features used in compute_piano_reward() plus values
    used in gate conditions.
    """
    piano_notes = get_piano_notes(midi)

    if len(piano_notes) < 4:
        return {}

    return {
        # The 2 reward features
        'total_chords': total_chords(piano_notes),
        'chords_per_bar': chords_per_bar(piano_notes),
        # Gate inputs
        'out_of_key_ratio': out_of_key_ratio(piano_notes),
        'velocity_variance': velocity_variance(piano_notes),
        'attack_variance': attack_variance(piano_notes),
    }
