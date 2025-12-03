
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
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 100),  # Hihat
    (0.75, 38, 100),  # Snare on 2
    (1.125, 42, 100),  # Hihat
    (1.5, 36, 100),  # Kick on 3
    (1.875, 42, 100),  # Hihat
    (2.25, 38, 100),  # Snare on 4
    (2.625, 42, 100),  # Hihat
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, roots and fifths with chromatic approaches
# F7 -> Bb7 -> Cm7 -> D7
# Roots: F, Bb, C, D
# Fifths: C, F, G, A
# Chromatic approaches: Eb (to F), A (to Bb), B (to C), C# (to D)

bass_notes = [
    (1.5, 70, 70),  # F (C4)
    (1.875, 68, 70),  # Eb (F#4)
    (2.25, 72, 70),  # C (G4)
    (2.625, 71, 70),  # Bb (A4)
    (3.0, 76, 70),  # Bb (Bb4)
    (3.375, 74, 70),  # A (B4)
    (3.75, 77, 70),  # C (C5)
    (4.125, 76, 70),  # B (B4)
    (4.5, 79, 70),  # D (D5)
    (4.875, 81, 70),  # C# (E5)
    (5.25, 82, 70),  # D (F5)
    (5.625, 84, 70),  # E (G5)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Cm7 (C, Eb, G, Bb)
# Bar 5: D7 (D, F#, A, C)

piano_notes = [
    # Bar 2
    (1.5, 76, 100),  # F (F4)
    (1.5, 82, 100),  # A (A4)
    (1.5, 78, 100),  # C (C5)
    (1.5, 83, 100),  # E (E5)
    # Bar 3
    (2.25, 81, 100),  # Bb (Bb4)
    (2.25, 86, 100),  # D (D5)
    (2.25, 78, 100),  # F (F5)
    (2.25, 85, 100),  # Ab (Ab5)
    # Bar 4
    (3.0, 76, 100),  # C (C4)
    (3.0, 80, 100),  # Eb (Eb4)
    (3.0, 79, 100),  # G (G4)
    (3.0, 82, 100),  # Bb (Bb4)
    # Bar 5
    (3.75, 79, 100),  # D (D4)
    (3.75, 83, 100),  # F# (F#4)
    (3.75, 81, 100),  # A (A4)
    (3.75, 78, 100),  # C (C5)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: Motif - Haunting, incomplete, singable
# Start the motif, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    (1.5, 76, 100),  # F (F5)
    (1.75, 83, 100),  # E (E5)
    (2.0, 82, 100),  # D (D5)
    (2.25, 82, 100),  # D (D5)
    # Bar 3
    (3.0, 79, 100),  # C (C5)
    (3.25, 83, 100),  # E (E5)
    (3.5, 82, 100),  # D (D5)
    (3.75, 82, 100),  # D (D5)
    # Bar 4
    (4.5, 76, 100),  # F (F5)
    (4.75, 83, 100),  # E (E5)
    (5.0, 82, 100),  # D (D5)
    (5.25, 82, 100),  # D (D5)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.875, 42, 100),  # Hihat
    (2.25, 38, 100),  # Snare on 2
    (2.625, 42, 100),  # Hihat
    (3.0, 36, 100),  # Kick on 3
    (3.375, 42, 100),  # Hihat
    (3.75, 38, 100),  # Snare on 4
    (4.125, 42, 100),  # Hihat
    (4.5, 36, 100),  # Kick on 1
    (4.875, 42, 100),  # Hihat
    (5.25, 38, 100),  # Snare on 2
    (5.625, 42, 100),  # Hihat
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
