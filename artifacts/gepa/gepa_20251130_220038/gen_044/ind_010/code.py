
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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on 2
    (1.25, 42, 100), # Hihat on &2
    (1.5, 36, 100),  # Kick on 3
    (1.75, 42, 100), # Hihat on &3
    (2.0, 38, 100),  # Snare on 4
    (2.25, 42, 100)  # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus - Walking bass line in D
bass_notes = [
    (1.5, 72, 100),  # D
    (1.75, 71, 100), # C#
    (2.0, 74, 100),  # F
    (2.25, 72, 100), # D
    (2.5, 71, 100),  # C#
    (2.75, 74, 100), # F
    (3.0, 72, 100),  # D
    (3.25, 71, 100), # C#
    (3.5, 74, 100),  # F
    (3.75, 72, 100), # D
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane - 7th chords, comp on 2 and 4
piano_notes = [
    (1.75, 72, 100),  # D7 (D, F#, A, C)
    (1.75, 76, 100),
    (1.75, 82, 100),
    (1.75, 87, 100),
    (2.25, 72, 100),  # D7 again
    (2.25, 76, 100),
    (2.25, 82, 100),
    (2.25, 87, 100),
    (2.75, 72, 100),  # D7
    (2.75, 76, 100),
    (2.75, 82, 100),
    (2.75, 87, 100),
    (3.25, 72, 100),  # D7
    (3.25, 76, 100),
    (3.25, 82, 100),
    (3.25, 87, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Dante - Tenor sax melody (Bar 2: start of motif)
sax_notes = [
    (1.5, 65, 100),  # Bb
    (1.6, 67, 100),  # C
    (1.7, 64, 100),  # A
    (1.75, 62, 100), # G
    (1.8, 65, 100),  # Bb
    (1.9, 67, 100),  # C
    (2.0, 69, 100),  # D
    (2.25, 64, 100), # A
    (2.5, 69, 100),  # D
    (2.75, 71, 100), # E
    (3.0, 69, 100),  # D
    (3.25, 67, 100), # C
    (3.5, 64, 100),  # A
    (3.75, 62, 100), # G
    (4.0, 65, 100),  # Bb
    (4.25, 67, 100), # C
    (4.5, 69, 100),  # D
    (4.75, 71, 100), # E
    (5.0, 69, 100),  # D
    (5.25, 67, 100), # C
    (5.5, 64, 100),  # A
    (5.75, 62, 100), # G
    (6.0, 65, 100)   # Bb
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.05))

# Drums for Bars 2-4
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 100), # Hihat on &1
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 100), # Hihat on &2
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 100), # Hihat on &4
    (3.5, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on &1
    (4.0, 38, 100),  # Snare on 2
    (4.25, 42, 100), # Hihat on &2
    (4.5, 36, 100),  # Kick on 3
    (4.75, 42, 100), # Hihat on &3
    (5.0, 38, 100),  # Snare on 4
    (5.25, 42, 100), # Hihat on &4
    (5.5, 36, 100),  # Kick on 1
    (5.75, 42, 100), # Hihat on &1
    (6.0, 38, 100),  # Snare on 2
    (6.25, 42, 100)  # Hihat on &2
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_moment.mid")
