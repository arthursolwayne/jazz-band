
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    (1.5, 50), (1.875, 49), (2.25, 51), (2.625, 50),
    (3.0, 48), (3.375, 47), (3.75, 49), (4.125, 48)
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: Dm7
    (2.25, 62), (2.25, 67), (2.25, 70), (2.25, 72),
    # Bar 2, beat 4: G7
    (2.625, 67), (2.625, 71), (2.625, 74), (2.625, 76),
    # Bar 3, beat 2: Cm7
    (3.75, 60), (3.75, 65), (3.75, 68), (3.75, 70),
    # Bar 3, beat 4: F7
    (4.125, 65), (4.125, 69), (4.125, 72), (4.125, 74)
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Sax: one short motif, make it sing
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, F, G, Bb (D, F, G, Bb)
sax_notes = [
    (1.5, 62), (1.875, 65), (2.25, 67), (2.625, 69),
    (3.0, 62), (3.375, 65), (3.75, 67), (4.125, 69)
]
for time, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    (3.0, 48), (3.375, 47), (3.75, 49), (4.125, 48),
    (4.5, 50), (4.875, 49), (5.25, 51), (5.625, 50)
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2: Cm7
    (3.75, 60), (3.75, 65), (3.75, 68), (3.75, 70),
    # Bar 3, beat 4: F7
    (4.125, 65), (4.125, 69), (4.125, 72), (4.125, 74),
    # Bar 4, beat 2: Bb7
    (5.25, 67), (5.25, 71), (5.25, 74), (5.25, 76),
    # Bar 4, beat 4: Eb7
    (5.625, 62), (5.625, 66), (5.625, 69), (5.625, 71)
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Sax: return to motif, finish it
# D, F, G, Bb
sax_notes = [
    (3.0, 62), (3.375, 65), (3.75, 67), (4.125, 69),
    (4.5, 62), (4.875, 65), (5.25, 67), (5.625, 69)
]
for time, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    (4.5, 50), (4.875, 49), (5.25, 51), (5.625, 50),
    (6.0, 48), (6.375, 47), (6.75, 49), (7.125, 48)
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2: Bb7
    (5.25, 67), (5.25, 71), (5.25, 74), (5.25, 76),
    # Bar 4, beat 4: Eb7
    (5.625, 62), (5.625, 66), (5.625, 69), (5.625, 71)
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Sax: final rest
sax_notes = [
    (6.0, 62), (6.0, 62)
]
for time, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
