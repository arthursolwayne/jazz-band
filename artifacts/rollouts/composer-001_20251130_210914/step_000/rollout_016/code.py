
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
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starts here
sax_notes = [
    (1.5, 62), (1.75, 67), (2.0, 64), (2.25, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line in Dm
bass_notes = [
    (1.5, 50), (1.75, 51), (2.0, 48), (2.25, 50),
    (2.5, 52), (2.75, 51), (3.0, 48), (3.25, 50)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (1.75, 62), (1.75, 67), (1.75, 69), (1.75, 71),
    (2.25, 62), (2.25, 67), (2.25, 69), (2.25, 71),
    (2.75, 62), (2.75, 67), (2.75, 69), (2.75, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums continue
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with slight variation
sax_notes = [
    (3.0, 62), (3.25, 67), (3.5, 64), (3.75, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line in Dm
bass_notes = [
    (3.0, 50), (3.25, 51), (3.5, 48), (3.75, 50),
    (4.0, 52), (4.25, 51), (4.5, 48), (4.75, 50)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (3.25, 62), (3.25, 67), (3.25, 69), (3.25, 71),
    (3.75, 62), (3.75, 67), (3.75, 69), (3.75, 71),
    (4.25, 62), (4.25, 67), (4.25, 69), (4.25, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums continue
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Complete the motif
sax_notes = [
    (4.5, 62), (4.75, 67), (5.0, 64), (5.25, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line in Dm
bass_notes = [
    (4.5, 50), (4.75, 51), (5.0, 48), (5.25, 50),
    (5.5, 52), (5.75, 51), (6.0, 48), (6.25, 50)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (4.75, 62), (4.75, 67), (4.75, 69), (4.75, 71),
    (5.25, 62), (5.25, 67), (5.25, 69), (5.25, 71),
    (5.75, 62), (5.75, 67), (5.75, 69), (5.75, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums continue
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
