
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.6875, end=1.875),  # D#
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.0625, end=2.25),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.4375),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=2.4375, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=2.8125),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.8125, end=3.0),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.1875, end=3.375),  # D#
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.5625, end=3.75),   # C
    # Bar 4 continuation
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=3.9375),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=3.9375, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.3125),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.3125, end=4.5),    # D
    # Bar 4 resolution
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.6875),   # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.6875, end=4.875),  # D#
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.0625, end=5.25),   # C
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.4375),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=5.4375, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=5.8125),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.8125, end=6.0),    # D
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords, on 2 and 4
piano_notes = [
    # Bar 2 (on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),   # B
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),   # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.375),  # C#
    # Bar 3 (on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=62, start=2.8125, end=2.9375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.8125, end=2.9375), # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.8125, end=2.9375), # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.8125, end=2.9375), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=3.1875, end=3.3125), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.3125), # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.1875, end=3.3125), # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.1875, end=3.3125), # C#
    # Bar 4 (on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=62, start=3.9375, end=4.0625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.9375, end=4.0625), # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.9375, end=4.0625), # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.9375, end=4.0625), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=4.3125, end=4.4375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.3125, end=4.4375), # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.3125, end=4.4375), # B
    pretty_midi.Note(velocity=100, pitch=69, start=4.3125, end=4.4375), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375),    # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375),    # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.375),    # B
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.375),    # C#
]
piano.notes.extend(piano_notes)

# Saxophone - Dante: Melody with emotional build
sax_notes = [
    # Bar 2: Start with a whisper
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.6875),    # E
    pretty_midi.Note(velocity=90, pitch=62, start=1.6875, end=1.875),   # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0),     # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),      # G
    # Bar 3: Build with tension
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.4375),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.4375, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.8125), # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.8125, end=3.0),   # B
    # Bar 4: Resolve with emotion
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.1875),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.5625, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.9375, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.3125), # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.3125, end=4.5),   # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.6875),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.6875, end=4.875), # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.0625, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.4375),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=5.4375, end=5.625), # E
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=5.8125), # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.8125, end=6.0),   # A
]
sax.notes.extend(sax_notes)

# Drums - Bar 2-4 (1.5 - 6.0s)
bar2_drums = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.3125)
]
bar3_drums = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875)
]
bar4_drums = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(bar2_drums + bar3_drums + bar4_drums)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
