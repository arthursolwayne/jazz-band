
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
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drums_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass Line - Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=39, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=37, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=40, start=2.75, end=3.0),  # Gb

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=37, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=35, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=4.25, end=4.5),  # Gb

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=34, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=37, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=35, start=5.75, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Diane - Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),

    # Bar 3 (3.0 - 4.5s) - comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.0),

    # Bar 4 (4.5 - 6.0s) - comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Dante - Tenor Sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s) - Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=3.0),  # F

    # Bar 3 (3.0 - 4.5s) - Let it breathe
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # G

    # Bar 4 (4.5 - 6.0s) - Come back and finish it
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
