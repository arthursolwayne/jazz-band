
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
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),   # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5),   # E
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),  # D#
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.25),  # Bb
    # Bar 3: F7 on 4
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),   # Bb
    # Bar 4: F7 on 2
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.25),  # Bb
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Motif: F - Bb - D - F (F7 arpeggio with a twist)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # D
    # Leave it hanging
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375),  # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=5.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.875, end=6.0),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
