
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=2.75, end=3.0))  # C

# Bass (walking line in Fm)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=2.0))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=2.5, end=2.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=2.75, end=3.0))  # Ab

# Piano (7th chords on 2 and 4)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0))  # D

# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.0))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=4.25, end=4.5))  # C

# Bass (walking line in Fm)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.25))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=3.25, end=3.5))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.0))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=4.0, end=4.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=4.25, end=4.5))  # Ab

# Piano (7th chords on 2 and 4)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5))  # D

# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.5))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=5.75, end=6.0))  # C

# Bass (walking line in Fm)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.75))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=4.75, end=5.0))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.25))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.5))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=5.5, end=5.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=5.75, end=6.0))  # Ab

# Piano (7th chords on 2 and 4)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0))  # D

# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
