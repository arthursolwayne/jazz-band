
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36, 100), (0.375, 42, 80), (0.75, 42, 80), (1.125, 42, 80), (1.5, 36, 100),
    (1.875, 38, 100), (2.25, 42, 80), (2.625, 42, 80), (3.0, 42, 80),
    (3.375, 36, 100), (3.75, 38, 100), (4.125, 42, 80), (4.5, 42, 80), (4.875, 42, 80),
    (5.25, 36, 100), (5.625, 38, 100), (6.0, 42, 80)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    (1.5, 59, 100), (1.75, 57, 100), (2.0, 60, 100), (2.25, 62, 100),
    (2.5, 64, 100), (2.75, 62, 100), (3.0, 60, 100)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.75, 60, 100), (1.75, 64, 100), (1.75, 67, 100), (1.75, 71, 100),  # F7
    (2.25, 60, 100), (2.25, 64, 100), (2.25, 67, 100), (2.25, 71, 100),  # F7
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Dante on sax: motif starts here, ends with a question
sax_notes = [
    (1.5, 62, 100), (1.75, 58, 100), (2.0, 62, 100), (2.25, 66, 80),  # motif
    (2.5, 62, 100), (2.75, 66, 80), (3.0, 62, 100), (3.25, 66, 80)   # ends with a question
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass
bass_notes = [
    (3.0, 60, 100), (3.25, 58, 100), (3.5, 59, 100), (3.75, 60, 100),
    (4.0, 62, 100), (4.25, 60, 100), (4.5, 62, 100)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (3.25, 60, 100), (3.25, 64, 100), (3.25, 67, 100), (3.25, 71, 100),  # F7
    (3.75, 60, 100), (3.75, 64, 100), (3.75, 67, 100), (3.75, 71, 100),  # F7
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Little Ray on drums
drum_notes = [
    (3.0, 36, 100), (3.375, 38, 100), (3.75, 42, 80), (4.125, 42, 80), (4.5, 36, 100),
    (4.875, 38, 100), (5.25, 42, 80), (5.625, 42, 80), (6.0, 42, 80)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Dante on sax: variation of motif, ends with a space
sax_notes = [
    (3.0, 62, 100), (3.25, 58, 100), (3.5, 62, 100), (3.75, 66, 80),  # motif
    (4.0, 62, 100), (4.25, 66, 80), (4.5, 62, 100), (4.75, 66, 80),  # ends with a question
    (5.0, 62, 100), (5.25, 66, 80), (5.5, 62, 100), (5.75, 66, 80)   # holds the tension
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus on bass
bass_notes = [
    (4.5, 62, 100), (4.75, 60, 100), (5.0, 62, 100), (5.25, 64, 100),
    (5.5, 62, 100), (5.75, 60, 100), (6.0, 62, 100)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (4.75, 60, 100), (4.75, 64, 100), (4.75, 67, 100), (4.75, 71, 100),  # F7
    (5.25, 60, 100), (5.25, 64, 100), (5.25, 67, 100), (5.25, 71, 100),  # F7
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Little Ray on drums
drum_notes = [
    (4.5, 36, 100), (4.875, 38, 100), (5.25, 42, 80), (5.625, 42, 80), (6.0, 36, 100),
    (6.375, 38, 100), (6.75, 42, 80), (7.125, 42, 80), (7.5, 42, 80)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Dante on sax: final phrase, leaves it hanging
sax_notes = [
    (4.5, 62, 100), (4.75, 58, 100), (5.0, 62, 100), (5.25, 66, 80),  # motif
    (5.5, 62, 100), (5.75, 66, 80), (6.0, 62, 100), (6.25, 66, 80),  # ends with a question
    (6.5, 62, 100), (6.75, 66, 80), (7.0, 62, 100), (7.25, 66, 80)   # leaves it hanging
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("intro.mid")
