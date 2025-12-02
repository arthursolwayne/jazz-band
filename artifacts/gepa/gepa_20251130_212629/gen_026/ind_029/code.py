
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in Fm, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.625))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=35, start=1.625, end=1.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=34, start=1.75, end=1.875))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=1.875, end=2.0))  # F

# Diane: 7th chords comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.75))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5))

# Dante: Motif - start it, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=110, pitch=63, start=1.5, end=1.75))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5))  # B
sax.notes.append(pretty_midi.Note(velocity=110, pitch=63, start=2.5, end=2.75))  # Bb

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line in Fm
bass.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.125))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=34, start=3.125, end=3.25))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=35, start=3.25, end=3.375))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=37, start=3.375, end=3.5))  # F

# Diane: 7th chords comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.25))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.0))

# Dante: Motif - continue and end with a question
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.25))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=63, start=3.25, end=3.5))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75))  # B
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=63, start=4.25, end=4.5))  # Bb (ends with a question)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line in Fm
bass.notes.append(pretty_midi.Note(velocity=90, pitch=37, start=4.5, end=4.625))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=35, start=4.625, end=4.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=34, start=4.75, end=4.875))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=4.875, end=5.0))  # F

# Diane: 7th chords comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.75))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.5))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_intro.mid")
