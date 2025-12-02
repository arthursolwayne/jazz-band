
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=35, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=37, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=2.25),  # A (F7)
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.375),
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.375),
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.375),
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.375),
]
piano.notes.extend(piano_notes)

# Sax: Sparse melody, one motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.9375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.9375, end=2.125),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.125, end=2.3125),  # D#
    pretty_midi.Note(velocity=100, pitch=62, start=2.3125, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.6875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.6875, end=2.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.875, end=3.0),  # C
]
sax.notes.extend(sax_notes)

# Bar 3 (3.0 - 4.5s): Full quartet
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=39, start=3.375, end=3.75),  # G#
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.75),  # A (F7)
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.875),
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.875),
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.875),
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: Continue melody with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.4375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.4375, end=3.625),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=3.625, end=3.8125),  # D#
    pretty_midi.Note(velocity=100, pitch=62, start=3.8125, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.1875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.1875, end=4.375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.375, end=4.5),  # C
]
sax.notes.extend(sax_notes)

# Bar 4 (4.5 - 6.0s): Full quartet
# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0),  # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=5.25),  # A (F7)
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.375),
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.375),
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.375),
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.375),
]
piano.notes.extend(piano_notes)

# Sax: Finale of motif, more space, more tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.9375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.9375, end=5.125),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=5.125, end=5.3125),  # D#
    pretty_midi.Note(velocity=100, pitch=62, start=5.3125, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.6875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.6875, end=5.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.875, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
