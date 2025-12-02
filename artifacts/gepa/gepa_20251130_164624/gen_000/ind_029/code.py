
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
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[1], start=note[0], end=note[0] + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 59), (1.875, 60), (2.25, 61), (2.625, 62),  # Dm7 walking
    (3.0, 60), (3.375, 61), (3.75, 62), (4.125, 63),  # Cm7 walking
    # Bar 3 (3.0 - 4.5s)
    (4.5, 63), (4.875, 64), (5.25, 62), (5.625, 60),  # Bb7 walking
    (6.0, 60), (6.375, 61), (6.75, 62), (7.125, 63),  # Cm7 walking
    # Bar 4 (4.5 - 6.0s)
    (7.5, 63), (7.875, 64), (8.25, 62), (8.625, 60),  # Bb7 walking
    (9.0, 60), (9.375, 61), (9.75, 62), (10.125, 63)  # Cm7 walking
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[1], start=note[0], end=note[0] + 0.1875))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62), (1.5, 67), (1.5, 69), (1.5, 71),  # Dm7
    (2.0, 62), (2.0, 67), (2.0, 69), (2.0, 71),  # Dm7
    (2.5, 60), (2.5, 65), (2.5, 67), (2.5, 69),  # Cm7
    (3.0, 62), (3.0, 67), (3.0, 69), (3.0, 71),  # Dm7
    # Bar 3 (3.0 - 4.5s)
    (3.5, 62), (3.5, 67), (3.5, 69), (3.5, 71),  # Dm7
    (4.0, 62), (4.0, 67), (4.0, 69), (4.0, 71),  # Dm7
    (4.5, 59), (4.5, 64), (4.5, 66), (4.5, 69),  # Bb7
    (5.0, 62), (5.0, 67), (5.0, 69), (5.0, 71),  # Dm7
    # Bar 4 (4.5 - 6.0s)
    (5.5, 62), (5.5, 67), (5.5, 69), (5.5, 71),  # Dm7
    (6.0, 62), (6.0, 67), (6.0, 69), (6.0, 71),  # Dm7
    (6.5, 59), (6.5, 64), (6.5, 66), (6.5, 69),  # Bb7
    (7.0, 62), (7.0, 67), (7.0, 69), (7.0, 71)   # Dm7
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[1], start=note[0], end=note[0] + 0.1875))

# Little Ray on drums: Keep the same pattern from Bar 1 but continue for the full 4 bars
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42),
    # Bar 3 (3.0 - 4.5s)
    (7.5, 36), (7.875, 42), (8.25, 36), (8.625, 42),
    (9.0, 38), (9.375, 42), (9.75, 38), (10.125, 42),
    # Bar 4 (4.5 - 6.0s)
    (10.5, 36), (10.875, 42), (11.25, 36), (11.625, 42),
    (12.0, 38), (12.375, 42), (12.75, 38), (13.125, 42)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[1], start=note[0], end=note[0] + 0.1875))

# Dante on tenor sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62), (1.75, 65), (1.95, 67), (2.1, 67),  # D to F to G, rest on G
    # Bar 3 (3.0 - 4.5s)
    (3.0, 67), (3.25, 65), (3.45, 62), (3.6, 62),  # G to F to D, rest on D
    # Bar 4 (4.5 - 6.0s)
    (4.5, 62), (4.75, 65), (4.95, 67), (5.1, 67),  # D to F to G, rest on G
    (5.3, 65), (5.5, 62), (5.7, 60), (5.9, 59)     # F to D to C to Bb, resolving
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[1], start=note[0], end=note[0] + 0.1))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
