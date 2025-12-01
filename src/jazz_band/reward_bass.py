"""
Bass Reward Features: Feature extractors for jazz walking bass evaluation.

Designed for 4-bar jazz intros at 160 BPM (6.0 seconds).
Features are computed from bass track (program=33) notes.

Feature Categories:
1. RHYTHM: Walking feel, quarter note pulse
2. PITCH: Register, root motion
3. MELODIC: Interval variety, direction changes
4. GROOVE: Chromatic approaches, beat targeting
"""

import math
from collections import Counter
from typing import TYPE_CHECKING, List, Dict, Tuple

if TYPE_CHECKING:
    import pretty_midi


# =============================================================================
# Constants
# =============================================================================

# At 160 BPM: quarter=0.375s, eighth=0.1875s, half=0.75s
QUARTER_NOTE = 0.375
EIGHTH_NOTE = 0.1875
TOLERANCE = 0.05  # Timing tolerance for beat detection

# Bass register (MIDI notes)
BASS_REGISTER_LOW = 28   # E1
BASS_REGISTER_HIGH = 55  # G3


# =============================================================================
# Bass Note Extraction
# =============================================================================

def get_bass_notes(midi: "pretty_midi.PrettyMIDI") -> List:
    """
    Extract bass track notes (program=33) or fallback to lowest-register track.
    Returns notes sorted by start time.
    """
    # First try: explicit bass program
    for inst in midi.instruments:
        if not inst.is_drum and inst.program == 33:
            return sorted(inst.notes, key=lambda n: n.start)

    # Fallback: find lowest-register non-drum track
    best_track = None
    lowest_avg_pitch = float('inf')

    for inst in midi.instruments:
        if not inst.is_drum and inst.notes:
            avg_pitch = sum(n.pitch for n in inst.notes) / len(inst.notes)
            if avg_pitch < lowest_avg_pitch:
                lowest_avg_pitch = avg_pitch
                best_track = inst.notes

    if best_track:
        return sorted(best_track, key=lambda n: n.start)
    return []


# =============================================================================
# RHYTHM FEATURES
# =============================================================================

def quarter_note_ratio(notes: List) -> float:
    """
    Ratio of inter-onset intervals (IOIs) that are quarter notes.

    Walking bass should have mostly quarter note IOIs.
    Higher = better (more walking feel).

    Reference samples: IOIs around 0.375-0.4s
    Bad samples: IOIs at 0.25s (too fast) or irregular
    """
    if len(notes) < 2:
        return 0.0

    quarter_count = 0
    total = len(notes) - 1

    for i in range(total):
        ioi = notes[i+1].start - notes[i].start
        # Quarter note = 0.375s, allow some swing tolerance
        if 0.3 <= ioi <= 0.5:
            quarter_count += 1

    return quarter_count / total


def ioi_swing(notes: List) -> float:
    """
    Coefficient of variation in IOIs (natural timing variation / swing).

    Human jazz bass has natural timing variation (swing feel).
    Machine outputs are TOO regular (robotic, CV=0).
    Higher CV = more swing = better (correlates with human quality).

    Reference: CV = 0.4-0.98 (natural swing)
    Bad samples: CV = 0 (robotic)
    """
    if len(notes) < 3:
        return 0.0

    iois = [notes[i+1].start - notes[i].start for i in range(len(notes)-1)]
    # Filter out overlapping notes (IOI=0)
    iois = [x for x in iois if x > 0.01]

    if len(iois) < 2:
        return 0.0

    mean = sum(iois) / len(iois)
    if mean <= 0:
        return 0.0

    var = sum((x - mean)**2 for x in iois) / len(iois)
    cv = math.sqrt(var) / mean

    # Higher CV = more swing = better
    return cv


def beat_density(notes: List) -> float:
    """
    Notes per bar (normalized for 4 bars at 160 BPM).

    Walking bass: ~4 notes per bar (one per beat).
    Too few = sparse; too many = busy eighth-note lines.

    Returns: 1.0 for 4 notes/bar, decreasing for deviation
    """
    if not notes:
        return 0.0

    # At 160 BPM, 4 bars = 6.0 seconds
    duration = max(n.end for n in notes) - min(n.start for n in notes)
    if duration <= 0:
        return 0.0

    # Bars 2-4 = 4.5s of bass (bar 1 is drums only per prompt)
    effective_bars = 3.0
    notes_per_bar = len(notes) / effective_bars

    # Ideal is 4 notes/bar; score drops off for deviation
    ideal = 4.0
    deviation = abs(notes_per_bar - ideal)

    return max(0, 1 - deviation / ideal)


