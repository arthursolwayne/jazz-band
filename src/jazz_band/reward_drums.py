"""
Drum Reward Functions for Jazz MIDI Generation.

Features designed to capture jazz drumming quality:
- Swing feel (timing variation, off-beat emphasis)
- Sparseness (kick restraint, dynamic range)
- Pattern variety (velocity dynamics, ghost notes)

MIDI Drum Mapping:
  kick=36, snare=38, hihat_closed=42, hihat_pedal=44, hihat_open=46, ride=51, crash=49
"""

import math
from collections import Counter
from typing import TYPE_CHECKING, List, Dict, Set, Tuple

if TYPE_CHECKING:
    import pretty_midi

# =============================================================================
# MIDI Drum Constants
# =============================================================================

KICK = 36
SNARE = 38
HIHAT_CLOSED = 42
HIHAT_PEDAL = 44
HIHAT_OPEN = 46
RIDE = 51
CRASH = 49

ALL_HIHATS = {HIHAT_CLOSED, HIHAT_PEDAL, HIHAT_OPEN}
TIMEKEEPING = ALL_HIHATS | {RIDE}


# =============================================================================
# Helpers
# =============================================================================

def get_drum_notes(midi: "pretty_midi.PrettyMIDI") -> List:
    """Extract all drum notes from MIDI, sorted by start time."""
    notes = []
    for inst in midi.instruments:
        if inst.is_drum:
            notes.extend(inst.notes)
    return sorted(notes, key=lambda n: n.start)


def get_notes_by_pitch(notes: List, pitches) -> List:
    """Filter notes by pitch(es)."""
    if isinstance(pitches, int):
        pitches = {pitches}
    return [n for n in notes if n.pitch in pitches]


def get_kick_notes(notes: List) -> List:
    """Extract kick drum notes (pitch 36)."""
    return get_notes_by_pitch(notes, KICK)


def get_snare_notes(notes: List) -> List:
    """Extract snare drum notes (pitch 38)."""
    return get_notes_by_pitch(notes, SNARE)


def get_hihat_notes(notes: List) -> List:
    """Extract hi-hat notes (closed, pedal, open)."""
    return get_notes_by_pitch(notes, ALL_HIHATS)


def get_ride_notes(notes: List) -> List:
    """Extract ride cymbal notes (pitch 51)."""
    return get_notes_by_pitch(notes, RIDE)


def get_timekeeping_notes(notes: List) -> List:
    """Extract hi-hat and ride notes (timekeeping pattern)."""
    return get_notes_by_pitch(notes, TIMEKEEPING)


def get_duration(notes: List) -> float:
    """Get total duration from first to last note end."""
    if not notes:
        return 0.0
    return max(n.end for n in notes) - min(n.start for n in notes)


# =============================================================================
# Feature Functions (12 total)
# =============================================================================

# --- Category: Kick Sparseness ---

def kick_sparseness(notes: List) -> float:
    """
    Ratio of (1 - kick_density) normalized by duration.

    Jazz drumming typically has very sparse or no kick drums - the bass
    carries the low end while drums focus on timekeeping and accents.

    Returns: 0.0 (heavy kicks) to 1.0 (no kicks)
    Direction: Higher = Better
    """
    duration = get_duration(notes)
    if duration <= 0:
        return 1.0

    kicks = get_kick_notes(notes)
    kicks_per_sec = len(kicks) / duration

    # Map density to sparseness: 0 kicks/sec -> 1.0, 2+ kicks/sec -> ~0
    # Using exponential decay
    return math.exp(-kicks_per_sec)


def kick_off_beat_ratio(notes: List) -> float:
    """
    Proportion of kicks that land off the beat.

    Mechanical drumming tends to put kicks squarely on beats 1 and 3.
    Jazz kicks, when used, often syncopate against the pulse.

    Returns: 0.0 (all on-beat) to 1.0 (all off-beat)
    Direction: Higher = Better (more syncopation)
    """
    kicks = get_kick_notes(notes)
    if not kicks:
        return 1.0  # No kicks = perfect sparseness

    beat_duration = 0.5  # Assume ~120 BPM
    on_beat = 0

    for k in kicks:
        beat_pos = (k.start % beat_duration) / beat_duration
        # Within 15% of beat start/end
        if beat_pos < 0.15 or beat_pos > 0.85:
            on_beat += 1

    return 1 - (on_beat / len(kicks))


