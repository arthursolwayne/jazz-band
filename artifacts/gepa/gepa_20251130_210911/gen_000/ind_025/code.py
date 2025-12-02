
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody (F7, G7, A7, Bb7)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=87, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=88, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=89, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=85, start=2.625, end=3.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: walking in F (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=58, start=2.625, end=3.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords: 7ths on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25s) - G7 on 2
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=78, start=1.875, end=2.25),

    # Bar 3 (2.25 - 3.0s) - C7 on 4
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=79, start=2.625, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax repeats motif, slightly higher
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=88, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=89, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=90, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=86, start=4.125, end=4.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: walking in F (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=58, start=4.125, end=4.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords: 7ths on 2 and 4
piano_notes = [
    # Bar 3 (3.0 - 3.75s) - G7 on 2
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=78, start=3.375, end=3.75),

    # Bar 4 (3.75 - 4.5s) - C7 on 4
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=77, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax finishes the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=89, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=90, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=91, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=87, start=5.625, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: walking in F (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=58, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords: resolve with F7 on 4
piano_notes = [
    # Bar 4 (4.5 - 6.0s) - F7 on 4
    pretty_midi.Note(velocity=90, pitch=77, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=80, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=82, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=84, start=5.625, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums for Bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5 - 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat
    for i in range(4):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
