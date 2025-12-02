
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
hihat_start = 0.0
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_start + 0.375))
    hihat_start += 0.375

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=2.0, end=2.25))  # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.5))  # F#

# Bass walking line in Fm
# F, Gb, Ab, A (Fm7)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.5))

# Piano: 7th chords, comp on 2 and 4
# Fm7 on beat 2 (F, Ab, C, Db)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody, continuation
sax.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.25))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=3.25, end=3.5))  # F#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=3.5, end=3.75))  # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0))  # F

# Bass walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.5, end=3.75))  # Gb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0))  # Ab

# Piano: 7th chords, comp on 2 and 4
# Fm7 on beat 2 (F, Ab, C, Db)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=4.0))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax ends on a question, leaving it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0))  # F

# Bass walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.75))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0))  # Bb

# Piano: 7th chords, comp on 2 and 4
# Fm7 on beat 2 (F, Ab, C, Db)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.5))

# Drums: bar 4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=95, pitch=38, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=95, pitch=38, start=6.0, end=6.125))

# Hi-hat on every eighth
hihat_start = 4.5
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_start + 0.375))
    hihat_start += 0.375

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro_wayne.mid")
