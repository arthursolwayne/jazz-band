
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: chromatic walking line, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=1.875),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.0, end=2.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.375, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=2.5, end=2.625),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.875, end=3.0),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=79, start=1.75, end=2.0),  # B7
    pretty_midi.Note(velocity=80, pitch=74, start=1.75, end=2.0),  # F7
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),  # C7
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # G7

    pretty_midi.Note(velocity=90, pitch=79, start=2.75, end=3.0),  # B7
    pretty_midi.Note(velocity=80, pitch=74, start=2.75, end=3.0),  # F7
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0),  # C7
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),  # G7
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: short motif, makes it sing, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.625),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=2.375, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=2.875),  # F#
    pretty_midi.Note(velocity=100, pitch=72, start=2.875, end=3.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass: chromatic walking line again
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=3.625, end=3.75),  # F#
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=3.875, end=4.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.125, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.375),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=4.375, end=4.5),  # F#
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.0),  # B7
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.0),  # F7
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),  # C7
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0),  # G7

    pretty_midi.Note(velocity=90, pitch=79, start=4.75, end=5.0),  # B7
    pretty_midi.Note(velocity=80, pitch=74, start=4.75, end=5.0),  # F7
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),  # C7
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),  # G7
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: continuation of motif, ends with a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.125),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.625),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.625, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=3.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=3.875, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.375),  # F#
    pretty_midi.Note(velocity=100, pitch=72, start=4.375, end=4.5),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus on bass: chromatic walking line again
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.625),  # F#
    pretty_midi.Note(velocity=80, pitch=64, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=4.75, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.125),  # F#
    pretty_midi.Note(velocity=80, pitch=66, start=5.125, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.375),  # F#
    pretty_midi.Note(velocity=80, pitch=64, start=5.375, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=5.5, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=5.75, end=5.875),  # F#
    pretty_midi.Note(velocity=80, pitch=66, start=5.875, end=6.0),  # G
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.5),  # B7
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.5),  # F7
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5),  # C7
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5),  # G7

    pretty_midi.Note(velocity=90, pitch=79, start=5.75, end=6.0),  # B7
    pretty_midi.Note(velocity=80, pitch=74, start=5.75, end=6.0),  # F7
    pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0),  # C7
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=6.0),  # G7
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: finish the motif, end on a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.625),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=4.625, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.125),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=5.125, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=5.375, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=5.875),  # F#
    pretty_midi.Note(velocity=100, pitch=72, start=5.875, end=6.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
