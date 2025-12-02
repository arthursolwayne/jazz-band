
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38),
    (0.0, 42), (0.375, 42), (0.75, 42), (1.125, 42), (1.5, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 46), (1.875, 48), (2.25, 47), (2.625, 45),
    # Bar 3
    (3.0, 46), (3.375, 48), (3.75, 47), (4.125, 45),
    # Bar 4
    (4.5, 46), (4.875, 48), (5.25, 47), (5.625, 45)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.75, 62), (1.75, 67), (1.75, 69), (1.75, 71),
    # Bar 3
    (3.25, 62), (3.25, 67), (3.25, 69), (3.25, 71),
    # Bar 4
    (4.75, 62), (4.75, 67), (4.75, 69), (4.75, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Saxophone: Melody - start with a whisper, build to a cry
sax_notes = [
    # Bar 2
    (1.5, 65), (1.625, 67), (1.75, 69), (1.875, 67), (2.0, 65),
    # Bar 3
    (3.0, 67), (3.125, 69), (3.25, 71), (3.375, 69), (3.5, 67),
    # Bar 4
    (4.5, 69), (4.625, 71), (4.75, 72), (4.875, 71), (5.0, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums continue for bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 38), (2.25, 36), (2.625, 38),
    (1.5, 42), (1.875, 42), (2.25, 42), (2.625, 42),
    # Bar 3
    (3.0, 36), (3.375, 38), (3.75, 36), (4.125, 38),
    (3.0, 42), (3.375, 42), (3.75, 42), (4.125, 42),
    # Bar 4
    (4.5, 36), (4.875, 38), (5.25, 36), (5.625, 38),
    (4.5, 42), (4.875, 42), (5.25, 42), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
