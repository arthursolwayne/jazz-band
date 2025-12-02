
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody starts here, with restraint and tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=2.625, end=3.0),   # Bb
]

sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),   # C
]

bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),

    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F7 again
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),
]

piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the melody with emotional build
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=4.125, end=4.5),   # Bb
]

sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0),   # C
]

bass.notes.extend(bass_notes)

# Piano: Comp again
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # F7
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),

    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # F7 again
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),
]

piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Resolve with emotional clarity
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # F
]

sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0),   # C
]

bass.notes.extend(bass_notes)

# Piano: Comp again
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # F7
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),
]

piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
