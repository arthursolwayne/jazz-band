
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    (0.0, 36, 100),     # Kick on beat 1
    (0.75, 42, 100),    # Hihat on beat 2
    (1.5, 38, 100),     # Snare on beat 3
    (2.25, 42, 100),    # Hihat on beat 4
    (3.0, 36, 100),     # Kick on beat 1 of next bar
    (3.75, 42, 100),    # Hihat on beat 2
    (4.5, 38, 100),     # Snare on beat 3
    (5.25, 42, 100)     # Hihat on beat 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus
bass_notes = [
    (1.5, 64, 100),     # Fm root
    (2.0, 65, 100),     # Bb
    (2.5, 67, 100),     # D
    (3.0, 64, 100),     # Fm root
    (3.5, 66, 100),     # Ab
    (4.0, 67, 100),     # D
    (4.5, 64, 100),     # Fm root
    (5.0, 65, 100),     # Bb
    (5.5, 67, 100)      # D
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano - Diane
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 64, 100),     # F7 (F, A, C, E)
    (1.75, 69, 100),
    (2.0, 60, 100),
    (2.25, 66, 100),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 64, 100),
    (3.25, 69, 100),
    (3.5, 60, 100),
    (3.75, 66, 100),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 64, 100),
    (4.75, 69, 100),
    (5.0, 60, 100),
    (5.25, 66, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums - Little Ray
drum_notes = [
    (1.5, 36, 100),     # Kick on beat 1
    (2.25, 38, 100),    # Snare on beat 2
    (3.0, 36, 100),     # Kick on beat 3
    (3.75, 38, 100),    # Snare on beat 4
    (4.5, 36, 100),     # Kick on beat 1
    (5.25, 38, 100),    # Snare on beat 2
    (1.5, 42, 100),     # Hihat on beat 1
    (2.0, 42, 100),     # Hihat on beat 2
    (2.5, 42, 100),     # Hihat on beat 3
    (3.0, 42, 100),     # Hihat on beat 4
    (3.5, 42, 100),     # Hihat on beat 1
    (4.0, 42, 100),     # Hihat on beat 2
    (4.5, 42, 100),     # Hihat on beat 3
    (5.0, 42, 100),     # Hihat on beat 4
    (5.5, 42, 100)      # Hihat on beat 1 of next bar
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax - Dante
# Motif: F (64) -> Ab (67) -> C (69) -> F (64) (suspended, left hanging)
sax_notes = [
    (1.5, 64, 100),     # F
    (1.75, 67, 100),    # Ab
    (2.0, 69, 100),     # C
    (2.25, 64, 100),    # F (suspended)
    (4.5, 64, 100),     # F (return)
    (4.75, 67, 100),    # Ab
    (5.0, 69, 100),     # C
    (5.25, 64, 100)     # F (resolve)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
