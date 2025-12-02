
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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
# Sax: motif - D, F#, A, D (Dorian)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in D Dorian
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=45, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=1.875),  # F#
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=90, pitch=52, start=2.125, end=2.25),  # B
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=2.375, end=2.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, beat 2 (7th chord on D, D7)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=1.875),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=1.875),  # D
    # Bar 2, beat 4 (7th chord on G, G7)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.375),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: motif variation - A, D, F#, A (Dorian)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in D Dorian
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=90, pitch=52, start=3.125, end=3.25),  # B
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=3.5, end=3.625),  # E
    pretty_midi.Note(velocity=90, pitch=59, start=3.625, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=3.875),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.0),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 3, beat 2 (7th chord on A, A7)
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=78, start=3.25, end=3.375),  # G
    # Bar 3, beat 4 (7th chord on D, D7)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.875),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: motif variation - D, B, F#, D (Dorian)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=4.75),  # B
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in D Dorian
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.625, end=4.75),  # E
    pretty_midi.Note(velocity=90, pitch=66, start=4.75, end=4.875),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.125),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.125, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.375),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=5.375, end=5.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 4, beat 2 (7th chord on D, D7)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=4.875),  # D
    # Bar 4, beat 4 (7th chord on G, G7)
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.375),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.375),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.375),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Add drum patterns for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    end = start + 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    hihat = [
        pretty_midi.Note(velocity=90, pitch=42, start=start + i*0.375, end=start + i*0.375 + 0.375)
        for i in range(4)
    ]
    for note in [kick, kick2, snare, snare2]:
        drums.notes.append(note)
    for note in hihat:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
