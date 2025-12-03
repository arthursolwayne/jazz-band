
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

# Bass line: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F2 (fifth), chromatic approach to G2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.125),
    pretty_midi.Note(velocity=80, pitch=40, start=2.125, end=2.375),
    pretty_midi.Note(velocity=90, pitch=43, start=2.375, end=2.75),
    # Bar 3: G2 (fifth), D2 (root), chromatic approach to A2
    pretty_midi.Note(velocity=90, pitch=43, start=2.75, end=3.125),
    pretty_midi.Note(velocity=90, pitch=38, start=3.125, end=3.5),
    pretty_midi.Note(velocity=80, pitch=41, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),
    # Bar 4: A2 (chromatic), G2 (fifth), D2 (root), chromatic approach to C2
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.375),
    pretty_midi.Note(velocity=90, pitch=43, start=4.375, end=4.75),
    pretty_midi.Note(velocity=90, pitch=38, start=4.75, end=5.125),
    pretty_midi.Note(velocity=80, pitch=40, start=5.125, end=5.375),
    pretty_midi.Note(velocity=90, pitch=37, start=5.375, end=5.75),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=85, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=75, pitch=67, start=1.5, end=2.0),  # C4
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=85, pitch=71, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.5),  # D4
    pretty_midi.Note(velocity=75, pitch=65, start=2.0, end=2.5),  # F4
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=3.0),  # C4
    pretty_midi.Note(velocity=85, pitch=63, start=2.5, end=3.0),  # Eb4
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=75, pitch=62, start=2.5, end=3.0),  # Bb4
])
piano.notes.extend(piano_notes)

# Sax: short motif, start it, leave it hanging, come back and finish it
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, F, Eb, G
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=105, pitch=65, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=63, start=2.0, end=2.25),  # Eb4
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D4 (return)
    pretty_midi.Note(velocity=105, pitch=65, start=2.75, end=3.0),  # F4 (return)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