# =============================================================================
# PITCH FEATURES
# =============================================================================

def bass_register_ratio(notes: List) -> float:
    """
    Ratio of notes in proper bass register (E1-G3, MIDI 28-55).

    Walking bass should stay low. Higher = better.

    Reference: pitches 24-50
    Bad samples: pitches 48-77 (too high)
    """
    if not notes:
        return 0.0

    in_register = sum(1 for n in notes
                      if BASS_REGISTER_LOW <= n.pitch <= BASS_REGISTER_HIGH)
    return in_register / len(notes)


def root_on_downbeat(notes: List) -> float:
    """
    How often does beat 1 of a bar have a root/5th pitch class?

    Walking bass convention: root or 5th on downbeats.
    Approximated by detecting most common pitch classes on bar starts.

    Higher = better (harmonic grounding).
    """
    if len(notes) < 4:
        return 0.0

    # Detect root as most common pitch class
    pc_counts = Counter(n.pitch % 12 for n in notes)
    root_pc = pc_counts.most_common(1)[0][0]
    fifth_pc = (root_pc + 7) % 12

    # Find notes on downbeats (multiples of bar length)
    # Bar 1: 0.0s, Bar 2: 1.5s, Bar 3: 3.0s, Bar 4: 4.5s
    bar_starts = [1.5, 3.0, 4.5]  # Skip bar 1 (drums only)

    downbeat_notes = []
    for n in notes:
        for bar_start in bar_starts:
            if abs(n.start - bar_start) < TOLERANCE:
                downbeat_notes.append(n)
                break

    if not downbeat_notes:
        return 0.5  # No clear downbeats, neutral score

    root_fifth_count = sum(1 for n in downbeat_notes
                          if n.pitch % 12 in (root_pc, fifth_pc))
    return root_fifth_count / len(downbeat_notes)


def pitch_range(notes: List) -> float:
    """
    Pitch range in semitones (normalized).

    Walking bass should have moderate range (octave to two octaves).
    Too narrow = boring; too wide = jumping around unnaturally.

    Returns: 1.0 for 12-24 semitone range, lower otherwise
    """
    if len(notes) < 2:
        return 0.0

    pitches = [n.pitch for n in notes]
    span = max(pitches) - min(pitches)

    # Ideal range: 12-24 semitones (octave to two octaves)
    if 12 <= span <= 24:
        return 1.0
    elif span < 12:
        return span / 12  # Penalize narrow range
    else:
        return max(0, 1 - (span - 24) / 24)  # Penalize too wide


# =============================================================================
# MELODIC FEATURES
# =============================================================================

def interval_variety(notes: List) -> float:
    """
    Entropy of interval distribution.

    Walking bass should have variety: steps, skips, occasional leaps.
    Purely chromatic (all -1s) = low variety = bad.

    Higher = better (more varied intervals).
    """
    if len(notes) < 2:
        return 0.0

    intervals = [notes[i+1].pitch - notes[i].pitch for i in range(len(notes)-1)]
    counts = Counter(intervals)
    total = len(intervals)

    if total == 0:
        return 0.0

    entropy = -sum((c/total) * math.log2(c/total) for c in counts.values() if c > 0)

    # Normalize: max entropy for this length is log2(n)
    max_entropy = math.log2(total) if total > 1 else 1
    return entropy / max_entropy if max_entropy > 0 else 0


def direction_changes(notes: List) -> float:
    """
    Ratio of direction changes in the melodic line.

    Walking bass should change direction, not just descend/ascend.
    Reference: varied intervals with direction changes
    Bad: purely descending chromatic lines

    Higher = better (more direction changes).
    """
    if len(notes) < 3:
        return 0.0

    intervals = [notes[i+1].pitch - notes[i].pitch for i in range(len(notes)-1)]
    # Filter out repeated notes
    intervals = [x for x in intervals if x != 0]

    if len(intervals) < 2:
        return 0.0

    changes = 0
    for i in range(len(intervals) - 1):
        # Direction change: sign changes
        if (intervals[i] > 0) != (intervals[i+1] > 0):
            changes += 1

    return changes / (len(intervals) - 1)


