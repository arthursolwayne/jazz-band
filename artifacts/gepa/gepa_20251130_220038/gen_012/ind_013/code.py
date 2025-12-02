
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # D#
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=61, start=2.625, end=3.0),   # C
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.125),  # D#
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),   # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano - Diane
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # G7
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # E7
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C7
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # A7
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Sax - Dante
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),   # D
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),   # C
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),   # G
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5),   # E
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),   # G
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),   # E
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),   # D
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
