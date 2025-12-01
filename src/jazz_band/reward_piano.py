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
    Coefficient of variation in note velocities.

    Rationale: Good comping has dynamic expression,
    not constant velocity.
    Direction: Moderate is better.
    """
    if len(notes) < 2:
        return 0.0

    velocities = [n.velocity for n in notes]
    mean_vel = sum(velocities) / len(velocities)

    if mean_vel <= 0:
        return 0.0

    variance = sum((v - mean_vel) ** 2 for v in velocities) / len(velocities)
    return math.sqrt(variance) / mean_vel


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


# =============================================================================
# RECOMMENDED REWARD FEATURES (based on rigorous statistical analysis)
# =============================================================================
#
# Analysis on n=11 samples (5 standards score=9.0, 3 opus 4.5-5.5, 3 RLVR 3.0-4.5)
# See baselines/notes.md and baselines/piano_analysis.py for methodology.
#
# Individual Feature Correlations (sorted by |r|):
#   gap_ratio:                r=-0.853  R^2=0.728  (DOMINANT)
#   attack_variance:          r=+0.626  R^2=0.392
#   velocity_variance:        r=+0.618  R^2=0.382
#   voice_leading_smoothness: r=-0.611  R^2=0.373  (contradicts theory)
#   register_below_melody:    r=+0.339  R^2=0.115
#   rootless_ratio:           r=+0.336  R^2=0.113
#   register_separation:      r=+0.246  R^2=0.061
#   avg_chord_spread:         r=+0.088  R^2=0.008
#
# Exhaustive N-Feature Search (Z-Sum with equal weights):
#   N=1: R^2=0.728 -> gap_ratio
#   N=2: R^2=0.770 -> gap_ratio, voice_leading_smoothness
#   N=3: R^2=0.822 -> voicing_richness, avg_chord_spread, gap_ratio
#   N=4: R^2=0.897 -> avg_chord_spread, gap_ratio, register_separation, velocity_variance
#   N=5: R^2=0.851 -> (overfitting)
#
# Selected 4 features (R^2=0.897, MAE=0.62):
#   1. avg_chord_spread:    r=+0.088 (higher=better) - open voicings
#   2. gap_ratio:           r=-0.853 (lower=better)  - active comping
#   3. register_separation: r=+0.246 (higher=better) - stay out of melody
#   4. velocity_variance:   r=+0.618 (higher=better) - dynamic expression
#
# Collinearity warning: gap_ratio and velocity_variance are correlated (r=-0.84)
# but the combination still yields the best z-sum R^2.
# =============================================================================

# Model-derived stats (n=568 RLVR outputs, 2024-11-30)
PIANO_REFERENCE_STATS = {
    'avg_chord_spread': {'mean': 7.994, 'std': 2.363, 'direction': 1},
    'gap_ratio': {'mean': 0.601, 'std': 0.170, 'direction': -1},
    'register_separation': {'mean': 3.805, 'std': 3.692, 'direction': 1},
    'velocity_variance': {'mean': 0.003, 'std': 0.013, 'direction': 1},
}


def compute_piano_reward(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Compute piano comping reward using 4 statistically validated features.

    Model performance (n=11 samples):
        R^2 = 0.897 (89.7% variance explained)
        MAE = 0.62 points

    Reward structure (designed for GRPO):
        - 0.0 to 0.10: Partial credit (few piano notes)
        - 0.3 to 1.0: Full scoring (z-sum of 4 features)

    Features used (equal-weighted z-sum):
        1. avg_chord_spread:    Open voicings (higher = better)
        2. gap_ratio:           Active comping (lower = better)
        3. register_separation: Stay out of melody range (higher = better)
        4. velocity_variance:   Dynamic expression (higher = better)

    Gate (soft penalty):
        - velocity_variance == 0 AND attack_variance == 0: 50% penalty (robotic)
    """
    piano_notes = get_piano_notes(midi)
    sax_notes = get_sax_notes(midi)

    # Partial credit for outputs with few piano notes
    if len(piano_notes) < 4:
        if len(piano_notes) == 0:
            return 0.0
        return 0.05 + 0.05 * len(piano_notes) / 4  # 0.05 to 0.10

    # Compute the 4 recommended features
    spread = avg_chord_spread(piano_notes)
    gap = gap_ratio(piano_notes)
    reg_sep = register_separation(piano_notes, sax_notes)
    vel_var = velocity_variance(piano_notes)

    # Also compute attack_variance for the gate
    attack_var = attack_variance(piano_notes)

    # Gate: penalize completely robotic outputs (no variation at all)
    variety = 1.0
    if vel_var == 0 and attack_var == 0:
        variety *= 0.5  # No dynamic or rhythmic variation = mechanical

    # Z-score computation using reference stats
    stats = PIANO_REFERENCE_STATS

    # Feature 1: avg_chord_spread (higher = better)
    spread_z = (spread - stats['avg_chord_spread']['mean']) / stats['avg_chord_spread']['std']
    spread_z = max(-3.0, min(3.0, spread_z))

    # Feature 2: gap_ratio (lower = better, direction = -1)
    gap_z = -(gap - stats['gap_ratio']['mean']) / stats['gap_ratio']['std']
    gap_z = max(-3.0, min(3.0, gap_z))

    # Feature 3: register_separation (higher = better)
    reg_z = (reg_sep - stats['register_separation']['mean']) / stats['register_separation']['std']
    reg_z = max(-3.0, min(3.0, reg_z))

    # Feature 4: velocity_variance (higher = better)
    vel_z = (vel_var - stats['velocity_variance']['mean']) / stats['velocity_variance']['std']
    vel_z = max(-3.0, min(3.0, vel_z))

    # Sum z-scores (equal weights)
    raw_reward = spread_z + gap_z + reg_z + vel_z

    # Apply variety gate to raw z-sum
    # NOTE: Sigmoid is applied in compute_combined_reward() for final output
    return raw_reward * variety


