
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
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (1.5, 63), (1.875, 62), (2.25, 64), (2.625, 65),
    (3.0, 67), (3.375, 65), (3.75, 64), (4.125, 63),
    (4.5, 62), (4.875, 63), (5.25, 65), (5.625, 67)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 2
    (1.5, 64), (1.5, 69), (1.5, 71), (1.5, 74),
    (2.25, 64), (2.25, 69), (2.25, 71), (2.25, 74),
    # Bar 3
    (3.0, 64), (3.0, 69), (3.0, 71), (3.0, 74),
    (3.75, 64), (3.75, 69), (3.75, 71), (3.75, 74),
    # Bar 4
    (4.5, 64), (4.5, 69), (4.5, 71), (4.5, 74),
    (5.25, 64), (5.25, 69), (5.25, 71), (5.25, 74)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Fm7 -> G7 -> Am7 -> D7 (F, Ab, Bb, C -> G, Bb, D, F -> A, C, E, G -> D, F, A, C)
# 1.5s: F (65), Ab (67), Bb (62), rest
# 2.25s: G (67), Bb (62), D (67), F (65)
# 3.0s: A (69), C (67), E (64), G (67)
# 4.5s: D (67), F (65), A (69), C (67)
sax_notes = [
    (1.5, 65), (1.5, 67), (1.5, 62), (1.5, 0),
    (2.25, 67), (2.25, 62), (2.25, 67), (2.25, 65),
    (3.0, 69), (3.0, 67), (3.0, 64), (3.0, 67),
    (4.5, 67), (4.5, 65), (4.5, 69), (4.5, 67)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42),
    # Bar 3
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 4
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
