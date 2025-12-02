
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 38),
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 38)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: walking with chromatic approaches
bass_notes = [
    (1.5, 51), (1.75, 50), (2.0, 53), (2.25, 52),
    (2.5, 51), (2.75, 50), (3.0, 53), (3.25, 52)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (2.0, 62), (2.0, 67), (2.0, 69), (2.0, 71),  # D7 chord
    (3.0, 62), (3.0, 67), (3.0, 69), (3.0, 71)   # D7 chord
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Motif starts here, leaves it hanging
sax_notes = [
    (1.5, 62), (1.75, 65), (2.0, 67), (2.25, 62),
    (2.5, 65), (2.75, 67), (3.0, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: walking with chromatic approaches
bass_notes = [
    (3.0, 51), (3.25, 50), (3.5, 53), (3.75, 52),
    (4.0, 51), (4.25, 50), (4.5, 53), (4.75, 52)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (3.5, 62), (3.5, 67), (3.5, 69), (3.5, 71),  # D7 chord
    (4.5, 62), (4.5, 67), (4.5, 69), (4.5, 71)   # D7 chord
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Continue motif and finish it
sax_notes = [
    (3.0, 62), (3.25, 65), (3.5, 67), (3.75, 62),
    (4.0, 65), (4.25, 67), (4.5, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 38),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 38)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: walking with chromatic approaches
bass_notes = [
    (4.5, 51), (4.75, 50), (5.0, 53), (5.25, 52),
    (5.5, 51), (5.75, 50), (6.0, 53), (6.25, 52)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (5.0, 62), (5.0, 67), (5.0, 69), (5.0, 71),  # D7 chord
    (6.0, 62), (6.0, 67), (6.0, 69), (6.0, 71)   # D7 chord
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Finish the motif, leave it open
sax_notes = [
    (4.5, 62), (4.75, 65), (5.0, 67), (5.25, 62),
    (5.5, 65), (5.75, 67), (6.0, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 38),
    (6.0, 36), (6.375, 42), (6.75, 36), (7.125, 38)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
