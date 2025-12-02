
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif (Fm7 -> Eb7 -> Dm7 -> C7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),  # C
]

sax.notes.extend(sax_notes)

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # A
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Fm7 on 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=85, pitch=43, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=75, pitch=40, start=1.875, end=2.25),  # D
    # C7 on 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=85, pitch=52, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=75, pitch=48, start=2.625, end=3.0),  # Bb
]

piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif again but transposed up a third (Abm7 -> Gbm7 -> Fm7 -> Eb7)
sax_notes2 = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # Eb
]

sax.notes.extend(sax_notes2)

# Bass: Walking line in Abm (Ab, Bb, C, Db)
bass_notes2 = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),  # Db
]

bass.notes.extend(bass_notes2)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes2 = [
    # Abm7 on 2 (3.375 - 3.75)
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=85, pitch=46, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=75, pitch=43, start=3.375, end=3.75),  # F
    # Eb7 on 4 (4.125 - 4.5)
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=85, pitch=54, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),  # Ab
    pretty_midi.Note(velocity=75, pitch=50, start=4.125, end=4.5),  # Db
]

piano.notes.extend(piano_notes2)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Motif again but transposed up a third (Bbm7 -> Abm7 -> Gbm7 -> Fm7)
sax_notes3 = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # Gb
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F
]

sax.notes.extend(sax_notes3)

# Bass: Walking line in Bbm (Bb, C, Db, Eb)
bass_notes3 = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=54, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),  # Db
    pretty_midi.Note(velocity=80, pitch=57, start=5.625, end=6.0),  # Eb
]

bass.notes.extend(bass_notes3)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes3 = [
    # Bbm7 on 2 (4.875 - 5.25)
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=85, pitch=49, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=75, pitch=46, start=4.875, end=5.25),  # G
    # F7 on 4 (5.625 - 6.0)
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=85, pitch=52, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=75, pitch=48, start=5.625, end=6.0),  # D
]

piano.notes.extend(piano_notes3)

# Drums: Bar 3-4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes2)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
