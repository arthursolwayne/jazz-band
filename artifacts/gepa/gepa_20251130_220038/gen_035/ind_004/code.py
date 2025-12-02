
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

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    (1.5, 62, 100), (1.875, 63, 100),  # D -> Eb
    (2.25, 65, 100), (2.625, 62, 100),  # F# -> D
    (3.0, 62, 100), (3.375, 63, 100),   # D -> Eb
    (3.75, 65, 100), (4.125, 62, 100),  # F# -> D
    (4.5, 62, 100), (4.875, 63, 100),   # D -> Eb
    (5.25, 65, 100), (5.625, 62, 100)   # F# -> D
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Piano: 7th chords on 2 and 4, sparse comping
piano_notes = [
    (2.25, 67, 90), (2.25, 71, 90), (2.25, 74, 90),  # D7 on 2
    (3.75, 67, 90), (3.75, 71, 90), (3.75, 74, 90),  # D7 on 4
    (5.25, 67, 90), (5.25, 71, 90), (5.25, 74, 90)   # D7 on 2
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: Motif - start with a whisper, leave it hanging
# D (62) -> Eb (63) -> F# (66) -> rest -> D (62)
sax_notes = [
    (1.5, 62, 60), (1.75, 63, 60), (2.0, 66, 60),
    (2.25, 62, 60), (2.5, 63, 60), (2.75, 66, 60),
    (3.0, 62, 60), (3.25, 63, 60), (3.5, 66, 60),
    (3.75, 62, 60), (4.0, 63, 60), (4.25, 66, 60),
    (4.5, 62, 60), (4.75, 63, 60), (5.0, 66, 60),
    (5.25, 62, 60), (5.5, 63, 60), (5.75, 66, 60)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.save("dante_intro.mid")
