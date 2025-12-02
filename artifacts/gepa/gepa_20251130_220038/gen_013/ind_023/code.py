
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
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 55),  # D
    (1.875, 56),  # Eb
    (2.25, 57),  # E
    (2.625, 59),  # G
    (2.875, 60),  # G#
    (3.25, 62),  # A#
    (3.625, 60),  # G#
    (4.0, 59),  # G
    (4.375, 57),  # E
    (4.75, 55),  # D
    (5.125, 53),  # C
    (5.5, 55),  # D
    (5.875, 57),  # E
    (6.25, 59),  # G
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25))

# Diane: 7th chords, comp on 2 and 4
# D7 = D, F#, A, C
# F#7 = F#, A#, C#, E
# B7 = B, D#, F#, A
# G7 = G, B, D, F
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    (1.5, 62),  # D
    (1.5, 67),  # F#
    (1.5, 69),  # A
    (1.5, 64),  # C
    # Bar 3 (2.5 - 3.0s)
    (2.5, 67),  # F#
    (2.5, 71),  # A#
    (2.5, 74),  # C#
    (2.5, 69),  # E
    # Bar 4 (3.5 - 4.0s)
    (3.5, 67),  # B
    (3.5, 72),  # D#
    (3.5, 74),  # F#
    (3.5, 69),  # A
    # Bar 4 (4.5 - 5.0s)
    (4.5, 71),  # G
    (4.5, 76),  # B
    (4.5, 78),  # D
    (4.5, 73),  # F
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25))

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (67), A (69), D (62)
# Play on beat 1 of bar 2, then beat 3 of bar 2, then beat 1 of bar 3, then beat 3 of bar 3

sax_notes = [
    (1.5, 62),  # D
    (1.875, 67),  # F#
    (2.25, 69),  # A
    (2.625, 62),  # D
    (3.0, 67),  # F#
    (3.375, 69),  # A
    (3.75, 62),  # D
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125))

# Drums: fill the bar
# Bar 2 (1.5 - 2.0s)
for i in range(0, 4):
    start = 1.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 3 (2.5 - 3.0s)
for i in range(0, 4):
    start = 2.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 4 (3.5 - 4.0s)
for i in range(0, 4):
    start = 3.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Kick on 1 and 3 of bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))

# Kick on 1 and 3 of bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.5))

# Kick on 1 and 3 of bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))

# Snare on 2 and 4 of bar 2
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75))

# Snare on 2 and 4 of bar 3
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625))

# Snare on 2 and 4 of bar 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
