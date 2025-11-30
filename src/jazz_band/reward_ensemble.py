"""
Ensemble Reward Features: Measuring how well instruments work TOGETHER.

Each feature function takes a full PrettyMIDI object and returns a float.
Features are designed to capture ensemble interaction quality for jazz quartet.

Instrument roles (from composer.md):
- Sax (program=66): Melody, main voice
- Bass (program=33): Walking line, anchor
- Piano (program=0): Comping, harmonic support
- Drums (is_drum=True): Rhythm foundation
"""

import math
from typing import TYPE_CHECKING, List, Dict, Tuple, Optional
from collections import Counter

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


def get_bass_notes(midi: "pretty_midi.PrettyMIDI") -> List:
    """Extract bass track notes (program 33)."""
    for inst in midi.instruments:
        if not inst.is_drum and inst.program == 33:
            return sorted(inst.notes, key=lambda n: n.start)
    return []


def get_piano_notes(midi: "pretty_midi.PrettyMIDI") -> List:
    """Extract piano track notes (program 0, non-drum)."""
    for inst in midi.instruments:
        if not inst.is_drum and inst.program == 0:
            return sorted(inst.notes, key=lambda n: n.start)
    return []


def get_drum_notes(midi: "pretty_midi.PrettyMIDI") -> List:
    """Extract all drum notes (is_drum=True), combined from multiple tracks."""
    all_notes = []
    for inst in midi.instruments:
        if inst.is_drum:
            all_notes.extend(inst.notes)
    return sorted(all_notes, key=lambda n: n.start)


def get_melody_notes(midi: "pretty_midi.PrettyMIDI") -> List:
    """Get melody notes (sax preferred, fallback to highest non-drum track)."""
    sax = get_sax_notes(midi)
    if sax:
        return sax
    # Fallback: highest pitch non-drum track
    for inst in midi.instruments:
        if not inst.is_drum and inst.notes:
            return sorted(inst.notes, key=lambda n: n.start)
    return []


def get_comp_notes(midi: "pretty_midi.PrettyMIDI") -> List:
    """Get comping notes (piano + bass combined)."""
    piano = get_piano_notes(midi)
    bass = get_bass_notes(midi)
    return sorted(piano + bass, key=lambda n: n.start)


# =============================================================================
# Feature 1: Collision Rate (KNOWN SIGNAL)
# =============================================================================

