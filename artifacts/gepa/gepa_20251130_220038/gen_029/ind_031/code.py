
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
    (0.0, 36, 100),      # Kick on 1
    (0.75, 42, 100),     # Hihat on &1
    (1.0, 38, 100),      # Snare on 2
    (1.75, 42, 100),     # Hihat on &2
    (2.0, 36, 100),      # Kick on 3
    (2.75, 42, 100),     # Hihat on &3
    (3.0, 38, 100),      # Snare on 4
    (3.75, 42, 100)      # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D minor
bass_notes = [
    (1.5, 62, 100), (1.75, 60, 100), (2.0, 63, 100), (2.25, 62, 100),  # Dm7
    (2.5, 65, 100), (2.75, 64, 100), (3.0, 67, 100), (3.25, 65, 100),  # G7
    (3.5, 67, 100), (3.75, 65, 100), (4.0, 68, 100), (4.25, 67, 100),  # Cm7
    (4.5, 71, 100), (4.75, 70, 100), (5.0, 72, 100), (5.25, 71, 100)   # F7
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Diane: Piano comping on 2 and 4 with 7th chords
piano_notes = [
    (2.0, 67, 100), (2.0, 71, 100),  # Dm7 (D, F, A, C)
    (2.0, 74, 100), (2.0, 76, 100),  # Dm7 (D, F, A, C)
    (3.0, 77, 100), (3.0, 81, 100),  # G7 (G, B, D, F)
    (3.0, 84, 100), (3.0, 86, 100),  # G7 (G, B, D, F)
    (4.0, 71, 100), (4.0, 74, 100),  # Cm7 (C, Eb, G, Bb)
    (4.0, 77, 100), (4.0, 79, 100),  # Cm7 (C, Eb, G, Bb)
    (5.0, 76, 100), (5.0, 81, 100),  # F7 (F, A, C, Eb)
    (5.0, 84, 100), (5.0, 86, 100)   # F7 (F, A, C, Eb)
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100), (1.5, 42, 100), (1.75, 42, 100), (2.0, 38, 100),
    (2.0, 42, 100), (2.25, 42, 100), (2.5, 36, 100), (2.75, 42, 100),
    (3.0, 38, 100), (3.0, 42, 100), (3.25, 42, 100), (3.5, 36, 100),
    (3.75, 42, 100), (4.0, 38, 100), (4.0, 42, 100), (4.25, 42, 100),
    (4.5, 36, 100), (4.75, 42, 100), (5.0, 38, 100), (5.0, 42, 100),
    (5.25, 42, 100)
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Dante: Tenor sax melody (bars 2-4)
sax_notes = [
    (2.0, 67, 100), (2.25, 69, 100), (2.5, 67, 100), (2.75, 71, 100),  # D - F - D - G
    (3.0, 69, 100), (3.25, 67, 100), (3.5, 71, 100), (3.75, 69, 100),  # F - D - G - F
    (4.0, 67, 100), (4.25, 71, 100), (4.5, 69, 100), (4.75, 67, 100),  # D - G - F - D
    (5.0, 67, 100), (5.25, 69, 100), (5.5, 67, 100), (5.75, 71, 100)   # D - F - D - G
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
