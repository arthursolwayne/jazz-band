"""
Orchestra Configuration

Defines the five-instrument ensemble with MIDI program mappings, channel assignments,
and pitch ranges. Follows General MIDI standard with drums on channel 10.

Instruments:
- Bass: Acoustic bass on channel 0
- Drums: GM percussion on channel 10 (kick, snare, hihat)
- Piano: Acoustic grand piano on channel 1
- Sax: Tenor saxophone on channel 2
- Trumpet: Trumpet on channel 3
"""

from dataclasses import dataclass
from typing import Literal, Optional


InstrumentName = Literal["bass", "snare", "hihat", "piano", "sax", "trumpet"]


@dataclass
class Instrument:
    """
    Configuration for a single instrument in the ensemble.

    Attributes:
        name: Instrument identifier
        midi_program: General MIDI program number (0-127)
        channel: MIDI channel (0-15, with 10 reserved for drums)
        pitch_range: Tuple of (lowest_note, highest_note) in scientific pitch notation
        display_name: Human-readable name
    """
    name: InstrumentName
    midi_program: int
    channel: int
    pitch_range: Optional[tuple[str, str]]  # None for drums (uses pitch mapping instead)
    display_name: str


# Drum pitch mapping for General MIDI percussion (channel 10)
# Maps drum part names to MIDI note numbers
DRUM_PITCH_MAP = {
    "snare": 38,   # Acoustic Snare
    "hihat": 42,   # Closed Hi-Hat (standard)
}


class OrchestraSpec:
    """
    Specification for the six-part jazz ensemble.

    Provides instrument configurations, MIDI mappings, and utility functions
    for working with the ensemble.
    """

    def __init__(self):
        """Initialize the orchestra with six parts."""
        self.instruments = {
            "bass": Instrument(
                name="bass",
                midi_program=33,  # Electric Bass (program 34 in 1-indexed, 33 in 0-indexed)
                channel=0,
                pitch_range=("E1", "G3"),
                display_name="Electric Bass"
            ),
            "snare": Instrument(
                name="snare",
                midi_program=0,  # Not used for drums (channel 10 triggers percussion)
                channel=9,  # Channel 10 in 1-indexed, 9 in 0-indexed
                pitch_range=None,  # Drums use pitch mapping instead
                display_name="Snare Drum (GM Channel 10)"
            ),
            "hihat": Instrument(
                name="hihat",
                midi_program=0,  # Not used for drums (channel 10 triggers percussion)
                channel=9,  # Channel 10 in 1-indexed, 9 in 0-indexed
                pitch_range=None,  # Drums use pitch mapping instead
                display_name="Hi-Hat (GM Channel 10)"
            ),
            "piano": Instrument(
                name="piano",
                midi_program=0,  # Acoustic Grand Piano
                channel=1,
                pitch_range=("A0", "C8"),
                display_name="Acoustic Grand Piano"
            ),
            "sax": Instrument(
                name="sax",
                midi_program=66,  # Tenor Sax (program 67 in 1-indexed)
                channel=2,
                pitch_range=("Ab2", "E5"),
                display_name="Tenor Saxophone"
            ),
            "trumpet": Instrument(
                name="trumpet",
                midi_program=56,  # Trumpet (program 57 in 1-indexed)
                channel=3,
                pitch_range=("E3", "C6"),
                display_name="Trumpet"
            ),
        }

    def get_instrument(self, name: InstrumentName) -> Instrument:
        """
        Get instrument configuration by name.

        Args:
            name: Instrument identifier

        Returns:
            Instrument configuration object

        Raises:
            KeyError: If instrument name is not recognized
        """
        if name not in self.instruments:
            raise KeyError(f"Unknown instrument: {name}")
        return self.instruments[name]

    def get_drum_pitch(self, drum_name: str) -> int:
        """
        Convert drum symbolic name to MIDI pitch number.

        Args:
            drum_name: Drum identifier (kick, snare, hihat)

        Returns:
            MIDI pitch number for the drum

        Raises:
            KeyError: If drum name is not recognized
        """
        if drum_name not in DRUM_PITCH_MAP:
            raise KeyError(f"Unknown drum: {drum_name}. Valid drums: {list(DRUM_PITCH_MAP.keys())}")
        return DRUM_PITCH_MAP[drum_name]

    def get_velocity_value(self, velocity: str) -> int:
        """
        Convert symbolic velocity to MIDI velocity value.

        Args:
            velocity: Symbolic velocity (lo, med, hi)

        Returns:
            MIDI velocity value (0-127)

        Raises:
            ValueError: If velocity is not recognized
        """
        velocity_map = {
            "lo": 40,
            "med": 70,
            "hi": 100,
        }
        if velocity not in velocity_map:
            raise ValueError(f"Unknown velocity: {velocity}. Valid velocities: {list(velocity_map.keys())}")
        return velocity_map[velocity]

    def list_instruments(self) -> list[str]:
        """
        Get list of all instrument names in the ensemble.

        Returns:
            List of instrument names
        """
        return list(self.instruments.keys())

    def summary(self) -> str:
        """
        Generate a human-readable summary of the orchestra configuration.

        Returns:
            Multi-line string describing the ensemble
        """
        lines = ["Orchestra Configuration:"]
        for name, inst in self.instruments.items():
            channel_str = f"Channel {inst.channel + 1}"  # Display as 1-indexed
            if name in ["snare", "hihat"]:
                # Percussion instruments (no program or range)
                lines.append(f"  {inst.display_name}: {channel_str}")
            else:
                # Regular instruments with program and range
                prog_str = f"Program {inst.midi_program + 1}"  # Display as 1-indexed
                range_str = f"Range {inst.pitch_range[0]}-{inst.pitch_range[1]}"
                lines.append(f"  {inst.display_name}: {channel_str}, {prog_str}, {range_str}")
        return "\n".join(lines)


# Default orchestra instance for convenience
DEFAULT_ORCHESTRA = OrchestraSpec()
