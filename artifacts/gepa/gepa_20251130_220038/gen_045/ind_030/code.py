
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 70, 100), (1.75, 69, 100), (2.0, 68, 100), (2.25, 67, 100),
    (2.5, 69, 100), (2.75, 70, 100), (3.0, 71, 100), (3.25, 72, 100),
    # Bar 3 (3.0 - 4.5s)
    (3.5, 72, 100), (3.75, 71, 100), (4.0, 70, 100), (4.25, 69, 100),
    (4.5, 68, 100), (4.75, 67, 100), (5.0, 69, 100), (5.25, 70, 100),
    # Bar 4 (4.5 - 6.0s)
    (5.5, 70, 100), (5.75, 69, 100), (6.0, 68, 100), (6.25, 67, 100)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.75, 70, 100), (1.75, 68, 100), (1.75, 67, 100), (1.75, 64, 100),
    (2.25, 70, 100), (2.25, 68, 100), (2.25, 67, 100), (2.25, 64, 100),
    # Bar 3 (3.0 - 4.5s)
    (3.75, 70, 100), (3.75, 68, 100), (3.75, 67, 100), (3.75, 64, 100),
    (4.25, 70, 100), (4.25, 68, 100), (4.25, 67, 100), (4.25, 64, 100),
    # Bar 4 (4.5 - 6.0s)
    (5.75, 70, 100), (5.75, 68, 100), (5.75, 67, 100), (5.75, 64, 100),
    (6.25, 70, 100), (6.25, 68, 100), (6.25, 67, 100), (6.25, 64, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100), (1.875, 42, 100),
    (2.25, 38, 100), (2.625, 42, 100),
    (3.0, 36, 100), (3.375, 42, 100),
    (3.75, 38, 100), (4.125, 42, 100),
    (4.5, 36, 100), (4.875, 42, 100),
    (5.25, 38, 100), (5.625, 42, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Dante: Melody in Dm, one short motif, make it sing
sax_notes = [
    (1.5, 62, 100), (1.75, 64, 100), (2.0, 60, 100), (2.25, 62, 100),
    (2.5, 64, 100), (2.75, 62, 100), (3.0, 60, 100), (3.25, 62, 100),
    (3.5, 64, 100), (3.75, 62, 100), (4.0, 60, 100), (4.25, 62, 100),
    (4.5, 64, 100), (4.75, 62, 100), (5.0, 60, 100), (5.25, 62, 100),
    (5.5, 64, 100), (5.75, 62, 100), (6.0, 60, 100)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
