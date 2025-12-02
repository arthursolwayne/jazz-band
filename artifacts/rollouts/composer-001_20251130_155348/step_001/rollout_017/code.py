
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=3.0),   # A
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # A#
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.125),  # C#
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),   # D#
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=80, pitch=58, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E♭)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=68, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),
    # Bar 3: B♭7 (B♭, D, F, A♭)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),
    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: Melody
# Motif: F - E♭ - D - G (F, E♭, D, G)
# Start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # E♭
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
