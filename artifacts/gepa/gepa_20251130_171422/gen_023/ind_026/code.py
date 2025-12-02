
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5)
]
drums.notes.extend(drums_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=1.875),    # D
    pretty_midi.Note(velocity=80, pitch=54, start=1.875, end=2.25),   # C
    pretty_midi.Note(velocity=80, pitch=56, start=2.25, end=2.625),   # Eb
    pretty_midi.Note(velocity=80, pitch=57, start=2.625, end=3.0),    # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.875, end=2.25),   # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=85, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=85, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=85, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=85, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=85, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=85, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=85, pitch=69, start=2.625, end=3.0)
]
piano.notes.extend(piano_notes)

# Sax: Start the melody, short motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),    # E
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Chromatic walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.375),    # G
    pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.75),   # F
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125),   # D
    pretty_midi.Note(velocity=80, pitch=56, start=4.125, end=4.5),    # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=3.375, end=3.75),   # F7
    pretty_midi.Note(velocity=85, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=85, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=85, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=85, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=85, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=85, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=85, pitch=69, start=4.125, end=4.5)
]
piano.notes.extend(piano_notes)

# Sax: Continue the melody, finish the phrase
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),   # C
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),    # C
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=6.0)
]
drums.notes.extend(drums_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.875),    # G#
    pretty_midi.Note(velocity=80, pitch=58, start=4.875, end=5.25),   # G
    pretty_midi.Note(velocity=80, pitch=56, start=5.25, end=5.625),   # Eb
    pretty_midi.Note(velocity=80, pitch=57, start=5.625, end=6.0),    # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=85, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=85, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=85, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=85, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=85, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=85, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=85, pitch=69, start=5.625, end=6.0)
]
piano.notes.extend(piano_notes)

# Sax: End the phrase with a rest, leave it hanging
sax_notes = []
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
