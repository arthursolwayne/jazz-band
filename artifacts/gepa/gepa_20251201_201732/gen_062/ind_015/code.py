
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass (Marcus)
bass_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Ab (b9)
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # C (5th)
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # D (6th)
]

# Piano (Diane: Fm7 -> Bb7 -> Eb7 -> Am7)
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # D

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=56, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625),  # Ab

    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=54, start=2.625, end=3.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D

    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),   # E
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375),   # G
]

# Sax (Dante)
sax_notes = [
    # Motif: F (bar 2), Bb (bar 3), Eb (bar 4), A (bar 4)
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=54, start=2.625, end=3.0),   # Eb
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),   # A
]

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
