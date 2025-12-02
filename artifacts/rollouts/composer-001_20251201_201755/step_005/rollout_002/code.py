
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
    # Hi-hats on every eighth
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

# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # F#2
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # F#2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=3.0),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),    # A4
    # Bar 3: Leave it hanging (rest)
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.6875, end=4.875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),    # A4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.3125, end=start + 1.5),
    drums.notes.extend([

    ])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
