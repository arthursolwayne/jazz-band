
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
    (0.0, 36, 100), (0.375, 42, 100),
    (0.75, 38, 100), (1.125, 42, 100),
    (1.5, 36, 100), (1.875, 42, 100),
    (2.25, 38, 100), (2.625, 42, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: simple, emotive motif (Dm7 -> F -> C -> Bb)
sax_notes = [
    (1.5, 62, 90), (1.75, 65, 90), (2.0, 67, 90), (2.25, 66, 90)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bass: walking line, chromatic approaches
bass_notes = [
    (1.5, 50, 80), (1.75, 51, 80), (2.0, 49, 80), (2.25, 50, 80),
    (2.5, 52, 80), (2.75, 51, 80), (3.0, 50, 80), (3.25, 52, 80)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.75, 60, 100), (1.75, 64, 100), (1.75, 62, 100), (1.75, 67, 100),
    (2.25, 60, 100), (2.25, 64, 100), (2.25, 62, 100), (2.25, 67, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: motif variation (G -> Bb -> C -> D)
sax_notes = [
    (3.0, 67, 90), (3.25, 66, 90), (3.5, 67, 90), (3.75, 62, 90)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bass: walking line, chromatic approaches
bass_notes = [
    (3.0, 52, 80), (3.25, 51, 80), (3.5, 50, 80), (3.75, 49, 80),
    (4.0, 50, 80), (4.25, 51, 80), (4.5, 52, 80), (4.75, 53, 80)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (3.25, 62, 100), (3.25, 66, 100), (3.25, 64, 100), (3.25, 67, 100),
    (3.75, 62, 100), (3.75, 66, 100), (3.75, 64, 100), (3.75, 67, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36, 100), (3.375, 42, 100),
    (3.75, 38, 100), (4.125, 42, 100),
    (4.5, 36, 100), (4.875, 42, 100),
    (5.25, 38, 100), (5.625, 42, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: motif resolution (D -> C -> Bb -> D)
sax_notes = [
    (4.5, 62, 90), (4.75, 60, 90), (5.0, 66, 90), (5.25, 62, 90)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bass: walking line, chromatic approaches
bass_notes = [
    (4.5, 50, 80), (4.75, 51, 80), (5.0, 49, 80), (5.25, 50, 80),
    (5.5, 52, 80), (5.75, 51, 80), (6.0, 50, 80), (6.25, 52, 80)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (4.75, 60, 100), (4.75, 64, 100), (4.75, 62, 100), (4.75, 67, 100),
    (5.25, 60, 100), (5.25, 64, 100), (5.25, 62, 100), (5.25, 67, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100), (4.875, 42, 100),
    (5.25, 38, 100), (5.625, 42, 100),
    (6.0, 36, 100), (6.375, 42, 100),
    (6.75, 38, 100), (7.125, 42, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