def non_chromatic_ratio(notes: List) -> float:
    """
    Ratio of NON-chromatic intervals (not half-step).

    Reference samples: 0% chromatic (all intervals > 1 semitone)
    Machine outputs: 40-100% chromatic (too much half-step motion)

    Higher = better (less chromatic = more musical variety).
    """
    if len(notes) < 2:
        return 0.0

    intervals = [abs(notes[i+1].pitch - notes[i].pitch) for i in range(len(notes)-1)]
    non_chromatic = sum(1 for i in intervals if i != 1)
    return non_chromatic / len(intervals)


def stepwise_ratio(notes: List) -> float:
    """
    Ratio of stepwise motion (1-2 semitones).

    Walking bass is primarily stepwise but not exclusively.
    Ideal: 50-70% stepwise, rest skips/leaps.

    Returns: 1.0 for 50-70%, lower otherwise
    """
    if len(notes) < 2:
        return 0.0

    intervals = [abs(notes[i+1].pitch - notes[i].pitch) for i in range(len(notes)-1)]
    stepwise = sum(1 for i in intervals if 1 <= i <= 2)
    ratio = stepwise / len(intervals)

    # Ideal: 50-70% stepwise
    if 0.5 <= ratio <= 0.7:
        return 1.0
    elif ratio < 0.5:
        return ratio / 0.5
    else:
        return max(0, 1 - (ratio - 0.7) / 0.3)


# =============================================================================
# GROOVE FEATURES
# =============================================================================

def note_count(notes: List) -> int:
    """
    Simple note count.

    Walking bass: 10-16 notes for 3 bars (bars 2-4).
    Too few = sparse; too many = busy.
    """
    return len(notes)


def note_count_normalized(notes: List) -> float:
    """
    Note count normalized to ideal range.

    Ideal: 10-16 notes for bars 2-4 at 160 BPM.
    Returns: 1.0 for ideal range, lower otherwise
    """
    n = len(notes)
    if n == 0:
        return 0.0

    # Ideal: 10-16 notes (about 3-4 per bar for 3 bars)
    if 10 <= n <= 16:
        return 1.0
    elif n < 10:
        return n / 10
    else:
        return max(0, 1 - (n - 16) / 16)


def repeated_note_ratio(notes: List) -> float:
    """
    Ratio of repeated consecutive pitches (same note twice).

    Prompt says "never the same note twice", so lower = better.
    We return 1 - ratio so higher = better.
    """
    if len(notes) < 2:
        return 1.0  # No repetition possible

    repeated = sum(1 for i in range(len(notes)-1)
                   if notes[i].pitch == notes[i+1].pitch)
    ratio = repeated / (len(notes) - 1)

    return 1 - ratio  # Invert: less repetition = higher score


# =============================================================================
# Feature Registry
# =============================================================================

BASS_FEATURES = {
    # Rhythm features
    'quarter_note_ratio': (quarter_note_ratio, 'higher'),
    'ioi_swing': (ioi_swing, 'higher'),
    'beat_density': (beat_density, 'higher'),

    # Pitch features
    'bass_register_ratio': (bass_register_ratio, 'higher'),
    'root_on_downbeat': (root_on_downbeat, 'higher'),
    'pitch_range': (pitch_range, 'higher'),

    # Melodic features
    'interval_variety': (interval_variety, 'higher'),
    'direction_changes': (direction_changes, 'higher'),
    'non_chromatic_ratio': (non_chromatic_ratio, 'higher'),
    'stepwise_ratio': (stepwise_ratio, 'higher'),

    # Groove features
    'note_count_normalized': (note_count_normalized, 'higher'),
    'repeated_note_ratio': (repeated_note_ratio, 'higher'),
}


def compute_bass_features(midi: "pretty_midi.PrettyMIDI") -> Dict[str, float]:
    """
    Compute all bass features for a MIDI file.
    Returns dict of {feature_name: value}.
    """
    notes = get_bass_notes(midi)
    if len(notes) < 2:
        return {}

    return {name: func(notes) for name, (func, _) in BASS_FEATURES.items()}


# =============================================================================
# Correlation Analysis
# =============================================================================

def pearson_correlation(x: List[float], y: List[float]) -> float:
    """Compute Pearson correlation coefficient."""
    n = len(x)
    if n < 2:
        return 0.0

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denom_x = math.sqrt(sum((xi - mean_x)**2 for xi in x))
    denom_y = math.sqrt(sum((yi - mean_y)**2 for yi in y))

    if denom_x == 0 or denom_y == 0:
        return 0.0

    return numerator / (denom_x * denom_y)


