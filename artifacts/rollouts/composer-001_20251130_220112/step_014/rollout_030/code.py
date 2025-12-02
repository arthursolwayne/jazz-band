
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Dm
bass_notes = [
    (1.5, 62), (1.75, 60), (2.0, 59), (2.25, 62),
    (2.5, 62), (2.75, 60), (3.0, 59), (3.25, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: Dm7
    (2.0, 62), (2.0, 67), (2.0, 72), (2.0, 74),
    # Bar 2, beat 4: Gm7
    (3.0, 67), (3.0, 72), (3.0, 77), (3.0, 79)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: motif starts here
# Dm7 -> F7 -> Bb7 -> Dm7
sax_notes = [
    (1.5, 65), (1.75, 67), (2.0, 72), (2.25, 67),
    (2.5, 72), (2.75, 74), (3.0, 77), (3.25, 72)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Dm
bass_notes = [
    (3.0, 62), (3.25, 60), (3.5, 59), (3.75, 62),
    (4.0, 62), (4.25, 60), (4.5, 59), (4.75, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: Cm7
    (3.5, 60), (3.5, 65), (3.5, 70), (3.5, 72),
    # Bar 3, beat 4: F7
    (4.5, 67), (4.5, 72), (4.5, 77), (4.5, 79)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: motif continues
# Cm7 -> F7 -> Bb7 -> Dm7
sax_notes = [
    (3.0, 65), (3.25, 60), (3.5, 67), (3.75, 72),
    (4.0, 74), (4.25, 77), (4.5, 77), (4.75, 65)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Dm
bass_notes = [
    (4.5, 62), (4.75, 60), (5.0, 59), (5.25, 62),
    (5.5, 62), (5.75, 60), (6.0, 59), (6.25, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: Bb7
    (5.0, 67), (5.0, 72), (5.0, 77), (5.0, 79),
    # Bar 4, beat 4: Dm7
    (6.0, 62), (6.0, 67), (6.0, 72), (6.0, 74)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: motif closes
# Dm7 -> F7 -> Bb7 -> Dm7
sax_notes = [
    (4.5, 65), (4.75, 67), (5.0, 72), (5.25, 67),
    (5.5, 72), (5.75, 74), (6.0, 77), (6.25, 65)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.save('dante_intro.mid')
