
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),  # Bar 1
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),  # Bar 2
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),  # Bar 3
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)   # Bar 4
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 53), (1.875, 52), (2.25, 51), (2.625, 50),
    (3.0, 52), (3.375, 53), (3.75, 54), (4.125, 55),
    (4.5, 53), (4.875, 52), (5.25, 51), (5.625, 50)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 62), (1.875, 67), (1.875, 69), (1.875, 71),
    # Bar 3
    (3.375, 62), (3.375, 67), (3.375, 69), (3.375, 71),
    # Bar 4
    (4.875, 62), (4.875, 67), (4.875, 69), (4.875, 71)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65), (1.875, 67), (2.25, 69), (2.625, 67),
    (3.0, 65), (3.375, 67), (3.75, 69), (4.125, 67),
    (4.5, 65), (4.875, 67), (5.25, 69), (5.625, 67)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