# --- Category: Velocity Dynamics ---

def velocity_variance(notes: List) -> float:
    """
    Standard deviation of drum note velocities.

    Human drummers naturally vary their attack strength. Machine-generated
    patterns often have uniform velocity. Ghost notes, accents, and
    natural variation all contribute to higher variance.

    Returns: 0.0 to ~40 (typical range)
    Direction: Higher = Better
    """
    if len(notes) < 2:
        return 0.0

    velocities = [n.velocity for n in notes]
    mean = sum(velocities) / len(velocities)
    variance = sum((v - mean) ** 2 for v in velocities) / len(velocities)
    return math.sqrt(variance)


def ghost_note_ratio(notes: List) -> float:
    """
    Proportion of snare hits that are ghost notes (velocity < 80).

    Ghost notes are quiet snare hits that add texture and swing feel.
    They're a hallmark of jazz drumming, filling space between accents
    without overpowering the groove.

    Returns: 0.0 (no ghosts) to 1.0 (all ghosts)
    Direction: Higher = Better (within reason)
    """
    snares = get_snare_notes(notes)
    if not snares:
        return 0.0

    ghosts = [n for n in snares if n.velocity < 80]
    return len(ghosts) / len(snares)


def dynamics_range(notes: List) -> float:
    """
    Ratio of soft notes (<70 vel) to loud notes (>100 vel).

    Musical drumming has dynamic contrast - whisper-to-roar range.
    This captures the balance between quiet texture and accents.

    Returns: 0.0 to high values (capped at 5.0)
    Direction: Higher = Better (more soft notes relative to loud)
    """
    if not notes:
        return 0.0

    soft = len([n for n in notes if n.velocity < 70])
    loud = len([n for n in notes if n.velocity > 100])

    # Avoid division by zero, cap at 5.0
    return min(5.0, soft / max(1, loud))


# --- Category: Timing & Swing ---

def ioi_cv(notes: List) -> float:
    """
    Coefficient of variation in inter-onset intervals for timekeeping.

    Swing feel comes from varied timing - some notes rushed, some laid back.
    Perfectly regular intervals (low CV) sound mechanical. Higher CV
    indicates more human-like timing variation.

    Returns: 0.0 (perfectly regular) to ~2.0 (highly varied)
    Direction: Higher = Better (up to ~1.5)
    """
    timekeepers = sorted(get_timekeeping_notes(notes), key=lambda n: n.start)

    if len(timekeepers) < 2:
        return 0.0

    ioi = []
    for i in range(len(timekeepers) - 1):
        interval = timekeepers[i + 1].start - timekeepers[i].start
        if interval > 0:
            ioi.append(interval)

    if not ioi:
        return 0.0

    mean = sum(ioi) / len(ioi)
    if mean <= 0:
        return 0.0

    variance = sum((i - mean) ** 2 for i in ioi) / len(ioi)
    return math.sqrt(variance) / mean


def ioi_entropy(notes: List) -> float:
    """
    Entropy of quantized inter-onset intervals.

    Higher entropy means more varied rhythmic patterns - not just
    straight 8ths or quarter notes, but a mix of subdivisions.

    Returns: 0.0 to ~3.0 bits
    Direction: Higher = Better
    """
    timekeepers = sorted(get_timekeeping_notes(notes), key=lambda n: n.start)

    if len(timekeepers) < 2:
        return 0.0

    ioi = []
    for i in range(len(timekeepers) - 1):
        interval = timekeepers[i + 1].start - timekeepers[i].start
        # Quantize to 32nd notes at 120 BPM (0.0625s)
        quantized = round(interval * 16) / 16
        if quantized > 0:
            ioi.append(quantized)

    if not ioi:
        return 0.0

    counts = Counter(ioi)
    total = sum(counts.values())
    entropy = -sum((c / total) * math.log2(c / total) for c in counts.values() if c > 0)

    return entropy


