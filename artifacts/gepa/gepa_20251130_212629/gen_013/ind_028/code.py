
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line (walking line, chromatic approaches)
bass_notes = [
    (1.5, 62), (1.875, 61), (2.25, 63), (2.625, 64),
    (3.0, 65), (3.375, 64), (3.75, 63), (4.125, 62),
    (4.5, 61), (4.875, 60), (5.25, 62), (5.625, 64)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Diane - Piano (7th chords, comp on 2 and 4)
piano_notes = [
    (2.25, 62), (2.25, 67), (2.25, 71), (2.25, 74),  # D7
    (3.75, 62), (3.75, 67), (3.75, 71), (3.75, 74),  # D7
    (5.25, 64), (5.25, 69), (5.25, 73), (5.25, 76)   # F#7
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Little Ray - Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    (1.5, 36), (1.875, 38), (2.25, 36), (2.625, 38),
    (3.0, 36), (3.375, 38), (3.75, 36), (4.125, 38),
    (4.5, 36), (4.875, 38), (5.25, 36), (5.625, 38)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(dr)

# Dante - Sax (short motif, one phrase, leave it hanging)
sax_notes = [
    (1.5, 62), (1.75, 64), (2.0, 62), (2.25, 60),  # D G D Bb
    (2.5, 62), (2.75, 64), (3.0, 62), (3.25, 60),  # D G D Bb
    (3.5, 62), (3.75, 64), (4.0, 62), (4.25, 60),  # D G D Bb
    (4.5, 62), (4.75, 64), (5.0, 62), (5.25, 60),  # D G D Bb
    (5.5, 62), (5.75, 64), (6.0, 62)              # D G D (end on D)
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
