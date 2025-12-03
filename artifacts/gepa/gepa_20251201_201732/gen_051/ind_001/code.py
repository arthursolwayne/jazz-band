
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F
bass_notes = [
    # Bar 2: F (root) with chromatic approach
    pretty_midi.Note(velocity=70, pitch=53, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=70, pitch=52, start=1.875, end=2.0),  # E (chromatic)
    # Bar 3: C (fifth) with chromatic approach
    pretty_midi.Note(velocity=70, pitch=57, start=2.0, end=2.375),  # C (D2)
    pretty_midi.Note(velocity=70, pitch=56, start=2.375, end=2.5),  # B (chromatic)
    # Bar 4: F (root) with chromatic approach
    pretty_midi.Note(velocity=70, pitch=53, start=2.5, end=2.875),  # F
    pretty_midi.Note(velocity=70, pitch=52, start=2.875, end=3.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.5 + 0.375),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.0 + 0.375),
    pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.0 + 0.375),
    pretty_midi.Note(velocity=90, pitch=57, start=2.0, end=2.0 + 0.375),
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.0 + 0.375),
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=55, start=2.5, end=2.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=58, start=2.5, end=2.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=2.5 + 0.375),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=36, start=3.375, end=3.625),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
]
drums.notes.extend(drum_notes)

# Sax: Bar 2-4 - Motif, haunting, incomplete
# Bar 2: F to Bb, wide interval, sparse
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.25),  # Bb
    # Bar 3: Rest
    # Bar 4: F again, but with a chromatic twist
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=52, start=3.25, end=3.5),  # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
