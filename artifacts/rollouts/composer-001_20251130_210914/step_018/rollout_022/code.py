
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # D#
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # D#
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # B
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # D7 (D F A C)
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),  # F#
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums in bars 2-4
drum_notes_2 = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),  # Snare on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),  # Snare on 4
]

# Hi-hat on every eighth
for start in [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]:
    drum_notes_2.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375))

for note in drum_notes_2:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
