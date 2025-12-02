
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2: Start of sax melody
# Motif: Fm7 (F, Ab, Bb, D) -> F Ab Bb D -> skip a beat, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Marcus: Walking bass line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=46, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # D
    # Bar 3: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # D
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Bar 2: Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet
# Sax continues motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Marcus: bass line (Ab, Bb, B, C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # D
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
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

# Bar 4: Full quartet
# Sax ends motif with resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Marcus: bass line (Db, D, Eb, E)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.875),  # Db
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=49, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
