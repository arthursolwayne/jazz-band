"""
Symbol Engine: Shared MIDI generation logic for RLVR and GEPA.

- SYSTEM_PROMPT: Instructions for LLM to generate pretty_midi code
- execute_midi_code(): Run LLM-generated code, return PrettyMIDI object
- compute_reward(): 6-feature z-sum reward
"""

import json
import math
from pathlib import Path
from collections import Counter
from typing import TYPE_CHECKING, List, Dict, Tuple

if TYPE_CHECKING:
    import pretty_midi

# Timing constants (variable BPM)
TARGET_DURATION = 6.0  # 4 bars at ~160 BPM
DURATION_TOLERANCE = 3.0  # Allow 3-9 seconds (flexible for different tempos)

# Paths
PROMPT_FILE = Path(__file__).parent.parent.parent / "prompts" / "composer.md"
STATS_FILE = Path(__file__).parent.parent.parent / "baselines" / "reward_stats.json"

# Load system prompt
SYSTEM_PROMPT = PROMPT_FILE.read_text().strip()


# =============================================================================
# Code Execution
# =============================================================================

def execute_midi_code(code: str):
    """
    Execute LLM-generated code and return PrettyMIDI object.

    Returns:
        (midi, cleaned_code, error) - midi is None if execution failed
    """
    import pretty_midi

    # Clean code (remove markdown fences if present)
    if "```python" in code:
        code = code.split("```python")[1].split("```")[0]
    elif "```" in code:
        code = code.split("```")[1].split("```")[0]

    # Execute in isolated namespace
    namespace = {"pretty_midi": pretty_midi}
    try:
        exec(code, namespace)
        return namespace.get("midi", None), code, None
    except Exception as e:
        return None, code, str(e)


# =============================================================================
# Reward Computation
# =============================================================================

def load_stats() -> Dict[str, Tuple[float, float]]:
    """Load feature stats from JSON. Returns dict of {feature: (mean, std)}."""
    if not STATS_FILE.exists():
        raise FileNotFoundError(f"Stats file not found: {STATS_FILE}")
    data = json.loads(STATS_FILE.read_text())
    return {f: (s['mean'], s['std']) for f, s in data['features'].items()}


def save_stats(features_data: List[Dict], path: Path = STATS_FILE) -> Dict:
    """
    Recompute and save stats from a list of feature dicts.
    Call this after collecting new human-scored samples.
    """
    feature_names = list(features_data[0].keys())
    stats = {"n_samples": len(features_data), "features": {}}

    for f in feature_names:
        vals = [d[f] for d in features_data]
        mean = sum(vals) / len(vals)
        std = math.sqrt(sum((v - mean)**2 for v in vals) / len(vals))
        stats["features"][f] = {"mean": round(mean, 4), "std": round(std, 4)}

    path.write_text(json.dumps(stats, indent=2))
    return stats


def passes_sanity_checks(midi: "pretty_midi.PrettyMIDI") -> bool:
    """Hard validity checks for full reward eligibility."""
    if midi is None:
        return False

    # Has notes
    total_notes = sum(len(inst.notes) for inst in midi.instruments)
    if total_notes == 0:
        return False

    # Duration in range
    max_end = max((n.end for inst in midi.instruments for n in inst.notes), default=0)
    if abs(max_end - TARGET_DURATION) > DURATION_TOLERANCE:
        return False

    # Has enough sax notes for feature computation
    sax_notes = get_sax_notes(midi)
    if len(sax_notes) < 4:
        return False

    return True


