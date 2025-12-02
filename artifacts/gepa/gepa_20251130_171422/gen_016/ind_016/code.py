
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, never the same note twice
# Dm7 walking line: D, C, Bb, B, C#, D, Eb, D, C, Bb, B, C#, D
bass_notes = [
    (1.5, 2), (1.75, 1), (2.0, 10), (2.25, 11),
    (2.5, 13), (2.75, 2), (3.0, 3), (3.25, 2),
    (3.5, 1), (3.75, 10), (4.0, 11), (4.25, 13),
    (4.5, 2), (4.75, 1), (5.0, 10), (5.25, 11),
    (5.5, 13), (5.75, 2)
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane on piano: 7th chords, comp on 2 and 4
# Dm7 = D, F, A, C
piano_notes = [
    (1.75, 2), (1.75, 5), (1.75, 9), (1.75, 11),
    (2.0, 2), (2.0, 5), (2.0, 9), (2.0, 11),
    (3.25, 2), (3.25, 5), (3.25, 9), (3.25, 11),
    (3.5, 2), (3.5, 5), (3.5, 9), (3.5, 11),
    (4.75, 2), (4.75, 5), (4.75, 9), (4.75, 11),
    (5.0, 2), (5.0, 5), (5.0, 9), (5.0, 11)
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Dante on sax: short motif, start it, leave it hanging, come back and finish
# Dm motif: D, Eb, C, Bb (melodic minor) with some space
sax_notes = [
    (1.5, 2), (1.666, 3), (1.833, 1), (2.0, 10),
    (2.5, 2), (2.666, 3), (2.833, 1), (3.0, 10),
    (3.5, 2), (3.666, 3), (3.833, 1), (4.0, 10),
    (4.5, 2), (4.666, 3), (4.833, 1), (5.0, 10)
]
for time, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.166)
    sax.notes.append(note_obj)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
