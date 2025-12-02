
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

# Drums - Bar 1 (0.0 - 1.5s)
drum_notes = [
    (0.0, 36, 100),  # Kick on beat 1
    (0.5, 42, 100),  # Hihat on beat 2
    (1.0, 38, 100),  # Snare on beat 3
    (1.5, 42, 100),  # Hihat on beat 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax - Bar 2 (1.5 - 3.0s)
sax_notes = [
    (1.5, 62, 100),  # D5
    (1.625, 65, 100),  # F#5
    (1.75, 67, 100),  # A5
    (2.125, 62, 100),  # D5 (rest for 0.375s)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Bass - Bar 2 (1.5 - 3.0s)
bass_notes = [
    (1.5, 45, 100),  # D3
    (1.875, 47, 100),  # F#3
    (2.25, 49, 100),  # A3
    (2.625, 45, 100),  # D3
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Piano - Bar 2 (1.5 - 3.0s)
piano_notes = [
    (1.5, 62, 100),  # D5 (7th chord)
    (1.5, 67, 100),  # A5
    (1.5, 64, 100),  # F5
    (1.5, 69, 100),  # C6
    (2.0, 62, 100),  # D5
    (2.0, 67, 100),  # A5
    (2.0, 64, 100),  # F5
    (2.0, 69, 100),  # C6
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Drums - Bar 2 (1.5 - 3.0s)
drum_notes = [
    (1.5, 36, 100),  # Kick on beat 1
    (2.0, 38, 100),  # Snare on beat 2
    (2.5, 36, 100),  # Kick on beat 3
    (3.0, 38, 100),  # Snare on beat 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax - Bar 3 (3.0 - 4.5s)
sax_notes = [
    (3.0, 62, 100),  # D5
    (3.125, 65, 100),  # F#5
    (3.25, 67, 100),  # A5
    (3.625, 62, 100),  # D5 (rest for 0.375s)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Bass - Bar 3 (3.0 - 4.5s)
bass_notes = [
    (3.0, 45, 100),  # D3
    (3.375, 47, 100),  # F#3
    (3.75, 49, 100),  # A3
    (4.125, 45, 100),  # D3
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Piano - Bar 3 (3.0 - 4.5s)
piano_notes = [
    (3.0, 62, 100),  # D5 (7th chord)
    (3.0, 67, 100),  # A5
    (3.0, 64, 100),  # F5
    (3.0, 69, 100),  # C6
    (3.5, 62, 100),  # D5
    (3.5, 67, 100),  # A5
    (3.5, 64, 100),  # F5
    (3.5, 69, 100),  # C6
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Drums - Bar 3 (3.0 - 4.5s)
drum_notes = [
    (3.0, 36, 100),  # Kick on beat 1
    (3.5, 38, 100),  # Snare on beat 2
    (4.0, 36, 100),  # Kick on beat 3
    (4.5, 38, 100),  # Snare on beat 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax - Bar 4 (4.5 - 6.0s)
sax_notes = [
    (4.5, 62, 100),  # D5
    (4.625, 65, 100),  # F#5
    (4.75, 67, 100),  # A5
    (5.125, 62, 100),  # D5 (rest for 0.375s)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Bass - Bar 4 (4.5 - 6.0s)
bass_notes = [
    (4.5, 45, 100),  # D3
    (4.875, 47, 100),  # F#3
    (5.25, 49, 100),  # A3
    (5.625, 45, 100),  # D3
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Piano - Bar 4 (4.5 - 6.0s)
piano_notes = [
    (4.5, 62, 100),  # D5 (7th chord)
    (4.5, 67, 100),  # A5
    (4.5, 64, 100),  # F5
    (4.5, 69, 100),  # C6
    (5.0, 62, 100),  # D5
    (5.0, 67, 100),  # A5
    (5.0, 64, 100),  # F5
    (5.0, 69, 100),  # C6
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Drums - Bar 4 (4.5 - 6.0s)
drum_notes = [
    (4.5, 36, 100),  # Kick on beat 1
    (5.0, 38, 100),  # Snare on beat 2
    (5.5, 36, 100),  # Kick on beat 3
    (6.0, 38, 100),  # Snare on beat 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
