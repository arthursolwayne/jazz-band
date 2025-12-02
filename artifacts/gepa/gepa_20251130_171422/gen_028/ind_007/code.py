
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36, 100), (0.375, 42, 80),
    (0.75, 36, 100), (1.125, 42, 80),
    (1.5, 38, 100), (1.875, 42, 80),
    (2.25, 38, 100), (2.625, 42, 80)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 2: Everyone in (1.5 - 3.0s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    (1.5, 61, 100), (1.75, 60, 100), (2.0, 62, 100), (2.25, 61, 100)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    (1.5, 62, 80), (1.5, 67, 70), (1.5, 69, 70), (1.5, 71, 80),
    # Bar 3 (2.0 - 2.5s)
    (2.0, 62, 80), (2.0, 67, 70), (2.0, 70, 70), (2.0, 72, 80)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Dante: One short motif, make it sing
sax_notes = [
    (1.5, 64, 100), (1.75, 66, 100), (2.0, 64, 100), (2.25, 67, 100)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Everyone in (3.0 - 4.5s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    (3.0, 61, 100), (3.25, 60, 100), (3.5, 62, 100), (3.75, 61, 100)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3 (3.0 - 3.5s)
    (3.0, 62, 80), (3.0, 67, 70), (3.0, 70, 70), (3.0, 72, 80),
    # Bar 4 (3.5 - 4.0s)
    (3.5, 62, 80), (3.5, 67, 70), (3.5, 69, 70), (3.5, 71, 80)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Dante: Continue the motif, leave it hanging
sax_notes = [
    (3.0, 64, 100), (3.25, 66, 100), (3.5, 64, 100), (3.75, 67, 100)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 4: Everyone in (4.5 - 6.0s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    (4.5, 61, 100), (4.75, 60, 100), (5.0, 62, 100), (5.25, 61, 100)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4 (4.5 - 5.0s)
    (4.5, 62, 80), (4.5, 67, 70), (4.5, 70, 70), (4.5, 72, 80),
    # Bar 4 (5.0 - 5.5s)
    (5.0, 62, 80), (5.0, 67, 70), (5.0, 69, 70), (5.0, 71, 80)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Dante: Return to the motif, finish it with a question
sax_notes = [
    (4.5, 64, 100), (4.75, 66, 100), (5.0, 64, 100), (5.25, 65, 100)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Add drum fills in bar 4
drum_notes = [
    (4.5, 36, 100), (4.875, 42, 80),
    (5.25, 36, 100), (5.625, 42, 80),
    (6.0, 38, 100), (6.375, 42, 80)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
