
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm
bass_notes = [
    # Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=66, start=2.0, end=2.125),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=62, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.375, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.625),  # B (chromatic)
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.875, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.625, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.875, end=4.0),  # B
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=95, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # C
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # C
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=95, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Dante: Sax solo motif (start at 1.5s)
# Short motif: Dm7 -> G7 -> Cm7 -> F7
# Notes: D, F, A, C, G, B, D, F, C, Eb, Bb, D
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=105, pitch=64, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=105, pitch=69, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=105, pitch=71, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=105, pitch=74, start=2.125, end=2.25),  # B
    pretty_midi.Note(velocity=105, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=105, pitch=64, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=105, pitch=69, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=105, pitch=67, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=105, pitch=65, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=105, pitch=62, start=2.875, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
