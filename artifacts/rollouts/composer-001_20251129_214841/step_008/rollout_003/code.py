
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=1.625, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=1.875),  # D#
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=2.25, end=2.375),  # A#
    pretty_midi.Note(velocity=80, pitch=71, start=2.375, end=2.5),   # B
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=2.875),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=2.875, end=3.0),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # B
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=2.75, end=3.0),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax motif
sax_notes = [
    # Bar 2: First note of the motif
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # E
    # Bar 3: Second note of the motif
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    # Bar 4: Third note of the motif
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # A
    # Bar 4: Final note of the motif
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(3):
    start = 1.5 + i * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5),
    ]
    for note in drum_notes:
        drums.notes.append(note)

# Bar 4: Drums continue
start = 3.0
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
