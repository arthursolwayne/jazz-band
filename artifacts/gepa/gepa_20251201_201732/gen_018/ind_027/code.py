
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approach on Fm7
# Fm7: F, Ab, D, C
bass_notes = [
    (1.5, 38), (1.875, 40), (2.25, 38), (2.625, 41),
    (3.0, 38), (3.375, 40), (3.75, 38), (4.125, 41)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Piano: Fm7 -> Bb7 -> Eb7 -> Am7
# Bar 2: Fm7 (F, Ab, D, C)
piano_notes = [
    (1.5, 53), (1.5, 60), (1.5, 62), (1.5, 58),
    (1.5, 56), (1.5, 60), (1.5, 62), (1.5, 58)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Sax: Motif
# F, Ab, Bb, B (melodic minor)
sax_notes = [
    (1.5, 53), (1.875, 60), (2.25, 62), (2.625, 63)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approach on Bb7
# Bb7: Bb, D, F, Ab
bass_notes = [
    (3.0, 40), (3.375, 42), (3.75, 40), (4.125, 41),
    (4.5, 40), (4.875, 42), (5.25, 40), (5.625, 41)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Piano: Bb7 -> Eb7 -> Am7
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    (3.0, 56), (3.0, 62), (3.0, 58), (3.0, 60),
    (3.0, 54), (3.0, 62), (3.0, 58), (3.0, 60)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Sax: Motif
# Bb, B, C, Db
sax_notes = [
    (3.0, 62), (3.375, 63), (3.75, 64), (4.125, 65)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approach on Eb7
# Eb7: Eb, G, Bb, D
bass_notes = [
    (4.5, 41), (4.875, 43), (5.25, 41), (5.625, 45),
    (6.0, 41), (6.375, 43), (6.75, 41), (7.125, 45)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Piano: Eb7 -> Am7 -> Fm7
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    (4.5, 54), (4.5, 62), (4.5, 58), (4.5, 64),
    (4.5, 53), (4.5, 60), (4.5, 62), (4.5, 58)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Sax: Motif
# Eb, F, G, Ab
sax_notes = [
    (4.5, 64), (4.875, 65), (5.25, 67), (5.625, 68)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
