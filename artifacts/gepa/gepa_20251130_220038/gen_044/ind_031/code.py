
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38),
    (1.875, 42), (2.25, 38), (2.625, 42), (3.0, 36), (3.375, 42),
    (3.75, 36), (4.125, 42), (4.5, 38), (4.875, 42), (5.25, 38),
    (5.625, 42), (6.0, 36)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus - walking line in Dm, chromatic approaches
bass_notes = [
    (1.5, 62), (1.875, 60), (2.25, 62), (2.625, 64), (3.0, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane - 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 70), (1.5, 72),
    (2.25, 60), (2.25, 65), (2.25, 68), (2.25, 70),
    (3.0, 62), (3.0, 67), (3.0, 70), (3.0, 72)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Dante - sax melody (start with a whisper, build into a cry)
sax_notes = [
    (1.5, 62), (1.875, 65), (2.25, 67), (2.625, 69),
    (3.0, 67), (3.375, 65), (3.75, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus - walking line in Dm, chromatic approaches
bass_notes = [
    (3.0, 62), (3.375, 60), (3.75, 62), (4.125, 64), (4.5, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane - 7th chords, comp on 2 and 4
piano_notes = [
    (3.0, 62), (3.0, 67), (3.0, 70), (3.0, 72),
    (3.75, 60), (3.75, 65), (3.75, 68), (3.75, 70),
    (4.5, 62), (4.5, 67), (4.5, 70), (4.5, 72)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Dante - sax melody (build naturally)
sax_notes = [
    (3.0, 67), (3.375, 69), (3.75, 71), (4.125, 72),
    (4.5, 70), (4.875, 68), (5.25, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus - walking line in Dm, chromatic approaches
bass_notes = [
    (4.5, 62), (4.875, 60), (5.25, 62), (5.625, 64), (6.0, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane - 7th chords, comp on 2 and 4
piano_notes = [
    (4.5, 62), (4.5, 67), (4.5, 70), (4.5, 72),
    (5.25, 60), (5.25, 65), (5.25, 68), (5.25, 70),
    (6.0, 62), (6.0, 67), (6.0, 70), (6.0, 72)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Dante - sax melody (end with a cry)
sax_notes = [
    (4.5, 69), (4.875, 71), (5.25, 72), (5.625, 71),
    (6.0, 69), (6.375, 67), (6.75, 65)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42), (6.0, 38),
    (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
