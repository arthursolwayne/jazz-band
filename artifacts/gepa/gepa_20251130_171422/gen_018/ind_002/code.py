
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

# Bass: Walking line, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625))  # C
bass.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0))  # D

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875))  # B7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625))  # B7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # Bb

# Sax: Motif, start it, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0))  # C

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875))

# Bass: Walking line, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375))  # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125))  # Db
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5))  # Eb

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375))  # B7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125))  # B7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125))  # Bb

# Sax: Motif, continue it, resolve it
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5))  # C

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375))

# Bass: Walking line, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25))  # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625))  # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0))  # F

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875))  # B7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625))  # B7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625))  # Bb

# Sax: Motif, finish it, leave space
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0))  # D

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
