
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
for i in range(4):
    time = i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.1875, end=time + 0.3125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    (1.5, 50, 100),  # D
    (1.875, 49, 100), # C#
    (2.25, 51, 100),  # Eb
    (2.625, 52, 100)  # E
]
for start, pitch, vel in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.375))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (1.875, 50, 100),  # D
    (1.875, 62, 100),  # Bb
    (1.875, 64, 100),  # C
    (1.875, 67, 100),  # Eb
    (2.625, 50, 100),  # D
    (2.625, 62, 100),  # Bb
    (2.625, 64, 100),  # C
    (2.625, 67, 100)   # Eb
]
for start, pitch, vel in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.375))

# Dante: Motif - start on D (62) with a minor 3rd approach
sax_notes = [
    (1.5, 60, 110),  # C (chromatic approach)
    (1.625, 62, 110),  # D
    (1.75, 64, 110),  # Eb
    (2.125, 62, 110),  # D (return)
    (2.25, 60, 110),  # C
    (2.375, 62, 110)   # D (resolve)
]
for start, pitch, vel in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    (3.0, 52, 100),  # E
    (3.375, 53, 100), # F
    (3.75, 50, 100),  # D
    (4.125, 49, 100)  # C#
]
for start, pitch, vel in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.375))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (3.375, 52, 100),  # E
    (3.375, 64, 100),  # C
    (3.375, 67, 100),  # Eb
    (3.375, 71, 100),  # G
    (4.125, 52, 100),  # E
    (4.125, 64, 100),  # C
    (4.125, 67, 100),  # Eb
    (4.125, 71, 100)   # G
]
for start, pitch, vel in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.375))

# Dante: Motif variation
sax_notes = [
    (3.0, 64, 110),  # Eb
    (3.125, 62, 110),  # D
    (3.25, 60, 110),  # C
    (3.625, 62, 110),  # D
    (3.75, 64, 110),  # Eb
    (3.875, 62, 110),  # D
    (4.0, 60, 110),  # C
    (4.125, 62, 110)   # D
]
for start, pitch, vel in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    (4.5, 49, 100),  # C#
    (4.875, 50, 100),  # D
    (5.25, 52, 100),  # E
    (5.625, 53, 100)  # F
]
for start, pitch, vel in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.375))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (4.875, 50, 100),  # D
    (4.875, 62, 100),  # Bb
    (4.875, 64, 100),  # C
    (4.875, 67, 100),  # Eb
    (5.625, 50, 100),  # D
    (5.625, 62, 100),  # Bb
    (5.625, 64, 100),  # C
    (5.625, 67, 100)   # Eb
]
for start, pitch, vel in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.375))

# Dante: Motif variation
sax_notes = [
    (4.5, 60, 110),  # C
    (4.625, 62, 110),  # D
    (4.75, 64, 110),  # Eb
    (5.125, 62, 110),  # D
    (5.25, 60, 110),  # C
    (5.375, 62, 110),  # D
    (5.5, 64, 110),  # Eb
    (5.625, 62, 110)   # D
]
for start, pitch, vel in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.125))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = 1.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.1875, end=time + 0.3125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
