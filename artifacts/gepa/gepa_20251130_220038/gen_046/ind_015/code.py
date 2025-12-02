
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

# Bars 2–4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # Dm7: D
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),  # C
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.5),  # F
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.0),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: melody - starts simple, builds tension, ends with a breath
sax_notes = [
    # Bar 2: D (rested on 1), E (on 2), D (on 3), C (on 4)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),  # C
    # Bar 3: F (on 1), E (on 2), D (on 3), D (on 4)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # D
    # Bar 4: Eb (on 1), D (on 2), C (on 3), Bb (on 4) - unexpected resolution
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