# --- Category: Pattern Variety ---

def snare_pattern_entropy(notes: List) -> float:
    """
    Entropy of snare timing within a bar (8 divisions).

    Varied snare placement creates interesting patterns. Always on beats
    2 and 4 is predictable; varying placement adds musicality.

    Returns: 0.0 to ~3.0 bits
    Direction: Higher = Better (more varied placement)
    """
    snares = get_snare_notes(notes)
    if len(snares) < 2:
        return 0.0

    # Quantize to 8 positions per bar (assume 2-second bar at 120 BPM)
    bar_duration = 2.0
    positions = []
    for s in snares:
        pos = int((s.start % bar_duration) / bar_duration * 8) % 8
        positions.append(pos)

    counts = Counter(positions)
    total = len(positions)
    entropy = -sum((c / total) * math.log2(c / total) for c in counts.values() if c > 0)

    return entropy


def unique_drum_pitches(notes: List) -> int:
    """
    Count of distinct drum sounds used.

    More variety in drum sounds (kick, snare, toms, cymbals) indicates
    richer drumming vocabulary. Minimum viable is ~2-3 (basic kit).

    Returns: 0 to ~10+
    Direction: Higher = Better (within reason, 2-6 is typical for jazz)
    """
    return len(set(n.pitch for n in notes))


def duration_variety(notes: List) -> int:
    """
    Count of distinct note durations (quantized to 32nd notes).

    Varied note lengths indicate more expressive playing - short accents,
    longer sustains, etc.

    Returns: 1 to ~10+
    Direction: Higher = Better
    """
    if not notes:
        return 0

    durations = [round((n.end - n.start) * 16) / 16 for n in notes]
    return len(set(durations))


# --- Category: Jazz-Specific ---

def ride_presence(notes: List) -> float:
    """
    Presence of ride cymbal in timekeeping pattern.

    Jazz drumming often uses the ride cymbal as the primary timekeeping
    voice, rather than hi-hat. This is a signature of the style.

    Returns: 0.0 (no ride) to 1.0 (ride dominates timekeeping)
    Direction: Higher = Better for jazz feel
    """
    rides = get_ride_notes(notes)
    hihats = get_hihat_notes(notes)

    total = len(rides) + len(hihats)
    if total == 0:
        return 0.0

    return len(rides) / total


def snare_backbeat_ratio(notes: List) -> float:
    """
    Proportion of snares on traditional backbeat positions (beats 2, 4).

    While backbeats are essential, exclusive backbeat placement is
    mechanical. Some backbeat presence is good, but variation is better.

    Returns: 0.0 to 1.0
    Direction: Moderate is best (~0.3-0.5) - too high or too low is worse
    """
    snares = get_snare_notes(notes)
    if not snares:
        return 0.0

    bar_duration = 2.0  # 2 seconds per bar at 120 BPM
    backbeat_count = 0

    for s in snares:
        bar_pos = s.start % bar_duration
        # Backbeat at ~0.5s (beat 2) or ~1.5s (beat 4)
        if 0.4 < bar_pos < 0.6 or 1.4 < bar_pos < 1.6:
            backbeat_count += 1

    return backbeat_count / len(snares)


# =============================================================================
# Feature Extraction
# =============================================================================

ALL_FEATURES = [
    # Sparseness (lower kick density = better)
    ('kick_sparseness', kick_sparseness),
    ('kick_off_beat_ratio', kick_off_beat_ratio),
    # Dynamics
    ('velocity_variance', velocity_variance),
    ('ghost_note_ratio', ghost_note_ratio),
    ('dynamics_range', dynamics_range),
    # Timing
    ('ioi_cv', ioi_cv),
    ('ioi_entropy', ioi_entropy),
    # Pattern variety
    ('snare_pattern_entropy', snare_pattern_entropy),
    ('unique_drum_pitches', unique_drum_pitches),
    ('duration_variety', duration_variety),
    # Jazz-specific
    ('ride_presence', ride_presence),
    ('snare_backbeat_ratio', snare_backbeat_ratio),
]


