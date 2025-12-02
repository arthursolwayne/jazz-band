
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))

# Hihat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 42),  # F
    (1.875, 44),  # F# (chromatic)
    (2.25, 43),  # E (approach to F)
    (2.625, 45),  # G (walking)
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 on 2 and 4
piano_notes = [
    (1.875, 53), (1.875, 50), (1.875, 60), (1.875, 62),  # F7 (F, A, C, E)
    (2.625, 53), (2.625, 50), (2.625, 60), (2.625, 62)
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Sax: Whispering motif (F, G#, Bb, F)
sax_notes = [
    (1.5, 65),     # F
    (1.75, 68),    # G#
    (2.0, 62),     # Bb
    (2.25, 65),    # F
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    (3.0, 45),  # G
    (3.375, 47),  # G#
    (3.75, 46),  # F# (approach to G)
    (4.125, 48),  # A
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Piano: 7th chords, comp on 2 and 4
# Bar 3: Bb7 on 2 and 4
piano_notes = [
    (3.375, 55), (3.375, 52), (3.375, 62), (3.375, 64),  # Bb7 (Bb, D, F, Ab)
    (4.125, 55), (4.125, 52), (4.125, 62), (4.125, 64)
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Sax: Continue the motif, build it up
sax_notes = [
    (3.0, 65),     # F
    (3.25, 68),    # G#
    (3.5, 62),     # Bb
    (3.75, 65),    # F
    (4.0, 65),     # F
    (4.25, 68),    # G#
    (4.5, 62),     # Bb
    (4.75, 65),    # F
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    (4.5, 48),  # A
    (4.875, 50),  # Bb
    (5.25, 49),  # A# (approach to Bb)
    (5.625, 51),  # B
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Piano: 7th chords, comp on 2 and 4
# Bar 4: D7 on 2 and 4
piano_notes = [
    (4.875, 57), (4.875, 54), (4.875, 64), (4.875, 67),  # D7 (D, F#, A, C)
    (5.625, 57), (5.625, 54), (5.625, 64), (5.625, 67)
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Sax: Cry out, finish the motif
sax_notes = [
    (4.5, 65),     # F
    (4.75, 68),    # G#
    (5.0, 62),     # Bb
    (5.25, 65),    # F
    (5.5, 65),     # F
    (5.75, 68),    # G#
    (6.0, 62),     # Bb
    (6.25, 65),    # F
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))

# Hihat on every eighth
for i in range(0, 6):
    start = i * 0.375 + 3.0
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
