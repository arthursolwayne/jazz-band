
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # Bar 2: F2 (chromatic approach to G2)
    pretty_midi.Note(velocity=70, pitch=40, start=1.875, end=2.25),
    # Bar 2: G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),
    # Bar 2: D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),
    # Bar 3: D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),
    # Bar 3: F2 (chromatic approach to G2)
    pretty_midi.Note(velocity=70, pitch=40, start=3.375, end=3.75),
    # Bar 3: G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),
    # Bar 3: D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),
    # Bar 4: D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),
    # Bar 4: F2 (chromatic approach to G2)
    pretty_midi.Note(velocity=70, pitch=40, start=4.875, end=5.25),
    # Bar 4: G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),
    # Bar 4: D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, different chords each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm9 (D, F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=85, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=75, pitch=67, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=70, pitch=72, start=1.5, end=1.875),  # E5
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=85, pitch=76, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=75, pitch=69, start=3.0, end=3.375),  # F4
    # Bar 4: Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=75, pitch=71, start=4.5, end=4.875),  # B4
]
piano.notes.extend(piano_notes)

# Sax (Dante) - short motif, make it sing
sax_notes = [
    # Bar 2: D4 (start of motif)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    # Bar 2: F4 (next note)
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),
    # Bar 3: Bb4 (chromatic approach to B4)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    # Bar 3: B4 (resolution)
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),
    # Bar 4: D4 (return to motif)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    # Bar 4: F4 (finish motif)
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
