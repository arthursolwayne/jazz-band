
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38),
    (0.0, 42), (0.375, 38), (0.75, 42), (1.125, 38), (1.5, 42),
    (0.0, 42), (0.375, 42), (0.75, 42), (1.125, 42), (1.5, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Dm (F, Ab, D, C)
# Bar 2: F, Ab, D, C
# Bar 3: F, Ab, D, C
# Bar 4: F, Ab, D, C
bass_notes = [
    (1.5, 66), (1.875, 70), (2.25, 62), (2.625, 60),
    (3.0, 66), (3.375, 70), (3.75, 62), (4.125, 60),
    (4.5, 66), (4.875, 70), (5.25, 62), (5.625, 60)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords on 2 and 4, Dm7, F7, Bbm7, Ab7
# Bar 2: Dm7 at 2, F7 at 4
# Bar 3: Bbm7 at 2, Ab7 at 4
# Bar 4: Dm7 at 2, F7 at 4
piano_notes = [
    # Dm7 (2.0)
    (2.0, 62), (2.0, 67), (2.0, 72), (2.0, 74),
    # F7 (2.5)
    (2.5, 65), (2.5, 72), (2.5, 77), (2.5, 81),
    # Bbm7 (3.0)
    (3.0, 57), (3.0, 62), (3.0, 67), (3.0, 72),
    # Ab7 (3.5)
    (3.5, 58), (3.5, 63), (3.5, 68), (3.5, 72),
    # Dm7 (4.0)
    (4.0, 62), (4.0, 67), (4.0, 72), (4.0, 74),
    # F7 (4.5)
    (4.5, 65), (4.5, 72), (4.5, 77), (4.5, 81)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42), (3.0, 38),
    (1.5, 42), (1.875, 38), (2.25, 42), (2.625, 38), (3.0, 42),
    (1.5, 42), (1.875, 42), (2.25, 42), (2.625, 42), (3.0, 42),
    # Bar 3
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42), (4.5, 38),
    (3.0, 42), (3.375, 38), (3.75, 42), (4.125, 38), (4.5, 42),
    (3.0, 42), (3.375, 42), (3.75, 42), (4.125, 42), (4.5, 42),
    # Bar 4
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42), (6.0, 38),
    (4.5, 42), (4.875, 38), (5.25, 42), (5.625, 38), (6.0, 42),
    (4.5, 42), (4.875, 42), (5.25, 42), (5.625, 42), (6.0, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor Sax motif (Dm scale, 1 short motif)
# Dm: D, F, G, A, Bb, C, D
# Motif: D, F, G, Bb (1.5s), leave it hanging (2.0s), come back and finish it (4.5s)
sax_notes = [
    (1.5, 62), (1.625, 67), (1.75, 69), (1.875, 64),
    (4.5, 62), (4.625, 67), (4.75, 69), (4.875, 64)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
