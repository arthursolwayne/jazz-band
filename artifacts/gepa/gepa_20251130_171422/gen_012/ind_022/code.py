
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# Dm7 -> G7 -> Cmaj7 -> F7
bass_notes = [
    (1.5, 62),  # D
    (1.875, 61), # C#
    (2.25, 64),  # E
    (2.625, 65), # F
    (2.75, 67),  # G
    (3.125, 69), # A
    (3.5, 71),   # B
    (3.875, 72), # C
    (4.25, 74),  # D
    (4.625, 73), # C#
    (5.0, 76),   # E
    (5.375, 77), # F
    (5.5, 79),   # G
    (5.875, 81), # A
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25))

# Piano: 7th chords on 2 and 4
# Dm7, G7, Cmaj7, F7
piano_notes = [
    # Dm7 (Bar 2)
    (1.5, 62), (1.5, 67), (1.5, 69), (1.5, 71),
    # G7 (Bar 3)
    (3.0, 67), (3.0, 71), (3.0, 74), (3.0, 76),
    # Cmaj7 (Bar 4)
    (4.5, 60), (4.5, 64), (4.5, 67), (4.5, 71),
    # F7 (Bar 4)
    (5.25, 55), (5.25, 58), (5.25, 62), (5.25, 66),
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Sax: Motif in D, 4-note phrase (Bar 2)
# D - F - G - B (Dm7)
sax_notes = [
    (1.5, 62), (1.5, 65), (1.5, 67), (1.5, 71)
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.125))

# Drums: Bars 2-4
# Kick on 1 and 3
for i in range(2, 4):
    start = i * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))

# Snare on 2 and 4
for i in range(2, 4):
    start = i * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0))

# Hi-hat on every eighth
for bar in range(2, 4):
    for i in range(0, 4):
        start = bar * 1.5 + i * 0.375
        end = start + 0.125
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
