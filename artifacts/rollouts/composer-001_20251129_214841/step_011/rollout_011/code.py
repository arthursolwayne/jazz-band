
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(drum_kick_1)
drums.notes.append(drum_kick_2)

# Snare on 2 and 4
drum_snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0)
drums.notes.append(drum_snare_1)
drums.notes.append(drum_snare_2)

# Hi-hat on every eighth note
for i in range(0, 6):
    start = i * 0.375
    end = start + 0.125
    note = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass - walking line, chromatic approaches
bass_notes = [
    (1.5, 60),   # C
    (1.875, 61), # C#
    (2.25, 62),  # D
    (2.625, 60), # C
    (2.875, 59), # B
    (3.0, 60)    # C
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (1.875s)
    (1.875, 60), (1.875, 64), (1.875, 67), (1.875, 71),
    # Bar 2, beat 4 (2.625s)
    (2.625, 60), (2.625, 64), (2.625, 67), (2.625, 71)
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125)
    piano.notes.append(note)

# Dante on sax - motif in C (start at 1.5s)
sax_notes = [
    (1.5, 65), # E
    (1.875, 67), # G
    (2.25, 69), # Bb
    (2.625, 67), # G
    (2.875, 65), # E
    (3.0, 64)    # D
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass - walking line, chromatic approaches
bass_notes = [
    (3.0, 60),   # C
    (3.375, 61), # C#
    (3.75, 62),  # D
    (4.125, 60), # C
    (4.375, 59), # B
    (4.5, 60)    # C
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (3.375s)
    (3.375, 60), (3.375, 64), (3.375, 67), (3.375, 71),
    # Bar 3, beat 4 (4.125s)
    (4.125, 60), (4.125, 64), (4.125, 67), (4.125, 71)
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125)
    piano.notes.append(note)

# Little Ray on drums
# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
drums.notes.append(drum_kick_1)
drums.notes.append(drum_kick_2)

# Snare on 2 and 4
drum_snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0)
drums.notes.append(drum_snare_1)
drums.notes.append(drum_snare_2)

# Hi-hat on every eighth note
for i in range(6, 12):
    start = i * 0.375
    end = start + 0.125
    note = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus on bass - walking line, chromatic approaches
bass_notes = [
    (4.5, 60),   # C
    (4.875, 61), # C#
    (5.25, 62),  # D
    (5.625, 60), # C
    (5.875, 59), # B
    (6.0, 60)    # C
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (4.875s)
    (4.875, 60), (4.875, 64), (4.875, 67), (4.875, 71),
    # Bar 4, beat 4 (5.625s)
    (5.625, 60), (5.625, 64), (5.625, 67), (5.625, 71)
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125)
    piano.notes.append(note)

# Little Ray on drums
# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drums.notes.append(drum_kick_1)
drums.notes.append(drum_kick_2)

# Snare on 2 and 4
drum_snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=6.125, end=6.25)
drums.notes.append(drum_snare_1)
drums.notes.append(drum_snare_2)

# Hi-hat on every eighth note
for i in range(12, 18):
    start = i * 0.375
    end = start + 0.125
    note = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(note)

# Dante on sax - motif in C (start at 4.5s)
sax_notes = [
    (4.5, 65), # E
    (4.875, 67), # G
    (5.25, 69), # Bb
    (5.625, 67), # G
    (5.875, 65), # E
    (6.0, 64)    # D
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
