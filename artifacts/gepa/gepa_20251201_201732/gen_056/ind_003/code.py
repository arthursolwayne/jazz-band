
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in
# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # G2
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),   # B2
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),   # A2
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: D7 with #11 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.875),  # B4 (#11)
]
# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # F4
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=80, pitch=63, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # Bb4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, haunting and incomplete. Start it, leave it hanging. Come back and finish it.
# Melody: D4 - F#4 - G4 - C5 (start), then D4 - Bb4 - A4 - rest (leave hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # C5
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=2.375, end=2.5),   # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.625),   # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),  # rest (D4)
]
sax.notes.extend(sax_notes)

# Drums continue in bars 2-4
# Bar 2: same pattern, but with slight variation in velocity
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=42, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
