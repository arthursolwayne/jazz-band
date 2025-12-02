
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

# Hihat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# SAX: Start the motif
# Dm7 -> Eb7 -> Gm7 -> C7
# Dm7 (D F A C)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.625))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.625))

# BASS: Walking line, chromatic approaches
# Dm7 -> Eb7 -> Gm7 -> C7
# D -> Eb -> F -> G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=1.75, end=2.0))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=2.0, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.5))

# PIANO: 7th chords on 2 and 4
# Dm7 on 2, Eb7 on 4
# Dm7 (D F A C)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0))

# Eb7 (Eb G Bb D)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5))

# Drums continue
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.25))

# Hihat on every eighth
for i in range(4, 8):
    start = (i - 4) * 0.375 + 1.5
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 3: Full quartet (3.0 - 4.5s)
# SAX: Continue the motif
# Gm7 (G Bb D F)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.125))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.125))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.125))

# BASS: Walking line, chromatic approaches
# Gm7 -> C7
# G -> A -> B -> C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=3.25, end=3.5))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=3.5, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.0))

# PIANO: 7th chords on 2 and 4
# Gm7 on 2, C7 on 4
# Gm7 (G Bb D F)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5))

# C7 (C E G B)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0))

# Drums continue
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.625, end=4.75))

# Hihat on every eighth
for i in range(8, 12):
    start = (i - 8) * 0.375 + 3.0
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 4: Full quartet (4.5 - 6.0s)
# SAX: Finish the motif
# C7 (C E G B)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625))

# BASS: Walking line, chromatic approaches
# C -> D -> E -> F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5))

# PIANO: 7th chords on 2 and 4
# C7 on 2 and 4
# C7 (C E G B)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0))

piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75))

# Drums continue
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=6.125, end=6.25))

# Hihat on every eighth
for i in range(12, 16):
    start = (i - 12) * 0.375 + 4.5
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
