
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

# Bar 2: Full quartet in (1.5 - 3.0s)
# Diane (piano) plays a 7th chord on beat 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.75))

# Marcus (bass) walks chromatically with a slight syncopation
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.625))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=1.625, end=1.75))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=1.875))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0))  # G#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=2.0, end=2.125))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=2.125, end=2.25))  # A#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.375))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=2.375, end=2.5))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.125))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=3.125, end=3.25))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.375))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5))  # G#

# Dante (sax) plays a short motif with space and tension
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25))  # E
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=3.0))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25))  # E

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane (piano) continues comping but with a different chord
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.125))

# Marcus (bass) continues walking chromatically
bass.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=3.5, end=3.625))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3.625, end=3.75))  # A#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=3.875))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=3.875, end=4.0))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.0, end=4.125))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.25))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.375))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=4.375, end=4.5))  # G#

# Dante (sax) continues motif but leaves it hanging
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0))  # E
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=4.0, end=4.25))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5))  # E

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane (piano) plays a more open chord
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=4.875, end=5.25))

# Marcus (bass) continues walking
bass.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.625))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=4.625, end=4.75))  # A#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=4.75, end=4.875))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=5.0))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.125))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=5.125, end=5.25))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.375))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=5.375, end=5.5))  # G#

# Dante (sax) ends on a question, not a statement
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0))  # E
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5))  # E

# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
