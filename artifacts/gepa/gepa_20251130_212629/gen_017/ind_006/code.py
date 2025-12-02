
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

# Kick on 1 and 3 with slight rhythmic tension
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4 with subtle syncopation
drums.notes.append(pretty_midi.Note(velocity=85, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth note, but slightly off-time for subtle tension
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.1875))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5625))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.9375))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.3125))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=1.6875))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.0))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - Marcus: Walking line, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=1.625, end=1.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.0))

# Piano - Diane: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.625))  # Dm7
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.625))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=1.625))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=1.5, end=1.625))  # C

piano.notes.append(pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.375))  # Dm7
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.375))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.375))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=2.25, end=2.375))  # C

# Sax - Dante: Melody, short motif, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0))   # C

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - Marcus: Walking line, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.125))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.125, end=3.25))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.5))

# Piano - Diane: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.125))  # Dm7
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.125))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.125))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=3.0, end=3.125))  # C

piano.notes.append(pretty_midi.Note(velocity=85, pitch=62, start=3.75, end=3.875))  # Dm7
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=3.875))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=3.75, end=3.875))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=3.75, end=3.875))  # C

# Sax - Dante: Melody variation, leave it hanging again
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5))   # D

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass - Marcus: Walking line, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.625))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=4.625, end=4.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=4.875))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.0))

# Piano - Diane: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.625))  # Dm7
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.625))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=4.5, end=4.625))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=4.5, end=4.625))  # C

piano.notes.append(pretty_midi.Note(velocity=85, pitch=62, start=5.25, end=5.375))  # Dm7
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.375))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=5.25, end=5.375))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=5.25, end=5.375))  # C

# Sax - Dante: Melody variation, end with a question
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=4.875))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0))   # D

# Add the drum fill for the end of bar 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=5.0, end=5.125))  # Kick
drums.notes.append(pretty_midi.Note(velocity=85, pitch=38, start=5.25, end=5.375))  # Snare
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=5.0, end=5.5))    # Hi-hat

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
