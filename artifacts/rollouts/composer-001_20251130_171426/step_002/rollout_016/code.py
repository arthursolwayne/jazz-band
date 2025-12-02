
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone: short motif in D (D4, F#4, G4, A4)
sax_notes = [
    (1.5, 62), (1.75, 66), (1.875, 67), (2.0, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line with chromatic approaches
bass_notes = [
    (1.5, 55), (1.75, 56), (1.875, 57), (2.0, 59),
    (2.25, 60), (2.5, 61), (2.625, 62), (2.75, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (1.75, 62), (1.75, 67), (1.75, 71), (1.75, 72),
    (2.25, 62), (2.25, 67), (2.25, 71), (2.25, 72)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone: repeat motif starting on D4
sax_notes = [
    (3.0, 62), (3.25, 66), (3.375, 67), (3.5, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line with chromatic approaches
bass_notes = [
    (3.0, 60), (3.25, 61), (3.375, 62), (3.5, 64),
    (3.75, 65), (4.0, 66), (4.125, 67), (4.25, 67)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (3.25, 62), (3.25, 67), (3.25, 71), (3.25, 72),
    (3.75, 62), (3.75, 67), (3.75, 71), (3.75, 72)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone: repeat motif again, but end on A4
sax_notes = [
    (4.5, 62), (4.75, 66), (4.875, 67), (5.0, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line with chromatic approaches
bass_notes = [
    (4.5, 65), (4.75, 66), (4.875, 67), (5.0, 69),
    (5.25, 70), (5.5, 71), (5.625, 72), (5.75, 72)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (4.75, 62), (4.75, 67), (4.75, 71), (4.75, 72),
    (5.25, 62), (5.25, 67), (5.25, 71), (5.25, 72)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