if __name__ == "__main__":
    # Test on sample files
    import pretty_midi

    # Sample files with human scores
    samples = [
        # References (score=9.0)
        ("reference_riffs/moanin_jazzband.mid", 9.0),
        ("reference_riffs/sowhat_jazzband.mid", 9.0),
        ("reference_riffs/songformyfather_jazzband.mid", 9.0),
        ("reference_riffs/watermelon_jazzband.mid", 9.0),
        ("reference_riffs/cantina_jazzband.mid", 9.0),
        # Opus outputs
        ("baselines/opus/20251129_131245/run_000/output.mid", 5.0),
        ("baselines/opus/20251129_131327/run_000/output.mid", 5.5),
        ("baselines/opus/20251129_131404/run_000/output.mid", 4.5),
        # RLVR outputs
        ("artifacts/rollouts/composer-001_20251130_091414/step_000/rollout_000/output.mid", 4.5),
        ("artifacts/rollouts/composer-001_20251130_091414/step_000/rollout_001/output.mid", 4.0),
        ("artifacts/rollouts/composer-001_20251129_202149/step_000/rollout_002/output.mid", 3.0),
    ]

    # Compute features
    results = []
    for path, score in samples:
        try:
            midi = pretty_midi.PrettyMIDI(path)
            features = compute_bass_features(midi)
            if features:
                features['human_score'] = score
                features['path'] = path
                results.append(features)
                print(f"{path.split('/')[-1]}: {len(get_bass_notes(midi))} notes")
            else:
                print(f"{path}: No bass notes or too few")
        except Exception as e:
            print(f"{path}: Error - {e}")

    # Print feature table
    print("\n" + "="*80)
    print("FEATURE VALUES")
    print("="*80)
    feature_names = list(BASS_FEATURES.keys())
    header = "File".ljust(25) + "Score" + "  " + "  ".join(f[:8].ljust(8) for f in feature_names)
    print(header)
    print("-"*len(header))

    for r in results:
        name = r['path'].split('/')[-1][:24].ljust(25)
        score = f"{r['human_score']:.1f}".ljust(6)
        vals = "  ".join(f"{r.get(f, 0):.3f}".ljust(8) for f in feature_names)
        print(f"{name}{score}{vals}")

    # Compute correlations
    print("\n" + "="*80)
    print("CORRELATIONS WITH HUMAN SCORE")
    print("="*80)

    scores = [r['human_score'] for r in results]
    correlations = {}

    for f in feature_names:
        vals = [r.get(f, 0) for r in results]
        r = pearson_correlation(vals, scores)
        correlations[f] = r
        flag = " WEAK" if abs(r) < 0.4 else " *STRONG*"
        print(f"{f:30} r={r:+.3f}{flag}")

    # Recommendations
    print("\n" + "="*80)
    print("RECOMMENDATIONS")
    print("="*80)
    strong = [(f, r) for f, r in correlations.items() if abs(r) >= 0.4]
    strong.sort(key=lambda x: -abs(x[1]))

    print(f"\nStrong features (|r| >= 0.4): {len(strong)}")
    for f, r in strong:
        print(f"  {f}: r={r:+.3f}")

    print("\n" + "-"*80)
    print("RECOMMENDED FINAL 4 FEATURES FOR REWARD FUNCTION:")
    print("-"*80)
    print("""
Based on signal strength and low collinearity:

1. non_chromatic_ratio (r=+0.846) - MELODIC
   Strongest signal. References use varied intervals, machines over-use chromatic.

2. ioi_swing (r=+0.697) - RHYTHM
   Human players have natural timing variation; machines are robotic.

3. direction_changes (r=+0.552) - MELODIC
   References change melodic direction; machines descend/ascend monotonically.

4. bass_register_ratio (r=+0.423) - PITCH
   Keeps bass in proper register (MIDI 28-55). Machines drift too high.

Note: Dropped repeated_note_ratio (r=-0.571) because the negative correlation
reflects that references sometimes use pedal tones (intentional repetition),
which the prompt actually discourages. This is a mismatch between the prompt
instruction and actual jazz practice.
""")


# =============================================================================
# FINAL REWARD FUNCTION (from regression analysis)
# =============================================================================

