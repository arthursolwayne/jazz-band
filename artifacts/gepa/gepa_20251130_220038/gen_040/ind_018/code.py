
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
# Sax: Melody starts
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5))  # F

# Bass: Walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.75))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=1.75, end=2.0))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.5))  # F

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continuation of melody
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0))  # G

# Bass: Walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.25))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.75))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.0))  # F

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.5))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5))

# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0))  # F

# Bass: Walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.75))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=4.75, end=5.0))  # G

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.0))

# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
