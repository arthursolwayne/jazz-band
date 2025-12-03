
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full ensemble enters
# Sax: 4-note motif - F5, G5, D5, Bb4 (F7, G7, D7, Bb6)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line - F2, G2, A2, Bb2 (F2, G2, A2, Bb2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat every eighth
# Bar 2 (1.5 - 3.0)
for start in [1.5, 2.625]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
for start in [1.875, 3.0]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
for start in [1.5, 1.875, 2.25, 2.625, 3.0]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=3.0))

# Bar 3 (3.0 - 4.5)
for start in [3.0, 4.125]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
for start in [3.375, 4.5]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
for start in [3.0, 3.375, 3.75, 4.125, 4.5]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=4.5))

# Bar 4 (4.5 - 6.0)
for start in [4.5, 5.625]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
for start in [4.875, 6.0]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
for start in [4.5, 4.875, 5.25, 5.625, 6.0]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=6.0))

# Sax: Bar 4 - repeats the motif, but shifts slightly
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Bar 3-4
# Bar 3: G2, A2, Bb2, C3 (G2, A2, Bb2, C3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=39, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 4: C2, D2, Eb2, F2 (C2, D2, Eb2, F2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
