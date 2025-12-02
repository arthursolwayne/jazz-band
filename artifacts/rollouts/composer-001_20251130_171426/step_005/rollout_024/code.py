
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm
bass_notes = [
    (1.5, 44), (1.875, 43), (2.25, 42), (2.625, 40),
    (3.0, 44), (3.375, 43), (3.75, 42), (4.125, 40)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.875, 64), (1.875, 67), (1.875, 71), (1.875, 74),  # F7
    (2.625, 64), (2.625, 67), (2.625, 71), (2.625, 74),  # F7
    (3.375, 64), (3.375, 67), (3.375, 71), (3.375, 74),  # F7
    (4.125, 64), (4.125, 67), (4.125, 71), (4.125, 74)   # F7
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(n)

# Sax: Motif - Fm, F, D, Bb (F, D, Bb, F), suspended, then resolve
sax_notes = [
    (1.5, 87), (1.875, 82), (2.25, 77), (2.625, 87),  # F, D, Bb, F
    (3.0, 87), (3.375, 82), (3.75, 77), (4.125, 87)   # Repeat motif
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm
bass_notes = [
    (3.0, 44), (3.375, 43), (3.75, 42), (4.125, 40),
    (4.5, 44), (4.875, 43), (5.25, 42), (5.625, 40)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (3.375, 64), (3.375, 67), (3.375, 71), (3.375, 74),  # F7
    (4.125, 64), (4.125, 67), (4.125, 71), (4.125, 74),  # F7
    (4.875, 64), (4.875, 67), (4.875, 71), (4.875, 74),  # F7
    (5.625, 64), (5.625, 67), (5.625, 71), (5.625, 74)   # F7
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(n)

# Sax: Motif - Fm, F, D, Bb (F, D, Bb, F), suspended, then resolve
sax_notes = [
    (3.0, 87), (3.375, 82), (3.75, 77), (4.125, 87),  # F, D, Bb, F
    (4.5, 87), (4.875, 82), (5.25, 77), (5.625, 87)   # Repeat motif
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(n)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm
bass_notes = [
    (4.5, 44), (4.875, 43), (5.25, 42), (5.625, 40),
    (6.0, 44), (6.375, 43), (6.75, 42), (7.125, 40)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (4.875, 64), (4.875, 67), (4.875, 71), (4.875, 74),  # F7
    (5.625, 64), (5.625, 67), (5.625, 71), (5.625, 74),  # F7
    (6.375, 64), (6.375, 67), (6.375, 71), (6.375, 74),  # F7
    (7.125, 64), (7.125, 67), (7.125, 71), (7.125, 74)   # F7
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(n)

# Sax: Motif - Fm, F, D, Bb (F, D, Bb, F), suspended, then resolve
sax_notes = [
    (4.5, 87), (4.875, 82), (5.25, 77), (5.625, 87),  # F, D, Bb, F
    (6.0, 87), (6.375, 82), (6.75, 77), (7.125, 87)   # Repeat motif
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(n)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
