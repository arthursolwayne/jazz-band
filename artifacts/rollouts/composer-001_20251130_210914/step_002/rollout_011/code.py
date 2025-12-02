
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=80, pitch=73, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # G
    # Bar 3 (2.25 - 3.0)
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=82, start=2.25, end=2.625),  # D
    # Bar 4 (3.0 - 3.75)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # G
    # Bar 5 (3.75 - 4.5)
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=82, start=3.75, end=4.125),  # D
    # Bar 6 (4.5 - 5.25)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # G
    # Bar 7 (5.25 - 6.0)
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=82, start=5.25, end=5.625),  # D
]
piano.notes.extend(piano_notes)

# Sax: Melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
