
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: Fm7 -> Ab7 -> Bb7 -> Cm7
# Fm7: F, Ab, Db, Eb
# Ab7: Ab, C, Eb, Gb
# Bb7: Bb, D, F, Ab
# Cm7: C, Eb, Gb, Bb

# Sax notes (start times: 1.5, 1.75, 2.0, 2.25)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # Db
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # Eb
]

sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches
# F -> Gb -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> F
# Bar 2: F, Gb, G, Ab
# Bar 3: A, Bb, B, C
# Bar 4: D, Eb, F, Gb

bass_notes = [
    pretty_midi.Note(velocity=100, pitch=46, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=47, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=48, start=1.875, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=100, pitch=51, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=100, pitch=55, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=2.875, end=3.0),  # Gb
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: Fm7 on 2 (1.75), Ab7 on 4 (2.25)
# Bar 3: Bb7 on 2 (2.75), Cm7 on 4 (3.25)
# Bar 4: Fm7 on 2 (3.75), Ab7 on 4 (4.25)

# Bar 2: Fm7 (F, Ab, Db, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Db
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Eb

    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.5),  # Gb

    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.75, end=3.0),  # Ab

    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Bb

    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # Db
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # Eb

    pretty_midi.Note(velocity=100, pitch=68, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=63, start=4.25, end=4.5),  # Gb
]

piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
