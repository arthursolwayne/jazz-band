
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth note
for i in range(4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 2: Full ensemble starts (1.5 - 3.0s)

# Sax: Fm7 -> Bb -> Ab -> Gm7
# Fm7: F, Ab, Db, Eb
# Bb: Bb
# Ab: Ab
# Gm7: G, Bb, D, F

sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0))  # Ab
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25))  # Db
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5))  # Eb

# Bass: Walking line in Fm
# F -> G -> Ab -> A
# F -> G -> Ab -> A -> Bb -> C -> Db -> D

bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.625))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.625, end=1.75))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=68, start=1.75, end=1.875))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.125))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=2.125, end=2.25))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=73, start=2.25, end=2.375))  # Db
bass.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=2.375, end=2.5))  # D

# Piano: Fm7 on 2 and 4
# 2: Fm7 (F, Ab, Db, Eb)
# 4: Gm7 (G, Bb, D, F)

# 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=1.75, end=2.0))  # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0))  # Db
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0))  # Eb

# 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5))  # F

# Bar 3: Full ensemble (3.0 - 4.5s)

# Sax: Gm7 -> C -> Bb -> Am7
# Gm7: G, Bb, D, F
# C: C
# Bb: Bb
# Am7: A, C, E, G

sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=3.5, end=3.75))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.0))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=4.0, end=4.25))  # C
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=4.25, end=4.5))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=5.0))  # C
sax.notes.append(pretty_midi.Note(velocity=110, pitch=76, start=5.0, end=5.25))  # E
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5))  # G

# Bass: Walking line in Gm
# G -> A -> Bb -> B
# G -> A -> Bb -> B -> C -> D -> Eb -> E

bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.125))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.125, end=3.25))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.375))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.5))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.625))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=3.625, end=3.75))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=73, start=3.75, end=3.875))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=3.875, end=4.0))  # E

# Piano: Gm7 on 2 and 4
# 2: Gm7 (G, Bb, D, F)
# 4: Am7 (A, C, E, G)

# 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0))  # F

# 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.25, end=4.5))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=4.25, end=4.5))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5))  # G

# Bar 4: Full ensemble (4.5 - 6.0s)

# Sax: Am7 -> D -> C -> Bm7
# Am7: A, C, E, G
# D: D
# C: C
# Bm7: B, D, F#, A

sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=5.0))  # C
sax.notes.append(pretty_midi.Note(velocity=110, pitch=76, start=5.0, end=5.25))  # E
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=5.5, end=5.75))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=5.75, end=6.0))  # C
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=6.0, end=6.25))  # B
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=6.25, end=6.5))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=76, start=6.5, end=6.75))  # F#
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=6.75, end=7.0))  # A

# Bass: Walking line in Am
# A -> B -> C -> D
# A -> B -> C -> D -> Eb -> F -> G -> Ab

bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.625))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=4.625, end=4.75))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=4.75, end=4.875))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.0))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=5.0, end=5.125))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=5.125, end=5.25))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=5.25, end=5.375))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=78, start=5.375, end=5.5))  # Ab

# Piano: Am7 on 2 and 4
# 2: Am7 (A, C, E, G)
# 4: Bm7 (B, D, F#, A)

# 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.5))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.5))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5))  # G

# 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=5.75, end=6.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=5.75, end=6.0))  # F#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0))  # A

# Drums: continue playing
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0))

# Hi-hat on every eighth note
for i in range(6):
    start = 3.0 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

for i in range(6):
    start = 4.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
