
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in F (F, G, Ab, A, Bb, B, C, Db, D, Eb, F...)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2, beat 2 (1.875s): F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    # Bar 2, beat 4 (2.625s): Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: motif in F (F, Ab, Bb, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=70, start=2.0625, end=2.25),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line continues
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5),   # Db
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 3, beat 2 (3.375s): D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    # Bar 3, beat 4 (4.125s): G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: repeat and extend motif (F, Ab, Bb, F, Eb, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.1875),    # F
    pretty_midi.Note(velocity=110, pitch=68, start=3.1875, end=3.375),  # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5625),  # Bb
    pretty_midi.Note(velocity=110, pitch=70, start=3.5625, end=3.75),   # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=3.9375),   # Eb
    pretty_midi.Note(velocity=110, pitch=70, start=3.9375, end=4.125),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line continues
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),   # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),  # Db
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 4, beat 2 (4.875s): C7 (C, E, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    # Bar 4, beat 4 (5.625s): F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: resolve motif (F, Ab, Bb, F), then a final F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.6875),    # F
    pretty_midi.Note(velocity=110, pitch=68, start=4.6875, end=4.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0625),  # Bb
    pretty_midi.Note(velocity=110, pitch=70, start=5.0625, end=5.25),   # F
    pretty_midi.Note(velocity=110, pitch=70, start=5.25, end=5.625),    # F
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Hi-hat on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
