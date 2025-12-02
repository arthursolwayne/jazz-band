
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax: Start the motif
# F7 (F A C E) -> F7 is F A C E, but we play F A G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=2.75, end=3.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F7 (F A C E)
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 4):
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=i*1.5, end=i*1.5+0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=i*1.5+0.75, end=i*1.5+1.125),  # Snare on 2
        pretty_midi.Note(velocity=100, pitch=36, start=i*1.5+1.5, end=i*1.5+1.875),  # Kick on 3
        pretty_midi.Note(velocity=100, pitch=38, start=i*1.5+2.25, end=i*1.5+2.625),  # Snare on 4
    ]
    for note in drum_notes:
        drums.notes.append(note)

    # Hihat on every eighth
    for j in range(0, 4):
        pretty_midi.Note(velocity=90, pitch=42, start=i*1.5 + j*0.375, end=i*1.5 + j*0.375 + 0.1875)

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: Develop the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.5),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=4.25, end=4.5),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # F7
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(3, 4):
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=i*1.5, end=i*1.5+0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=i*1.5+0.75, end=i*1.5+1.125),  # Snare on 2
        pretty_midi.Note(velocity=100, pitch=36, start=i*1.5+1.5, end=i*1.5+1.875),  # Kick on 3
        pretty_midi.Note(velocity=100, pitch=38, start=i*1.5+2.25, end=i*1.5+2.625),  # Snare on 4
    ]
    for note in drum_notes:
        drums.notes.append(note)

    # Hihat on every eighth
    for j in range(0, 4):
        pretty_midi.Note(velocity=90, pitch=42, start=i*1.5 + j*0.375, end=i*1.5 + j*0.375 + 0.1875)

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax: End the motif with a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=5.75, end=6.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F7
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4, 5):
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=i*1.5, end=i*1.5+0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=i*1.5+0.75, end=i*1.5+1.125),  # Snare on 2
        pretty_midi.Note(velocity=100, pitch=36, start=i*1.5+1.5, end=i*1.5+1.875),  # Kick on 3
        pretty_midi.Note(velocity=100, pitch=38, start=i*1.5+2.25, end=i*1.5+2.625),  # Snare on 4
    ]
    for note in drum_notes:
        drums.notes.append(note)

    # Hihat on every eighth
    for j in range(0, 4):
        pretty_midi.Note(velocity=90, pitch=42, start=i*1.5 + j*0.375, end=i*1.5 + j*0.375 + 0.1875)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")
