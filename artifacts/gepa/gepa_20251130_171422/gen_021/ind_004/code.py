
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

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),   # Ab
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 2.25)
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=49, start=1.5, end=1.875),  # D
    # Bar 3 (2.25 - 3.0)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.875),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=2.625, end=2.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=2.875),  # B
    pretty_midi.Note(velocity=100, pitch=49, start=2.625, end=2.875),  # D
    # Bar 4 (3.0 - 3.75)
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.625),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.625),  # B
    pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.625),  # D
    # Bar 4 (3.75 - 4.5)
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.375),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=4.125, end=4.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.375),  # B
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.375),  # D
    # Bar 4 (4.5 - 5.25)
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.125),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.125),  # B
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.125),  # D
    # Bar 4 (5.25 - 6.0)
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.875),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=5.625, end=5.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=5.875),  # B
    pretty_midi.Note(velocity=100, pitch=49, start=5.625, end=5.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: Dante (short motif, start it, leave it hanging, come back and finish it)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # Bb (Fm7)
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),   # B (Fm7)
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),   # A (Fm7)
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),   # Bb (Fm7)
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),   # B (Fm7)
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),   # A (Fm7)
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),   # Bb (Fm7)
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.0),   # B (Fm7)
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25),   # A (Fm7)
    pretty_midi.Note(velocity=110, pitch=65, start=4.25, end=4.5),   # Bb (Fm7)
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.75),   # B (Fm7)
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),   # A (Fm7)
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),   # Bb (Fm7)
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.5),   # B (Fm7)
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),   # A (Fm7)
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0),   # Bb (Fm7)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
