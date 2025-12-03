
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),     # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),    # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),    # A2 (fifth of D)
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),     # G2
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),     # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),    # F2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),    # A2
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),     # G2
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),     # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25),    # F2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),    # A2
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)      # G2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D-F#-A-C) open voicing
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C5

    # Bar 3: Gm7 (G-Bb-D-F) open voicing
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # F4

    # Bar 4: Cmaj7 (C-E-G-B) open voicing
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.875),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0),

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.625),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=3.8125),
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax — one short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.75),  # B4
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),   # A4
    pretty_midi.Note(velocity=120, pitch=72, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=120, pitch=73, start=2.5, end=2.75),  # C5
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=120, pitch=72, start=3.75, end=4.0),  # B4
    pretty_midi.Note(velocity=120, pitch=73, start=4.0, end=4.25),  # C5
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=120, pitch=72, start=5.25, end=5.5),  # B4
    pretty_midi.Note(velocity=120, pitch=73, start=5.5, end=5.75),  # C5
    pretty_midi.Note(velocity=110, pitch=72, start=5.75, end=6.0),  # B4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
