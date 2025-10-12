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

        # Get expected bar duration from time signature
        time_sig = meter.TimeSignature(jam_json["time_sig"])
        bar_duration = time_sig.barDuration.quarterLength

        # Process each bar
        for bar_data in jam_json["bars"]:
            for inst_name, events in bar_data["parts"].items():
                part = parts[inst_name]

                # Special handling for piano: check if events should be a chord
                if inst_name == "piano" and self._should_be_chord(events):
                    # Create a chord from all pitched notes with the same duration
                    chord_notes = []
                    duration_value = None
                    velocity_value = 70  # default

                    for event in events:
                        if event["pitch"] != "rest":
                            try:
                                n = note.Note(event["pitch"])
                                chord_notes.append(n)
                                # Get duration from first note
                                if duration_value is None:
                                    duration_map = {"e": 0.5, "q": 1.0, "h": 2.0, "w": 4.0}
                                    duration_value = duration_map.get(event["dur"], 1.0)
                                # Get velocity
                                if "vel" in event:
                                    velocity_value = self.orchestra.get_velocity_value(event["vel"])
                            except Exception:
                                pass  # Skip invalid notes

                    if chord_notes and duration_value:
                        c = chord.Chord(chord_notes)
                        c.quarterLength = duration_value
                        c.volume.velocity = velocity_value
                        part.append(c)
                        # Pad if chord is shorter than bar
                        if duration_value < bar_duration:
                            rest_duration = bar_duration - duration_value
                            r = note.Rest()
                            r.quarterLength = rest_duration
                            part.append(r)
                else:
                    # Sequential note processing for non-piano instruments
                    current_bar_duration = 0.0
                    for event in events:
                        # Check if adding this event would exceed bar duration
                        event_duration = {"e": 0.5, "q": 1.0, "h": 2.0, "w": 4.0}.get(event["dur"], 1.0)
                        if current_bar_duration + event_duration > bar_duration:
                            # Truncate: skip remaining events and pad with rest
                            break

                        # Convert event to music21 object
                        m21_obj = self._event_to_music21(event, inst_name)
                        if m21_obj:
                            part.append(m21_obj)
                            current_bar_duration += event_duration

                    # Pad remaining duration with a rest if bar is incomplete
                    if current_bar_duration < bar_duration:
                        rest_duration = bar_duration - current_bar_duration
                        r = note.Rest()
                        r.quarterLength = rest_duration
                        part.append(r)

        # Add all parts to the score
        for part in parts.values():
            score.append(part)

        return score

    def _should_be_chord(self, events: list[JamEvent]) -> bool:
        """
        Determine if a list of piano events should be rendered as a chord.

        Returns True if:
        - There are multiple pitched notes (not rests)
        - All notes have the same duration
        - Total duration matches a single chord duration (not sequential notes)

        Args:
            events: List of JamEvents for a piano part in one bar

        Returns:
            True if events should be rendered as a simultaneous chord
        """
        # Filter out rests
        pitched_events = [e for e in events if e["pitch"] != "rest"]

        if len(pitched_events) < 2:
            return False  # Need at least 2 notes for a chord

        # Check if all notes have the same duration
        durations = set(e["dur"] for e in pitched_events)
        if len(durations) != 1:
            return False  # Mixed durations means sequential, not chord

        # If we have 3-4 notes with the same duration (typical jazz voicing),
        # treat as a chord
        if len(pitched_events) in [3, 4]:
            return True

        return False

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

        # Count bars from the longest part duration
        if time_sig and score.parts:
            # Get the duration of the first part (all parts should be same length)
            part_duration = score.parts[0].quarterLength
            bar_length = time_sig[0].barDuration.quarterLength
            num_bars = int(part_duration / bar_length)
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
