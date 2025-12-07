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

from .symbol_engine import clamp_z

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

# Latin percussion (GM drum map)
LATIN_PERCUSSION = {
    56,  # cowbell
    65, 66,  # timbales hi/lo
    62, 63, 64,  # congas (mute, open, lo)
    60, 61,  # bongos hi/lo
    67, 68,  # agogo hi/lo
    69,  # cabasa
    70,  # maracas
    73, 74,  # guiro long/short
    75,  # claves
}


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

def rhythmic_vocabulary(notes: List) -> float:
    """
    Measure diversity of inter-onset intervals across all drum notes.

    Good drums have varied rhythmic vocabulary:
    - Fast IOIs (< 0.1s): bursts, rolls, fills
    - Medium IOIs (0.1-0.3s): groove, swing patterns
    - Slow IOIs (> 0.3s): space, breathing room

    Boring drums are monotonous (all same speed).
    Spam is all fast. Sparse is all slow.
    Great drums have ALL THREE in balance.

    Returns: 0.0 to ~2.0 bits (entropy of IOI distribution)
    Direction: Higher = Better (more diverse vocabulary)
    """
    if len(notes) < 3:
        return 0.0

    sorted_notes = sorted(notes, key=lambda n: n.start)

    # Compute all inter-onset intervals (include simultaneous as 0.001)
    iois = []
    for i in range(len(sorted_notes) - 1):
        ioi = sorted_notes[i + 1].start - sorted_notes[i].start
        # Treat simultaneous notes as very fast IOI
        iois.append(max(0.001, ioi))

    if len(iois) < 2:
        return 0.0

    # Bucket IOIs into rhythmic categories
    # Fast (bursts): < 0.1s
    # Medium-fast: 0.1-0.2s (16th notes at 120bpm)
    # Medium: 0.2-0.4s (8th notes)
    # Slow: 0.4-0.8s (quarter notes)
    # Very slow: > 0.8s (space)
    buckets = [0, 0, 0, 0, 0]
    for ioi in iois:
        if ioi < 0.1:
            buckets[0] += 1
        elif ioi < 0.2:
            buckets[1] += 1
        elif ioi < 0.4:
            buckets[2] += 1
        elif ioi < 0.8:
            buckets[3] += 1
        else:
            buckets[4] += 1

    # Compute entropy of bucket distribution
    total = sum(buckets)
    if total == 0:
        return 0.0

    entropy = 0.0
    for count in buckets:
        if count > 0:
            p = count / total
            entropy -= p * math.log2(p)

    return entropy


def voice_independence(notes: List) -> float:
    """
    Measure how independently different drum voices move.

    Polyrhythmic layering requires voices doing DIFFERENT things.
    If kick, snare, and hi-hat all hit together, that's unison (boring).
    If they interleave and complement, that's independence (interesting).

    Measures: what fraction of time windows have exactly ONE voice active?
    Higher = more independent movement, less unison.

    Returns: 0.0 (all unison) to 1.0 (perfect independence)
    Direction: Higher = Better
    """
    if len(notes) < 4:
        return 0.0

    duration = get_duration(notes)
    if duration <= 0:
        return 0.0

    # Use 50ms windows (fast enough to catch independence)
    window_size = 0.05
    num_windows = int(duration / window_size) + 1

    # Track which voices are active in each window
    # Group by rough categories: kick, snare, cymbals, other
    window_voices = [set() for _ in range(num_windows)]

    for n in notes:
        win_idx = min(int(n.start / window_size), num_windows - 1)
        if n.pitch == KICK:
            window_voices[win_idx].add('kick')
        elif n.pitch == SNARE:
            window_voices[win_idx].add('snare')
        elif n.pitch in TIMEKEEPING:
            window_voices[win_idx].add('cymbal')
        else:
            window_voices[win_idx].add('other')

    # Count windows with exactly 1 voice (independent movement)
    single_voice = sum(1 for wv in window_voices if len(wv) == 1)
    # Count windows with any activity
    active_windows = sum(1 for wv in window_voices if len(wv) > 0)

    if active_windows == 0:
        return 0.0

    return single_voice / active_windows


