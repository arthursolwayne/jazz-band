
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
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# Dm7: D F A C
# Walking line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D...

# Bar 2 (1.5 - 3.0s)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=1.625, end=1.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=1.875))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0))   # G

# Bar 3 (3.0 - 4.5s)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.125))  # A
bass.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=3.125, end=3.25))  # Bb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.375))  # B
bass.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.5))   # C

# Bar 4 (4.5 - 6.0s)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=4.625, end=4.75))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=4.875))  # A
bass.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.0))   # C

# Piano: 7th chords, comp on 2 and 4
# Dm7: D F A C

# Bar 2 (1.5 - 3.0s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0))   # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0))   # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0))   # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=2.0))   # C

# Bar 3 (3.0 - 4.5s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5))   # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5))   # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5))   # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5))   # C

# Bar 4 (4.5 - 6.0s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0))   # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0))   # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0))   # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.0))   # C

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875))  # A

# Bar 3: Leave it hanging, then return
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5))   # A

# Bar 4: Finish it
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625))  # B
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=4.75))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0))   # F

# Drums: Bar 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))

# Hihat on every eighth
# Bar 2
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0))
# Bar 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5))
# Bar 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
