
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25),  # Db
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),
    # Bar 3 - G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    # Bar 4 - C7 (C, E, G, B)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - short motif, sing it, leave it hanging, come back
sax_notes = [
    # Bar 2 - start the motif
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    # Bar 3 - leave it hanging
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # E
    # Bar 4 - come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: continue in bars 2-4
# Bar 2 (1.5 - 3.0s)
for i in range(4):
    start = 1.5 + i * 0.75
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)  # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)  # Snare on 2 and 4
    for j in range(4):
        pretty_midi.Note(velocity=90, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375)  # Hi-hat

# Bar 3 (3.0 - 4.5s)
for i in range(4):
    start = 3.0 + i * 0.75
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)  # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)  # Snare on 2 and 4
    for j in range(4):
        pretty_midi.Note(velocity=90, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375)  # Hi-hat

# Bar 4 (4.5 - 6.0s)
for i in range(4):
    start = 4.5 + i * 0.75
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)  # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)  # Snare on 2 and 4
    for j in range(4):
        pretty_midi.Note(velocity=90, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375)  # Hi-hat

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
