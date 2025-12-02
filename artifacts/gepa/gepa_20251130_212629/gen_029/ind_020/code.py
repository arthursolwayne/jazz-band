
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.5 + 0.375 * 8))

# Bar 2: Full quartet (1.5s)

# Bass: Walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.625))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=1.625, end=1.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=1.75, end=1.875))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.0))  # A

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.625))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.625))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.625))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.375))

# Sax: Short motif, start and leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5))  # G

# Bar 3: Full quartet (2.5s)

# Bass: Continue walking line
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=2.5, end=2.625))  # Bb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=54, start=2.625, end=2.75))  # A
bass.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=2.75, end=2.875))  # C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=59, start=2.875, end=3.0))  # D

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.625))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.375))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.375))

# Sax: Continue motif, build tension
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5))  # Bb

# Bar 4: Full quartet (3.5s)

# Bass: Continue walking line
bass.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.625))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.625, end=3.75))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.875))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.875, end=4.0))  # Bb

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.625))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.625))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.625))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.625))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.375))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.375))

# Sax: End with a question, not a statement
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.25, end=4.5))  # Bb

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.5 + 0.375 * 8))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('intro.mid')
