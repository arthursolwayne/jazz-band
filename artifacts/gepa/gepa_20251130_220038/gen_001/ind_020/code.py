
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G#
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=2.0),  # F#
    # Bar 2: G7 on beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.5),  # G
]
piano.notes.extend(piano_notes)

# Drums: same pattern repeated
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend([note for note in drum_notes])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif returns, slightly altered
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=3.75),  # C#
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # D#
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: G7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5),  # G
    # Bar 3: A7 on beat 4
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=75, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.0),  # A
]
piano.notes.extend(piano_notes)

# Drums: same pattern repeated
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend([note for note in drum_notes])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Motif returns, finishes it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=73, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=75, start=5.25, end=5.5),  # G#
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: A7 on beat 2
    pretty_midi.Note(velocity=90, pitch=70, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=75, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=77, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=4.75, end=5.0),  # A
    # Bar 4: B7 on beat 4
    pretty_midi.Note(velocity=90, pitch=73, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=90, pitch=78, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=90, pitch=80, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=82, start=5.25, end=5.5),  # B
]
piano.notes.extend(piano_notes)

# Drums: same pattern repeated
for note in drum_notes:
    note.start += 4.5
    note.end += 4.5
drums.notes.extend([note for note in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