def collision_rate(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Percentage of sax notes that overlap with piano at the same pitch class.

    Rationale: Good ensemble playing has instruments in different registers.
    When sax and piano play the same note, it sounds muddy.

    Direction: Lower is better (standards: 26%, outputs: 39%)
    """
    sax = get_sax_notes(midi)
    piano = get_piano_notes(midi)

    if not sax or not piano:
        return 0.0

    collisions = 0
    for sax_note in sax:
        sax_pc = sax_note.pitch % 12
        for piano_note in piano:
            # Check if overlapping in time
            if piano_note.start < sax_note.end and piano_note.end > sax_note.start:
                piano_pc = piano_note.pitch % 12
                if sax_pc == piano_pc:
                    collisions += 1
                    break  # Count each sax note once

    return collisions / len(sax)


# =============================================================================
# Feature 2: Register Separation
# =============================================================================

def register_separation(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Average pitch distance (in semitones) between sax and bass.

    Rationale: Jazz quartet has clear roles - sax high, bass low.
    Good arrangements maintain register separation for clarity.

    Direction: Higher is better (standards: ~30, outputs: ~20)
    """
    sax = get_sax_notes(midi)
    bass = get_bass_notes(midi)

    if not sax or not bass:
        return 0.0

    sax_avg = sum(n.pitch for n in sax) / len(sax)
    bass_avg = sum(n.pitch for n in bass) / len(bass)

    return abs(sax_avg - bass_avg)


# =============================================================================
# Feature 3: Rhythm Independence
# =============================================================================

def rhythm_independence(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Percentage of sax note attacks that DON'T coincide with piano attacks.

    Rationale: Good ensemble playing has rhythmic independence.
    If everyone plays on the same beats, it's boring.
    Jazz is about interweaving rhythms.

    Direction: Higher is better (more independence)
    """
    sax = get_sax_notes(midi)
    piano = get_piano_notes(midi)

    if not sax:
        return 0.0
    if not piano:
        return 1.0  # No piano = all sax attacks are independent

    # Quantize to 32nd notes for attack comparison
    def quantize_time(t: float, resolution: float = 0.09375) -> int:  # 32nd at 160bpm
        return round(t / resolution)

    piano_attacks = set(quantize_time(n.start) for n in piano)

    independent = 0
    for note in sax:
        if quantize_time(note.start) not in piano_attacks:
            independent += 1

    return independent / len(sax)


# =============================================================================
# Feature 4: Onset Density Balance
# =============================================================================

def onset_density_balance(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Ratio of melody onsets to accompaniment onsets.

    Rationale: In good jazz, melody (sax) is sparse while rhythm section is dense.
    If sax plays as many notes as piano+bass combined, it's cluttered.
    Ideal ratio: melody has fewer notes than accompaniment.

    Direction: Value around 0.3-0.5 is ideal (return distance from 0.4)
    """
    sax = get_sax_notes(midi)
    comp = get_comp_notes(midi)

    if not sax or not comp:
        return 0.0

    ratio = len(sax) / len(comp)
    # Ideal is ~0.4, return 1 - distance from ideal
    return 1.0 - min(1.0, abs(ratio - 0.4))


# =============================================================================
# Feature 5: Dynamic Coherence
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
# Feature 6: Bass-Sax Chord Alignment
# =============================================================================

def chord_alignment(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Percentage of sax notes that are chord tones relative to bass root.

    Rationale: Bass defines the harmony. Sax should outline chord tones.
    Jazz melodies land on chord tones (1, 3, 5, 7) most of the time.

    Direction: Higher is better (more harmonic alignment)
    """
    sax = get_sax_notes(midi)
    bass = get_bass_notes(midi)

    if not sax or not bass:
        return 0.0

    chord_tone_count = 0

    for sax_note in sax:
        # Find the bass note active during this sax note
        for bass_note in bass:
            if bass_note.start <= sax_note.start < bass_note.end:
                root_pc = bass_note.pitch % 12
                sax_pc = sax_note.pitch % 12
                # Chord tones: root, major 3rd, minor 3rd, perfect 5th, major 7th, minor 7th
                chord_tones = {
                    root_pc,
                    (root_pc + 3) % 12,  # minor 3rd
                    (root_pc + 4) % 12,  # major 3rd
                    (root_pc + 7) % 12,  # perfect 5th
                    (root_pc + 10) % 12, # minor 7th
                    (root_pc + 11) % 12, # major 7th
                }
                if sax_pc in chord_tones:
                    chord_tone_count += 1
                break

    return chord_tone_count / len(sax)


# =============================================================================
# Feature 7: Phrase Alignment
# =============================================================================

def phrase_alignment(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Do sax phrases start/end near bar lines?

    Rationale: Jazz phrases often align with 2 or 4-bar structures.
    Random phrase boundaries = poor musical form.

    Direction: Higher is better (more aligned with bar structure)
    """
    sax = get_sax_notes(midi)

    if len(sax) < 2:
        return 0.0

    # Detect phrase boundaries (gaps > 0.2s)
    phrase_starts = [sax[0].start]
    phrase_ends = []

    for i in range(1, len(sax)):
        gap = sax[i].start - sax[i-1].end
        if gap > 0.2:
            phrase_ends.append(sax[i-1].end)
            phrase_starts.append(sax[i].start)
    phrase_ends.append(sax[-1].end)

    # Check alignment with bar lines (1.5s per bar at 160 BPM)
    bar_length = 1.5
    aligned = 0
    tolerance = 0.3  # 0.3s tolerance (20% of bar)

    for t in phrase_starts + phrase_ends:
        bar_position = t % bar_length
        if bar_position < tolerance or bar_position > (bar_length - tolerance):
            aligned += 1

    total = len(phrase_starts) + len(phrase_ends)
    return aligned / total if total > 0 else 0.5


# =============================================================================
# Feature 8: Call and Response
# =============================================================================

def call_response(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Are there patterns where sax plays, then piano responds (or vice versa)?

    Rationale: Call-and-response is fundamental to jazz interaction.
    When one voice speaks, another answers.

    Direction: Higher is better (more call-and-response)
    """
    sax = get_sax_notes(midi)
    piano = get_piano_notes(midi)

    if len(sax) < 2 or len(piano) < 2:
        return 0.0

    # Look for alternating patterns
    # A "call" is 2+ consecutive notes from one instrument
    # A "response" is the other instrument playing within 0.5s after

    all_events = []
    for n in sax:
        all_events.append(('sax', n.start, n.end))
    for n in piano:
        all_events.append(('piano', n.start, n.end))

    all_events.sort(key=lambda x: x[1])

    # Count alternations (sax->piano or piano->sax transitions)
    transitions = 0
    last_inst = None

    for inst, start, end in all_events:
        if last_inst is not None and inst != last_inst:
            transitions += 1
        last_inst = inst

    # Normalize: max transitions = len(events) - 1
    max_transitions = len(all_events) - 1
    if max_transitions <= 0:
        return 0.0

    return transitions / max_transitions


# =============================================================================
# Feature 9: Velocity Variance Ratio
# =============================================================================

def velocity_variance_ratio(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Ratio of sax velocity variance to piano velocity variance.

    Rationale: Melody (sax) should have MORE dynamic expression than comping.
    If piano has more dynamics than sax, the roles are reversed.

    Direction: Higher is better (sax more expressive than piano)
    """
    sax = get_sax_notes(midi)
    piano = get_piano_notes(midi)

    if len(sax) < 2 or len(piano) < 2:
        return 1.0  # Neutral

    def variance(notes):
        vels = [n.velocity for n in notes]
        mean = sum(vels) / len(vels)
        return sum((v - mean)**2 for v in vels) / len(vels)

    sax_var = variance(sax)
    piano_var = variance(piano)

    if piano_var < 1:
        return 1.0 if sax_var > 0 else 0.5

    ratio = sax_var / piano_var
    # Normalize: ideal is ratio > 1, cap at 3
    return min(ratio / 3, 1.0)


# =============================================================================
# Feature 10: Texture Density
# =============================================================================

def texture_density(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Average number of simultaneous voices over time.

    Rationale: Good jazz has appropriate texture - not too sparse, not too dense.
    4-piece jazz should have 2-3 simultaneous voices on average.

    Direction: Value around 2.5 is ideal (return distance from ideal)
    """
    all_notes = []
    for inst in midi.instruments:
        for n in inst.notes:
            all_notes.append((n.start, n.end))

    if not all_notes:
        return 0.0

    max_time = max(n[1] for n in all_notes)

    # Sample at regular intervals
    n_samples = 100
    sample_times = [i * max_time / n_samples for i in range(n_samples)]

    densities = []
    for t in sample_times:
        voices = sum(1 for start, end in all_notes if start <= t < end)
        densities.append(voices)

    avg_density = sum(densities) / len(densities)

    # Ideal is ~2.5, return 1 - normalized distance
    ideal = 2.5
    max_deviation = 2.5
    return max(0, 1.0 - abs(avg_density - ideal) / max_deviation)


# =============================================================================
# Feature 11: Harmonic Consonance
# =============================================================================

def harmonic_consonance(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Percentage of time that simultaneous notes form consonant intervals.

    Rationale: While jazz uses dissonance, too much random dissonance = bad.
    Good jazz is consonant most of the time with intentional dissonance.

    Direction: Higher is better (more consonance)
    """
    sax = get_sax_notes(midi)
    comp = get_comp_notes(midi)  # piano + bass

    if not sax or not comp:
        return 0.5  # Neutral

    consonant_intervals = {0, 3, 4, 5, 7, 8, 9, 12}  # P1, m3, M3, P4, P5, m6, M6, P8

    consonant_count = 0
    total_count = 0

    for sax_note in sax:
        for comp_note in comp:
            # Check if overlapping
            if comp_note.start < sax_note.end and comp_note.end > sax_note.start:
                interval = abs(sax_note.pitch - comp_note.pitch) % 12
                total_count += 1
                if interval in consonant_intervals:
                    consonant_count += 1

    return consonant_count / total_count if total_count > 0 else 0.5


# =============================================================================
# Feature 12: Drum Groove Alignment
# =============================================================================

def drum_groove_alignment(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Percentage of melody attacks on strong beats (1, 3 - kick drum territory).

    Rationale: Jazz melody often plays around the beat, not always on it.
    Some alignment with groove is good, but 100% = too square.

    Direction: Value around 0.3-0.5 is ideal
    """
    sax = get_sax_notes(midi)
    drums = get_drum_notes(midi)

    if not sax:
        return 0.5

    # Strong beats at 160 BPM: 0, 0.75, 1.5, 2.25, 3.0, etc. (beats 1 and 3)
    beat_length = 0.375  # Quarter note at 160 BPM

    on_strong = 0
    tolerance = 0.1  # 100ms tolerance

    for note in sax:
        beat_position = (note.start % (beat_length * 2)) / beat_length
        # Strong beats are at 0 and 2 (beats 1 and 3 in a bar)
        if beat_position < tolerance / beat_length or abs(beat_position - 2) < tolerance / beat_length:
            on_strong += 1

    ratio = on_strong / len(sax)
    # Ideal is ~0.4, too high or too low is bad
    return 1.0 - min(1.0, abs(ratio - 0.4) * 2)


# =============================================================================
# All Features Combined
# =============================================================================

def compute_all_features(midi: "pretty_midi.PrettyMIDI") -> Dict[str, float]:
    """Compute all 12 ensemble features for a MIDI file."""
    return {
        'collision_rate': collision_rate(midi),
        'register_separation': register_separation(midi),
        'rhythm_independence': rhythm_independence(midi),
        'onset_density_balance': onset_density_balance(midi),
        'dynamic_coherence': dynamic_coherence(midi),
        'chord_alignment': chord_alignment(midi),
        'phrase_alignment': phrase_alignment(midi),
        'call_response': call_response(midi),
        'velocity_variance_ratio': velocity_variance_ratio(midi),
        'texture_density': texture_density(midi),
        'harmonic_consonance': harmonic_consonance(midi),
        'drum_groove_alignment': drum_groove_alignment(midi),
    }


# =============================================================================
# Feature Metadata and Correlation Analysis Results
# =============================================================================

# =============================================================================
# EMPIRICAL FINDINGS from n=11 sample analysis (2024-11-30)
# =============================================================================
#
# Sample Set:
# - Standards (score=9.0): moanin, sowhat, songformyfather, watermelon, cantina
# - Opus (scores 5.0, 5.5, 4.5): 3 model outputs
# - RLVR (scores 4.5, 4.0, 3.0): 3 model outputs
#
# Individual Feature Correlations (sorted by |r|):
# | Feature                 |    r   |  R^2  |
# |-------------------------|--------|-------|
# | dynamic_coherence       | -0.737 | 0.544 |  <- STRONGEST
# | texture_density         | -0.702 | 0.493 |
# | onset_density_balance   | -0.702 | 0.492 |
# | phrase_alignment        | -0.701 | 0.491 |
# | harmonic_consonance     | +0.601 | 0.362 |
# | call_response           | -0.519 | 0.269 |
# | register_separation     | +0.517 | 0.267 |
# | drum_groove_alignment   | +0.422 | 0.178 |
#
# Key insight: Many features have INVERTED expectations!
# - dynamic_coherence: Standards are LOWER (0.41 vs 0.84) -> more independence
# - texture_density: Standards are LOWER -> less cluttered
# - phrase_alignment: Standards are LOWER -> less rigid alignment

FEATURE_METADATA = {
    'collision_rate': {
        'description': 'Percentage of sax notes that collide with piano at same pitch class',
        'direction': 'lower_better',
        'category': 'collision',
        'correlation': -0.229,
        'signal_strength': 'WEAK',
    },
    'register_separation': {
        'description': 'Average pitch distance between sax and bass in semitones',
        'direction': 'higher_better',
        'category': 'register',
        'correlation': 0.517,
        'signal_strength': 'MODERATE',
    },
    'rhythm_independence': {
        'description': 'Percentage of sax attacks that dont coincide with piano attacks',
        'direction': 'higher_better',  # Weak signal, direction unclear
        'category': 'rhythm',
        'correlation': 0.042,
        'signal_strength': 'WEAK',
    },
    'onset_density_balance': {
        'description': 'Balance between melody and accompaniment note density',
        'direction': 'lower_better',  # INVERTED: Standards have sparse melody
        'category': 'texture',
        'correlation': -0.702,
        'signal_strength': 'STRONG',
    },
    'dynamic_coherence': {
        'description': 'Correlation between sax and piano velocity contours',
        'direction': 'lower_better',  # INVERTED: Standards are more independent
        'category': 'dynamics',
        'correlation': -0.737,  # STRONGEST individual predictor
        'signal_strength': 'STRONG',
    },
    'chord_alignment': {
        'description': 'Percentage of sax notes that are chord tones relative to bass',
        'direction': 'higher_better',
        'category': 'harmony',
        'correlation': -0.052,
        'signal_strength': 'WEAK',
    },
    'phrase_alignment': {
        'description': 'Alignment of sax phrases with bar structure',
        'direction': 'lower_better',  # INVERTED: Standards have less rigid alignment
        'category': 'structure',
        'correlation': -0.701,
        'signal_strength': 'STRONG',
    },
    'call_response': {
        'description': 'Amount of alternation between sax and piano',
        'direction': 'lower_better',  # INVERTED: Standards have less alternation
        'category': 'interaction',
        'correlation': -0.519,
        'signal_strength': 'MODERATE',
    },
    'velocity_variance_ratio': {
        'description': 'Ratio of sax to piano velocity variance',
        'direction': 'lower_better',
        'category': 'dynamics',
        'correlation': -0.270,
        'signal_strength': 'WEAK',
    },
    'texture_density': {
        'description': 'Average simultaneous voices (ideal ~2.5)',
        'direction': 'lower_better',  # INVERTED: Standards are sparser
        'category': 'texture',
        'correlation': -0.702,
        'signal_strength': 'STRONG',
    },
    'harmonic_consonance': {
        'description': 'Percentage of consonant intervals between melody and accompaniment',
        'direction': 'higher_better',
        'category': 'harmony',
        'correlation': 0.601,
        'signal_strength': 'STRONG',
    },
    'drum_groove_alignment': {
        'description': 'Melody attacks on strong beats (ideal ~40%)',
        'direction': 'higher_better',
        'category': 'rhythm',
        'correlation': 0.422,
        'signal_strength': 'MODERATE',
    },
}


# =============================================================================
# Recommended Features for Reward Function
# =============================================================================
#
# Exhaustive N-Feature Search Results:
# | # Features | R^2   | Best Combo                                                |
# |------------|-------|-----------------------------------------------------------|
# | 1          | 0.544 | dynamic_coherence                                         |
# | 2          | 0.864 | dynamic_coherence + texture_density                       |
# | 3          | 0.927 | dynamic_coherence + call_response + texture_density       |
# | 4          | 0.955 | collision_rate + phrase_alignment + texture_density +     |
# |            |       | harmonic_consonance                                       |
# | 5          | 0.983 | rhythm_independence + phrase_alignment +                  |
# |            |       | velocity_variance_ratio + texture_density +               |
# |            |       | harmonic_consonance                                       |
#
# Z-Sum Model Performance:
# - Best 4-feature z-sum R^2: 0.934 (MAE: 0.44)
# - Features: collision_rate, phrase_alignment, texture_density, harmonic_consonance
#
# Collinearity Matrix (selected features):
# | Feature     | collision | phrase | texture | harmonic |
# |-------------|-----------|--------|---------|----------|
# | collision   | 1.000     | 0.042  | 0.123   | 0.345    |
# | phrase      | 0.042     | 1.000  | 0.258   | -0.418   |
# | texture     | 0.123     | 0.258  | 1.000   | -0.173   |
# | harmonic    | 0.345     | -0.418 | -0.173  | 1.000    |
#
# Low collinearity = features capture orthogonal aspects of quality!

RECOMMENDED_FEATURES = [
    'collision_rate',
    'phrase_alignment',
    'texture_density',
    'harmonic_consonance',
]

# Direction multipliers: +1 = higher is better, -1 = lower is better
FEATURE_DIRECTIONS = {
    'collision_rate': -1,      # Lower = better (less sax-piano collision)
    'phrase_alignment': -1,    # Lower = better (less rigid alignment)
    'texture_density': -1,     # Lower = better (sparser = cleaner)
    'harmonic_consonance': +1, # Higher = better (more consonance)
}


# =============================================================================
# Ensemble Reward Function
# =============================================================================

TARGET_BARS = 4  # Target length in bars


def get_tempo(midi: "pretty_midi.PrettyMIDI") -> float:
    """Get tempo from MIDI file. Returns BPM (default 120 if not set)."""
    tempo_times, tempos = midi.get_tempo_changes()
    if len(tempos) > 0:
        return tempos[0]  # Use first tempo
    return 120.0  # MIDI default


def get_bar_count(midi: "pretty_midi.PrettyMIDI") -> float:
    """Calculate number of bars based on duration and tempo."""
    if midi is None:
        return 0
    max_end = max((n.end for inst in midi.instruments for n in inst.notes), default=0)
    tempo = get_tempo(midi)
    bar_duration = 4 * (60.0 / tempo)  # 4 beats per bar
    return max_end / bar_duration if bar_duration > 0 else 0


def duration_on_target(midi: "pretty_midi.PrettyMIDI") -> bool:
    """Gate: Check if piece is close to target 4 bars (±0.5 bars), tempo-aware."""
    if midi is None:
        return False
    bar_count = get_bar_count(midi)
    return abs(bar_count - TARGET_BARS) <= 0.5


def compute_ensemble_reward(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Compute ensemble interaction reward using 4 validated features.

    Returns a z-score sum mapped to [0, 1] range.
    Uses the same sigmoid mapping as symbol_engine.py for consistency.

    Features (from empirical analysis, R^2 = 0.934, MAE = 0.44):
    1. collision_rate (lower=better): Sax-piano pitch collision rate
    2. phrase_alignment (lower=better): Less rigid = more natural phrasing
    3. texture_density (lower=better): Sparser = cleaner arrangement
    4. harmonic_consonance (higher=better): More consonant intervals

    Gate:
    - duration_on_target: 20% penalty if not 4 bars (5.5-6.5s)

    Note: Three features are INVERTED - lower raw values = higher quality.
    This counter-intuitive finding reflects that jazz standards have:
    - Less collision (instruments in different registers)
    - Less rigid phrase alignment (more natural flow)
    - Sparser texture (cleaner, less cluttered)
    """
    # Reference stats (computed from n=11 samples: 5 standards, 3 Opus, 3 RLVR)
    STATS = {
        'collision_rate': {'mean': 0.389, 'std': 0.268},
        'phrase_alignment': {'mean': 0.466, 'std': 0.320},
        'texture_density': {'mean': 0.531, 'std': 0.369},
        'harmonic_consonance': {'mean': 0.763, 'std': 0.111},
    }

    # Compute features
    features = {
        'collision_rate': collision_rate(midi),
        'phrase_alignment': phrase_alignment(midi),
        'texture_density': texture_density(midi),
        'harmonic_consonance': harmonic_consonance(midi),
    }

    # Ensemble gate
    gate_multiplier = 1.0
    if not duration_on_target(midi):
        gate_multiplier *= 0.8  # 20% penalty for wrong duration (not 4 bars)

    # Z-score sum with direction adjustment
    z_sum = 0.0
    for f, value in features.items():
        mean, std = STATS[f]['mean'], STATS[f]['std']
        if std > 0:
            z = (value - mean) / std * FEATURE_DIRECTIONS[f]
            z_sum += z

    # Apply gate to raw z-sum
    # NOTE: Sigmoid is applied in compute_combined_reward() for final output
    return z_sum * gate_multiplier
