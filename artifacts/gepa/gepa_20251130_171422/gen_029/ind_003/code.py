
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
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    (1.5, 48), (1.75, 49), (2.0, 50), (2.25, 51),
    (2.5, 50), (2.75, 49), (3.0, 48), (3.25, 47)
]
for start, note in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (1.75, 57), (1.75, 62), (1.75, 64), (1.75, 67),
    (2.25, 57), (2.25, 62), (2.25, 64), (2.25, 67),
    (3.0, 59), (3.0, 64), (3.0, 67), (3.0, 71)
]
for start, note in piano_notes:
    note = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: sparse melody with space
sax_notes = [
    (1.5, 62), (1.5, 65), (1.75, 67), (2.0, 65),
    (2.25, 62), (2.5, 60), (2.75, 62), (3.0, 65)
]
for start, note in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches, variation
bass_notes = [
    (3.0, 51), (3.25, 50), (3.5, 49), (3.75, 48),
    (4.0, 49), (4.25, 50), (4.5, 51), (4.75, 52)
]
for start, note in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (3.25, 62), (3.25, 64), (3.25, 67), (3.25, 71),
    (3.75, 64), (3.75, 67), (3.75, 71), (3.75, 76),
    (4.5, 66), (4.5, 69), (4.5, 72), (4.5, 76)
]
for start, note in piano_notes:
    note = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: sparse melody with space
sax_notes = [
    (3.0, 65), (3.0, 62), (3.25, 60), (3.5, 62),
    (3.75, 65), (4.0, 67), (4.25, 65), (4.5, 62)
]
for start, note in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches, variation
bass_notes = [
    (4.5, 52), (4.75, 51), (5.0, 50), (5.25, 49),
    (5.5, 50), (5.75, 51), (6.0, 52), (6.25, 53)
]
for start, note in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (4.75, 64), (4.75, 67), (4.75, 71), (4.75, 74),
    (5.25, 64), (5.25, 67), (5.25, 71), (5.25, 76),
    (6.0, 67), (6.0, 71), (6.0, 74), (6.0, 76)
]
for start, note in piano_notes:
    note = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: sparse melody with space, ends on a question
sax_notes = [
    (4.5, 62), (4.75, 65), (5.0, 67), (5.25, 65),
    (5.5, 62), (5.75, 60), (6.0, 62), (6.25, 65)
]
for start, note in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 38), (7.125, 42)
]
for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
