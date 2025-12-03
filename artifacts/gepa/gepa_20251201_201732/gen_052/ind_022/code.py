
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
    (0.0, 36, 100),  # Kick
    (0.375, 42, 100),  # Hihat
    (0.75, 38, 100),  # Snare
    (1.125, 42, 100),  # Hihat
    (1.5, 36, 100),  # Kick
    (1.875, 42, 100),  # Hihat
    (2.25, 38, 100),  # Snare
    (2.625, 42, 100),  # Hihat
]

for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody starts with a short motif

# Saxophone line (F5, Bb5, D6, rest)
sax_notes = [
    (1.5, 77, 100),  # F5
    (1.875, 81, 100),  # Bb5
    (2.25, 84, 100),  # D6
    (3.0, 77, 100),  # F5 (rest at 2.625-3.0)
]

for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bass line: walking line with chromatic approaches
# F2 (D), Ab2 (Eb), Bb2 (F), C3 (G)
bass_notes = [
    (1.5, 38, 80),  # F2
    (1.875, 40, 80),  # Ab2
    (2.25, 41, 80),  # Bb2
    (2.625, 43, 80),  # C3
]

for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Piano: Open voicings, different chord each bar
# Bar 2: F7 (F A C E)
piano_notes = [
    (1.5, 65, 90),  # F4
    (1.5, 67, 90),  # A4
    (1.5, 69, 90),  # C5
    (1.5, 72, 90),  # E5
]

for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bar 3: Bb7 (Bb D F A)
piano_notes = [
    (3.0, 62, 95),  # Bb4
    (3.0, 65, 95),  # D5
    (3.0, 67, 95),  # F5
    (3.0, 70, 95),  # A5
]

for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bar 4: D7 (D F# A C)
piano_notes = [
    (4.5, 67, 100),  # D5
    (4.5, 70, 100),  # F#5
    (4.5, 72, 100),  # A5
    (4.5, 75, 100),  # C6
]

for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Drums in bars 2-4: Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth
for bar in range(2, 5):
    for beat in range(0, 4):
        start = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(100, 36, start, start + 0.375))
        elif beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(100, 38, start, start + 0.375))
        drums.notes.append(pretty_midi.Note(100, 42, start, start + 0.375))

# Saxophone: Final note to resolve the motif
sax_notes = [
    (4.5, 77, 100),  # F5
]

for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