def density_contrast(notes: List) -> float:
    """
    Measure contrast between dense and sparse moments.

    Great drums have BOTH:
    - Dense moments (fills, bursts, building intensity)
    - Sparse moments (breathing room, space for other instruments)

    Uses Gini coefficient of note density across time windows.
    High Gini = notes concentrated in few windows (bursty)
    Low Gini = notes evenly spread (monotonous)

    Returns: 0.0 (perfectly even) to 1.0 (all notes in one moment)
    Direction: Higher = Better (more contrast), but extreme = spam
    """
    if len(notes) < 4:
        return 0.0

    duration = get_duration(notes)
    if duration <= 0:
        return 0.0

    # Use 0.25s windows (quarter note at 120bpm)
    window_size = 0.25
    num_windows = max(1, int(duration / window_size))

    # Count notes per window
    counts = [0] * num_windows
    for n in notes:
        win_idx = min(int(n.start / window_size), num_windows - 1)
        counts[win_idx] += 1

    # Compute Gini coefficient
    counts_sorted = sorted(counts)
    n = len(counts_sorted)
    if n == 0 or sum(counts_sorted) == 0:
        return 0.0

    # Gini formula: sum of |xi - xj| / (2 * n * mean)
    total = sum(counts_sorted)
    mean = total / n

    cumsum = 0
    weighted_sum = 0
    for i, c in enumerate(counts_sorted):
        cumsum += c
        weighted_sum += (i + 1) * c

    # Gini = (2 * weighted_sum) / (n * total) - (n + 1) / n
    gini = (2 * weighted_sum) / (n * total) - (n + 1) / n

    return max(0.0, min(1.0, gini))


def burst_quality(notes: List) -> float:
    """
    Combined metric for drum burst/fill quality.

    Great drum fills have:
    1. High density contrast (clustered notes vs space)
    2. Low rhythmic vocabulary (IOIs concentrated = uniform bursts)

    Formula: contrast * (1 - vocab/max_vocab)

    This rewards concentrated bursts separated by breathing room.
    Hard to game: spam gives low contrast, sparse gives low contrast,
    random gives high vocab. Only real bursts score high.

    Returns: 0.0 to ~0.7
    Direction: Higher = Better
    """
    contrast = density_contrast(notes)
    vocab = rhythmic_vocabulary(notes)
    max_vocab = math.log2(5)  # 2.32 bits for 5 IOI buckets

    inv_vocab = 1 - (vocab / max_vocab)
    return contrast * inv_vocab


def density_arc(notes: List) -> float:
    """
    Measure variation in note density across bars.

    Good drum phrases have ARC - they're not static loops.
    Bar 1 might be sparse, bar 2-3 build, bar 4 has a fill.
    Flat density = boring loop. High variance = development.

    Uses coefficient of variation (std/mean) of notes-per-bar.

    Returns: 0.0 (perfectly flat) to ~1.5 (high variation)
    Direction: Higher = Better (more arc/development)
    """
    if len(notes) < 4:
        return 0.0

    duration = get_duration(notes)
    if duration <= 0:
        return 0.0

    # Assume 2s bars at 120bpm
    bar_dur = 2.0
    num_bars = max(1, int(duration / bar_dur))

    # Count notes per bar
    bar_counts = [0] * num_bars
    for n in notes:
        bar_idx = min(int(n.start / bar_dur), num_bars - 1)
        bar_counts[bar_idx] += 1

    if num_bars < 2:
        return 0.0

    mean = sum(bar_counts) / num_bars
    if mean <= 0:
        return 0.0

    variance = sum((c - mean) ** 2 for c in bar_counts) / num_bars
    std = math.sqrt(variance)

    # Coefficient of variation
    return std / mean


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


def syncopation_ratio(notes: List) -> float:
    """
    Ratio of notes on syncopated (offbeat) positions.

    Latin feel comes from heavy syncopation - notes landing between
    the main beats, especially on 16th note subdivisions.

    Quantizes to 16th note grid:
    - On-beat: positions 0, 4, 8, 12 (beats 1, 2, 3, 4)
    - Upbeat: positions 2, 6, 10, 14 (the "ands")
    - Offbeat: everything else (16th note syncopation)

    Returns: 0.0 (all on-beat) to 1.0 (all offbeat)
    Direction: Higher = more Latin/syncopated feel
    """
    if not notes:
        return 0.0

    # Assume 120 BPM = 2 sec per bar, 16 16th notes per bar
    sixteenth = 0.125  # seconds

    offbeat_positions = {1, 3, 5, 7, 9, 11, 13, 15}
    offbeat_count = 0

    for n in notes:
        pos = int((n.start % 2.0) / sixteenth) % 16
        if pos in offbeat_positions:
            offbeat_count += 1

    return offbeat_count / len(notes)


