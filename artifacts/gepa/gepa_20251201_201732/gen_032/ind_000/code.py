
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

# Bar 2: Sax enters with motif (1.5 - 3.0s)
# Motif: Dm7 -> G7 -> Cm7 -> F7 (the "question")
# Dm7 (F, A, C, D) -> G7 (B, D, F, G) -> Cm7 (Eb, G, Bb, C) -> F7 (A, C, Eb, F)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.4375), # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.8125), # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line on Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) -> Eb2 (39) -> G2 (43) -> A2 (45)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=39, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=45, start=2.0, end=2.1875),
    # Bar 3: C2 (36) -> Db2 (37) -> F2 (41) -> G2 (43)
    pretty_midi.Note(velocity=80, pitch=36, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=37, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=43, start=2.8125, end=3.0),
    # Bar 4: Bb2 (34) -> B2 (35) -> Eb2 (39) -> F2 (41)
    pretty_midi.Note(velocity=80, pitch=34, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=35, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=39, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=41, start=3.5625, end=3.75),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.6875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
]
# Bar 3: G7 (B, D, F, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.4375),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.4375),  # G
])
# Bar 4: Cm7 (Eb, G, Bb, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.1875),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.1875),  # C
])
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.8125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.8125),
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.8125, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.5625, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.9375, end=4.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=2.999),
    pretty_midi.Note(velocity=80, pitch=42, start=2.999, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.3125, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.0625, end=5.4375),
    pretty_midi.Note(velocity=100, pitch=38, start=5.4375, end=5.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.499),
    pretty_midi.Note(velocity=80, pitch=42, start=4.499, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
