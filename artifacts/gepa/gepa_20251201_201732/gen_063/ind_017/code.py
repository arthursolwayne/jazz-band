
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus bass: F2 (38) - Bb2 (42) - C2 (36) - Eb2 (39)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # Bb2
    pretty_midi.Note(velocity=80, pitch=36, start=2.25, end=2.625),  # C2
    pretty_midi.Note(velocity=80, pitch=39, start=2.625, end=3.0)   # Eb2
]
bass.notes.extend(bass_notes)

# Diane piano: Fm7 (F, Ab, C, Eb) -> Bb7 (Bb, D, F, Ab)
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=3.0),  # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # C4
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # Eb4
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=4.5),  # Ab4
]
piano.notes.extend(piano_notes)

# Dante sax: motif in Fm
# Motif: F (65), Ab (60), C (67), leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0)   # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus bass: Bb2 (42) - D2 (45) - F2 (38) - Ab2 (40)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75),  # D2
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5)   # Ab2
]
bass.notes.extend(bass_notes)

# Diane piano: Eb7 (Eb, G, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5)   # D4
]
piano.notes.extend(piano_notes)

# Dante sax: motif continues
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5)   # D4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus bass: Ab2 (40) - C2 (36) - Eb2 (39) - F2 (38)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875),  # Ab2
    pretty_midi.Note(velocity=80, pitch=36, start=4.875, end=5.25),  # C2
    pretty_midi.Note(velocity=80, pitch=39, start=5.25, end=5.625),  # Eb2
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0)   # F2
]
bass.notes.extend(bass_notes)

# Diane piano: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=6.0),  # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0)   # Eb4
]
piano.notes.extend(piano_notes)

# Dante sax: motif resolves
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0)   # F4
]
sax.notes.extend(sax_notes)

# Drums for bar 3 and 4
drum_notes = [
    # Bar 3: Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
