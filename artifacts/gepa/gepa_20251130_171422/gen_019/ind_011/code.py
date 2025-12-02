
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
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Fm7 -> Ab -> G -> Eb (sparse, expressive)
sax_notes = [
    (1.5, 87, 100),  # F (Ab7)
    (1.75, 84, 100),  # Eb (Ab7)
    (2.0, 83, 100),   # G (Ab7)
    (2.25, 81, 100),  # Eb (Ab7)
    (2.5, 87, 100),   # F (Ab7)
    (2.75, 84, 100),  # Eb (Ab7)
    (3.0, 83, 100)    # G (Ab7)
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (1.5, 46, 70),  # F (Fm7)
    (1.75, 45, 90),  # Eb (chromatic approach)
    (2.0, 48, 80),   # Ab (Fm7)
    (2.25, 47, 60),  # G (chromatic approach)
    (2.5, 46, 70),   # F (Fm7)
    (2.75, 44, 90),  # D (chromatic approach)
    (3.0, 48, 80)    # Ab (Fm7)
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.75, 64, 80),  # Cm7 (Fm7)
    (1.75, 67, 80),  # Eb (Fm7)
    (1.75, 71, 80),  # G (Fm7)
    (1.75, 76, 80),  # Bb (Fm7),
    (2.25, 64, 80),  # Cm7 (Fm7)
    (2.25, 67, 80),  # Eb (Fm7)
    (2.25, 71, 80),  # G (Fm7)
    (2.25, 76, 80),  # Bb (Fm7),
    (2.5, 64, 80),   # Cm7 (Fm7)
    (2.5, 67, 80),   # Eb (Fm7)
    (2.5, 71, 80),   # G (Fm7)
    (2.5, 76, 80),   # Bb (Fm7)
    (3.0, 64, 80),   # Cm7 (Fm7)
    (3.0, 67, 80),   # Eb (Fm7)
    (3.0, 71, 80),   # G (Fm7)
    (3.0, 76, 80)    # Bb (Fm7)
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: G -> F -> Eb -> D (sparse, expressive)
sax_notes = [
    (3.0, 83, 100),  # G (Fm7)
    (3.25, 87, 100),  # F (Fm7)
    (3.5, 81, 100),   # Eb (Fm7)
    (3.75, 79, 100),  # D (Fm7)
    (4.0, 83, 100),   # G (Fm7)
    (4.25, 87, 100),  # F (Fm7)
    (4.5, 81, 100)    # Eb (Fm7)
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (3.0, 48, 70),  # Ab (Fm7)
    (3.25, 47, 90),  # G (chromatic approach)
    (3.5, 46, 80),   # F (Fm7)
    (3.75, 44, 60),  # D (chromatic approach)
    (4.0, 48, 70),   # Ab (Fm7)
    (4.25, 47, 90),  # G (chromatic approach)
    (4.5, 46, 80)    # F (Fm7)
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (3.25, 64, 80),  # Cm7 (Fm7)
    (3.25, 67, 80),  # Eb (Fm7)
    (3.25, 71, 80),  # G (Fm7)
    (3.25, 76, 80),  # Bb (Fm7),
    (3.75, 64, 80),  # Cm7 (Fm7)
    (3.75, 67, 80),  # Eb (Fm7)
    (3.75, 71, 80),  # G (Fm7)
    (3.75, 76, 80),  # Bb (Fm7),
    (4.0, 64, 80),   # Cm7 (Fm7)
    (4.0, 67, 80),   # Eb (Fm7)
    (4.0, 71, 80),   # G (Fm7)
    (4.0, 76, 80),   # Bb (Fm7)
    (4.5, 64, 80),   # Cm7 (Fm7)
    (4.5, 67, 80),   # Eb (Fm7)
    (4.5, 71, 80),   # G (Fm7)
    (4.5, 76, 80)    # Bb (Fm7)
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: F -> Eb -> D -> C (sparse, expressive)
sax_notes = [
    (4.5, 87, 100),  # F (Fm7)
    (4.75, 81, 100),  # Eb (Fm7)
    (5.0, 79, 100),   # D (Fm7)
    (5.25, 76, 100),  # C (Fm7)
    (5.5, 87, 100),   # F (Fm7)
    (5.75, 81, 100),  # Eb (Fm7)
    (6.0, 79, 100)    # D (Fm7)
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (4.5, 46, 70),  # F (Fm7)
    (4.75, 44, 90),  # D (chromatic approach)
    (5.0, 48, 80),   # Ab (Fm7)
    (5.25, 50, 60),  # Bb (chromatic approach)
    (5.5, 46, 70),   # F (Fm7)
    (5.75, 44, 90),  # D (chromatic approach)
    (6.0, 48, 80)    # Ab (Fm7)
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (4.75, 64, 80),  # Cm7 (Fm7)
    (4.75, 67, 80),  # Eb (Fm7)
    (4.75, 71, 80),  # G (Fm7)
    (4.75, 76, 80),  # Bb (Fm7),
    (5.25, 64, 80),  # Cm7 (Fm7)
    (5.25, 67, 80),  # Eb (Fm7)
    (5.25, 71, 80),  # G (Fm7)
    (5.25, 76, 80),  # Bb (Fm7),
    (5.5, 64, 80),   # Cm7 (Fm7)
    (5.5, 67, 80),   # Eb (Fm7)
    (5.5, 71, 80),   # G (Fm7)
    (5.5, 76, 80),   # Bb (Fm7)
    (6.0, 64, 80),   # Cm7 (Fm7)
    (6.0, 67, 80),   # Eb (Fm7)
    (6.0, 71, 80),   # G (Fm7)
    (6.0, 76, 80)    # Bb (Fm7)
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 36), (7.125, 42)
]
for time, note in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_introduction.mid')
