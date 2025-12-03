
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (0.0, 36, 100),   # Kick on beat 1
    (0.75, 42, 100),  # Hihat on & of 1
    (1.0, 38, 100),   # Snare on beat 2
    (1.25, 42, 100),  # Hihat on & of 2
    (1.5, 36, 100),   # Kick on beat 3
    (1.75, 42, 100),  # Hihat on & of 3
    (2.0, 38, 100),   # Snare on beat 4
    (2.25, 42, 100),  # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 53, 100),  # F2
    (1.75, 55, 100), # F#2 (chromatic approach)
    (2.0, 57, 100),  # G2
    (2.25, 55, 100), # F#2
    (2.5, 60, 100),  # C3
    (2.75, 58, 100), # Bb3 (chromatic approach)
    (3.0, 62, 100),  # D3

    # Bar 3 (3.0 - 4.5s)
    (3.0, 62, 100),  # D3
    (3.25, 60, 100), # C3
    (3.5, 58, 100),  # Bb3
    (3.75, 57, 100), # G3 (chromatic approach)
    (4.0, 65, 100),  # F4
    (4.25, 63, 100), # Eb4 (chromatic approach)
    (4.5, 67, 100),  # A4

    # Bar 4 (4.5 - 6.0s)
    (4.5, 67, 100),  # A4
    (4.75, 65, 100), # F4
    (5.0, 63, 100),  # Eb4
    (5.25, 62, 100), # D4 (chromatic approach)
    (5.5, 72, 100),  # F5
    (5.75, 69, 100), # D5 (chromatic approach)
    (6.0, 72, 100),  # F5
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Fmaj7
    (1.5, 65, 100),  # F4
    (1.5, 69, 100),  # A4
    (1.5, 71, 100),  # C5
    (1.5, 74, 100),  # E5

    # Bar 3 (3.0 - 4.5s) - Bbm7
    (3.0, 62, 100),  # Bb4
    (3.0, 67, 100),  # D5
    (3.0, 69, 100),  # F5
    (3.0, 72, 100),  # Ab5

    # Bar 4 (4.5 - 6.0s) - D7
    (4.5, 67, 100),  # D5
    (4.5, 72, 100),  # F5
    (4.5, 74, 100),  # A5
    (4.5, 76, 100),  # C6
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 72, 100),  # F5
    (1.75, 76, 100), # A5 (up a 4th)
    (2.0, 72, 100),  # F5

    # Bar 3 (3.0 - 4.5s)
    (3.0, 76, 100),  # A5

    # Bar 4 (4.5 - 6.0s)
    (4.5, 72, 100),  # F5
    (4.75, 76, 100), # A5
    (5.0, 72, 100),  # F5
    (5.25, 76, 100), # A5
    (5.5, 72, 100),  # F5
    (5.75, 76, 100), # A5
    (6.0, 72, 100),  # F5
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Bar 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 36, 100),   # Kick on beat 1
    (1.75, 42, 100),  # Hihat on & of 1
    (2.0, 38, 100),   # Snare on beat 2
    (2.25, 42, 100),  # Hihat on & of 2
    (2.5, 36, 100),   # Kick on beat 3
    (2.75, 42, 100),  # Hihat on & of 3
    (3.0, 38, 100),   # Snare on beat 4
    (3.25, 42, 100),  # Hihat on & of 4

    # Bar 3 (3.0 - 4.5s)
    (3.0, 36, 100),   # Kick on beat 1
    (3.25, 42, 100),  # Hihat on & of 1
    (3.5, 38, 100),   # Snare on beat 2
    (3.75, 42, 100),  # Hihat on & of 2
    (4.0, 36, 100),   # Kick on beat 3
    (4.25, 42, 100),  # Hihat on & of 3
    (4.5, 38, 100),   # Snare on beat 4
    (4.75, 42, 100),  # Hihat on & of 4

    # Bar 4 (4.5 - 6.0s)
    (4.5, 36, 100),   # Kick on beat 1
    (4.75, 42, 100),  # Hihat on & of 1
    (5.0, 38, 100),   # Snare on beat 2
    (5.25, 42, 100),  # Hihat on & of 2
    (5.5, 36, 100),   # Kick on beat 3
    (5.75, 42, 100),  # Hihat on & of 3
    (6.0, 38, 100),   # Snare on beat 4
    (6.25, 42, 100),  # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
