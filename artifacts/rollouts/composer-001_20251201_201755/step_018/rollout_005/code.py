
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),  # C2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # Bb2
]
bass.notes.extend(bass_notes)

# Diane on piano: open voicings
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # F5
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # Eb5
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),  # G5
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # Bb5
]
piano.notes.extend(piano_notes)

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Dante on sax: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875),  # A4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.4375),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.4375, end=2.625),  # A4
    pretty_midi.Note(velocity=110, pitch=65, start=2.8125, end=3.0),   # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
