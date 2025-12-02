
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
    (0.0, 36, 100),    # Kick on 1
    (0.75, 42, 100),   # Hihat on 2
    (1.125, 38, 100),  # Snare on 3
    (1.5, 42, 100)     # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (walking line, chromatic approaches)
bass_notes = [
    (1.5, 54, 100),    # Fm7 - F
    (1.75, 53, 100),   # Eb (chromatic approach)
    (2.0, 55, 100),    # G (Fm7)
    (2.25, 56, 100),   # Ab (chromatic approach)
    (2.5, 55, 100),    # G (Fm7)
    (2.75, 54, 100),   # F (Fm7)
    (3.0, 53, 100),    # Eb (chromatic approach)
    (3.25, 55, 100),   # G (Fm7)
    (3.5, 54, 100),    # F (Fm7)
    (3.75, 53, 100),   # Eb (chromatic approach)
    (4.0, 55, 100),    # G (Fm7)
    (4.25, 56, 100),   # Ab (chromatic approach)
    (4.5, 55, 100),    # G (Fm7)
    (4.75, 54, 100),   # F (Fm7)
    (5.0, 53, 100),    # Eb (chromatic approach)
    (5.25, 55, 100),   # G (Fm7)
    (5.5, 54, 100),    # F (Fm7)
    (5.75, 53, 100)    # Eb (chromatic approach)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane on piano (7th chords, comp on 2 and 4)
piano_notes = [
    (1.5, 64, 100),    # Fm7 (F, Ab, C, Eb)
    (1.75, 62, 100),
    (1.75, 67, 100),
    (1.75, 60, 100),
    (2.25, 62, 100),   # Fm7
    (2.25, 67, 100),
    (2.25, 60, 100),
    (3.0, 64, 100),    # Fm7
    (3.25, 62, 100),
    (3.25, 67, 100),
    (3.25, 60, 100),
    (3.75, 62, 100),   # Fm7
    (3.75, 67, 100),
    (3.75, 60, 100),
    (4.5, 64, 100),    # Fm7
    (4.75, 62, 100),
    (4.75, 67, 100),
    (4.75, 60, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Little Ray on drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    (1.5, 36, 100),    # Kick on 1
    (1.75, 38, 100),   # Snare on 2
    (1.875, 42, 100),  # Hihat on 2.5
    (2.0, 36, 100),    # Kick on 3
    (2.25, 38, 100),   # Snare on 4
    (2.375, 42, 100),  # Hihat on 4.5
    (2.5, 36, 100),    # Kick on 1
    (2.75, 38, 100),   # Snare on 2
    (2.875, 42, 100),  # Hihat on 2.5
    (3.0, 36, 100),    # Kick on 3
    (3.25, 38, 100),   # Snare on 4
    (3.375, 42, 100),  # Hihat on 4.5
    (3.5, 36, 100),    # Kick on 1
    (3.75, 38, 100),   # Snare on 2
    (3.875, 42, 100),  # Hihat on 2.5
    (4.0, 36, 100),    # Kick on 3
    (4.25, 38, 100),   # Snare on 4
    (4.375, 42, 100),  # Hihat on 4.5
    (4.5, 36, 100),    # Kick on 1
    (4.75, 38, 100),   # Snare on 2
    (4.875, 42, 100),  # Hihat on 2.5
    (5.0, 36, 100),    # Kick on 3
    (5.25, 38, 100),   # Snare on 4
    (5.375, 42, 100),  # Hihat on 4.5
    (5.5, 36, 100),    # Kick on 1
    (5.75, 38, 100),   # Snare on 2
    (5.875, 42, 100),  # Hihat on 2.5
    (6.0, 36, 100),    # Kick on 3
    (6.25, 38, 100),   # Snare on 4
    (6.375, 42, 100)   # Hihat on 4.5
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Dante on tenor (one short motif, make it sing)
sax_notes = [
    (1.5, 71, 100),    # G (Fm7)
    (1.625, 74, 100),  # Bb (chromatic approach)
    (1.75, 72, 100),   # A (Fm7)
    (2.0, 71, 100),    # G (Fm7)
    (2.125, 74, 100),  # Bb (chromatic approach)
    (2.25, 72, 100),   # A (Fm7)
    (2.5, 71, 100),    # G (Fm7)
    (2.625, 74, 100),  # Bb (chromatic approach)
    (2.75, 72, 100),   # A (Fm7)
    (3.0, 71, 100),    # G (Fm7)
    (3.125, 74, 100),  # Bb (chromatic approach)
    (3.25, 72, 100),   # A (Fm7)
    (3.5, 71, 100),    # G (Fm7)
    (3.625, 74, 100),  # Bb (chromatic approach)
    (3.75, 72, 100),   # A (Fm7)
    (4.0, 71, 100),    # G (Fm7)
    (4.125, 74, 100),  # Bb (chromatic approach)
    (4.25, 72, 100),   # A (Fm7)
    (4.5, 71, 100),    # G (Fm7)
    (4.625, 74, 100),  # Bb (chromatic approach)
    (4.75, 72, 100),   # A (Fm7)
    (5.0, 71, 100),    # G (Fm7)
    (5.125, 74, 100),  # Bb (chromatic approach)
    (5.25, 72, 100),   # A (Fm7)
    (5.5, 71, 100),    # G (Fm7)
    (5.625, 74, 100),  # Bb (chromatic approach)
    (5.75, 72, 100),   # A (Fm7)
    (6.0, 71, 100)     # G (Fm7)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
