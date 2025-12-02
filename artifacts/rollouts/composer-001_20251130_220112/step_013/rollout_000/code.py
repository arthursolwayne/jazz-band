
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=100, pitch=39, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # B
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25),  # F7
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125),  # F7
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.625),  # F7
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),  # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25),  # E
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.75),  # E
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0),  # E
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Fill the bar
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
