
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
    pretty_midi.Note(velocity=64, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=64, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=70, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=70, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),   # D (root)
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # C# (chromatic)
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # Eb (3rd)
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),   # E (chromatic)
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),   # D (root)
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),  # C# (chromatic)
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # Eb (3rd)
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),   # E (chromatic)
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),   # D (root)
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),  # C# (chromatic)
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625),  # Eb (3rd)
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),   # E (chromatic)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # F
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Motif starting with D, then Eb, then G, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),   # D (repeat)
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),   # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),   # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),   # G
]
sax.notes.extend(sax_notes)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = 1.5 + bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=64, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=64, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=80, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=80, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=start, end=start + 0.1875),
    pretty_midi.Note(velocity=70, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=70, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=70, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=70, pitch=42, start=start + 1.3125, end=start + 1.5),

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
