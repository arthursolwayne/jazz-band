
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5))  # F7 again
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5))  # D

# Marcus: Walking line, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.5))  # F

# Dante: Melody, sparse but expressive
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.25))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5))  # F

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0))  # F7 again
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.0))  # D

# Marcus: Walking line, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=3.25, end=3.5))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0))  # F

# Dante: Melody, sparse but expressive
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0))  # F

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5))  # F7 again
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.5))  # D

# Marcus: Walking line, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=4.75, end=5.0))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.25))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5))  # F

# Dante: Melody, sparse but expressive
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.75))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=5.0, end=5.25))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5))  # F

# Drums: full pattern
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.5))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
