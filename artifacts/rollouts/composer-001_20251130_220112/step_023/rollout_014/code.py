
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

# Bar 2: Sax starts melody, bass walks, piano comps, drums continue
# Sax: Dm7 -> G7 -> Cm7 -> F7
# D (F# dim) -> G (Bb dim) -> C (Eb dim) -> F (Ab dim)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.1875, end=2.375), # F#
    pretty_midi.Note(velocity=100, pitch=64, start=2.375, end=2.5625), # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.5625, end=2.75), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=2.9375), # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.9375, end=3.125), # F#
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.3125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.3125, end=3.5),   # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.6875),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.6875, end=3.875), # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),   # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
# F -> G -> A -> Bb -> C -> D -> Eb -> F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=80, pitch=70, start=2.0, end=2.1875),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=2.1875, end=2.375), # C
    pretty_midi.Note(velocity=80, pitch=74, start=2.375, end=2.5625), # D
    pretty_midi.Note(velocity=80, pitch=75, start=2.5625, end=2.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=2.9375),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.9375, end=3.125), # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.125, end=3.3125), # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.3125, end=3.5),   # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.6875),   # C
    pretty_midi.Note(velocity=80, pitch=74, start=3.6875, end=3.875), # D
    pretty_midi.Note(velocity=80, pitch=75, start=3.875, end=4.0),    # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: G7 (G, B, D, F)
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    # Bar 2, beat 2: Dm7
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.1875), # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.1875), # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.1875), # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.1875), # C
    # Bar 3, beat 2: G7
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.6875), # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.6875), # B
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.6875), # D
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.6875), # F
    # Bar 4, beat 2: Cm7
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.1875), # C
    pretty_midi.Note(velocity=80, pitch=63, start=5.0, end=5.1875), # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.1875), # G
    pretty_midi.Note(velocity=80, pitch=70, start=5.0, end=5.1875), # Bb
]
piano.notes.extend(piano_notes)

# Bar 2: Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.9375),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.3125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.4375),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.625, end=4.8125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.9375),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.1875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=6.1875, end=6.375),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
