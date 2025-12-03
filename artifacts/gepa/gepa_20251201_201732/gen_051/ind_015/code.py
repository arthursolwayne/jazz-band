
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 90), # Hihat
    (0.75, 42, 90),
    (1.125, 42, 90),
    (1.5, 38, 100),  # Snare on 2
    (1.875, 42, 90),
    (2.25, 42, 90),
    (2.625, 42, 90),
    (3.0, 36, 100),  # Kick on 3
    (3.375, 42, 90),
    (3.75, 42, 90),
    (4.125, 42, 90),
    (4.5, 38, 100),  # Snare on 4
    (4.875, 42, 90),
    (5.25, 42, 90),
    (5.625, 42, 90),
]

for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Fm (F, Ab, D, Eb)
# Roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 70, 80),  # F2 (root)
    (1.875, 68, 80), # Eb (chromatic approach)
    (2.25, 67, 80),  # D2 (fifth)
    (2.625, 69, 80), # Eb (chromatic approach)
    (3.0, 70, 80),   # F2 (root)
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (1.5, 71, 100), # F4
    (1.5, 77, 100), # Ab4
    (1.5, 76, 100), # C4
    (1.5, 78, 100), # D4

    # Bar 3: Bb7 (Bb, D, F, Ab)
    (2.25, 73, 100), # Bb4
    (2.25, 76, 100), # D4
    (2.25, 71, 100), # F4
    (2.25, 77, 100), # Ab4

    # Bar 4: D7 (D, F#, A, C)
    (3.0, 76, 100), # D4
    (3.0, 81, 100), # F#4
    (3.0, 78, 100), # A4
    (3.0, 76, 100), # C4 (resolve on D)
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0)
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.875, 42, 90), # Hihat
    (2.25, 42, 90),
    (2.625, 42, 90),
    (3.0, 38, 100),  # Snare on 2
    (3.375, 42, 90),
    (3.75, 42, 90),
    (4.125, 42, 90),
    (4.5, 36, 100),  # Kick on 3
    (4.875, 42, 90),
    (5.25, 42, 90),
    (5.625, 42, 90),
    (6.0, 38, 100),  # Snare on 4
    (6.375, 42, 90),
    (6.75, 42, 90),
    (7.125, 42, 90),
]

for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Dante's sax solo (Bar 2-4)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, Db
# Melody: F, Ab, A, Bb, rest, F, Ab, rest, A, Bb

sax_notes = [
    (1.5, 71, 100), # F4
    (1.75, 77, 100), # Ab4
    (2.0, 78, 100), # A4
    (2.25, 76, 100), # Bb4
    (2.5, 71, 100), # F4
    (2.75, 77, 100), # Ab4
    (3.0, 78, 100), # A4
    (3.25, 76, 100), # Bb4
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
