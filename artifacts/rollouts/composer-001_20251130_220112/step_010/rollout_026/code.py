
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

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=2.75, end=3.0),  # Eb

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=53, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=51, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=4.25, end=4.5),  # F

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=51, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=53, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=5.75, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - F7 on 2 (1.75) and 4 (2.25)
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375),

    # Bar 3 (3.0 - 4.5s) - Bb7 on 2 (3.25) and 4 (3.75)
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=78, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=78, start=3.75, end=3.875),

    # Bar 4 (4.5 - 6.0s) - Eb7 on 2 (4.75) and 4 (5.25)
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=70, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.375),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm - F, Ab, Bb, Db
# Start on F (64), then Ab (67), then Bb (69), then Db (66). End on Bb (69)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.0),  # Db
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=2.875, end=3.0),  # Db
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
