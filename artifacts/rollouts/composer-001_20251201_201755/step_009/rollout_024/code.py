
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # D (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625),  # G (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # F (root)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # D (chromatic)
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.125),  # G (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # F (root)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # D (chromatic)
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.625),  # G (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # F (root)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # E
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),  # F
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # Bb
]
piano.notes.extend(piano_notes)

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),
    drums.notes.extend([

    ])

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) -> G (67) -> E (64) -> F (65) -> leave it on the 3rd beat, resolve on the 4th
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),  # F (resolve)
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=4.25, end=4.5),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
