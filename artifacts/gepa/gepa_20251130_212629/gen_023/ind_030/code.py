
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.0, end=0.375))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))  # Snare on 4

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75))  # F7
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0))  # A7
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25))  # F7
sax.notes.append(pretty_midi.Note(velocity=110, pitch=63, start=2.25, end=2.5))  # D7
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75))  # F7

# Bass: walking line
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.75))   # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=1.75, end=2.0))   # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=39, start=2.0, end=2.25))   # E
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.5))   # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.75))   # A

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=1.75, end=2.0))   # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=1.75, end=2.0))   # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=2.0))   # C
piano.notes.append(pretty_midi.Note(velocity=95, pitch=71, start=1.75, end=2.0))   # E
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=2.5, end=2.75))   # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=2.5, end=2.75))   # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=2.5, end=2.75))   # C
piano.notes.append(pretty_midi.Note(velocity=95, pitch=71, start=2.5, end=2.75))   # E

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))  # Snare on 4

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif, variation
sax.notes.append(pretty_midi.Note(velocity=110, pitch=63, start=3.0, end=3.25))  # D7
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5))  # F7
sax.notes.append(pretty_midi.Note(velocity=110, pitch=63, start=3.5, end=3.75))  # D7
sax.notes.append(pretty_midi.Note(velocity=110, pitch=61, start=3.75, end=4.0))  # C7
sax.notes.append(pretty_midi.Note(velocity=110, pitch=63, start=4.0, end=4.25))  # D7

# Bass: walking line
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.25))   # Bb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=3.25, end=3.5))   # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=3.5, end=3.75))   # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=39, start=3.75, end=4.0))   # E
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=4.0, end=4.25))   # F

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=3.25, end=3.5))   # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.5))   # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=3.25, end=3.5))   # C
piano.notes.append(pretty_midi.Note(velocity=95, pitch=71, start=3.25, end=3.5))   # E
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=4.0, end=4.25))   # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=4.0, end=4.25))   # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=4.0, end=4.25))   # C
piano.notes.append(pretty_midi.Note(velocity=95, pitch=71, start=4.0, end=4.25))   # E

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))  # Snare on 4

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif, ends with a question
sax.notes.append(pretty_midi.Note(velocity=110, pitch=61, start=4.5, end=4.75))  # C7
sax.notes.append(pretty_midi.Note(velocity=110, pitch=63, start=4.75, end=5.0))  # D7
sax.notes.append(pretty_midi.Note(velocity=110, pitch=61, start=5.0, end=5.25))  # C7
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5))  # Bb7
sax.notes.append(pretty_midi.Note(velocity=110, pitch=61, start=5.5, end=5.75))  # C7

# Bass: walking line
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.75))   # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=4.75, end=5.0))   # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=39, start=5.0, end=5.25))   # E
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.5))   # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.75))   # A

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=4.75, end=5.0))   # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=4.75, end=5.0))   # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=4.75, end=5.0))   # C
piano.notes.append(pretty_midi.Note(velocity=95, pitch=71, start=4.75, end=5.0))   # E
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=5.5, end=5.75))   # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=5.5, end=5.75))   # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=5.5, end=5.75))   # C
piano.notes.append(pretty_midi.Note(velocity=95, pitch=71, start=5.5, end=5.75))   # E

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))  # Snare on 4

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