def latin_percussion_ratio(notes: List) -> float:
    """
    Ratio of Latin percussion sounds to total drum notes.

    Latin jazz uses specific percussion: cowbell, timbales, congas,
    bongos, agogo, cabasa, maracas, guiro, claves.

    Basic kit (kick, snare, hihat) = 0.0
    Full Latin percussion section = higher values

    Returns: 0.0 (no Latin) to 1.0 (all Latin percussion)
    Direction: Higher = more Latin character
    """
    if not notes:
        return 0.0

    latin_notes = [n for n in notes if n.pitch in LATIN_PERCUSSION]
    return len(latin_notes) / len(notes)


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
    # Latin jazz
    ('syncopation_ratio', syncopation_ratio),
    ('latin_percussion_ratio', latin_percussion_ratio),
    # Contrast & vocabulary (captures bursts, layering, variety)
    ('rhythmic_vocabulary', rhythmic_vocabulary),
    ('voice_independence', voice_independence),
    ('density_contrast', density_contrast),
    ('burst_quality', burst_quality),
    # Arc/development
    ('density_arc', density_arc),
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

# Validated features (2024-12-06)
# Based on standards analysis + human listening tests:
#   voice_independence: hihat/snare NOT locked (standards: 45-100%)
#   density_arc: variation across bars (not static loop)
#   ghost_note_ratio: quiet snares add texture (standards have them)
#   kick_sparseness: fewer kicks = better (standards: ~1.0)
REWARD_FEATURES = [
    "voice_independence",
    "density_arc",
    "ghost_note_ratio",
    "kick_sparseness",
]

# Model-derived stats (n=7089 RLVR outputs, 2024-12-06)
REWARD_STATS = {
    "voice_independence": {"mean": 0.584, "std": 0.196},
    "density_arc": {"mean": 0.299, "std": 0.284},
    "ghost_note_ratio": {"mean": 0.001, "std": 0.031},
    "kick_sparseness": {"mean": 0.405, "std": 0.120},
}


# Gate threshold: reject mechanical patterns where hihat/snare are locked
VOICE_INDEPENDENCE_GATE = 0.35


def compute_drum_reward(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Compute drum reward using equal-weighted z-sum of 4 features.

    Features (validated via standards analysis + human listening, 2024-12-06):
    1. voice_independence: Hihat/snare NOT locked together (standards: 45-100%)
    2. density_arc: Variation across bars, not static loop
    3. ghost_note_ratio: Quiet snares add texture
    4. kick_sparseness: Fewer kicks = better (standards have ~none)

    Gate: voice_independence >= 0.35 required (rejects mechanical patterns)

    Returns:
        float: Z-sum reward (higher = more jazz-like)
    """
    features = compute_drum_features(midi)
    if not features:
        return -10.0  # Penalty for no drums

    # Gate: reject mechanical patterns where voices are locked together
    if features.get("voice_independence", 0) < VOICE_INDEPENDENCE_GATE:
        return -10.0  # Fail gate

    z_sum = 0.0
    for fname in REWARD_FEATURES:
        value = features.get(fname, 0.0)
        mean = REWARD_STATS[fname]["mean"]
        std = REWARD_STATS[fname]["std"]
        if std > 0:
            z = (value - mean) / std
            z = clamp_z(z)
            z_sum += z

    return z_sum


def compute_drum_reward_detailed(midi: "pretty_midi.PrettyMIDI") -> dict:
    """
    Compute drum reward with per-feature breakdown.

    Returns dict with:
        - total: final reward (z-sum), or -10.0 if gated
        - gated: True if failed voice_independence gate
        - features: {name: {raw, z_score}} for each feature
    """
    features = compute_drum_features(midi)
    if not features:
        return {
            "total": -10.0,
            "gated": True,
            "features": {},
        }

    # Check gate
    voice_ind = features.get("voice_independence", 0)
    gated = voice_ind < VOICE_INDEPENDENCE_GATE

    feature_details = {}
    z_sum = 0.0
    for fname in REWARD_FEATURES:
        raw = features.get(fname, 0.0)
        mean = REWARD_STATS[fname]["mean"]
        std = REWARD_STATS[fname]["std"]
        z = (raw - mean) / std if std > 0 else 0.0
        z = clamp_z(z)
        z_sum += z
        feature_details[fname] = {"raw": raw, "z_score": z}

    return {
        "total": -10.0 if gated else z_sum,
        "gated": gated,
        "features": feature_details,
    }


def compute_drum_reward_from_notes(notes: List) -> float:
    """
    Compute drum reward from pre-extracted note list.
    """
    if not notes:
        return -10.0

    features = compute_drum_features_from_notes(notes)

    # Gate: reject mechanical patterns
    if features.get("voice_independence", 0) < VOICE_INDEPENDENCE_GATE:
        return -10.0

    z_sum = 0.0
    for fname in REWARD_FEATURES:
        value = features.get(fname, 0.0)
        mean = REWARD_STATS[fname]["mean"]
        std = REWARD_STATS[fname]["std"]
        if std > 0:
            z = (value - mean) / std
            z = clamp_z(z)
            z_sum += z

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
