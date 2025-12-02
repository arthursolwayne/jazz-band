
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
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line, chromatic approach to D
bass_notes = [
    (1.5, 62), (1.75, 63), (2.0, 64), (2.25, 65),
    (2.5, 67), (2.75, 69), (3.0, 71), (3.25, 69),
    (3.5, 67), (3.75, 65), (4.0, 64), (4.25, 63)
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 67), (1.5, 71), (1.5, 74), (1.5, 76),  # D7
    (2.0, 67), (2.0, 71), (2.0, 74), (2.0, 76),  # D7
    (2.5, 71), (2.5, 74), (2.5, 76), (2.5, 79),  # G7
    (3.0, 67), (3.0, 71), (3.0, 74), (3.0, 76)   # D7
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Dante: Melody - short motif, starts on 1.5s, ends with a question
sax_notes = [
    (1.5, 62), (1.625, 64), (1.75, 65), (1.875, 0),  # D, E, F#, rest
    (2.0, 67), (2.25, 69), (2.375, 71), (2.5, 0),    # G, A, B, rest
    (2.625, 69), (2.75, 67), (2.875, 65), (3.0, 0)   # A, G, F#, rest
]
for time, note in sax_notes:
    if note != 0:
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
        sax.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line, chromatic approach to Bm
bass_notes = [
    (3.0, 67), (3.25, 68), (3.5, 69), (3.75, 70),
    (4.0, 71), (4.25, 72), (4.5, 73), (4.75, 71),
    (5.0, 69), (5.25, 67), (5.5, 65), (5.75, 64)
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (3.0, 62), (3.0, 66), (3.0, 69), (3.0, 71),  # B7
    (3.5, 62), (3.5, 66), (3.5, 69), (3.5, 71),  # B7
    (4.0, 66), (4.0, 69), (4.0, 71), (4.0, 74),  # E7
    (4.5, 62), (4.5, 66), (4.5, 69), (4.5, 71)   # B7
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Dante: Melody - continuation of motif, ends with a question
sax_notes = [
    (3.0, 62), (3.125, 64), (3.25, 65), (3.375, 0),  # D, E, F#, rest
    (3.5, 67), (3.75, 69), (3.875, 71), (4.0, 0),    # G, A, B, rest
    (4.125, 69), (4.25, 67), (4.375, 65), (4.5, 0)   # A, G, F#, rest
]
for time, note in sax_notes:
    if note != 0:
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
        sax.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line, chromatic approach to D
bass_notes = [
    (4.5, 62), (4.75, 63), (5.0, 64), (5.25, 65),
    (5.5, 67), (5.75, 69), (6.0, 71), (6.25, 69),
    (6.5, 67), (6.75, 65), (7.0, 64), (7.25, 63)
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (4.5, 67), (4.5, 71), (4.5, 74), (4.5, 76),  # D7
    (5.0, 67), (5.0, 71), (5.0, 74), (5.0, 76),  # D7
    (5.5, 71), (5.5, 74), (5.5, 76), (5.5, 79),  # G7
    (6.0, 67), (6.0, 71), (6.0, 74), (6.0, 76)   # D7
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Dante: Melody - final phrase, ends with a question
sax_notes = [
    (4.5, 62), (4.625, 64), (4.75, 65), (4.875, 0),  # D, E, F#, rest
    (5.0, 67), (5.25, 69), (5.375, 71), (5.5, 0),    # G, A, B, rest
    (5.625, 69), (5.75, 67), (5.875, 65), (6.0, 0)   # A, G, F#, rest
]
for time, note in sax_notes:
    if note != 0:
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
        sax.notes.append(note_obj)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
