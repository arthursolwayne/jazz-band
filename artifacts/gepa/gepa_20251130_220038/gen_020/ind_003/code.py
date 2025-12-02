
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
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=i * 0.375, end=i * 0.375 + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
# Walking line in Dm, chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=1.75)),    # D
    (pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0)),    # Eb
    (pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25)),    # F
    (pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.5)),    # G
    (pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.75)),    # Ab
    (pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0)),    # Bb
    (pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25)),    # B
    (pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.5)),    # C
    (pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.75)),    # C#
    (pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.0)),    # D
    (pretty_midi.Note(velocity=80, pitch=75, start=4.0, end=4.25)),    # Eb
    (pretty_midi.Note(velocity=80, pitch=77, start=4.25, end=4.5)),    # F
    (pretty_midi.Note(velocity=80, pitch=79, start=4.5, end=4.75)),    # G
    (pretty_midi.Note(velocity=80, pitch=80, start=4.75, end=5.0)),    # Ab
    (pretty_midi.Note(velocity=80, pitch=82, start=5.0, end=5.25)),    # Bb
    (pretty_midi.Note(velocity=80, pitch=84, start=5.25, end=5.5)),    # B
    (pretty_midi.Note(velocity=80, pitch=86, start=5.5, end=5.75)),    # C
    (pretty_midi.Note(velocity=80, pitch=87, start=5.75, end=6.0)),    # C#
]
bass.notes.extend(bass_notes)

# Piano: Diane
# 7th chords on 2 and 4
# Dm7 on 2 (1.75 - 2.0)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0)) # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0)) # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0)) # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0)) # D

# Dm7 on 4 (3.5 - 4.0)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=4.0)) # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=4.0)) # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=4.0)) # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=4.0)) # D

# Sax: Dante - short motif, make it sing
# Dm7 phrase: D - Eb - F - G (1.5 - 2.0)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)) # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0)) # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5)) # G

# Repeat the motif with variation at bar 3
# D - Eb - F - Ab (3.0 - 3.5)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25)) # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5)) # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0)) # Ab

# Repeat the motif with variation at bar 4
# D - Eb - F - Bb (4.5 - 5.0)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75)) # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0)) # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5)) # Bb

# Drums: Bar 2 (1.5 - 3.0)
for i in range(4, 8):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=i * 0.375, end=i * 0.375 + 0.125))
for i in range(5, 9):
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=i * 0.375, end=i * 0.375 + 0.125))
for i in range(4, 8):
    for j in range(2):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=i * 0.375 + j * 0.125, end=i * 0.375 + j * 0.125 + 0.125))

# Drums: Bar 3 (3.0 - 4.5)
for i in range(8, 12):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=i * 0.375, end=i * 0.375 + 0.125))
for i in range(9, 13):
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=i * 0.375, end=i * 0.375 + 0.125))
for i in range(8, 12):
    for j in range(2):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=i * 0.375 + j * 0.125, end=i * 0.375 + j * 0.125 + 0.125))

# Drums: Bar 4 (4.5 - 6.0)
for i in range(12, 16):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=i * 0.375, end=i * 0.375 + 0.125))
for i in range(13, 17):
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=i * 0.375, end=i * 0.375 + 0.125))
for i in range(12, 16):
    for j in range(2):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=i * 0.375 + j * 0.125, end=i * 0.375 + j * 0.125 + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
