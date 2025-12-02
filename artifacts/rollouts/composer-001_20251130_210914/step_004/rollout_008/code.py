
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

# Bassline: Walking line, chromatic approaches, no repeated notes
# Fm: F, Ab, Bb, Db
# Walking bass line in Fm (key of F minor)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # C
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # C#
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=100, pitch=63, start=4.125, end=4.5),   # Eb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, Db
# Fm7 -> Bb7 -> Eb7 -> Ab7
piano_notes = [
    # Bar 2: Fm7 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=1.875, end=2.25),  # Db
    # Bar 3: Bb7 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.75),  # F#
    # Bar 4: Eb7 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=56, start=4.875, end=5.25),  # B
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone: Short motif, sing it, leave it hanging, come back and finish it
# Fm scale: F, Gb, Ab, A, Bb, B, Db, D
# Motif: F - Gb - Ab - A, then repeat on Bb - B - Db - D

# First iteration
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=63, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=110, pitch=61, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),   # A
]

# Second iteration
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.75),  # B
    pretty_midi.Note(velocity=110, pitch=59, start=2.75, end=2.875),  # Db
    pretty_midi.Note(velocity=110, pitch=60, start=2.875, end=3.0),   # D
])

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
