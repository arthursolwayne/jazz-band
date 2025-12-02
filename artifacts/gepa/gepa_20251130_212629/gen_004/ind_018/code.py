
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100), # Kick on 1
    (0.75, 42, 100), # Hihat on 2
    (1.125, 38, 100), # Snare on 3
    (1.5, 42, 100) # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2: Fm7 -> Bb -> C -> Eb
    (1.5, 53, 100), # F
    (1.875, 51, 100), # Eb
    (2.25, 52, 100), # E
    (2.625, 53, 100), # F

    # Bar 3: Fm7 -> Bb -> C -> Eb
    (3.0, 51, 100), # Eb
    (3.375, 50, 100), # D
    (3.75, 51, 100), # Eb
    (4.125, 53, 100), # F

    # Bar 4: Fm7 -> Bb -> C -> Eb
    (4.5, 53, 100), # F
    (4.875, 51, 100), # Eb
    (5.25, 52, 100), # E
    (5.625, 53, 100) # F
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 64, 100), # Bb
    (1.875, 69, 100), # D
    (1.875, 67, 100), # C
    (1.875, 71, 100), # F

    (2.625, 64, 100), # Bb
    (2.625, 69, 100), # D
    (2.625, 67, 100), # C
    (2.625, 71, 100), # F

    # Bar 3
    (3.375, 64, 100), # Bb
    (3.375, 69, 100), # D
    (3.375, 67, 100), # C
    (3.375, 71, 100), # F

    (4.125, 64, 100), # Bb
    (4.125, 69, 100), # D
    (4.125, 67, 100), # C
    (4.125, 71, 100), # F

    # Bar 4
    (4.875, 64, 100), # Bb
    (4.875, 69, 100), # D
    (4.875, 67, 100), # C
    (4.875, 71, 100), # F

    (5.625, 64, 100), # Bb
    (5.625, 69, 100), # D
    (5.625, 67, 100), # C
    (5.625, 71, 100), # F
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36, 100), # Kick on 1
    (1.875, 42, 100), # Hihat on 2
    (2.25, 38, 100), # Snare on 3
    (2.625, 42, 100), # Hihat on 4

    # Bar 3
    (3.0, 36, 100), # Kick on 1
    (3.375, 42, 100), # Hihat on 2
    (3.75, 38, 100), # Snare on 3
    (4.125, 42, 100), # Hihat on 4

    # Bar 4
    (4.5, 36, 100), # Kick on 1
    (4.875, 42, 100), # Hihat on 2
    (5.25, 38, 100), # Snare on 3
    (5.625, 42, 100) # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 64, 100), # G (Fm scale)
    (1.875, 62, 100), # E
    (2.25, 65, 100), # Ab
    (2.625, 64, 100), # G

    (3.0, 62, 100), # E
    (3.375, 64, 100), # G
    (3.75, 67, 100), # Bb
    (4.125, 64, 100), # G

    (4.5, 62, 100), # E
    (4.875, 64, 100), # G
    (5.25, 65, 100), # Ab
    (5.625, 64, 100) # G
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
