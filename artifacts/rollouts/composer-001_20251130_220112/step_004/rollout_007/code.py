
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Dm7 - D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # A
]
for note in sax_notes:
    sax.notes.append(note)

# Bass line - walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=48, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),   # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # C
    # Bar 3: G7 on 2
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.875, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.875, end=3.25),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=2.875, end=3.25),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody (reprise of first two notes)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Bass line - walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),   # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 3: G7 on 2
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # F
    # Bar 4: C7 on 2
    pretty_midi.Note(velocity=90, pitch=60, start=4.375, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.375, end=4.75),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.375, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.375, end=4.75),  # B
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody - resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # A
]
for note in sax_notes:
    sax.notes.append(note)

# Bass line - walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),   # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 4: C7 on 2
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # B
]
for note in piano_notes:
    piano.notes.append(note)

# Drums for Bar 2-4
# Bar 2: 1.5 - 3.0s
for i in range(2):
    start = 1.5 + i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for j in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375)
    for note in [pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
                 pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
                 pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
                 pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)]:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
