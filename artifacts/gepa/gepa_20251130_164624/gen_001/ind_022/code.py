
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
# Bass line: walking in Fm, chromatic approach to Bb
bass_notes = [
    # Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on Fm7 and Bb7
piano_notes = [
    # Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    # Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: short motif, start on F, then Ab, then Bb, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=68, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=70, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=110, pitch=71, start=2.0625, end=2.25),
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, chromatic approach to Eb
bass_notes = [
    # Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: comp on Eb7 and Ab7
piano_notes = [
    # Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    # Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: continuation of motif, leave it hanging on Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=70, start=3.5625, end=3.75),
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line, chromatic approach to F
bass_notes = [
    # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: comp on F7 and Bb7
piano_notes = [
    # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),
    # Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: finish the motif, come back and finish it on F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=110, pitch=68, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=110, pitch=70, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=71, start=5.0625, end=5.25),
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 4):
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=i*1.5, end=i*1.5+0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=i*1.5+1.125, end=i*1.5+1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=i*1.5+0.75, end=i*1.5+1.125)
    pretty_midi.Note(velocity=110, pitch=38, start=i*1.5+1.875, end=i*1.5+2.25)
    # Hihat on every eighth
    for j in range(4):
        pretty_midi.Note(velocity=90, pitch=42, start=i*1.5 + j*0.375, end=i*1.5 + (j+1)*0.375)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
