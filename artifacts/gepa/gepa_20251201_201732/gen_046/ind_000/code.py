
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.75),    # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.875)  # Hihat on 3 & 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # F2 (minor 3rd)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=85, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=75, pitch=67, start=1.5, end=1.875),  # C4
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=75, pitch=67, start=3.0, end=3.375),  # F4
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=85, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=75, pitch=65, start=4.5, end=4.875),  # Bb4
])
piano.notes.extend(piano_notes)

# Dante: Tenor sax motif (Dm scale, but with space and tension)
# Bar 2: Motif starts
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D4 (leave it hanging)
]
# Bar 3: Motif returns, transposed up
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # G4
])
# Bar 4: Motif finishes with resolution
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D4
])
sax.notes.extend(sax_notes)

# Bar 3: Drums continue
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.75),    # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.875)  # Hihat on 3 & 4
]
drums.notes.extend(drum_notes)

# Bar 4: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.25),    # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.375)  # Hihat on 3 & 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
