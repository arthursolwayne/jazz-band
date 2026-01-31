
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, roots and fifths with chromatic approaches
# D2 (D), F (F), C (C), A (A)
# Chromatic approach: C#, Eb, Ab, Bb
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # F (chromatic Eb)
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # A (chromatic Ab)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=37, start=3.75, end=4.125),  # C#
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # D2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # F (chromatic Eb)
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C4
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F4
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # Bb4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), F4 (65), A4 (69), C4 (67) - then repeat
# Start at 1.5s, end at 2.25s, then again at 3.75s to 4.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
for i in range(0, 2):
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i * 1.5, end=1.5 + i * 1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5 + i * 1.5 + 0.375, end=1.5 + i * 1.5 + 0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + i * 1.5, end=1.5 + i * 1.5 + 1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i * 1.5 + 0.75, end=1.5 + i * 1.5 + 1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5 + i * 1.5 + 1.125, end=1.5 + i * 1.5 + 1.5),

# Bar 3 (3.0 - 4.5s)
for i in range(0, 2):
    pretty_midi.Note(velocity=100, pitch=36, start=3.0 + i * 1.5, end=3.0 + i * 1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0 + i * 1.5 + 0.375, end=3.0 + i * 1.5 + 0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0 + i * 1.5, end=3.0 + i * 1.5 + 1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0 + i * 1.5 + 0.75, end=3.0 + i * 1.5 + 1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0 + i * 1.5 + 1.125, end=3.0 + i * 1.5 + 1.5),

# Bar 4 (4.5 - 6.0s)
for i in range(0, 2):
    pretty_midi.Note(velocity=100, pitch=36, start=4.5 + i * 1.5, end=4.5 + i * 1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5 + i * 1.5 + 0.375, end=4.5 + i * 1.5 + 0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5 + i * 1.5, end=4.5 + i * 1.5 + 1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5 + i * 1.5 + 0.75, end=4.5 + i * 1.5 + 1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5 + i * 1.5 + 1.125, end=4.5 + i * 1.5 + 1.5),

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
