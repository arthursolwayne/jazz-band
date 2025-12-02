
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

# Kicks on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snares on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth note
for i in range(4):
    hihat_start = i * 0.375
    hihat_end = hihat_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    (1.5, 62),  # D
    (1.875, 61), # C#
    (2.25, 63),  # Eb
    (2.625, 62), # D
    (2.875, 61), # C#
    (3.25, 63),  # Eb
    (3.625, 62), # D
    (4.0, 61),   # C#
    (4.375, 63), # Eb
    (4.75, 62),  # D
    (5.125, 61), # C#
    (5.5, 63),   # Eb
    (5.875, 62), # D
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25))

# Diane: 7th chords, comp on 2 and 4
# Bar 2: D7 on beat 2
piano_notes = [
    (1.875, 64), (1.875, 67), (1.875, 69), (1.875, 71),  # D7
    (2.625, 64), (2.625, 67), (2.625, 69), (2.625, 71),  # D7
    (3.5, 64), (3.5, 67), (3.5, 69), (3.5, 71),          # D7
    (4.375, 64), (4.375, 67), (4.375, 69), (4.375, 71),  # D7
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25))

# Dante: Motif - start with a phrase that sings
# D (62), F# (66), G (67), D (62) - then leave it hanging
sax_notes = [
    (1.5, 62), (1.5, 66), (1.5, 67), (1.5, 62),
    (2.25, 62), (2.25, 66), (2.25, 67), (2.25, 62),
    (3.0, 62), (3.0, 66), (3.0, 67), (3.0, 62),
    (3.75, 62), (3.75, 66), (3.75, 67), (3.75, 62),
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875))

# Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375))

# Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=6.375, end=6.75))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=6.75, end=6.875))

# Hihat on every eighth note for bars 2-4
for i in range(6):
    hihat_start = 1.5 + i * 0.375
    hihat_end = hihat_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_intro.mid")
