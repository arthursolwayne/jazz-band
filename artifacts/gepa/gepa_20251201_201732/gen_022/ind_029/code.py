
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
bar_length = 1.5
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=80, pitch=38, start=2.0, end=2.1875),  # D
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=43, start=2.1875, end=2.375), # A
    pretty_midi.Note(velocity=80, pitch=41, start=2.375, end=2.5625), # F
    pretty_midi.Note(velocity=80, pitch=38, start=2.5625, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=40, start=2.75, end=2.9375),  # G
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=40, start=2.9375, end=3.125), # G
    pretty_midi.Note(velocity=80, pitch=38, start=3.125, end=3.3125), # D
    pretty_midi.Note(velocity=80, pitch=41, start=3.3125, end=3.5),   # F
    pretty_midi.Note(velocity=80, pitch=38, start=3.5, end=3.6875),   # D
    pretty_midi.Note(velocity=80, pitch=40, start=3.6875, end=3.875), # G
    pretty_midi.Note(velocity=80, pitch=41, start=3.875, end=4.0),    # F
    pretty_midi.Note(velocity=80, pitch=38, start=4.0, end=4.1875),   # D
    pretty_midi.Note(velocity=80, pitch=43, start=4.1875, end=4.375), # A
    pretty_midi.Note(velocity=80, pitch=41, start=4.375, end=4.5625), # F
    pretty_midi.Note(velocity=80, pitch=38, start=4.5625, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=40, start=4.75, end=4.9375),  # G
    pretty_midi.Note(velocity=80, pitch=41, start=4.9375, end=5.125), # F
    pretty_midi.Note(velocity=80, pitch=38, start=5.125, end=5.3125), # D
    pretty_midi.Note(velocity=80, pitch=40, start=5.3125, end=5.5),   # G
    pretty_midi.Note(velocity=80, pitch=41, start=5.5, end=5.6875),   # F
    pretty_midi.Note(velocity=80, pitch=38, start=5.6875, end=5.875), # D
    pretty_midi.Note(velocity=80, pitch=43, start=5.875, end=6.0)     # A
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    # Bar 2 - Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.6875), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.6875), # C5
    # Bar 3 - Gm7 (G Bb D F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.1875, end=2.375), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.1875, end=2.375), # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.1875, end=2.375), # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.1875, end=2.375), # F4
    # Bar 4 - Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=2.9375, end=3.125), # C4
    pretty_midi.Note(velocity=100, pitch=63, start=2.9375, end=3.125), # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.9375, end=3.125), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.9375, end=3.125), # Bb4
]
piano.notes.extend(piano_notes)

# Sax (Dante)
sax_notes = [
    # Bar 2 - Motif: D (62), F# (66), D (62), F# (66)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=66, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.0),
    # Bar 3 - Rest
    # Bar 4 - Repeat and resolve
    pretty_midi.Note(velocity=110, pitch=62, start=5.125, end=5.25),
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=62, start=5.375, end=5.5),
    pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.625),
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=5.75),
    pretty_midi.Note(velocity=110, pitch=66, start=5.75, end=5.875)
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.6875, end=1.875), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.1875, end=2.375), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.375, end=2.5625), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.9375, end=3.125), # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.6875),   # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.125, end=3.3125), # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=3.875, end=4.0),    # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.9375, end=5.125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.3125, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.6875, end=5.875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
