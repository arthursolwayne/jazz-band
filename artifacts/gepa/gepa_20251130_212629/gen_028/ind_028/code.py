
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: minimal, with space and tension
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.375, end=0.5))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=1.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: first phrase, a simple motif with space
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.125, end=2.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75))

# Bass: walking line with chromatic approach
bass.notes.append(pretty_midi.Note(velocity=70, pitch=55, start=1.5, end=1.75))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=57, start=1.75, end=2.0))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=59, start=2.0, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=60, start=2.25, end=2.5))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=62, start=2.5, end=2.75))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=63, start=2.75, end=3.0))

# Piano: comping with 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0))  # D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=1.75, end=2.0))

piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0))  # D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=2.75, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=2.75, end=3.0))

# Drums: full pattern with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.625, end=1.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=2.375, end=2.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=3.0))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: answer to first phrase, with a slight variation and tension
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.625))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.375))

# Bass: walking line with chromatic approach
bass.notes.append(pretty_midi.Note(velocity=70, pitch=64, start=3.0, end=3.25))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=66, start=3.25, end=3.5))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=67, start=3.5, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=69, start=3.75, end=4.0))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=71, start=4.0, end=4.25))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=72, start=4.25, end=4.5))

# Piano: comping with 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5))  # D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=3.25, end=3.5))

piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5))  # D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=4.25, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=4.25, end=4.5))

# Drums: full pattern with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.125))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=3.125, end=3.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=3.875, end=4.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.5))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: ends with a question, leaving it open
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.125, end=5.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75))

# Bass: walking line with chromatic approach
bass.notes.append(pretty_midi.Note(velocity=70, pitch=74, start=4.5, end=4.75))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=76, start=4.75, end=5.0))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=77, start=5.0, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=79, start=5.25, end=5.5))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=81, start=5.5, end=5.75))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=82, start=5.75, end=6.0))

# Piano: comping with 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0))  # D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=4.75, end=5.0))

piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0))  # D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=5.75, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=5.75, end=6.0))

# Drums: full pattern with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.625))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=4.625, end=4.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.75, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=5.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro.mid")
