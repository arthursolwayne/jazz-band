
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
    (0.0, 36, 100),  # Kick on beat 1
    (0.375, 42, 100), # Hihat on &1
    (0.75, 38, 100),  # Snare on beat 2
    (1.125, 42, 100), # Hihat on &2
    (1.5, 36, 100),   # Kick on beat 3
    (1.875, 42, 100), # Hihat on &3
    (2.25, 38, 100),  # Snare on beat 4
    (2.625, 42, 100)  # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line with chromatic approaches
bass_notes = [
    (1.5, 48, 100),  # F
    (1.875, 50, 100), # F#
    (2.25, 52, 100),  # G
    (2.625, 51, 100), # Gb
    (3.0, 52, 100),   # G
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Diane on piano: open voicing, F7 (F, A, C, E)
piano_notes = [
    (1.5, 65, 100),  # F
    (1.5, 77, 100),  # A
    (1.5, 69, 100),  # C
    (1.5, 74, 100),  # E
    (2.0, 65, 100),  # F
    (2.0, 77, 100),  # A
    (2.0, 69, 100),  # C
    (2.0, 76, 100),  # D
    (2.5, 65, 100),  # F
    (2.5, 77, 100),  # A
    (2.5, 69, 100),  # C
    (2.5, 74, 100),  # E
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Dante on sax: haunting motif, incomplete
sax_notes = [
    (1.5, 71, 100),  # Bb
    (1.75, 74, 100),  # D
    (2.0, 71, 100),  # Bb
    (2.25, 76, 100),  # E
    (2.5, 74, 100),  # D
    (2.75, 71, 100),  # Bb
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus on bass: walking line with chromatic approaches
bass_notes = [
    (3.0, 52, 100),  # G
    (3.375, 53, 100), # G#
    (3.75, 55, 100),  # A
    (4.125, 54, 100), # Ab
    (4.5, 55, 100),   # A
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Diane on piano: open voicing, Bb7 (Bb, D, F, Ab)
piano_notes = [
    (3.0, 62, 100),  # Bb
    (3.0, 74, 100),  # D
    (3.0, 65, 100),  # F
    (3.0, 71, 100),  # Ab
    (3.5, 62, 100),  # Bb
    (3.5, 74, 100),  # D
    (3.5, 65, 100),  # F
    (3.5, 71, 100),  # Ab
    (4.0, 62, 100),  # Bb
    (4.0, 74, 100),  # D
    (4.0, 65, 100),  # F
    (4.0, 71, 100),  # Ab
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Dante on sax: continuation of the motif
sax_notes = [
    (3.0, 71, 100),  # Bb
    (3.25, 74, 100),  # D
    (3.5, 71, 100),  # Bb
    (3.75, 76, 100),  # E
    (4.0, 74, 100),  # D
    (4.25, 71, 100),  # Bb
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus on bass: walking line with chromatic approaches
bass_notes = [
    (4.5, 55, 100),  # A
    (4.875, 57, 100), # Bb
    (5.25, 59, 100),  # B
    (5.625, 58, 100), # Bb
    (6.0, 59, 100),   # B
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Diane on piano: open voicing, G7 (G, B, D, F)
piano_notes = [
    (4.5, 67, 100),  # G
    (4.5, 79, 100),  # B
    (4.5, 71, 100),  # D
    (4.5, 67, 100),  # G
    (5.0, 67, 100),  # G
    (5.0, 79, 100),  # B
    (5.0, 71, 100),  # D
    (5.0, 67, 100),  # G
    (5.5, 67, 100),  # G
    (5.5, 79, 100),  # B
    (5.5, 71, 100),  # D
    (5.5, 67, 100),  # G
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Dante on sax: final phrase of the motif, incomplete, haunting
sax_notes = [
    (4.5, 71, 100),  # Bb
    (4.75, 74, 100),  # D
    (5.0, 71, 100),  # Bb
    (5.25, 76, 100),  # E
    (5.5, 74, 100),  # D
    (5.75, 71, 100),  # Bb
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: kick on 1, snare on 2, hihat on 3, kick on 4
drum_notes = [
    (4.5, 36, 100),
    (4.875, 38, 100),
    (5.25, 42, 100),
    (5.625, 36, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
