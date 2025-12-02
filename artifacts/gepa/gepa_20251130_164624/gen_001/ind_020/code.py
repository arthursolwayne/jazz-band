
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
for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, never the same note twice
# F7 chord: F, A, C, E
# Walking bass line: F, G#, A, Bb, B, C, D, Eb, E, F#, G, Ab, A, Bb, B, C
bass_notes = [
    (1.5, 71), (1.875, 72), (2.25, 73), (2.625, 72),
    (3.0, 71), (3.375, 72), (3.75, 74), (4.125, 71),
    (4.5, 72), (4.875, 74), (5.25, 72), (5.625, 71)
]
for start, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, E
# B7 = B, D#, F#, A
# E7 = E, G#, B, D
# C7 = C, E, G, B
piano_notes = [
    # Bar 2: F7 on beat 2
    (2.25, 70), (2.25, 74), (2.25, 77), (2.25, 79),
    # Bar 3: B7 on beat 2
    (3.25, 71), (3.25, 76), (3.25, 78), (3.25, 81),
    # Bar 4: E7 on beat 2
    (4.25, 69), (4.25, 73), (4.25, 77), (4.25, 80),
    # Bar 4: C7 on beat 4
    (5.625, 68), (5.625, 72), (5.625, 76), (5.625, 79)
]
for start, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - D - F (F7 arpeggio, ascending)
sax_notes = [
    (1.5, 71), (1.5, 74), (1.5, 77), (1.5, 71),
    (2.25, 71), (2.25, 74), (2.25, 77), (2.25, 71),
    (3.75, 71), (3.75, 74), (3.75, 77), (3.75, 71),
    (4.5, 71), (4.5, 74), (4.5, 77), (4.5, 71)
]
for start, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(note_obj)

# Drums for Bars 2-4
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
