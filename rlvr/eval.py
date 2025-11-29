"""
RLVR Evaluation: Dummy reward for testing.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pretty_midi


def compute_reward(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Dummy reward: 1.0 if MIDI has notes, -1.0 otherwise.
    """
    if midi is None:
        return -1.0

    total_notes = sum(len(inst.notes) for inst in midi.instruments)
    return 1.0 if total_notes > 0 else -1.0
