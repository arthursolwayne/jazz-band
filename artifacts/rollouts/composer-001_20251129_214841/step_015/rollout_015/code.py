
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: C (60), E (64), G (67), B (71)
# Motif: C E G B, then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in C
# C (60), D (62), Eb (63), F (65), G (67), A (69), Bb (70), B (71)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=63, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# C7 (60, 64, 67, 71)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif but with a chromatic run up
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in C
# C (60), D (62), Eb (63), F (65), G (67), A (69), Bb (70), B (71)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=63, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# C7 (60, 64, 67, 71)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif and resolve it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in C
# C (60), D (62), Eb (63), F (65), G (67), A (69), Bb (70), B (71)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=63, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=67, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=70, start=6.0, end=6.25),
    pretty_midi.Note(velocity=80, pitch=71, start=6.25, end=6.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# C7 (60, 64, 67, 71)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=60, start=6.0, end=6.25),
    pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.25),
    pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.25),
    pretty_midi.Note(velocity=90, pitch=71, start=6.0, end=6.25),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick=36, snare=38, hihat=42

# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
