
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
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 100),  # Hihat
    (0.75, 38, 100),  # Snare on 2
    (1.125, 42, 100),  # Hihat
    (1.5, 36, 100),  # Kick on 3
    (1.875, 42, 100),  # Hihat
    (2.25, 38, 100),  # Snare on 4
    (2.625, 42, 100)   # Hihat
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in F (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 43, 80),  # F (43)
    (1.875, 41, 80),  # Eb (41) chromatic approach
    (2.25, 38, 80),  # D (38)
    (2.625, 40, 80)  # E (40) chromatic approach
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    (1.5, 62, 100),  # F (62)
    (1.5, 67, 100),  # A (67)
    (1.5, 69, 100),  # C (69)
    (1.5, 64, 100),  # Eb (64)

    (1.875, 65, 100),  # Ab (65) as color
    (1.875, 71, 100),  # D (71) chromatic
    (1.875, 76, 100),  # G (76) chromatic
    (1.875, 67, 100),  # A (67) again

    (2.25, 62, 100),  # F (62)
    (2.25, 67, 100),  # A (67)
    (2.25, 69, 100),  # C (69)
    (2.25, 64, 100),  # Eb (64)

    (2.625, 67, 100),  # A (67) resolving
    (2.625, 69, 100),  # C (69)
    (2.625, 71, 100),  # D (71)
    (2.625, 76, 100)   # G (76)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Dante: One short motif, make it sing. Start it, leave it hanging.
sax_notes = [
    (1.5, 66, 100),  # F# (66)
    (1.625, 69, 100),  # Bb (69)
    (1.75, 64, 100),  # Eb (64)
    (1.875, 66, 100),  # F# (66)
    (2.0, 62, 100),  # F (62)
    (2.125, 69, 100),  # Bb (69)
    (2.25, 66, 100),  # F# (66)
    (2.375, 64, 100),  # Eb (64)
    (2.5, 62, 100),  # F (62)
    (2.625, 69, 100),  # Bb (69)
    (2.75, 66, 100),  # F# (66)
    (2.875, 64, 100)   # Eb (64)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line with chromatic approaches
bass_notes = [
    (3.0, 38, 80),  # D (38)
    (3.375, 40, 80),  # E (40)
    (3.75, 38, 80),  # D (38)
    (4.125, 41, 80)  # Eb (41)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    (3.0, 57, 100),  # Bb (57)
    (3.0, 62, 100),  # D (62)
    (3.0, 64, 100),  # F (64)
    (3.0, 65, 100),  # Ab (65)

    (3.375, 60, 100),  # Eb (60) as color
    (3.375, 67, 100),  # A (67) chromatic
    (3.375, 71, 100),  # D (71) chromatic
    (3.375, 62, 100),  # D (62)

    (3.75, 57, 100),  # Bb (57)
    (3.75, 62, 100),  # D (62)
    (3.75, 64, 100),  # F (64)
    (3.75, 65, 100),  # Ab (65)

    (4.125, 62, 100),  # D (62) resolving
    (4.125, 64, 100),  # F (64)
    (4.125, 67, 100),  # A (67)
    (4.125, 71, 100)   # D (71)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Dante: Continue the motif but with a slight shift
sax_notes = [
    (3.0, 62, 100),  # F (62)
    (3.125, 64, 100),  # G (64)
    (3.25, 66, 100),  # A (66)
    (3.375, 67, 100),  # Bb (67)
    (3.5, 64, 100),  # G (64)
    (3.625, 62, 100),  # F (62)
    (3.75, 64, 100),  # G (64)
    (3.875, 66, 100),  # A (66)
    (4.0, 62, 100),  # F (62)
    (4.125, 64, 100),  # G (64)
    (4.25, 66, 100),  # A (66)
    (4.375, 67, 100)   # Bb (67)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line with chromatic approaches
bass_notes = [
    (4.5, 43, 80),  # F (43)
    (4.875, 41, 80),  # Eb (41)
    (5.25, 38, 80),  # D (38)
    (5.625, 40, 80)  # E (40)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    (4.5, 64, 100),  # Eb (64)
    (4.5, 67, 100),  # G (67)
    (4.5, 69, 100),  # Bb (69)
    (4.5, 71, 100),  # D (71)

    (4.875, 57, 100),  # Bb (57) as color
    (4.875, 62, 100),  # D (62) chromatic
    (4.875, 67, 100),  # G (67) chromatic
    (4.875, 64, 100),  # Eb (64)

    (5.25, 64, 100),  # Eb (64)
    (5.25, 67, 100),  # G (67)
    (5.25, 69, 100),  # Bb (69)
    (5.25, 71, 100),  # D (71)

    (5.625, 67, 100),  # G (67) resolving
    (5.625, 69, 100),  # Bb (69)
    (5.625, 71, 100),  # D (71)
    (5.625, 76, 100)   # G (76)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Dante: End the motif with a question mark
sax_notes = [
    (4.5, 66, 100),  # F# (66)
    (4.625, 69, 100),  # Bb (69)
    (4.75, 64, 100),  # Eb (64)
    (4.875, 66, 100),  # F# (66)
    (5.0, 62, 100),  # F (62)
    (5.125, 69, 100),  # Bb (69)
    (5.25, 66, 100),  # F# (66)
    (5.375, 64, 100),  # Eb (64)
    (5.5, 62, 100),  # F (62)
    (5.625, 69, 100),  # Bb (69)
    (5.75, 66, 100),  # F# (66)
    (5.875, 64, 100)   # Eb (64)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100),  # Kick on 1
    (4.875, 42, 100),  # Hihat
    (5.25, 38, 100),  # Snare on 2
    (5.625, 42, 100),  # Hihat
    (6.0, 36, 100),  # Kick on 3
    (6.375, 42, 100),  # Hihat
    (6.75, 38, 100),  # Snare on 4
    (7.125, 42, 100)   # Hihat
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
