
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=47, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=48, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=2.75, end=3.0),  # Gb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=50, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=51, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=4.0, end=4.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=47, start=4.25, end=4.5),  # E
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=51, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=48, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=5.5, end=5.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=5.75, end=6.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # F7: F (60)
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # A (64)
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),  # Bb (65)
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # Db (67)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # F7: F (60)
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # A (64)
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),  # Bb (65)
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # Db (67)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),  # F7: F (60)
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # A (64)
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),  # Bb (65)
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # Db (67)
]
piano.notes.extend(piano_notes)

# Sax: Motif, start it, leave it hanging, come back and finish
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0),  # Bb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.125),  # Db
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # Db
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=3.625, end=3.75),  # Bb
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.125),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.125, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=5.375, end=5.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.625),  # Db
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=5.75),  # Db
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Bar 2 (1.5 - 3.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0)
]
drums.notes.extend(drum_notes)

# Drums: Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
