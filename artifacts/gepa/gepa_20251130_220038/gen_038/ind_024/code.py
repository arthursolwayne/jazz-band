
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=54, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=56, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=58, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Add more drum fills
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
])

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("cellar_intro.mid")
