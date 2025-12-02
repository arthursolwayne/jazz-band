
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
# Sax motif: Dm7 (D F A C) -> D F A D (motif)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5))  # D

# Marcus: Walking bass line in Dm
bass.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=1.75, end=2.0))  # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=51, start=2.0, end=2.25))  # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5))  # F

# Diane: Comping on 2 and 4 with Dm7 (D F A C)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5))  # C

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=3.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=3.0))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Dm7 (D F A C) -> F A D F (motif variation)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0))  # F

# Marcus: Walking bass line in Dm
bass.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=3.25, end=3.5))  # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=51, start=3.5, end=3.75))  # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.0))  # F

# Diane: Comping on 2 and 4 with Dm7 (D F A C)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0))  # C

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.25, end=4.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.25, end=4.5))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Dm7 (D F A C) -> A D F A (motif resolution)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5))  # A

# Marcus: Walking bass line in Dm
bass.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.75))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=4.75, end=5.0))  # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=51, start=5.0, end=5.25))  # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.5))  # F

# Diane: Comping on 2 and 4 with Dm7 (D F A C)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5))  # C

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.75, end=6.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.75, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