def compute_drum_features(midi: "pretty_midi.PrettyMIDI") -> Dict[str, float]:
    """
    Compute all 12 drum features for a MIDI file.

    Returns dict of {feature_name: value}.
    Returns empty dict if no drum notes found.
    """
    drum_notes = get_drum_notes(midi)
    if not drum_notes:
        return {}

    return {name: func(drum_notes) for name, func in ALL_FEATURES}


def compute_drum_features_from_notes(notes: List) -> Dict[str, float]:
    """
    Compute all features from a pre-extracted note list.
    """
    if not notes:
        return {}

    return {name: func(notes) for name, func in ALL_FEATURES}


# =============================================================================
# Analysis Utilities
# =============================================================================

def correlation(x: List[float], y: List[float]) -> float:
    """Compute Pearson correlation coefficient."""
    n = len(x)
    if n < 2:
        return 0.0

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))

    var_x = sum((xi - mean_x) ** 2 for xi in x)
    var_y = sum((yi - mean_y) ** 2 for yi in y)

    denominator = math.sqrt(var_x * var_y)

    if denominator == 0:
        return 0.0

    return numerator / denominator


# =============================================================================
# Reward Function (Z-Sum Model)
# =============================================================================

# Statistics derived from 11 human-scored samples (5 standards + 6 model outputs)
# Model achieves R^2 = 0.886, MAE = 0.62 on validation set
REWARD_FEATURES = [
    "kick_off_beat_ratio",
    "snare_backbeat_ratio",
    "velocity_variance",
    "duration_variety",
]

REWARD_STATS = {
    "kick_off_beat_ratio": {"mean": 0.715909, "std": 0.261611},
    "snare_backbeat_ratio": {"mean": 0.097326, "std": 0.166207},
    "velocity_variance": {"mean": 13.775822, "std": 10.138839},
    "duration_variety": {"mean": 2.181818, "std": 0.833196},
}


def compute_drum_reward(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Compute drum reward using equal-weighted z-sum of 4 features.

    Features (validated via regression analysis, R^2 = 0.886):
    1. kick_off_beat_ratio: Jazz drums avoid on-beat kicks
    2. snare_backbeat_ratio: Varied snare placement (not just 2 & 4)
    3. velocity_variance: Dynamic variation (human feel)
    4. duration_variety: Mix of articulations

    Returns:
        float: Z-sum reward (higher = more jazz-like)
               Standards typically score > 0
               Machine outputs typically score < 0
    """
    features = compute_drum_features(midi)
    if not features:
        return -10.0  # Penalty for no drums

    z_sum = 0.0
    for fname in REWARD_FEATURES:
        value = features.get(fname, 0.0)
        mean = REWARD_STATS[fname]["mean"]
        std = REWARD_STATS[fname]["std"]
        if std > 0:
            z_sum += (value - mean) / std

    return z_sum


def compute_drum_reward_from_notes(notes: List) -> float:
    """
    Compute drum reward from pre-extracted note list.
    """
    if not notes:
        return -10.0

    features = compute_drum_features_from_notes(notes)

    z_sum = 0.0
    for fname in REWARD_FEATURES:
        value = features.get(fname, 0.0)
        mean = REWARD_STATS[fname]["mean"]
        std = REWARD_STATS[fname]["std"]
        if std > 0:
            z_sum += (value - mean) / std

    return z_sum


if __name__ == "__main__":
    # Quick test
    import pretty_midi

    test_file = "reference_riffs/moanin_jazzband.mid"
    midi = pretty_midi.PrettyMIDI(test_file)
    features = compute_drum_features(midi)
    reward = compute_drum_reward(midi)

    print(f"Drum features for {test_file}:")
    for name, value in features.items():
        print(f"  {name}: {value:.4f}")
    print(f"\nDrum reward (z-sum): {reward:.3f}")
