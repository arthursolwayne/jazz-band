
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
    (0.0, 36), (0.25, 42), (0.5, 36), (0.75, 42),  # Bar 1
    (1.0, 38), (1.25, 42), (1.5, 38), (1.75, 42),  # Bar 1
    (2.0, 36), (2.25, 42), (2.5, 36), (2.75, 42),  # Bar 2
    (3.0, 38), (3.25, 42), (3.5, 38), (3.75, 42),  # Bar 2
    (4.0, 36), (4.25, 42), (4.5, 36), (4.75, 42),  # Bar 3
    (5.0, 38), (5.25, 42), (5.5, 38), (5.75, 42),  # Bar 3
    (6.0, 36), (6.25, 42), (6.5, 36), (6.75, 42),  # Bar 4
    (7.0, 38), (7.25, 42), (7.5, 38), (7.75, 42)   # Bar 4
]

for time, note in drum_notes:
    midi_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(midi_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62), (1.75, 63), (2.0, 64), (2.25, 65),  # Bar 2
    (2.5, 65), (2.75, 64), (3.0, 63), (3.25, 62),  # Bar 3
    (3.5, 61), (3.75, 60), (4.0, 62), (4.25, 63),  # Bar 4
    (4.5, 64), (4.75, 65), (5.0, 66), (5.25, 67),  # Bar 4
    (5.5, 67), (5.75, 66), (6.0, 65), (6.25, 64)   # Bar 4
]

for time, note in bass_notes:
    midi_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(midi_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 67), (1.5, 71), (1.5, 72), (1.5, 76),  # D7
    (2.0, 67), (2.0, 71), (2.0, 72), (2.0, 76),  # D7
    (2.5, 71), (2.5, 74), (2.5, 76), (2.5, 80),  # G7
    (3.0, 71), (3.0, 74), (3.0, 76), (3.0, 80),  # G7
    (3.5, 67), (3.5, 71), (3.5, 72), (3.5, 76),  # D7
    (4.0, 67), (4.0, 71), (4.0, 72), (4.0, 76),  # D7
    (4.5, 71), (4.5, 74), (4.5, 76), (4.5, 80),  # G7
    (5.0, 71), (5.0, 74), (5.0, 76), (5.0, 80),  # G7
    (5.5, 67), (5.5, 71), (5.5, 72), (5.5, 76),  # D7
    (6.0, 67), (6.0, 71), (6.0, 72), (6.0, 76)    # D7
]

for time, note in piano_notes:
    midi_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(midi_note)

# Sax: Whisper at first, then a cry — one short motif, make it sing
sax_notes = [
    (1.5, 62), (1.75, 65), (2.0, 67), (2.25, 69),  # Bar 2
    (2.5, 67), (2.75, 69), (3.0, 71), (3.25, 67),  # Bar 3
    (3.5, 65), (3.75, 62), (4.0, 67), (4.25, 69),  # Bar 4
    (4.5, 71), (4.75, 67), (5.0, 69), (5.25, 65),  # Bar 4
    (5.5, 62), (5.75, 67), (6.0, 69), (6.25, 71)   # Bar 4
]

for time, note in sax_notes:
    midi_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(midi_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
