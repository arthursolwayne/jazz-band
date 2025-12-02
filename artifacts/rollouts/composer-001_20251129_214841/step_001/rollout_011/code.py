
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0, tempo=120)]

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bass: Walking line in C, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=61, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=61, start=2.75, end=3.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=59, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=58, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=58, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=59, start=4.25, end=4.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=61, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=61, start=5.75, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # C7
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # C7
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.25),  # C7
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody, one short motif, make it sing
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # C
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # C
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # C
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)

# Snare on 2 and 4
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.5625)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.3125)

# Hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    for i in range(0, 4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)

for note in drums.notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('wayne_intro.mid')
