
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=70, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=70, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    # Bar 2: D - C# - B - C
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),
    # Bar 3: F - E - D - E
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=63, start=4.125, end=4.5),
    # Bar 4: A - G# - G - A
    pretty_midi.Note(velocity=80, pitch=66, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=66, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane, 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 = D F# A C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),
    # Bar 3: F7 = F A C# E
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    # Bar 4: A7 = A C# E G
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante's motif
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
    # Bar 3: Second phrase (leave it hanging for a moment)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4: Finish it with a higher variation
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Add more drum fills in bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    offset = 1.5 + i * 1.5
    kick = pretty_midi.Note(velocity=90, pitch=36, start=offset, end=offset + 0.375)
    snare = pretty_midi.Note(velocity=95, pitch=38, start=offset + 0.75, end=offset + 1.125)
    hihat = [
        pretty_midi.Note(velocity=70, pitch=42, start=offset + 0.0, end=offset + 0.375),
        pretty_midi.Note(velocity=70, pitch=42, start=offset + 0.375, end=offset + 0.75),
        pretty_midi.Note(velocity=70, pitch=42, start=offset + 0.75, end=offset + 1.125),
        pretty_midi.Note(velocity=70, pitch=42, start=offset + 1.125, end=offset + 1.5),
    ]
    drums.notes.append(kick)
    drums.notes.append(snare)
    for n in hihat:
        drums.notes.append(n)

# Bar 3: Same pattern, but with a fill on 3
offset = 3.0
kick = pretty_midi.Note(velocity=90, pitch=36, start=offset, end=offset + 0.375)
snare = pretty_midi.Note(velocity=95, pitch=38, start=offset + 0.75, end=offset + 1.125)
hihat = [
    pretty_midi.Note(velocity=70, pitch=42, start=offset + 0.0, end=offset + 0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=offset + 0.375, end=offset + 0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=offset + 0.75, end=offset + 1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=offset + 1.125, end=offset + 1.5),
]
drums.notes.append(kick)
drums.notes.append(snare)
for n in hihat:
    drums.notes.append(n)

# Bar 4: Same pattern, but with a fill on 3
offset = 4.5
kick = pretty_midi.Note(velocity=90, pitch=36, start=offset, end=offset + 0.375)
snare = pretty_midi.Note(velocity=95, pitch=38, start=offset + 0.75, end=offset + 1.125)
hihat = [
    pretty_midi.Note(velocity=70, pitch=42, start=offset + 0.0, end=offset + 0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=offset + 0.375, end=offset + 0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=offset + 0.75, end=offset + 1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=offset + 1.125, end=offset + 1.5),
]
drums.notes.append(kick)
drums.notes.append(snare)
for n in hihat:
    drums.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
