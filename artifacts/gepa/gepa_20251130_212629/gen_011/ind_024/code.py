
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
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
]

for time, note in drum_notes:
    dr = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=time,
        end=time + 0.125
    )
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F, chromatic approaches
bass_notes = [
    (1.5, 70), (1.875, 69), (2.25, 68), (2.625, 70),
    (3.0, 71), (3.375, 70), (3.75, 69), (4.125, 68),
    (4.5, 70), (4.875, 69), (5.25, 68), (5.625, 70)
]
for time, note in bass_notes:
    n = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=time,
        end=time + 0.25
    )
    bass.notes.append(n)

# Diane: 7th chords, comp on 2 and 4
# Bar 2: F7 on 2 and 4
piano_notes = [
    # Bar 2
    (2.25, 71), (2.25, 74), (2.25, 77), (2.25, 81),
    (2.625, 71), (2.625, 74), (2.625, 77), (2.625, 81),
    # Bar 3
    (3.75, 71), (3.75, 74), (3.75, 77), (3.75, 81),
    (4.125, 71), (4.125, 74), (4.125, 77), (4.125, 81),
    # Bar 4
    (5.25, 71), (5.25, 74), (5.25, 77), (5.25, 81),
    (5.625, 71), (5.625, 74), (5.625, 77), (5.625, 81),
]
for time, note in piano_notes:
    n = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=time,
        end=time + 0.25
    )
    piano.notes.append(n)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 3
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42),
]
for time, note in drum_notes:
    dr = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=time,
        end=time + 0.125
    )
    drums.notes.append(dr)

# Dante: Tenor sax - concise motif with space
sax_notes = [
    # Bar 2
    (1.5, 72), (1.625, 76), (1.75, 74), (1.875, 70),
    # Bar 3
    (2.625, 70), (2.75, 72), (2.875, 76), (3.0, 74),
    # Bar 4
    (3.75, 74), (3.875, 76), (4.0, 72), (4.125, 68),
    # Finish the motif with a rest and return
    (4.5, 72), (4.625, 76), (4.75, 74), (4.875, 70)
]
for time, note in sax_notes:
    n = pretty_midi.Note(
        velocity=110,
        pitch=note,
        start=time,
        end=time + 0.125
    )
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
