
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
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

# Bass line (Marcus): walking line with chromatic approaches, roots and fifths
bass_notes = [
    # Bar 2: D2 (root), F#2 (fifth), E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),
    # Bar 3: G2 (fifth), Bb2 (chromatic approach), A2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.125),
    pretty_midi.Note(velocity=80, pitch=41, start=3.125, end=3.5),
    # Bar 4: C2 (root), D2 (chromatic), C#2 (chromatic), B2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=80, pitch=37, start=3.875, end=4.125),
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.375),
    pretty_midi.Note(velocity=80, pitch=40, start=4.375, end=4.75),
]
bass.notes.extend(bass_notes)

# Piano (Diane): open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Gm7/D (D, G, Bb, F)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=55, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=59, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=1.875),
    # Bar 3: E7/D (D, E, G#, B)
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=2.875),
    pretty_midi.Note(velocity=85, pitch=56, start=2.625, end=2.875),
    pretty_midi.Note(velocity=85, pitch=58, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.875),
    # Bar 4: F#m7/D (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=3.875),
    pretty_midi.Note(velocity=85, pitch=53, start=3.5, end=3.875),
    pretty_midi.Note(velocity=85, pitch=57, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=58, start=3.5, end=3.875),
]
piano.notes.extend(piano_notes)

# Drums (Little Ray): kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0625, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.4375, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.8125, end=5.0),
]
drums.notes.extend(drum_notes)

# Sax (Dante): haunting, incomplete motif
sax_notes = [
    # Bar 2: Start the motif (G4, A4, D5)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),
    # Bar 3: Rest (space)
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.625),  # rest
    # Bar 4: Return with variation (E4, F#4, B4)
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=100, pitch=66, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=100, pitch=71, start=3.875, end=4.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
