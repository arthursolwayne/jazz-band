
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
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass - walking line, chromatic approaches
bass_notes = [
    (1.5, 45), (1.875, 44), (2.25, 46), (2.625, 47),
    (3.0, 45), (3.375, 44), (3.75, 46), (4.125, 47)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 71), (1.5, 76),  # F7
    (2.25, 62), (2.25, 67), (2.25, 71), (2.25, 76),  # F7
    (3.0, 62), (3.0, 67), (3.0, 71), (3.0, 76),  # F7
    (3.75, 62), (3.75, 67), (3.75, 71), (3.75, 76)   # F7
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(n)

# Dante on sax - motif, short, suspending
sax_notes = [
    (1.5, 62), (1.5, 66), (1.75, 67), (2.0, 66),
    (2.25, 62), (2.5, 64), (2.75, 66), (3.0, 62)
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus on bass - walking line, chromatic approaches
bass_notes = [
    (3.0, 45), (3.375, 44), (3.75, 46), (4.125, 47),
    (4.5, 45), (4.875, 44), (5.25, 46), (5.625, 47)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    (3.0, 62), (3.0, 67), (3.0, 71), (3.0, 76),  # F7
    (3.75, 62), (3.75, 67), (3.75, 71), (3.75, 76),  # F7
    (4.5, 62), (4.5, 67), (4.5, 71), (4.5, 76),  # F7
    (5.25, 62), (5.25, 67), (5.25, 71), (5.25, 76)   # F7
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(n)

# Dante on sax - motif continuation, leaving it open
sax_notes = [
    (3.0, 62), (3.0, 66), (3.25, 67), (3.5, 66),
    (3.75, 62), (4.0, 64), (4.25, 66), (4.5, 62)
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus on bass - walking line, chromatic approaches
bass_notes = [
    (4.5, 45), (4.875, 44), (5.25, 46), (5.625, 47),
    (6.0, 45), (6.375, 44), (6.75, 46), (7.125, 47)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    (4.5, 62), (4.5, 67), (4.5, 71), (4.5, 76),  # F7
    (5.25, 62), (5.25, 67), (5.25, 71), (5.25, 76),  # F7
    (6.0, 62), (6.0, 67), (6.0, 71), (6.0, 76),  # F7
    (6.75, 62), (6.75, 67), (6.75, 71), (6.75, 76)   # F7
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(n)

# Dante on sax - motif resolution, leaving it hanging
sax_notes = [
    (4.5, 62), (4.5, 66), (4.75, 67), (5.0, 66),
    (5.25, 62), (5.5, 64), (5.75, 66), (6.0, 62)
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
