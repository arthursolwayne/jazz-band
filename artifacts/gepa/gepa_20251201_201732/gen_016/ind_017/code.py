
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
    (0.375, 42, 80), # Hihat on &1
    (0.75, 42, 80),  # Hihat on &2
    (1.125, 38, 100),# Snare on 2
    (1.5, 36, 100),  # Kick on 3
    (1.875, 42, 80), # Hihat on &3
    (2.25, 42, 80),  # Hihat on &4
    (2.625, 38, 100) # Snare on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS (Marcus): Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 77, 80),  # F2 (root)
    (1.875, 80, 80), # F#2 (chromatic approach)
    (2.25, 79, 80),  # G2 (fifth of C)
    (2.625, 77, 80), # F2 (root)
    (3.0, 80, 80),   # F#2
    (3.375, 82, 80), # A2 (fifth of D)
    (3.75, 80, 80),  # F#2
    (4.125, 77, 80), # F2
    (4.5, 82, 80),   # A2
    (4.875, 84, 80), # B2 (chromatic approach)
    (5.25, 83, 80),  # Bb2 (fifth of F)
    (5.625, 77, 80)  # F2 (root)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# PIANO (Diane): Open voicings, different chords each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    (1.5, 77, 95), (1.5, 82, 95), (1.5, 79, 95), (1.5, 84, 95), # Fmaj7
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (2.25, 72, 95), (2.25, 76, 95), (2.25, 77, 95), (2.25, 71, 95), # Bb7
    # Bar 4: Gm7 (G, Bb, D, F)
    (3.0, 82, 95), (3.0, 77, 95), (3.0, 80, 95), (3.0, 79, 95) # Gm7
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# SAX (You): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 82, 90),  # G (bar 2, 1)
    (1.75, 89, 85),  # A (bar 2, &2)
    (2.0, 82, 90),   # G (bar 2, 3)
    (2.25, 89, 85),  # A (bar 2, &3)
    (3.0, 82, 90),   # G (bar 3, 1)
    (3.25, 89, 85),  # A (bar 3, &2)
    (3.5, 82, 90),   # G (bar 3, 3)
    (3.75, 89, 85),  # A (bar 3, &3)
    (4.5, 82, 90),   # G (bar 4, 1)
    (4.75, 89, 85),  # A (bar 4, &2)
    (5.0, 82, 90),   # G (bar 4, 3)
    (5.25, 89, 85)   # A (bar 4, &3)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36, 100), (1.875, 42, 80), (2.25, 42, 80), (2.625, 38, 100),
    # Bar 3
    (3.0, 36, 100), (3.375, 42, 80), (3.75, 42, 80), (4.125, 38, 100),
    # Bar 4
    (4.5, 36, 100), (4.875, 42, 80), (5.25, 42, 80), (5.625, 38, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
