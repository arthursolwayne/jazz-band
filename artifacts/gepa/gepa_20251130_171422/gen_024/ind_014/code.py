
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Subtle dynamics and space
drum_notes = [
    # Kick on 1 & 3
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=70, pitch=36, start=1.125, end=1.5),
    # Snare on 2 & 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=85, pitch=38, start=1.5, end=1.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bass line (chromatic with melodic contour)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=2.75, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano comping (7th chords on 2 & 4, dynamic variation)
piano_notes = [
    # Bar 2: 2nd beat
    pretty_midi.Note(velocity=85, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=75, pitch=67, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=70, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=65, pitch=60, start=1.75, end=2.0),  # C
    # Bar 2: 4th beat
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=75, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=70, pitch=60, start=2.75, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone continues motif with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Bass line (melodic continuation)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=4.25, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Piano comping (7th chords on 2 & 4, dynamic variation)
piano_notes = [
    # Bar 3: 2nd beat
    pretty_midi.Note(velocity=85, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=75, pitch=67, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=70, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=65, pitch=60, start=3.25, end=3.5),  # C
    # Bar 3: 4th beat
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=75, pitch=64, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=70, pitch=60, start=4.25, end=4.5),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone resolves motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Bass line (melodic resolution)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=5.75, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano comping (7th chords on 2 & 4, dynamic variation)
piano_notes = [
    # Bar 4: 2nd beat
    pretty_midi.Note(velocity=85, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=75, pitch=67, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=70, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=65, pitch=60, start=4.75, end=5.0),  # C
    # Bar 4: 4th beat
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=6.0),  # Bb
    pretty_midi.Note(velocity=75, pitch=64, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=70, pitch=60, start=5.75, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue with variation
drum_notes = [
    # Kick on 1 & 3
    pretty_midi.Note(velocity=85, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=75, pitch=36, start=5.625, end=6.0),
    # Snare on 2 & 4
    pretty_midi.Note(velocity=95, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
