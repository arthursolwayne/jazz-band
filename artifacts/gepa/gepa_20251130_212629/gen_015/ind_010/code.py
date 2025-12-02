
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 2: Everybody in (1.5 - 3.0s)
# Marcus (bass) walking line
bass_notes = [
    (1.5, 62), (1.75, 63), (2.0, 64), (2.25, 65),
    (2.5, 65), (2.75, 64), (3.0, 63), (3.25, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane (piano) comping on 2 and 4
piano_notes = [
    (1.75, 71), (1.75, 67), (1.75, 64), (1.75, 62),
    (2.25, 71), (2.25, 67), (2.25, 64), (2.25, 62)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Dante (sax) plays the motif
sax_notes = [
    (1.5, 67), (1.5, 71), (1.75, 72), (2.0, 69),
    (2.25, 67), (2.5, 71), (2.75, 72), (3.0, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: (3.0 - 4.5s)
# Marcus (bass)
bass_notes = [
    (3.0, 62), (3.25, 63), (3.5, 64), (3.75, 65),
    (4.0, 65), (4.25, 64), (4.5, 63), (4.75, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane (piano) comping on 2 and 4
piano_notes = [
    (3.25, 71), (3.25, 67), (3.25, 64), (3.25, 62),
    (3.75, 71), (3.75, 67), (3.75, 64), (3.75, 62)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Little Ray (drums)
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Dante (sax) continues the motif
sax_notes = [
    (3.0, 67), (3.0, 71), (3.25, 72), (3.5, 69),
    (3.75, 67), (4.0, 71), (4.25, 72), (4.5, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: (4.5 - 6.0s)
# Marcus (bass)
bass_notes = [
    (4.5, 62), (4.75, 63), (5.0, 64), (5.25, 65),
    (5.5, 65), (5.75, 64), (6.0, 63), (6.25, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane (piano) comping on 2 and 4
piano_notes = [
    (4.75, 71), (4.75, 67), (4.75, 64), (4.75, 62),
    (5.25, 71), (5.25, 67), (5.25, 64), (5.25, 62)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Little Ray (drums)
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Dante (sax) resolves the motif
sax_notes = [
    (4.5, 67), (4.5, 71), (4.75, 72), (5.0, 69),
    (5.25, 67), (5.5, 71), (5.75, 72), (6.0, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
