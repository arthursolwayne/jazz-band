
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),   # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),   # C#
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=77, start=5.625, end=6.0),   # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=2.25),  # F7
    pretty_midi.Note(velocity=95, pitch=74, start=1.875, end=2.25),  # Ab

    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=95, pitch=60, start=2.625, end=3.0),   # Eb
    pretty_midi.Note(velocity=95, pitch=65, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=95, pitch=70, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=95, pitch=72, start=2.625, end=3.0),   # Eb7

    # Bar 4 (3.0 - 3.75s)
    pretty_midi.Note(velocity=95, pitch=62, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=95, pitch=72, start=3.375, end=3.75),  # F7
    pretty_midi.Note(velocity=95, pitch=74, start=3.375, end=3.75),  # Ab

    # Bar 4 (3.75 - 4.5s)
    pretty_midi.Note(velocity=95, pitch=60, start=4.125, end=4.5),   # Eb
    pretty_midi.Note(velocity=95, pitch=65, start=4.125, end=4.5),   # Ab
    pretty_midi.Note(velocity=95, pitch=70, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=95, pitch=72, start=4.125, end=4.5),   # Eb7
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Dante: motif, short and singable
# Motif: Dm7 -> Bb -> D -> Eb (chromatic descent) -> Dm7 again
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),   # Eb

    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),   # Eb

    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),   # Eb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: fill the bar
# Bar 2 (1.5 - 2.25s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3 (2.25 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4 (3.0 - 3.75s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4 (3.75 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4 (4.5 - 5.25s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4 (5.25 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
