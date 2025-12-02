
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Fm
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=1.5, end=1.875))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25)) # Gb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)) # Ab
bass.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0))  # Bb

# Diane: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875))  # Db
piano.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625)) # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625)) # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625)) # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625)) # Db

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))

# Dante: Tenor sax melody
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0))   # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25))   # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5))   # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75))   # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0))   # C#

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line in Fm
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=3.0, end=3.375))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75)) # Gb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)) # Ab
bass.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5))  # Bb

# Diane: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375))  # Db
piano.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125)) # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125)) # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125)) # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125)) # Db

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=4.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))

# Dante: Tenor sax melody
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25))   # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5))   # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75))   # C#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0))   # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25))   # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5))   # A

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=4.5, end=4.875))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25)) # Gb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)) # Ab
bass.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.0))  # Bb

# Diane: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875))  # Db
piano.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.625)) # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625)) # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625)) # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625)) # Db

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))

# Dante: Tenor sax melody
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75))   # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0))   # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25))   # C#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5))   # D#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75))   # C#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0))   # C

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
