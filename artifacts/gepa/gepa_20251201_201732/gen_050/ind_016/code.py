
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),      # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),   # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full ensemble
# Bass: Walking line, Fm7 -> Bbm7 -> Eb7 -> Am7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),    # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),   # D (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),   # C (chromatic)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),    # Bb (root)
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375),    # D (fifth)
    pretty_midi.Note(velocity=90, pitch=39, start=3.375, end=3.75),   # C (chromatic)
    pretty_midi.Note(velocity=90, pitch=37, start=3.75, end=4.125),   # Eb (root)
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),    # G (fifth)
    pretty_midi.Note(velocity=90, pitch=39, start=4.5, end=4.875),    # G# (chromatic)
    pretty_midi.Note(velocity=90, pitch=36, start=4.875, end=5.25),   # A (root)
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.625),   # C (fifth)
    pretty_midi.Note(velocity=90, pitch=37, start=5.625, end=6.0),    # Eb (chromatic)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.125),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.5 + 0.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.125),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.5 + 0.125),  # Eb
]

# Bar 3: Bbm7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.125),  # Ab
])

# Bar 4: Am7 (A, C, E, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625),  # G
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif
# Bar 2: Melody starts
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5 + 0.75, end=start + 1.5 + 1.125),

    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.5 + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5 + 0.375, end=start + 1.5 + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5 + 0.75, end=start + 1.5 + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5 + 1.125, end=start + 1.5 + 1.5)

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
