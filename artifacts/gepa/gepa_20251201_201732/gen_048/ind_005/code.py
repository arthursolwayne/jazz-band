
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 42), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 42), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 42), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 42), (5.625, 42)
]

for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.875, 40), (2.25, 38), (2.625, 39),
    (3.0, 43), (3.375, 41), (3.75, 43), (4.125, 42),
    (4.5, 38), (4.875, 40), (5.25, 38), (5.625, 39)
]

for start, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(note_obj)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 72), (1.5, 76),  # D, F#, A, C#
    (2.25, 62), (2.25, 67), (2.25, 72), (2.25, 76),
    (3.0, 62), (3.0, 67), (3.0, 72), (3.0, 76),
    (3.75, 62), (3.75, 67), (3.75, 72), (3.75, 76),
    (4.5, 62), (4.5, 67), (4.5, 72), (4.5, 76),
    (5.25, 62), (5.25, 67), (5.25, 72), (5.25, 76)
]

for start, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(note_obj)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 74), (1.75, 76), (2.0, 74), (2.25, 76),
    (3.0, 74), (3.25, 76), (3.5, 74), (3.75, 76),
    (4.5, 74), (4.75, 76), (5.0, 74), (5.25, 76)
]

for start, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
