
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
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

# Bar 2: Sax, Bass, Piano enter
# Sax: Motif - Fm7 -> Bb7 -> Eb7 -> Ab7
# Fm7 (F, Ab, C, Db) -> Bb7 (Bb, D, F, Ab) -> Eb7 (Eb, G, Bb, Db) -> Ab7 (Ab, C, Eb, Gb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),    # C
    pretty_midi.Note(velocity=100, pitch=68, start=2.0, end=2.1875),  # Db
    pretty_midi.Note(velocity=100, pitch=62, start=2.1875, end=2.375), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.375, end=2.5625), # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.5625, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.9375),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=2.9375, end=3.125), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.3125), # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.3125, end=3.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=3.5, end=3.6875),   # Db
    pretty_midi.Note(velocity=100, pitch=64, start=3.6875, end=3.875), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.0),    # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.1875),   # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.1875, end=4.375), # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.375, end=4.5625), # Gb
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
# Fm: F, C, Ab, Eb
# Bar 2: F -> Gb -> Ab -> A -> Bb -> B -> C -> Db
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.6875, end=1.875),  # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),    # Ab
    pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.1875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.1875, end=2.375), # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=2.375, end=2.5625), # B
    pretty_midi.Note(velocity=90, pitch=71, start=2.5625, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=2.9375),  # Db
    pretty_midi.Note(velocity=90, pitch=68, start=2.9375, end=3.125), # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.125, end=3.3125), # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.3125, end=3.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=3.6875),   # B
    pretty_midi.Note(velocity=90, pitch=71, start=3.6875, end=3.875), # C
    pretty_midi.Note(velocity=90, pitch=70, start=3.875, end=4.0),    # Db
    pretty_midi.Note(velocity=90, pitch=68, start=4.0, end=4.1875),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.1875, end=4.375), # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=4.375, end=4.5625), # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=4.5625, end=4.75),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=4.9375),  # C
    pretty_midi.Note(velocity=90, pitch=70, start=4.9375, end=5.125), # Db
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Db) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.6875),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.6875),  # C
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.6875),  # Db
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.4375), # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.4375), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.4375), # Ab
    # Bar 4: Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.1875),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.1875),  # Db
]
piano.notes.extend(piano_notes)

# Bar 3: Drums - same pattern
for i in range(1.5, 4.5, 1.5):
    drum_notes = [
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=i + 0.0, end=i + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=i + 1.125, end=i + 1.5),
        # Snare on 2 and 4
        pretty_midi.Note(velocity=110, pitch=38, start=i + 0.75, end=i + 0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=i + 1.875, end=i + 2.0),
        # Hihat on every eighth
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.0, end=i + 0.1875),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.1875, end=i + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.375, end=i + 0.5625),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.5625, end=i + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.75, end=i + 0.9375),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.9375, end=i + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 1.125, end=i + 1.3125),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 1.3125, end=i + 1.5)
    ]
    drums.notes.extend(drum_notes)

# Bar 4: Drums - same pattern
for i in range(4.5, 6.0, 1.5):
    drum_notes = [
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=i + 0.0, end=i + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=i + 1.125, end=i + 1.5),
        # Snare on 2 and 4
        pretty_midi.Note(velocity=110, pitch=38, start=i + 0.75, end=i + 0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=i + 1.875, end=i + 2.0),
        # Hihat on every eighth
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.0, end=i + 0.1875),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.1875, end=i + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.375, end=i + 0.5625),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.5625, end=i + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.75, end=i + 0.9375),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.9375, end=i + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 1.125, end=i + 1.3125),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 1.3125, end=i + 1.5)
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
