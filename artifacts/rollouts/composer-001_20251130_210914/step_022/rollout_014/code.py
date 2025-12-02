
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2: Fm7 -> Bb7 -> Eb7 -> Ab7
    # Walking line in Fm: F, Gb, G, Ab, A, Bb, B, C
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=70, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=2.375, end=2.5),  # C
    # Bar 3: Bb7 -> Eb7 -> Ab7 -> Db7
    # Walking line in Bb: Bb, B, C, Db, D, Eb, E, F
    pretty_midi.Note(velocity=90, pitch=70, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.75),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.875, end=3.0),  # Db
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5),  # F
    # Bar 4: Db7 -> Gb7 -> Bb7 -> Fm
    # Walking line in Db: Db, D, Eb, E, F, F#, G, G#
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.625),  # Db
    pretty_midi.Note(velocity=90, pitch=71, start=3.625, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=3.875, end=4.0),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=73, start=4.125, end=4.25),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=4.25, end=4.375),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=4.375, end=4.5),  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, Bb, Db), comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # Db
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),  # Db
    # Bar 3: Bb7 (Bb, D, F, Ab), comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=70, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=2.5, end=2.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.25),  # Ab
    # Bar 4: Db7 (Db, F, Gb, Bb), comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # Db
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),  # Db
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=70, start=4.0, end=4.25),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=1.875),  # F#
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=68, start=2.5, end=2.625),  # E
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=3.625),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=3.875),  # A
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.875, end=4.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.9375, end=4.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
