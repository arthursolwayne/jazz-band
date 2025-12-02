
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm, chromatic approaches
# Dm: D F A C
# Chromatic approach to D: C# -> D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875))  # C#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0))  # D

# Piano: 7th chords, comp on 2 and 4
# Dm7: D F A C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5))  # C

# Sax: Motif - start on D, ascend to F, hold on A, end on C with a rest
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.375))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.625))  # C

# Drums: Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5))  # E

# Piano: 7th chords
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0))  # C

# Sax: Motif variation - start on F, move to A, hold on D, end on Bb with a rest
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.875))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.875, end=4.125))  # Bb

# Drums: Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875))  # C#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0))  # E

# Piano: 7th chords
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5))  # C

# Sax: Motif variation - start on A, move to D, end on F with a rest
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.375))  # F

# Drums: Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
