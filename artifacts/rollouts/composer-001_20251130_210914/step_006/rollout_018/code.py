
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
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (Dm7 -> G7 -> Cm7 -> F7)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),  # F

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),  # D

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D7
    pretty_midi.Note(velocity=70, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=70, pitch=64, start=1.875, end=2.25),

    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D7
    pretty_midi.Note(velocity=70, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=70, pitch=64, start=2.625, end=3.0),

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G7
    pretty_midi.Note(velocity=70, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=70, pitch=69, start=3.75, end=4.125),

    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G7
    pretty_midi.Note(velocity=70, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=70, pitch=69, start=4.5, end=4.875),

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),  # Cm7
    pretty_midi.Note(velocity=70, pitch=65, start=5.25, end=5.625),
    pretty_midi.Note(velocity=70, pitch=62, start=5.25, end=5.625),

    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # Cm7
    pretty_midi.Note(velocity=70, pitch=65, start=5.625, end=6.0),
    pretty_midi.Note(velocity=70, pitch=62, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes.extend([
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),
])
drums.notes.extend(drum_notes)

# Dante: Short motif, Dm7 -> G7 -> Cm7 -> F7
# Start with a triplet on D (62), then a chromatic run to G (67)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),    # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.375, end=4.5),   # E
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.625),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=5.0),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.375),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=5.375, end=5.5),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.625),   # E
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),    # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
