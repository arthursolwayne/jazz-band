
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))

# Bar 2: Start of the quartet (1.5 - 3.0s)
# Sax: Short motif, start on beat 1
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75))

# Bass: Walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=1.5, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0))

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0))

# Bar 3: Continue the quartet (3.0 - 4.5s)
# Sax: Motif returns with a slight twist
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25))

# Bass: Walking line continues
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.125))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5))

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5))

# Bar 4: End of the intro (4.5 - 6.0s)
# Sax: End on a question, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75))

# Bass: Walking line continues
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.875))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0))

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")
