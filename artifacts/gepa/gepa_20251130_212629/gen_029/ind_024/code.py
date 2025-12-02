
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
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=1.625, end=1.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=1.875))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.0))  # G

# Diane: 7th chords comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75))  # D7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75))

# Dante: sax motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.6875))  # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.8125))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.8125, end=2.0))  # F

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.125))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.125, end=3.25))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.375))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.5))  # Eb

# Diane: 7th chords comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25))  # D7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25))

# Dante: sax motif (reprise with variation)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.1875))  # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.3125))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.3125, end=3.5))  # F

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.625))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=4.625, end=4.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=4.875))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0))  # G

# Diane: 7th chords comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75))  # D7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75))

# Dante: sax motif (final phrase, ends on a question)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.6875))  # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.8125))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.8125, end=5.0))  # F

# Little Ray: Bar 4 drum fill
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=4.75, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=4.875, end=5.0))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
