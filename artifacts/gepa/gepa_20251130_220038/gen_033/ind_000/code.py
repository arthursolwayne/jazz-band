
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)
# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=38, start=1.75, end=1.875),  # Db
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.125),  # G#
    pretty_midi.Note(velocity=80, pitch=44, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.375),  # A#
    pretty_midi.Note(velocity=80, pitch=46, start=2.375, end=2.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=44, start=2.5, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=40, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=38, start=2.875, end=3.0),  # Db
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=3.125, end=3.25),  # G#
    pretty_midi.Note(velocity=80, pitch=45, start=3.25, end=3.375),  # A#
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=44, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=3.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=38, start=3.875, end=4.0),  # Db
    pretty_midi.Note(velocity=80, pitch=41, start=4.0, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.25),  # G#
    pretty_midi.Note(velocity=80, pitch=45, start=4.25, end=4.375),  # A#
    pretty_midi.Note(velocity=80, pitch=46, start=4.375, end=4.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=40, start=4.75, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.0),  # Db
    pretty_midi.Note(velocity=80, pitch=41, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=5.125, end=5.25),  # G#
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.375),  # A#
    pretty_midi.Note(velocity=80, pitch=46, start=5.375, end=5.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=44, start=5.5, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.75),  # G
    pretty_midi.Note(velocity=80, pitch=40, start=5.75, end=5.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=38, start=5.875, end=6.0),  # Db
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=100, pitch=61, start=1.625, end=1.75),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # F7 - D
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.375),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # F7 - D
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=61, start=2.875, end=3.0),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=2.875, end=3.0),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # F7 - D
    # Bar 5 (3.0 - 3.5s)
    pretty_midi.Note(velocity=100, pitch=61, start=3.25, end=3.375),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # F7 - D
    # Bar 6 (3.5 - 4.0s)
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=3.875),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875),  # F7 - D
    # Bar 7 (4.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=61, start=4.25, end=4.375),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.375),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.375),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.375),  # F7 - D
    # Bar 8 (4.5 - 5.0s)
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=4.875),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=4.875),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=4.875),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # F7 - D
    # Bar 9 (5.0 - 5.5s)
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.375),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.375),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.375),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375),  # F7 - D
    # Bar 10 (5.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=61, start=5.75, end=6.0),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # F7 - D
]
piano.notes.extend(piano_notes)

# Sax: Short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=61, start=1.5, end=1.625),  # F (first note)
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=61, start=2.5, end=2.625),  # F (return)
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
