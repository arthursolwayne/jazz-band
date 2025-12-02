
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

# Hihat on every eighth note
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 44),  # F (root)
    (1.875, 46),  # G (chromatic up)
    (2.25, 45),  # Gb (chromatic down)
    (2.625, 43),  # E (approach to F)
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 1: F7 (F, A, C, E)
    (1.5, 71), (1.5, 69), (1.5, 67), (1.5, 65),
    # Bar 2, beat 2: comp on 2
    (1.875, 72), (1.875, 70), (1.875, 68), (1.875, 66),
    # Bar 2, beat 3: F7 again
    (2.25, 71), (2.25, 69), (2.25, 67), (2.25, 65),
    # Bar 2, beat 4: comp on 4
    (2.625, 72), (2.625, 70), (2.625, 68), (2.625, 66),
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=start + 0.375))

# Sax: Motif - start it, leave it hanging, come back and finish it
# F (66) -> C (60) -> B (62) -> F (66)
sax_notes = [
    (1.5, 66),  # F
    (1.875, 60),  # C
    (2.25, 62),  # B
    (2.625, 66),  # F
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=start + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (3.0, 46),  # G
    (3.375, 45),  # Gb
    (3.75, 44),  # F
    (4.125, 42),  # E
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 1: F7 (F, A, C, E)
    (3.0, 71), (3.0, 69), (3.0, 67), (3.0, 65),
    # Bar 3, beat 2: comp on 2
    (3.375, 72), (3.375, 70), (3.375, 68), (3.375, 66),
    # Bar 3, beat 3: F7 again
    (3.75, 71), (3.75, 69), (3.75, 67), (3.75, 65),
    # Bar 3, beat 4: comp on 4
    (4.125, 72), (4.125, 70), (4.125, 68), (4.125, 66),
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=start + 0.375))

# Sax: Motif variation - repeat with subtle change
# F (66) -> C (60) -> B (62) -> F# (67)
sax_notes = [
    (3.0, 66),  # F
    (3.375, 60),  # C
    (3.75, 62),  # B
    (4.125, 67),  # F#
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=start + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, 4):
    start = 3.0 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (4.5, 47),  # A
    (4.875, 46),  # G
    (5.25, 44),  # F
    (5.625, 43),  # E
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 1: F7 (F, A, C, E)
    (4.5, 71), (4.5, 69), (4.5, 67), (4.5, 65),
    # Bar 4, beat 2: comp on 2
    (4.875, 72), (4.875, 70), (4.875, 68), (4.875, 66),
    # Bar 4, beat 3: F7 again
    (5.25, 71), (5.25, 69), (5.25, 67), (5.25, 65),
    # Bar 4, beat 4: comp on 4
    (5.625, 72), (5.625, 70), (5.625, 68), (5.625, 66),
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=start + 0.375))

# Sax: Motif resolution - F (66) -> C (60) -> B (62) -> F (66), with a slight delay on the last note
sax_notes = [
    (4.5, 66),  # F
    (4.875, 60),  # C
    (5.25, 62),  # B
    (5.75, 66),  # F (delayed)
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=start + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, 4):
    start = 4.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
