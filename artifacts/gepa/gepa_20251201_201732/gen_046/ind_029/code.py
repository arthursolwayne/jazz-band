
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
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (root), F2 (fifth), chromatic approach to C2 (b9)
bass_notes = [
    (1.5, 38), (1.875, 37), (2.25, 38), (2.625, 39)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: Open voicing, Dm7b5 on bar 2, Gm7 on bar 3, F7 on bar 4
# Bar 2: Dm7b5 (D, F, Ab, C)
piano_notes = [
    (1.5, 62), (1.5, 65), (1.5, 67), (1.5, 69),
    (2.25, 67), (2.25, 70), (2.25, 72), (2.25, 76),
    (3.0, 74), (3.0, 77), (3.0, 79), (3.0, 81)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: Motif starts, hangs, returns later
sax_notes = [
    (1.5, 62), (1.5, 65), (1.5, 67), (1.5, 65),
    (2.25, 65), (2.25, 67), (2.25, 65), (2.25, 62),
    (3.0, 62), (3.0, 65), (3.0, 67), (3.0, 65)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G (fifth), Bb (chromatic), C (root), D (fifth)
bass_notes = [
    (3.0, 43), (3.375, 44), (3.75, 46), (4.125, 48)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: Gm7 (G, Bb, D, F)
piano_notes = [
    (3.0, 71), (3.0, 74), (3.0, 76), (3.0, 78),
    (3.75, 71), (3.75, 74), (3.75, 76), (3.75, 78),
    (4.5, 71), (4.5, 74), (4.5, 76), (4.5, 78)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: Motif continues, resolves on the last note
sax_notes = [
    (3.0, 62), (3.0, 65), (3.0, 67), (3.0, 62),
    (3.75, 67), (3.75, 65), (3.75, 62), (3.75, 60),
    (4.5, 62), (4.5, 65), (4.5, 67), (4.5, 65)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F (root), G (chromatic), A (fifth), Bb (chromatic)
bass_notes = [
    (4.5, 53), (4.875, 54), (5.25, 56), (5.625, 57)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: F7 (F, A, C, E)
piano_notes = [
    (4.5, 77), (4.5, 80), (4.5, 82), (4.5, 84),
    (5.25, 77), (5.25, 80), (5.25, 82), (5.25, 84),
    (6.0, 77), (6.0, 80), (6.0, 82), (6.0, 84)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: Motif returns, but only the first note
sax_notes = [
    (4.5, 62), (4.5, 65), (4.5, 67), (4.5, 62),
    (5.25, 65), (5.25, 67), (5.25, 65), (5.25, 62),
    (6.0, 62), (6.0, 65), (6.0, 67), (6.0, 65)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
