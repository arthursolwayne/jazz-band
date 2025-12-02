
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

# Bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: Fm (F, Ab, Bb, D)
# Start with a motif: F - Ab - Bb (1.5s to 2.25s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625))

# Bass: Walking line in Fm
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0))  # F

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875))

# Drums: Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Return to the motif, but end on D (Ab to Bb to D)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125))

# Bass: Walking line
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5))  # F

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375))

# Drums: Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif but resolve on F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=5.625, end=6.0))

# Bass: Walking line
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=5.625, end=6.0))  # F

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875))

# Drums: Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
