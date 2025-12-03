
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.625),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),  # A2
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),  # B2
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=54, start=4.125, end=4.5),  # C3
    pretty_midi.Note(velocity=80, pitch=54, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=80, pitch=56, start=4.875, end=5.25),  # D3
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),  # Db3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=57, start=5.625, end=6.0),  # E3
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Fmaj7
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # D4
    # Bar 3: Bb7
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # B4
    # Bar 4: E7
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # B4
    # Bar 4: Dm7 (resolution)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # B4
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),  # G4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
