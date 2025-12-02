
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

# Hihat on every eighth note
for i in range(8):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# D minor blues walk: D, C#, B, Bb, A, Ab, G, G#, F#, F, E, Eb, D
bass_notes = [
    (1.5, 64), (1.875, 63), (2.25, 62), (2.625, 60), 
    (3.0, 60), (3.375, 59), (3.75, 67), (4.125, 66),
    (4.5, 65), (4.875, 62), (5.25, 60), (5.625, 60)
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Diane: 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
# G7: G, Bb, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, E
# Dm7 (bar 2), G7 (bar 3), Cm7 (bar 4), F7 (bar 4)
piano_notes = [
    # Bar 2 (1.5 - 1.875)
    (1.5, 62), (1.5, 65), (1.5, 67), (1.5, 60),
    # Bar 3 (2.25 - 2.625)
    (2.25, 67), (2.25, 70), (2.25, 72), (2.25, 65),
    # Bar 4 (3.0 - 3.375)
    (3.0, 60), (3.0, 63), (3.0, 67), (3.0, 65),
    # Bar 4 (3.75 - 4.125)
    (3.75, 65), (3.75, 68), (3.75, 72), (3.75, 67)
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 motif: D, F, G, D
# D (62), F (65), G (67), D (62)
sax_notes = [
    (1.5, 62), (1.75, 65), (1.875, 67), (2.0, 62),
    (3.0, 62), (3.25, 65), (3.375, 67), (3.5, 62),
    (4.5, 62), (4.75, 65), (4.875, 67), (5.0, 62)
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 1.875)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))
for i in range(8):
    start = 1.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 3 (2.25 - 2.625)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.875))
for i in range(8):
    start = 2.25 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 4 (3.0 - 3.375)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.625))
for i in range(8):
    start = 3.0 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 4 (3.75 - 4.125)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.375))
for i in range(8):
    start = 3.75 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
