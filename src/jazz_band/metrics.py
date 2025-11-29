"""
Verifiable Metrics for Jazz Compositions

Computes 9 metrics from PrettyMIDI objects. Used by both RLVR and GEPA.
All metrics return 0.0-1.0.
"""

from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    import pretty_midi


# TODO: Implement helpers
# def _get_instrument(midi, name=None, is_drum=None) -> Instrument
# def _notes_in_bar(notes, bar_idx, bar_duration) -> List[Note]
# def _get_bar_count(midi, tempo) -> int


def compute_upbeat_syncopation(midi: "pretty_midi.PrettyMIDI", tempo: float = 144) -> float:
    """Percentage of hihat hits on upbeats. Target >0.6 for Latin jazz."""
    # TODO: Implement for pretty_midi
    raise NotImplementedError


def compute_seventh_chord_usage(midi: "pretty_midi.PrettyMIDI", tempo: float = 144) -> float:
    """Fraction of bars with 4+ unique pitch classes in piano."""
    # TODO: Implement for pretty_midi
    raise NotImplementedError


def compute_groove_alignment(midi: "pretty_midi.PrettyMIDI", tempo: float = 144) -> float:
    """Bass-drum correlation on downbeats."""
    # TODO: Implement for pretty_midi
    raise NotImplementedError


def compute_textural_arc(midi: "pretty_midi.PrettyMIDI", tempo: float = 144) -> float:
    """Progressive build: instrument activation trending upward."""
    # TODO: Implement for pretty_midi
    raise NotImplementedError


def compute_rhythmic_variety(midi: "pretty_midi.PrettyMIDI", tempo: float = 144) -> float:
    """Duration entropy + motif repetition balance."""
    # TODO: Implement for pretty_midi
    raise NotImplementedError


def compute_dynamic_contrast(midi: "pretty_midi.PrettyMIDI", tempo: float = 144) -> float:
    """High variance between instruments, low within."""
    # TODO: Implement for pretty_midi
    raise NotImplementedError


def compute_melodic_exploration(midi: "pretty_midi.PrettyMIDI", tempo: float = 144) -> float:
    """Pitch range + stepwise motion balance in sax."""
    # TODO: Implement for pretty_midi
    raise NotImplementedError


def compute_harmonic_movement(midi: "pretty_midi.PrettyMIDI", tempo: float = 144) -> float:
    """Optimal chord change rate (1-3 per 4 bars)."""
    # TODO: Implement for pretty_midi
    raise NotImplementedError


def compute_consonance(midi: "pretty_midi.PrettyMIDI", key: str = "Eb") -> float:
    """Percentage of notes in key scale."""
    # TODO: Implement for pretty_midi
    raise NotImplementedError


def compute_all(midi: "pretty_midi.PrettyMIDI", tempo: float = 144, key: str = "Eb") -> Dict[str, float]:
    """Compute all 9 metrics. Returns dict of metric_name -> value (0.0-1.0)."""
    # TODO: Implement for pretty_midi
    raise NotImplementedError
