
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line, chromatic approach to Fm7
bass_notes = [
    (1.5, 37), (1.875, 38), (2.25, 39), (2.625, 40),
    (3.0, 40), (3.375, 39), (3.75, 38), (4.125, 37),
    (4.5, 37), (4.875, 38), (5.25, 39), (5.625, 40)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: Comping with 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    (2.0, 64), (2.0, 67), (2.0, 69), (2.0, 71),
    # Bar 3: Fm7 on beat 2
    (3.5, 64), (3.5, 67), (3.5, 69), (3.5, 71),
    # Bar 4: Fm7 on beat 2
    (5.0, 64), (5.0, 67), (5.0, 69), (5.0, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 3
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Saxophone motif: Fm7 (F, Ab, Bb, Db) -> Bb7 (Bb, D, F, Ab) -> Fm7 -> resolution to D7
# Start on bar 2, beat 1 (1.5s)
sax_notes = [
    # Bar 2: Fm7
    (1.5, 66), (1.5, 69), (1.5, 71), (1.5, 72),
    # Bar 3: Bb7
    (3.0, 71), (3.0, 74), (3.0, 76), (3.0, 77),
    # Bar 4: Fm7
    (4.5, 66), (4.5, 69), (4.5, 71), (4.5, 72),
    # Bar 4: Resolution to D7 (D, F#, A, C)
    (5.25, 62), (5.25, 67), (5.25, 72), (5.25, 74)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter_intro.mid")
