
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
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0))

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=2.625, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=2.625, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0))

# Sax: Motif starting on F, with space and rests
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.8))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.8, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.1, end=2.3))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.4, end=2.6))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.7, end=2.9))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5))

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=4.125, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=4.125, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.875))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5))

# Sax: Continue the motif, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.15))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.15, end=3.3))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.45, end=3.6))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.6, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.9, end=4.05))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.05, end=4.2))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.35, end=4.5))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0))

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=5.625, end=6.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.375))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=5.625, end=6.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0))

# Sax: End with a question, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.65))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.65, end=4.8))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.95, end=5.1))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.1, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=5.4, end=5.55))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.55, end=5.7))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=5.85, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")
