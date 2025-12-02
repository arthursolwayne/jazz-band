
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),   # G#
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),   # C#
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),   # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: short motif, make it sing
# Start on F, leave it hanging, come back and finish
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.375, end=2.5),   # D
]
for note in sax_notes:
    sax.notes.append(note)

# Add drum fills for bar 2 and 3
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.25),   # Hi-hat
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=3.875),  # Hi-hat
    pretty_midi.Note(velocity=100, pitch=42, start=3.875, end=4.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.25, end=4.625),
    pretty_midi.Note(velocity=100, pitch=42, start=4.625, end=5.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.375),  # Hi-hat
    pretty_midi.Note(velocity=100, pitch=42, start=5.375, end=5.75),
    pretty_midi.Note(velocity=100, pitch=42, start=5.75, end=6.125),
    pretty_midi.Note(velocity=100, pitch=42, start=6.125, end=6.5),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
