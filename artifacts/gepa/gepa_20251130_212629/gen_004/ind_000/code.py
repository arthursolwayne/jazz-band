
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F, chromatic approaches
bass_notes = [
    (1.5, 69), (1.875, 67), (2.25, 68), (2.625, 71),
    (3.0, 72), (3.375, 71), (3.75, 70), (4.125, 69),
    (4.5, 68), (4.875, 67), (5.25, 69), (5.625, 71)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords, comp on 2 and 4
# F7, A7, D7, G7
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    (1.875, 65), (1.875, 69), (1.875, 60), (1.875, 64),
    # Bar 3: A7 (A, C#, E, G)
    (3.375, 69), (3.375, 71), (3.375, 67), (3.375, 70),
    # Bar 4: D7 (D, F#, A, C)
    (4.875, 62), (4.875, 67), (4.875, 69), (4.875, 60)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Dante: Tenor sax motif
# Start with a short motif: F, A, Bb, C
# Then leave it hanging on Bb
sax_notes = [
    (1.5, 65), (1.5 + 0.375, 69), (1.5 + 0.75, 67), (1.5 + 1.125, 60),
    (1.5 + 1.5, 67), (1.5 + 1.875, 67), (1.5 + 2.25, 67), (1.5 + 2.625, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
