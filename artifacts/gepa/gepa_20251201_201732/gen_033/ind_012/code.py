
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
    # Hi-hat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus - walking bass line in F (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # C3 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Bb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane - Open voicings, resolve on the last bar
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # E5
]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # F4
])
# Bar 4: C7 (C, E, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # E5
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # G5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Bb4
])
piano.notes.extend(piano_notes)

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
])
drums.notes.extend(drum_notes)

# Bar 2: Dante - Start motif
# F (65), A (70), D (69), Bb (71) - motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=70, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),
]
# Bar 3: Repeat motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),
    pretty_midi.Note(velocity=110, pitch=70, start=2.5, end=2.75),
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),
])
# Bar 4: Resolve motif (F, C, G, A)
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=72, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=77, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=70, start=3.75, end=4.0),
])
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
