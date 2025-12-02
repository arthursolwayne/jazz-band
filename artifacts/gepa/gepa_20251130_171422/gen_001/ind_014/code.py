
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus) - Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),   # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5),   # E
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.625),  # G#
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F7: F (62)
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.875),  # Bb (66)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # B (67)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # D (69)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # D
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # D
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax (Dante) - Short motif, start it, leave it hanging, finish it
# Melody: F (62), A (65), Bb (66), F (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
