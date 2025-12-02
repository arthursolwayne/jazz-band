
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
bar_duration = 1.5
time = 0.0

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 0.85))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.475))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75 * 2, end=time + 0.85 * 2))

# Hi-hat on every eighth
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.05))

time = 1.5

# Bar 2: F7, Diane plays F7sus4 -> F7
# Diane: F7sus4 (F, C, Bb) on beat 2, F7 (F, A, C, Bb) on beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time + 0.375, end=time + 0.475))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=time + 0.375, end=time + 0.475))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=time + 0.375, end=time + 0.475))  # Bb

piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time + 0.75, end=time + 0.85))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=time + 0.75, end=time + 0.85))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=time + 0.75, end=time + 0.85))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=time + 0.75, end=time + 0.85))  # Bb

# Marcus: walking bass line, F (D2), G (G2), Bb (Bb2), C (C3), F (D2)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=time + 0.375, end=time + 0.475))  # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=time + 0.75, end=time + 0.85))  # Bb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=45, start=time + 1.125, end=time + 1.225))  # C
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 1.5, end=time + 1.6))  # F

# Bar 2: Dante's motif (start on beat 1)
# F (E4), Ab (G4), Bb (A4), F (E4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=time, end=time + 0.1))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=time + 0.375, end=time + 0.475))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=time + 0.75, end=time + 0.85))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=time + 1.5, end=time + 1.6))

# Bar 3: F7, Diane plays F7 -> Fmaj7
# Diane: F7 (F, A, C, Bb) on beat 2, Fmaj7 (F, A, C, E) on beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time + 1.5 + 0.375, end=time + 1.5 + 0.475))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=time + 1.5 + 0.375, end=time + 1.5 + 0.475))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=time + 1.5 + 0.375, end=time + 1.5 + 0.475))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=time + 1.5 + 0.375, end=time + 1.5 + 0.475))  # Bb

piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time + 1.5 + 0.75, end=time + 1.5 + 0.85))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=time + 1.5 + 0.75, end=time + 1.5 + 0.85))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=time + 1.5 + 0.75, end=time + 1.5 + 0.85))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=time + 1.5 + 0.75, end=time + 1.5 + 0.85))  # E

# Marcus: walking bass line, F (D2), Ab (F2), Bb (G2), C (A2), F (D2)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 1.5, end=time + 1.6))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=time + 1.5 + 0.375, end=time + 1.5 + 0.475))  # Ab
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=time + 1.5 + 0.75, end=time + 1.5 + 0.85))  # Bb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=45, start=time + 1.5 + 1.125, end=time + 1.5 + 1.225))  # C
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 1.5 + 1.5, end=time + 1.5 + 1.6))  # F

# Bar 3: Drums (same pattern as bar 1)
time = 1.5
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 1.5 + i * 0.375, end=time + 1.5 + i * 0.375 + 0.05))

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 1.5, end=time + 1.6))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 1.5 + 0.75, end=time + 1.5 + 0.85))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 1.5 + 0.375, end=time + 1.5 + 0.475))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 1.5 + 0.75 * 2, end=time + 1.5 + 0.85 * 2))

# Bar 4: Fmaj7, Diane plays Fmaj7 -> F7
# Diane: Fmaj7 (F, A, C, E) on beat 2, F7 (F, A, C, Bb) on beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time + 3.0 + 0.375, end=time + 3.0 + 0.475))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=time + 3.0 + 0.375, end=time + 3.0 + 0.475))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=time + 3.0 + 0.375, end=time + 3.0 + 0.475))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=time + 3.0 + 0.375, end=time + 3.0 + 0.475))  # E

piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time + 3.0 + 0.75, end=time + 3.0 + 0.85))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=time + 3.0 + 0.75, end=time + 3.0 + 0.85))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=time + 3.0 + 0.75, end=time + 3.0 + 0.85))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=time + 3.0 + 0.75, end=time + 3.0 + 0.85))  # Bb

# Marcus: walking bass line, F (D2), G (G2), Bb (Bb2), C (C3), F (D2)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 3.0, end=time + 3.1))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=time + 3.0 + 0.375, end=time + 3.0 + 0.475))  # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=time + 3.0 + 0.75, end=time + 3.0 + 0.85))  # Bb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=45, start=time + 3.0 + 1.125, end=time + 3.0 + 1.225))  # C
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 3.0 + 1.5, end=time + 3.0 + 1.6))  # F

# Bar 4: Drums (same pattern as bar 1)
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 3.0 + i * 0.375, end=time + 3.0 + i * 0.375 + 0.05))

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 3.0, end=time + 3.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 3.0 + 0.75, end=time + 3.0 + 0.85))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 3.0 + 0.375, end=time + 3.0 + 0.475))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 3.0 + 0.75 * 2, end=time + 3.0 + 0.85 * 2))

# Bar 4: Dante's motif (end on beat 4)
# F (E4), Ab (G4), Bb (A4), F (E4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=time + 3.0 + 0.75, end=time + 3.0 + 0.85))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=time + 3.0 + 1.125, end=time + 3.0 + 1.225))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=time + 3.0 + 1.5, end=time + 3.0 + 1.6))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
