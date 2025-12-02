
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625),  # G#
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),   # A
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.375),  # A#
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),   # C#
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=56, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=57, start=5.625, end=6.0)   # F#
]
bass.notes.extend(bass_notes)

# Piano: Diane
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # D7
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # E7
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # G7
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # A7
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),  # D7
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # E7
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # G7
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # A7
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # E7
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # G7
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # A7
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # C7
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # E7
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # G7
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),   # A7
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # C7
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # G7
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # A7
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # C7
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # D7
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # G7
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # A7
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),   # C7
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),   # D7
]
piano.notes.extend(piano_notes)

# Sax: Dante
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # E
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # E
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
