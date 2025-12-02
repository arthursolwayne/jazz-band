
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    (1.5, 64),  # F
    (1.875, 63), # Eb
    (2.25, 61), # D
    (2.625, 64) # F
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Diane: 7th chords on 2 and 4 (Fm7 on beat 2, Bbm7 on beat 4)
# Fm7 = F, Ab, D, C
# Bbm7 = Bb, D, F, Ab
piano_notes = [
    # Fm7 on beat 2
    (1.875, 71), # F
    (1.875, 70), # Eb
    (1.875, 68), # D
    (1.875, 69), # C
    # Bbm7 on beat 4
    (2.625, 71), # Bb
    (2.625, 68), # D
    (2.625, 71), # F
    (2.625, 70), # Eb
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Dante: Tenor sax motif
# Start with F (66), Ab (64), D (62), and leave it hanging on D
sax_notes = [
    (1.5, 66), # F
    (1.75, 64), # Ab
    (2.0, 62), # D
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line in Fm
bass_notes = [
    (3.0, 64),  # F
    (3.375, 63), # Eb
    (3.75, 61), # D
    (4.125, 64) # F
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Diane: 7th chords on 2 and 4 (Fm7 on beat 2, Bbm7 on beat 4)
piano_notes = [
    # Fm7 on beat 2
    (3.875, 71), # F
    (3.875, 70), # Eb
    (3.875, 68), # D
    (3.875, 69), # C
    # Bbm7 on beat 4
    (4.625, 71), # Bb
    (4.625, 68), # D
    (4.625, 71), # F
    (4.625, 70), # Eb
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Dante: Tenor sax motif continuation
# Finish the motif on the D and move to Bb
sax_notes = [
    (3.0, 62), # D (from previous bar)
    (3.25, 62), # D
    (3.5, 62), # D
    (3.75, 62), # D
    (4.0, 62), # D
    (4.25, 62), # D
    (4.5, 62), # D
    (4.75, 64), # Bb
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    (4.5, 64),  # F
    (4.875, 63), # Eb
    (5.25, 61), # D
    (5.625, 64) # F
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Diane: 7th chords on 2 and 4 (Fm7 on beat 2, Bbm7 on beat 4)
piano_notes = [
    # Fm7 on beat 2
    (5.375, 71), # F
    (5.375, 70), # Eb
    (5.375, 68), # D
    (5.375, 69), # C
    # Bbm7 on beat 4
    (6.125, 71), # Bb
    (6.125, 68), # D
    (6.125, 71), # F
    (6.125, 70), # Eb
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Dante: Tenor sax motif ending
# Wrap up the motif with a downbeat resolution to Bb
sax_notes = [
    (4.5, 64), # Bb
    (4.75, 64), # Bb
    (5.0, 64), # Bb
    (5.25, 64), # Bb
    (5.5, 64), # Bb
    (5.75, 64), # Bb
    (6.0, 64) # Bb
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.25))

# Drums: Keep the same pattern for full energy
for i in range(6):
    start = i * 0.375 + 1.5
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
