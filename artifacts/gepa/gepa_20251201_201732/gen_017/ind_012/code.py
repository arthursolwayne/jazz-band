
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: Dm (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),     # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),    # F2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),    # A2
    pretty_midi.Note(velocity=100, pitch=37, start=2.625, end=3.0),     # C2
    # Bar 3: Gm7 (G-Bb-D-F)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),     # G2
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),    # Bb2
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),    # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),     # F2
    # Bar 4: C7 (C-E-G-B)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),     # C2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),    # E2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),    # G2
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0),     # B2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D-F-A-C) - open voicing
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),     # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),     # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),     # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),     # C5
    # Bar 3: Gm7 (G-Bb-D-F) - open voicing
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),     # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),     # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),     # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),     # F4
    # Bar 4: C7 (C-E-G-B) - open voicing
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),     # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),     # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),     # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),     # B4
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (start), F4 (end), leave it hanging on G4, return on A4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),     # D4
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75),    # F4
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.5),     # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.25),    # A4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
