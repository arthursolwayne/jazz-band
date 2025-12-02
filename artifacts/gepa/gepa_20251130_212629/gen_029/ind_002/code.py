
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
drum_notes = [
    (0.0, 36, 100),     # Kick on 1
    (0.375, 42, 100),   # Hihat on &1
    (0.75, 36, 100),    # Kick on 2
    (0.875, 42, 100),   # Hihat on &2
    (1.125, 38, 100),   # Snare on 3
    (1.375, 42, 100),   # Hihat on &3
    (1.5, 36, 100),     # Kick on 4
    (1.625, 42, 100),   # Hihat on &4
    (1.875, 38, 100),   # Snare on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.1875))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    (1.5, 57, 80),     # D (root)
    (1.625, 58, 80),   # Eb (chromatic)
    (1.75, 59, 80),    # E
    (1.875, 60, 80),   # F (chromatic)
    (2.0, 61, 80),     # F#
    (2.125, 62, 80),   # G
    (2.25, 63, 80),    # G#
    (2.375, 64, 80),   # A
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.125))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 60, 85),     # D7 (D F A C)
    (1.5, 62, 85),
    (1.5, 64, 85),
    (1.5, 67, 85),
    (1.625, 60, 85),   # D7 again
    (1.625, 62, 85),
    (1.625, 64, 85),
    (1.625, 67, 85),
    (2.25, 60, 85),    # D7 again
    (2.25, 62, 85),
    (2.25, 64, 85),
    (2.25, 67, 85),
    (2.375, 60, 85),   # D7 again
    (2.375, 62, 85),
    (2.375, 64, 85),
    (2.375, 67, 85),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.125))

# Dante: Motif, make it sing. Start it, leave it hanging.
sax_notes = [
    (1.5, 62, 100),    # E (melody start)
    (1.75, 62, 100),   # E (hold)
    (1.875, 60, 100),  # D (resolve?)
    (2.0, 62, 100),    # E (upper neighbor)
    (2.125, 60, 100),  # D (return)
    (2.25, 62, 100),   # E (resolve?)
    (2.375, 65, 100),  # G (suspense)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    (3.0, 64, 80),     # A
    (3.125, 65, 80),   # A#
    (3.25, 66, 80),    # B
    (3.375, 67, 80),   # B#
    (3.5, 68, 80),     # C
    (3.625, 69, 80),   # C#
    (3.75, 70, 80),    # D
    (3.875, 71, 80),   # D#
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.125))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (3.0, 62, 85),     # D7 again
    (3.0, 64, 85),
    (3.0, 67, 85),
    (3.0, 69, 85),
    (3.125, 62, 85),
    (3.125, 64, 85),
    (3.125, 67, 85),
    (3.125, 69, 85),
    (3.75, 62, 85),
    (3.75, 64, 85),
    (3.75, 67, 85),
    (3.75, 69, 85),
    (3.875, 62, 85),
    (3.875, 64, 85),
    (3.875, 67, 85),
    (3.875, 69, 85),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.125))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
drum_notes = [
    (3.0, 36, 100),     # Kick on 1
    (3.375, 42, 100),   # Hihat on &1
    (3.75, 36, 100),    # Kick on 2
    (3.875, 42, 100),   # Hihat on &2
    (4.125, 38, 100),   # Snare on 3
    (4.375, 42, 100),   # Hihat on &3
    (4.5, 36, 100),     # Kick on 4
    (4.625, 42, 100),   # Hihat on &4
    (4.875, 38, 100),   # Snare on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.1875))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    (4.5, 69, 80),     # D
    (4.625, 70, 80),   # Eb (chromatic)
    (4.75, 71, 80),    # E
    (4.875, 72, 80),   # F (chromatic)
    (5.0, 73, 80),     # F#
    (5.125, 74, 80),   # G
    (5.25, 75, 80),    # G#
    (5.375, 76, 80),   # A
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.125))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (4.5, 62, 85),     # D7 (D F A C)
    (4.5, 64, 85),
    (4.5, 67, 85),
    (4.5, 69, 85),
    (4.625, 62, 85),   # D7 again
    (4.625, 64, 85),
    (4.625, 67, 85),
    (4.625, 69, 85),
    (5.25, 62, 85),    # D7 again
    (5.25, 64, 85),
    (5.25, 67, 85),
    (5.25, 69, 85),
    (5.375, 62, 85),   # D7 again
    (5.375, 64, 85),
    (5.375, 67, 85),
    (5.375, 69, 85),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.125))

# Dante: Motif continuation, ends with a question
sax_notes = [
    (4.5, 65, 100),    # G
    (4.75, 65, 100),   # G (hold)
    (4.875, 63, 100),  # F (resolve?)
    (5.0, 65, 100),    # G (upper neighbor)
    (5.125, 63, 100),  # F (return)
    (5.25, 65, 100),   # G (resolve?)
    (5.375, 68, 100),  # Bb (question mark)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.125))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
drum_notes = [
    (4.5, 36, 100),     # Kick on 1
    (4.875, 42, 100),   # Hihat on &1
    (5.25, 36, 100),    # Kick on 2
    (5.375, 42, 100),   # Hihat on &2
    (5.625, 38, 100),   # Snare on 3
    (5.875, 42, 100),   # Hihat on &3
    (6.0, 36, 100),     # Kick on 4
    (6.125, 42, 100),   # Hihat on &4
    (6.375, 38, 100),   # Snare on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.1875))

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
