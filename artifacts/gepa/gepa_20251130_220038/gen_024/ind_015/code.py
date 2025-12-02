
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=40, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Fm7 chord on beat 2
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=74, start=1.875, end=2.0),
    # Fm7 chord on beat 4
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=2.8125),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=69, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=3.9375),
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=44, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=46, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=3.9375),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Fm7 chord on beat 2
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.5625),
    # Fm7 chord on beat 4
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.3125),
]
piano.notes.extend(piano_notes)

# Drums: same pattern in bar 3
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend([note.copy() for note in drum_notes])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.6875),
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=49, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=51, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.4375),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Fm7 chord on beat 2
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=70, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.0625),
    # Fm7 chord on beat 4
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=70, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=74, start=5.625, end=5.8125),
]
piano.notes.extend(piano_notes)

# Drums: same pattern in bar 4
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend([note.copy() for note in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
