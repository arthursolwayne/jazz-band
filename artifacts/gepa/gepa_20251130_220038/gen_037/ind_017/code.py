
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # Ab

    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=47, start=4.125, end=4.5),  # C

    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=51, start=5.625, end=6.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # F7: F
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F7: A
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # F7: C
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # F7: E

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # G7: G
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G7: B
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # G7: D
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # G7: F

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A7: A
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # A7: C#
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A7: E
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A7: A
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # D#

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # G

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums continue through bars 2-4
# Kick on 1 and 3
drum_notes.extend([
    pretty_midi.Note(velocity=90, pitch=36, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),
])

# Snare on 2 and 4
drum_notes.extend([
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
])

# Hihat on every eighth
drum_notes.extend([
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
])

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
