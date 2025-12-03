
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

# Bass line: Walking line in Fm (F, Ab, D, C, etc.)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),   # F (D2)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # Ab (E2)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # Bb (F2)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),   # F (D2)
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),   # Bb (F2)
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),  # G (E2)
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),   # G (E2)
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875),   # G (E2)
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.625),  # Ab (E2)
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),   # F (D2)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),  # F (E4)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),   # Ab (G4)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # Bb (A4)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),   # D (D4)
]
# Bar 3: Bb7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb (F4)
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),   # D (A4)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F (B4)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),   # Ab (G4)
])
# Bar 4: Cm7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # C (G4)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),   # Eb (B4)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F (C5)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),   # G (F4)
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (Fm scale)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F (A4)
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25), # Ab (B4)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Bb (C5)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F (A4)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F (A4)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Bar 2
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
])
# Hihat on every 8th
for i in range(3):
    for j in range(4):
        start = 1.5 + i * 1.5 + j * 0.375
        end = start + 0.375
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
])
# Hihat on every 8th
for i in range(3):
    for j in range(4):
        start = 3.0 + i * 1.5 + j * 0.375
        end = start + 0.375
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
])
# Hihat on every 8th
for i in range(3):
    for j in range(4):
        start = 4.5 + i * 1.5 + j * 0.375
        end = start + 0.375
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
