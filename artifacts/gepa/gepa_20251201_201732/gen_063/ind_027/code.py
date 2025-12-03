
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.5),     # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm (F, Ab, D, C, etc.)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25), # Ab2 (b3)
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.625), # D2 (5)
    pretty_midi.Note(velocity=80, pitch=55, start=2.625, end=3.0),  # C2 (7)
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75), # Ab2 (b3)
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125), # D2 (5)
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),  # C2 (7)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25), # Ab2 (b3)
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.625), # D2 (5)
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=6.0),  # C2 (7)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # D5
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F5
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # Ab4
])

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Eb5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G5
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb5
])

# Bar 4: Resolve on Fm7 (F, Ab, C, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # D5
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # D5
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # C5
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),   # F4
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # D5 (repeat)
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25), # C5
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625), # D5
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # F4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Bar 2: Kick on 1, snare on 2, kick on 3, snare on 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=2.25),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),   # Hihat on every 8th

    # Bar 3: Kick on 1, snare on 2, kick on 3, snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # Hihat on every 8th

    # Bar 4: Kick on 1, snare on 2, kick on 3, snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.0),     # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
