
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
bar1 = 1.5
drum_notes = [
    (0.0, 36, 100), (0.375, 42, 100),
    (0.75, 36, 100), (1.125, 42, 100),
    (1.5, 38, 100), (1.875, 42, 100),
    (2.25, 38, 100), (2.625, 42, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, chromatic approaches
bass_notes = [
    (1.5, 62, 100), (1.75, 63, 100), (2.0, 64, 100), (2.25, 65, 100),
    (2.5, 67, 100), (2.75, 68, 100), (3.0, 69, 100), (3.25, 70, 100),
    (3.5, 72, 100), (3.75, 73, 100), (4.0, 74, 100), (4.25, 75, 100),
    (4.5, 77, 100), (4.75, 78, 100), (5.0, 79, 100), (5.25, 80, 100)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    (1.5, 67, 100), (1.5, 72, 100), (1.5, 74, 100), (1.5, 79, 100),
    (2.0, 67, 100), (2.0, 72, 100), (2.0, 74, 100), (2.0, 79, 100),
    (2.5, 72, 100), (2.5, 74, 100), (2.5, 79, 100), (2.5, 84, 100),
    (3.0, 72, 100), (3.0, 74, 100), (3.0, 77, 100), (3.0, 82, 100),
    (3.5, 72, 100), (3.5, 74, 100), (3.5, 79, 100), (3.5, 84, 100),
    (4.0, 72, 100), (4.0, 74, 100), (4.0, 77, 100), (4.0, 82, 100),
    (4.5, 72, 100), (4.5, 74, 100), (4.5, 77, 100), (4.5, 82, 100),
    (5.0, 72, 100), (5.0, 74, 100), (5.0, 77, 100), (5.0, 82, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2 = 1.5
drum_notes = [
    (1.5, 36, 100), (1.875, 42, 100),
    (2.25, 36, 100), (2.625, 42, 100),
    (3.0, 38, 100), (3.375, 42, 100),
    (3.75, 38, 100), (4.125, 42, 100),
    (4.5, 36, 100), (4.875, 42, 100),
    (5.25, 36, 100), (5.625, 42, 100),
    (6.0, 38, 100), (6.375, 42, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1875))

# Sax: short motif, starts on beat 2 of bar 2, sings it, leaves it hanging
sax_notes = [
    (2.0, 62, 100), (2.0, 65, 100), (2.0, 69, 100), (2.0, 72, 100),
    (2.375, 69, 100), (2.375, 72, 100),
    (2.75, 65, 100), (2.75, 69, 100),
    (3.125, 62, 100), (3.125, 65, 100), (3.125, 69, 100), (3.125, 72, 100),
    (3.5, 69, 100), (3.5, 72, 100),
    (3.875, 65, 100), (3.875, 69, 100),
    (4.25, 62, 100), (4.25, 65, 100), (4.25, 69, 100), (4.25, 72, 100),
    (4.625, 69, 100), (4.625, 72, 100),
    (5.0, 65, 100), (5.0, 69, 100)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
