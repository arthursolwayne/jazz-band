
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # G2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # G2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # G2 (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.375),  # F# (F#4)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.375),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.375),  # C (C5)
]

# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.25 + 0.375),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.25 + 0.375),  # B (B4)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.25 + 0.375),  # D (D5)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.25 + 0.375),  # F (F5)
])

# Bar 4: D7 (D F# A C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.375),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.375),  # F# (F#4)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + 0.375),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.0 + 0.375),  # C (C5)
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Motif: D4 - E4 - G4 - D4 (start on 1.5, end on 2.25, then rest until 4.5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4 (come back)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue in bars 2-4
# Bar 2: Kick on 1, snare on 2, hihat on 8ths
for i in range(0, 3):
    start = 1.5 + i * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),  # Snare on 2
    for j in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375),  # Hihat on 8ths

# Bar 3: Kick on 1, snare on 2, hihat on 8ths
for i in range(0, 3):
    start = 3.0 + i * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),  # Snare on 2
    for j in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375),  # Hihat on 8ths

# Bar 4: Kick on 1, snare on 2, hihat on 8ths
for i in range(0, 3):
    start = 4.5 + i * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),  # Snare on 2
    for j in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375),  # Hihat on 8ths

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
