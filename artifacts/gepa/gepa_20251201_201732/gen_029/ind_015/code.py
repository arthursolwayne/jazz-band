
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
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (D2 is E, F2 is F), walking line with chromatic approaches
bass_notes = [
    (1.5, 43), (1.875, 42), (2.25, 44), (2.625, 43)
]
for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    (1.5, 64), (1.5, 67), (1.5, 71), (1.5, 76),  # Fm7 (F, Ab, C, Eb)
    (1.875, 65), (1.875, 68), (1.875, 72), (1.875, 76),  # Gm7 (G, Bb, D, F)
    (2.25, 66), (2.25, 69), (2.25, 73), (2.25, 77),  # Am7 (A, C, E, G)
    (2.625, 64), (2.625, 67), (2.625, 71), (2.625, 76)   # Fm7 again
]
for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Sax: One short motif, let it hang
# F, Ab, C, Eb (Fm7)
sax_notes = [
    (1.5, 77), (1.875, 80), (2.25, 84), (2.625, 87)
]
for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    (3.0, 44), (3.375, 43), (3.75, 45), (4.125, 44)
]
for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: Open voicings
piano_notes = [
    (3.0, 65), (3.0, 68), (3.0, 72), (3.0, 76),  # Gm7
    (3.375, 66), (3.375, 69), (3.375, 73), (3.375, 77),  # Am7
    (3.75, 67), (3.75, 70), (3.75, 74), (3.75, 78),  # Bm7
    (4.125, 64), (4.125, 67), (4.125, 71), (4.125, 76)   # Fm7
]
for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Sax: Repeat motif but leave it hanging
sax_notes = [
    (3.0, 77), (3.375, 80), (3.75, 84), (4.125, 87)
]
for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    (4.5, 45), (4.875, 44), (5.25, 46), (5.625, 45)
]
for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: Open voicings
piano_notes = [
    (4.5, 67), (4.5, 70), (4.5, 74), (4.5, 78),  # Bm7
    (4.875, 68), (4.875, 71), (4.875, 75), (4.875, 79),  # Cm7
    (5.25, 69), (5.25, 72), (5.25, 76), (5.25, 80),  # Dm7
    (5.625, 64), (5.625, 67), (5.625, 71), (5.625, 76)   # Fm7
]
for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Sax: Finish the motif
sax_notes = [
    (4.5, 77), (4.875, 80), (5.25, 84), (5.625, 87)
]
for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
