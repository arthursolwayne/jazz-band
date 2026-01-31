
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),   # G2
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),   # G2
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),   # G2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.25),  # C5
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=3.0),   # G4
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=3.0),   # Bb4
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0),   # D5
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),   # F5
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),   # C5
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),   # Eb5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),   # G5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),   # Bb5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, E, F, G, A, Bb, C
# Motif: D - F - A - (rest) -> D - F - A
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D5
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # F5
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # A5
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # F5
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # A5
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
