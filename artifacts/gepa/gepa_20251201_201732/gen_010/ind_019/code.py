
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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on 2
    (1.125, 38, 100),# Snare on 3
    (1.5, 42, 100)   # Hihat on 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D - F - Eb - D
    (1.5, 38, 100),  # D2
    (1.875, 43, 100), # F2
    (2.25, 41, 100),  # Eb2
    (2.625, 38, 100), # D2

    # Bar 3: C - D - Bb - C
    (3.0, 40, 100),  # C2
    (3.375, 38, 100), # D2
    (3.75, 37, 100),  # Bb2
    (4.125, 40, 100), # C2

    # Bar 4: D - F - Eb - D
    (4.5, 38, 100),  # D2
    (4.875, 43, 100), # F2
    (5.25, 41, 100),  # Eb2
    (5.625, 38, 100)  # D2
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Diane: Open voicings, resolve on the last beat of each bar
piano_notes = [
    # Bar 2: Dm7 - Gm7
    (1.5, 62, 100), (1.5, 67, 100), (1.5, 69, 100), (1.5, 71, 100),  # Dm7
    (2.25, 67, 100), (2.25, 72, 100), (2.25, 74, 100), (2.25, 76, 100), # Gm7

    # Bar 3: Cm7 - Fm7
    (3.0, 60, 100), (3.0, 65, 100), (3.0, 67, 100), (3.0, 69, 100),  # Cm7
    (3.75, 65, 100), (3.75, 70, 100), (3.75, 72, 100), (3.75, 74, 100), # Fm7

    # Bar 4: Dm7 - G7
    (4.5, 62, 100), (4.5, 67, 100), (4.5, 69, 100), (4.5, 71, 100),  # Dm7
    (5.25, 67, 100), (5.25, 72, 100), (5.25, 74, 100), (5.25, 76, 100) # G7
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36, 100), (1.875, 42, 100), (2.25, 38, 100), (2.625, 42, 100),
    # Bar 3
    (3.0, 36, 100), (3.375, 42, 100), (3.75, 38, 100), (4.125, 42, 100),
    # Bar 4
    (4.5, 36, 100), (4.875, 42, 100), (5.25, 38, 100), (5.625, 42, 100)
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C, D
sax_notes = [
    # Bar 2
    (1.5, 62, 100),            # D4
    (1.75, 64, 100),           # Eb4
    (2.0, 66, 100),            # F4
    (2.25, 69, 100),           # G4

    # Bar 3
    (3.0, 69, 100),            # G4
    (3.25, 71, 100),           # A4
    (3.5, 69, 100),            # G4
    (3.75, 71, 100),           # A4

    # Bar 4
    (4.5, 62, 100),            # D4
    (4.75, 64, 100),           # Eb4
    (5.0, 66, 100),            # F4
    (5.25, 69, 100)            # G4
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
