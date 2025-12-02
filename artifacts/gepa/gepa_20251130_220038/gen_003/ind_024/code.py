
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # Fm7 root
    pretty_midi.Note(velocity=90, pitch=54, start=1.875, end=2.25),  # b9
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625),  # 7th
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # 5th
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.375),  # b7
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # Fm7 root
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125),  # b9
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),  # 7th
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # 5th
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25),  # b7
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625),  # Fm7 root
    pretty_midi.Note(velocity=90, pitch=54, start=5.625, end=6.0),  # b9
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.875),
    # Bar 3: Bb7
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),
    # Bar 4: Dm7
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: short motif, make it sing
sax_notes = [
    # Bar 2: Fm7 - start with a short motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.6875, end=1.875),  # Bb
    # Bar 3: Bb7 - leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.1875, end=3.375),  # Bb
    # Bar 4: Dm7 - come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.6875, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.0625),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=5.0625, end=5.25),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = []
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0))
    # Hi-hat on every eighth
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875))

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
