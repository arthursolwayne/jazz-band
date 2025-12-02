
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif starts, leaves it hanging
sax_notes = [
    (1.5, 62, 0.5),  # D4
    (2.0, 67, 0.5),  # G4
    (2.5, 69, 0.5)   # A4
]
for time, pitch, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration))

# Bass: walking line, chromatic approaches
bass_notes = [
    (1.5, 45, 0.5),  # D3
    (2.0, 46, 0.5),  # Eb3
    (2.5, 47, 0.5),  # E3
    (3.0, 49, 0.5)   # G3
]
for time, pitch, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: comp on beat 2 (time 2.0)
    (2.0, 62, 0.25),  # D4
    (2.0, 67, 0.25),  # G4
    (2.0, 71, 0.25),  # B4
    (2.0, 74, 0.25),  # D5
    # Bar 3: comp on beat 4 (time 3.0)
    (3.0, 62, 0.25),  # D4
    (3.0, 67, 0.25),  # G4
    (3.0, 71, 0.25),  # B4
    (3.0, 74, 0.25)   # D5
]
for time, pitch, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat the motif but end it
sax_notes = [
    (3.0, 62, 0.5),  # D4
    (3.5, 67, 0.5),  # G4
    (4.0, 69, 0.5)   # A4
]
for time, pitch, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration))

# Bass: walking line, chromatic approaches
bass_notes = [
    (3.0, 49, 0.5),  # G3
    (3.5, 50, 0.5),  # Ab3
    (4.0, 51, 0.5),  # A3
    (4.5, 53, 0.5)   # C4
]
for time, pitch, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: comp on beat 2 (time 3.5)
    (3.5, 62, 0.25),  # D4
    (3.5, 67, 0.25),  # G4
    (3.5, 71, 0.25),  # B4
    (3.5, 74, 0.25),  # D5
    # Bar 4: comp on beat 4 (time 4.5)
    (4.5, 62, 0.25),  # D4
    (4.5, 67, 0.25),  # G4
    (4.5, 71, 0.25),  # B4
    (4.5, 74, 0.25)   # D5
]
for time, pitch, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: repeat the motif but end it, resolve the tension
sax_notes = [
    (4.5, 62, 0.5),  # D4
    (5.0, 67, 0.5),  # G4
    (5.5, 69, 0.5)   # A4
]
for time, pitch, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration))

# Bass: walking line, chromatic approaches
bass_notes = [
    (4.5, 53, 0.5),  # C4
    (5.0, 54, 0.5),  # Db4
    (5.5, 55, 0.5),  # D4
    (6.0, 57, 0.5)   # F4
]
for time, pitch, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: comp on beat 2 (time 5.0)
    (5.0, 62, 0.25),  # D4
    (5.0, 67, 0.25),  # G4
    (5.0, 71, 0.25),  # B4
    (5.0, 74, 0.25),  # D5
    # Bar 4: comp on beat 4 (time 6.0)
    (6.0, 62, 0.25),  # D4
    (6.0, 67, 0.25),  # G4
    (6.0, 71, 0.25),  # B4
    (6.0, 74, 0.25)   # D5
]
for time, pitch, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
