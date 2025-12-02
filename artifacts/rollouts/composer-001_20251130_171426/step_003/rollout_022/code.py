
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-Hat on every eighth
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

# Bass line (Marcus)
bass_line = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0),   # Bb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.125),  # Db
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),   # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=54, start=5.625, end=6.0)   # G
]
bass.notes.extend(bass_line)

# Piano (Diane)
piano_notes = [
    # Bar 2 (Comp on 2 and 4)
    pretty_midi.Note(velocity=95, pitch=60, start=2.25, end=2.625),  # F7
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Saxophone (Dante)
sax_notes = [
    # Bar 2 - Motif (F, Ab, Bb, C)
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=69, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=110, pitch=72, start=2.0625, end=2.25),
    # Bar 3 - Repeat motif
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=110, pitch=69, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=72, start=3.5625, end=3.75),
    # Bar 4 - Resolve motif
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=110, pitch=69, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=72, start=5.0625, end=5.25),
    # Bar 4 - Extension
    pretty_midi.Note(velocity=110, pitch=74, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=110, pitch=72, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=110, pitch=74, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=110, pitch=76, start=5.8125, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-Hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.875, end=start + 2.25)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 2.25, end=start + 2.625)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 2.625, end=start + 3.0)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
