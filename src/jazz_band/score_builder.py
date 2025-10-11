"""
Score Builder - JamJSON to music21 Conversion

Converts JamJSON symbolic representation to music21 Score objects and exports to MIDI.
Handles five-part arrangements with proper instrument assignments, MIDI channels,
and General MIDI drums on channel 10.

Key features:
- Converts JamJSON events to music21 notes and rests
- Assigns correct MIDI programs and channels
- Maps drum names (kick/snare/hihat) to GM percussion pitches
- Exports playable MIDI files
- Provides console summaries of generated scores
"""

from pathlib import Path
from typing import Optional

from music21 import stream, note, tempo, key, meter, instrument, chord

from .schema import JamJSON, JamEvent
from .orchestra import OrchestraSpec, DEFAULT_ORCHESTRA


class ScoreBuilder:
    """
    Converts JamJSON to music21 Score objects and handles MIDI export.

    Uses an OrchestraSpec to determine instrument configurations, MIDI programs,
    and channel assignments.
    """

    def __init__(self, orchestra: Optional[OrchestraSpec] = None):
        """
        Initialize the score builder.

        Args:
            orchestra: Orchestra specification (defaults to DEFAULT_ORCHESTRA)
        """
        self.orchestra = orchestra or DEFAULT_ORCHESTRA

    def from_jam_json(self, jam_json: JamJSON) -> stream.Score:
        """
        Convert JamJSON to a music21 Score.

        Creates a five-part score with proper instrument assignments, tempos,
        key signatures, and time signatures. Each part is placed on its
        designated MIDI channel.

        Args:
            jam_json: Validated JamJSON structure

        Returns:
            music21 Score object ready for playback or export

        Raises:
            ValueError: If JamJSON contains invalid musical data
        """
        # Create the score
        score = stream.Score()

        # Add metadata
        score.insert(0, tempo.MetronomeMark(number=jam_json["tempo"]))
        score.insert(0, key.Key(jam_json["key"]))
        score.insert(0, meter.TimeSignature(jam_json["time_sig"]))

        # Create parts for each instrument
        parts = {}
        for inst_name in ["bass", "snare", "hihat", "piano", "sax", "trumpet"]:
            inst_config = self.orchestra.get_instrument(inst_name)
            part = stream.Part()

            # Set instrument
            if inst_name == "bass":
                part.insert(0, instrument.ElectricBass())
            elif inst_name == "snare":
                # Snare drum on channel 9 (channel 10 in 1-indexed)
                part.insert(0, instrument.SnareDrum())
            elif inst_name == "hihat":
                # Hi-hat on channel 9 (channel 10 in 1-indexed)
                part.insert(0, instrument.HiHatCymbal())
            elif inst_name == "piano":
                part.insert(0, instrument.Piano())
            elif inst_name == "sax":
                part.insert(0, instrument.TenorSaxophone())
            elif inst_name == "trumpet":
                part.insert(0, instrument.Trumpet())

            # Set MIDI channel and program
            if inst_name in ["snare", "hihat"]:
                # Force percussion to channel 9 (MIDI channel 10)
                part.midiChannel = 9
            else:
                part.midiChannel = inst_config.channel
                part.midiProgram = inst_config.midi_program

            parts[inst_name] = part

        # Process each bar
        for bar_data in jam_json["bars"]:
            for inst_name, events in bar_data["parts"].items():
                part = parts[inst_name]
                for event in events:
                    # Convert event to music21 object
                    m21_obj = self._event_to_music21(event, inst_name)
                    if m21_obj:
                        part.append(m21_obj)

        # Add all parts to the score
        for part in parts.values():
            score.append(part)

        return score

    def _event_to_music21(
        self, event: JamEvent, inst_name: str
    ) -> Optional[note.Note | note.Rest]:
        """
        Convert a single JamEvent to a music21 Note or Rest.

        Args:
            event: JamEvent containing pitch, duration, velocity
            inst_name: Name of the instrument (used for drum pitch mapping)

        Returns:
            music21 Note, Rest, or None if the event is invalid
        """
        # Parse duration
        duration_map = {
            "e": 0.5,   # eighth note
            "q": 1.0,   # quarter note
            "h": 2.0,   # half note
            "w": 4.0,   # whole note
        }
        dur_value = duration_map.get(event["dur"])
        if dur_value is None:
            print(f"Warning: Unknown duration '{event['dur']}', skipping event")
            return None

        # Handle rests
        if event["pitch"] == "rest":
            r = note.Rest()
            r.quarterLength = dur_value
            return r

        # Handle drums (snare and hihat parts use fixed MIDI pitches)
        if inst_name in ["snare", "hihat"]:
            # Get the MIDI pitch for this drum part
            midi_pitch = self.orchestra.get_drum_pitch(inst_name)
            n = note.Note()
            n.pitch.midi = midi_pitch
        else:
            # Regular pitched note
            try:
                n = note.Note(event["pitch"])
            except Exception as e:
                print(f"Warning: Invalid pitch '{event['pitch']}': {e}, skipping event")
                return None

        # Set duration
        n.quarterLength = dur_value

        # Set velocity if specified
        if "vel" in event:
            velocity_value = self.orchestra.get_velocity_value(event["vel"])
            n.volume.velocity = velocity_value
        else:
            # Default to medium velocity
            n.volume.velocity = 70

        return n

    def export_midi(self, score: stream.Score, filepath: str | Path) -> None:
        """
        Export a music21 Score to a MIDI file.

        Creates parent directories if they don't exist.

        Args:
            score: music21 Score to export
            filepath: Path to output MIDI file

        Raises:
            IOError: If file cannot be written
        """
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        score.write("midi", fp=str(filepath))

    def summarize(self, score: stream.Score) -> str:
        """
        Generate a human-readable summary of a score.

        Includes:
        - Tempo, key, time signature
        - Number of bars
        - Note counts per instrument
        - Total duration

        Args:
            score: music21 Score to summarize

        Returns:
            Multi-line string summary
        """
        lines = ["Score Summary:"]

        # Get metadata
        tempo_mark = score.flatten().getElementsByClass(tempo.MetronomeMark)
        key_sig = score.flatten().getElementsByClass(key.Key)
        time_sig = score.flatten().getElementsByClass(meter.TimeSignature)

        if tempo_mark:
            lines.append(f"  Tempo: {tempo_mark[0].number} BPM")
        if key_sig:
            lines.append(f"  Key: {key_sig[0].tonic.name} {key_sig[0].mode}")
        if time_sig:
            lines.append(f"  Time Signature: {time_sig[0].ratioString}")

        # Count bars (approximate from duration and time signature)
        if time_sig:
            total_duration = score.quarterLength
            bar_length = time_sig[0].barDuration.quarterLength
            num_bars = int(total_duration / bar_length)
            lines.append(f"  Number of Bars: {num_bars}")

        lines.append("")
        lines.append("  Notes per Part:")

        # Count notes in each part
        for part in score.parts:
            inst = part.getInstrument()
            inst_name = inst.instrumentName if inst else "Unknown"

            # Count notes and rests
            notes = part.flatten().notes
            rests = part.flatten().notesAndRests.getElementsByClass(note.Rest)

            lines.append(f"    {inst_name}: {len(notes)} notes, {len(rests)} rests")

        return "\n".join(lines)


def quick_preview(jam_json: JamJSON, output_path: Optional[str] = None) -> str:
    """
    Convenience function to quickly convert JamJSON and get a summary.

    Args:
        jam_json: JamJSON to convert
        output_path: Optional path to export MIDI file

    Returns:
        String summary of the generated score
    """
    builder = ScoreBuilder()
    score = builder.from_jam_json(jam_json)

    if output_path:
        builder.export_midi(score, output_path)

    return builder.summarize(score)