def compute_partial_reward(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Partial credit for outputs that fail sanity checks but show progress.

    Returns 0.0 to 0.25 based on how close the output is to valid.
    This ensures GRPO gets variance even among "failures".
    """
    if midi is None:
        return 0.0  # Code crashed - no credit

    reward = 0.0

    # Credit for having any notes at all
    total_notes = sum(len(inst.notes) for inst in midi.instruments)
    if total_notes > 0:
        reward += 0.05
        # Bonus for more notes (diminishing returns)
        reward += min(0.05, 0.01 * math.log(total_notes + 1))

    # Credit for having sax track
    sax_notes = get_sax_notes(midi)
    if len(sax_notes) > 0:
        reward += 0.05
        # Bonus for approaching the 4-note threshold
        reward += min(0.05, 0.015 * len(sax_notes))

    # Partial credit for duration (closer to target = more credit)
    if total_notes > 0:
        max_end = max((n.end for inst in midi.instruments for n in inst.notes), default=0)
        duration_error = abs(max_end - TARGET_DURATION)
        if duration_error <= DURATION_TOLERANCE:
            reward += 0.05  # Within tolerance
        elif duration_error <= DURATION_TOLERANCE * 2:
            reward += 0.02  # Close but not quite

    return min(reward, 0.25)  # Cap partial rewards


def get_sax_notes(midi: "pretty_midi.PrettyMIDI") -> List:
    """Extract sax track notes (program 66) or fallback to first track."""
    for inst in midi.instruments:
        if not inst.is_drum and inst.program == 66:
            return sorted(inst.notes, key=lambda n: n.start)
    # Fallback: first non-drum track
    for inst in midi.instruments:
        if not inst.is_drum:
            return sorted(inst.notes, key=lambda n: n.start)
    return []


def detect_key_root(pitches: List[int]) -> int:
    """Estimate key root as most common pitch class."""
    pc_counts = Counter(p % 12 for p in pitches)
    return pc_counts.most_common(1)[0][0] if pc_counts else 0


# =============================================================================
# Feature Functions (6 features)
# =============================================================================

def melodic_entropy(notes: List) -> float:
    """Entropy of interval distribution. Higher = more varied."""
    if len(notes) < 2:
        return 0
    intervals = [notes[i+1].pitch - notes[i].pitch for i in range(len(notes)-1)]
    counts = Counter(intervals)
    total = len(intervals)
    return -sum((c/total) * math.log2(c/total) for c in counts.values() if c > 0)


def dur_cv(notes: List) -> float:
    """Coefficient of variation in note durations. Higher = more varied."""
    if len(notes) < 2:
        return 0
    durs = [n.end - n.start for n in notes]
    mean = sum(durs) / len(durs)
    var = sum((d - mean)**2 for d in durs) / len(durs)
    return math.sqrt(var) / mean if mean > 0 else 0


def sax_arpeggio_runs(notes: List) -> int:
    """Count chord tone runs (3+ consecutive chord tones)."""
    if len(notes) < 3:
        return 0
    pitches = [n.pitch for n in notes]
    root = detect_key_root(pitches)
    chord_tones = {root, (root+4) % 12, (root+7) % 12, (root+11) % 12}
    runs = current = 0
    for p in pitches:
        if p % 12 in chord_tones:
            current += 1
            if current >= 3:
                runs += 1
        else:
            current = 0
    return runs


def peak_not_late(notes: List) -> int:
    """1 if melodic peak is in first 66%, 0 otherwise."""
    if len(notes) < 2:
        return 0
    pitches = [n.pitch for n in notes]
    peak_idx = pitches.index(max(pitches))
    return 1 if peak_idx / (len(pitches) - 1) <= 0.66 else 0


def blue_ratio(notes: List) -> float:
    """Ratio of blue notes (b3, b5, b7 relative to detected root)."""
    if not notes:
        return 0
    pitches = [n.pitch for n in notes]
    root = detect_key_root(pitches)
    blue_pcs = {(root + 3) % 12, (root + 6) % 12, (root + 10) % 12}
    return sum(1 for p in pitches if p % 12 in blue_pcs) / len(pitches)


def rhythm_2grams(notes: List) -> int:
    """Count of repeated rhythm 2-grams. Higher = more rhythmic motifs."""
    if len(notes) < 2:
        return 0
    beat = 0.375  # Eighth note at 120 BPM

    def quantize(d):
        if d < beat * 0.75:
            return 'S'  # Short
        elif d < beat * 1.5:
            return 'M'  # Medium
        elif d < beat * 3:
            return 'L'  # Long
        else:
            return 'X'  # Extra long

    durs = [n.end - n.start for n in notes]
    seq = [quantize(d) for d in durs]
    grams = [seq[i] + seq[i+1] for i in range(len(seq)-1)]
    counts = Counter(grams)
    return sum(1 for c in counts.values() if c > 1)


# =============================================================================
# Variety Gates (prevent degenerate outputs)
# =============================================================================

def unique_durations(notes: List) -> int:
    """Count distinct note durations (quantized to 32nd notes)."""
    if len(notes) < 2:
        return 0
    durs = [round((n.end - n.start) * 8) / 8 for n in notes]
    return len(set(durs))


def has_rests(notes: List) -> bool:
    """Check if there are gaps between notes (musical phrasing)."""
    if len(notes) < 2:
        return False
    notes_sorted = sorted(notes, key=lambda n: n.start)
    for i in range(len(notes_sorted) - 1):
        if notes_sorted[i+1].start - notes_sorted[i].end > 0.1:
            return True
    return False


# =============================================================================
# Main Reward Function
# =============================================================================

def compute_reward(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Compute reward for a generated MIDI.

    Reward structure (designed for GRPO):
        - 0.0 to 0.25: Partial credit (failed sanity but shows progress)
        - 0.3 to 1.0: Full scoring (passes sanity, z-score features)
        - Soft gates: Multiply by 0.5 for each failed variety gate

    This ensures all rewards are non-negative, giving GRPO
    variance to learn from even when most outputs fail.
    """
    # Failed outputs get partial credit, not negative reward
    if not passes_sanity_checks(midi):
        return compute_partial_reward(midi)

    # Extract sax notes (guaranteed >= 4 by sanity check)
    sax_notes = get_sax_notes(midi)

    # Soft gates: variety multiplier (penalize degenerate outputs)
    # NOTE: These are SAX-specific gates. Other instruments have their own gates.
    variety = 1.0
    if unique_durations(sax_notes) < 2:
        variety *= 0.5  # 50% penalty for monotone rhythm
    if not has_rests(sax_notes):
        variety *= 0.5  # 50% penalty for no phrasing

    # Load reference stats
    stats = load_stats()

    # Compute 6 features
    features = {
        'melodic_entropy': melodic_entropy(sax_notes),
        'dur_cv': dur_cv(sax_notes),
        'sax_arpeggio_runs': sax_arpeggio_runs(sax_notes),
        'peak_not_late': peak_not_late(sax_notes),
        'blue_ratio': blue_ratio(sax_notes),
        'rhythm_2grams': rhythm_2grams(sax_notes),
    }

    # Z-score sum
    raw_reward = 0.0
    for f, value in features.items():
        mean, std = stats[f]
        if std > 0:
            raw_reward += (value - mean) / std

    # Apply variety gates to raw z-sum
    # NOTE: Sigmoid is applied in compute_combined_reward() for final output
    return raw_reward * variety


def compute_features(midi: "pretty_midi.PrettyMIDI") -> Dict[str, float]:
    """
    Compute all 6 features for a MIDI file.
    Useful for analysis and updating stats.
    """
    sax_notes = get_sax_notes(midi)
    if len(sax_notes) < 4:
        return {}

    return {
        'melodic_entropy': melodic_entropy(sax_notes),
        'dur_cv': dur_cv(sax_notes),
        'sax_arpeggio_runs': sax_arpeggio_runs(sax_notes),
        'peak_not_late': peak_not_late(sax_notes),
        'blue_ratio': blue_ratio(sax_notes),
        'rhythm_2grams': rhythm_2grams(sax_notes),
    }


# =============================================================================
# Combined Reward (all instruments)
# =============================================================================

def compute_combined_reward(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Compute combined reward from all 5 instrument rewards.

    Sums raw z-scores from:
        - Sax (6 features)
        - Bass (2 features)
        - Piano (4 features)
        - Drums (4 features)
        - Ensemble (4 features)

    Then applies ONE final sigmoid to map to [0, 1] range.
    This ensures non-negative rewards for GRPO training.

    Returns:
        float: Combined reward in [0, 1] range.
               0.5 = all instruments at mean (z-sum = 0)
               ~1.0 = significantly above mean
               ~0.0 = significantly below mean
    """
    from jazz_band.reward_bass import compute_bass_reward
    from jazz_band.reward_piano import compute_piano_reward
    from jazz_band.reward_drums import compute_drum_reward
    from jazz_band.reward_ensemble import compute_ensemble_reward

    # Sum all raw z-scores
    z_sum = 0.0
    z_sum += compute_reward(midi)          # Sax
    z_sum += compute_bass_reward(midi)     # Bass
    z_sum += compute_piano_reward(midi)    # Piano
    z_sum += compute_drum_reward(midi)     # Drums
    z_sum += compute_ensemble_reward(midi) # Ensemble

    # Map to [0, 1] using sigmoid
    # Scale factor 6 chosen because we have ~20 features total
    # GRPO normalizes within groups anyway, so absolute range doesn't matter
    return 1 / (1 + math.exp(-z_sum / 6))
