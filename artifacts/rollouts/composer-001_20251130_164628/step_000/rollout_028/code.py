
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

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # E
    # Bar 3: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # E
    # Bar 4: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody (Start it, leave it hanging, come back and finish it)
sax_notes = [
    # First note: F (1.5s)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),
    # Second note: G (2.25s)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),
    # Third note: A (3.0s)
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),
    # Fourth note: F (4.5s)
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),
    # Fifth note: Bb (5.25s)
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),
    # Sixth note: F (6.0s)
    pretty_midi.Note(velocity=110, pitch=65, start=6.0, end=6.375),
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
