
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875))  # Snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))  # Hihat on every eighth

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starts here
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75))    # F5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0))    # G5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25))    # A5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5))    # G5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75))    # F5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=3.0))    # E5

# Bass: Walking line in F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75))    # F3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0))    # G3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25))    # A3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.5))    # E3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=2.5, end=2.75))    # F3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=2.75, end=3.0))    # D3

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75))    # F5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.75))    # Bb5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75))    # B5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75))    # D5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5))    # F5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.5))    # Bb5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5))    # B5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5))    # D5

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))  # Snare on 4

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with variation
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25))    # F5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5))    # G5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75))    # A5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0))    # G5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25))    # F5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=4.25, end=4.5))    # E5

# Bass: Walking line in F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25))    # F3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=3.25, end=3.5))    # G3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.75))    # A3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.0))    # E3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=4.0, end=4.25))    # F3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=4.25, end=4.5))    # D3

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25))    # F5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.25))    # Bb5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25))    # B5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25))    # D5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0))    # F5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.0))    # Bb5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0))    # B5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0))    # D5

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))  # Snare on 4

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Motif returns and resolves
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75))    # F5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0))    # G5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25))    # A5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5))    # G5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75))    # F5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=5.75, end=6.0))    # E5

# Bass: Walking line in F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75))    # F3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=4.75, end=5.0))    # G3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=5.0, end=5.25))    # A3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.5))    # E3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=5.5, end=5.75))    # F3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=5.75, end=6.0))    # D3

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75))    # F5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.75))    # Bb5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75))    # B5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75))    # D5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5))    # F5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.5))    # Bb5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5))    # B5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5))    # D5

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))  # Snare on 4

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