def compute_piano_reward_detailed(midi: "pretty_midi.PrettyMIDI") -> dict:
    """
    Compute piano reward with per-feature breakdown.

    Returns dict with:
        - total: final reward (z-sum * gate)
        - variety_gate: gate multiplier applied
        - features: {name: {raw, z_score}} for each feature
    """
    piano_notes = get_piano_notes(midi)
    sax_notes = get_sax_notes(midi)

    if len(piano_notes) < 4:
        partial = 0.0 if len(piano_notes) == 0 else 0.05 + 0.05 * len(piano_notes) / 4
        return {
            "total": partial,
            "variety_gate": 0.0,
            "features": {},
        }

    # Compute raw values
    spread = avg_chord_spread(piano_notes)
    gap = gap_ratio(piano_notes)
    reg_sep = register_separation(piano_notes, sax_notes)
    vel_var = velocity_variance(piano_notes)
    attack_var = attack_variance(piano_notes)

    # Gate
    variety = 1.0
    if vel_var == 0 and attack_var == 0:
        variety *= 0.5

    stats = PIANO_REFERENCE_STATS

    # Z-scores with ±3 clamp
    spread_z = (spread - stats['avg_chord_spread']['mean']) / stats['avg_chord_spread']['std']
    spread_z = max(-3.0, min(3.0, spread_z))
    gap_z = -(gap - stats['gap_ratio']['mean']) / stats['gap_ratio']['std']  # inverted
    gap_z = max(-3.0, min(3.0, gap_z))
    reg_z = (reg_sep - stats['register_separation']['mean']) / stats['register_separation']['std']
    reg_z = max(-3.0, min(3.0, reg_z))
    vel_z = (vel_var - stats['velocity_variance']['mean']) / stats['velocity_variance']['std']
    vel_z = max(-3.0, min(3.0, vel_z))

    z_sum = spread_z + gap_z + reg_z + vel_z

    return {
        "total": z_sum * variety,
        "variety_gate": variety,
        "features": {
            "avg_chord_spread": {"raw": spread, "z_score": spread_z},
            "gap_ratio": {"raw": gap, "z_score": gap_z},
            "register_separation": {"raw": reg_sep, "z_score": reg_z},
            "velocity_variance": {"raw": vel_var, "z_score": vel_z},
        },
    }


def compute_recommended_features(midi: "pretty_midi.PrettyMIDI") -> Dict[str, float]:
    """
    Compute the 4 recommended features for analysis.

    Returns the features used in compute_piano_reward() plus attack_variance
    which is used in the gate condition.
    """
    piano_notes = get_piano_notes(midi)
    sax_notes = get_sax_notes(midi)

    if len(piano_notes) < 4:
        return {}

    return {
        # The 4 reward features
        'avg_chord_spread': avg_chord_spread(piano_notes),
        'gap_ratio': gap_ratio(piano_notes),
        'register_separation': register_separation(piano_notes, sax_notes),
        'velocity_variance': velocity_variance(piano_notes),
        # Gate feature
        'attack_variance': attack_variance(piano_notes),
    }