# Model-derived stats (n=568 RLVR outputs, 2024-11-30)
BASS_REWARD_STATS = {
    "ioi_swing": {"mean": 0.043, "std": 0.173},
    "non_chromatic_ratio": {"mean": 0.487, "std": 0.259},
}

# Features selected via exhaustive search
# R^2 = 0.7558 (75.6% variance explained)
# MAE = 0.91 (on 1-9 scale)
BASS_REWARD_FEATURES = ["ioi_swing", "non_chromatic_ratio"]


def has_direction_variety(notes: List) -> bool:
    """
    Gate: Check if bass has direction changes (not monotonic ascending/descending).

    Returns False if all intervals go the same direction (all up or all down).
    """
    if len(notes) < 3:
        return True  # Not enough notes to judge

    pitches = [n.pitch for n in notes]
    intervals = [pitches[i+1] - pitches[i] for i in range(len(pitches)-1)]

    # Filter out repeated notes (interval = 0)
    nonzero = [i for i in intervals if i != 0]
    if len(nonzero) < 2:
        return True  # Not enough movement to judge

    # Check if all nonzero intervals have same sign (all up or all down)
    signs = [1 if i > 0 else -1 for i in nonzero]
    return not all(s == signs[0] for s in signs)


def compute_bass_reward(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Compute bass reward using equal-weighted z-sum model.

    Features (selected via exhaustive search, R^2=0.7558):
    1. ioi_swing (r=+0.697): Timing variation/swing
    2. non_chromatic_ratio (r=+0.846): Interval variety (not all half-steps)

    Gate:
    - has_direction_variety: 50% penalty for monotonic bassline

    Returns:
        Z-sum reward (higher = better). Typical range: -3 to +3.
        Standards average +1.5, model outputs average -0.5.
    """
    notes = get_bass_notes(midi)
    if len(notes) < 2:
        return -3.0  # Penalize empty/sparse bass

    # Bass-specific gate
    gate_multiplier = 1.0
    if not has_direction_variety(notes):
        gate_multiplier *= 0.5  # 50% penalty for monotonic bassline

    # Compute feature values
    swing = ioi_swing(notes)
    non_chrom = non_chromatic_ratio(notes)

    # Z-score normalization with ±3 clamp
    z_swing = (swing - BASS_REWARD_STATS["ioi_swing"]["mean"]) / BASS_REWARD_STATS["ioi_swing"]["std"]
    z_swing = max(-3.0, min(3.0, z_swing))
    z_non_chrom = (non_chrom - BASS_REWARD_STATS["non_chromatic_ratio"]["mean"]) / BASS_REWARD_STATS["non_chromatic_ratio"]["std"]
    z_non_chrom = max(-3.0, min(3.0, z_non_chrom))

    # Equal-weighted z-sum with gate
    raw_reward = z_swing + z_non_chrom
    return raw_reward * gate_multiplier


def compute_bass_reward_detailed(midi: "pretty_midi.PrettyMIDI") -> dict:
    """
    Compute bass reward with per-feature breakdown.

    Returns dict with:
        - total: final reward (z-sum * gate)
        - direction_gate: gate multiplier applied
        - features: {name: {raw, z_score}} for each feature
    """
    notes = get_bass_notes(midi)
    if len(notes) < 2:
        return {
            "total": -3.0,
            "direction_gate": 0.0,
            "features": {},
        }

    # Gate
    gate = 1.0 if has_direction_variety(notes) else 0.5

    # Features
    swing = ioi_swing(notes)
    non_chrom = non_chromatic_ratio(notes)

    z_swing = (swing - BASS_REWARD_STATS["ioi_swing"]["mean"]) / BASS_REWARD_STATS["ioi_swing"]["std"]
    z_swing = max(-3.0, min(3.0, z_swing))
    z_non_chrom = (non_chrom - BASS_REWARD_STATS["non_chromatic_ratio"]["mean"]) / BASS_REWARD_STATS["non_chromatic_ratio"]["std"]
    z_non_chrom = max(-3.0, min(3.0, z_non_chrom))

    z_sum = z_swing + z_non_chrom

    return {
        "total": z_sum * gate,
        "direction_gate": gate,
        "features": {
            "ioi_swing": {"raw": swing, "z_score": z_swing},
            "non_chromatic_ratio": {"raw": non_chrom, "z_score": z_non_chrom},
        },
    }
