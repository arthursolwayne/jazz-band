
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
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

# Bass line (Marcus): walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=1.875),  # Fm7
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),   # G
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.5),   # Bb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.0),   # Ab
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # Bb (7th)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Ab (flat 7)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # C (9th)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # F (root)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Bb (7th)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Ab (flat 7)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # C (9th)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Bb (7th)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Ab (flat 7)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # C (9th)
]
piano.notes.extend(piano_notes)

# Saxophone (Dante): short motif, one phrase, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_shorter_moment.mid")
