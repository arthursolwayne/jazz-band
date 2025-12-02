
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
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 60), (1.875, 61), (2.25, 62), (2.625, 63),
    (3.0, 64), (3.375, 63), (3.75, 62), (4.125, 61),
    (4.5, 60), (4.875, 59), (5.25, 58), (5.625, 57)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (2.25, 64), (2.25, 67), (2.25, 69), (2.25, 71),  # C7
    (3.75, 64), (3.75, 67), (3.75, 69), (3.75, 71),  # C7
    (5.25, 64), (5.25, 67), (5.25, 69), (5.25, 71)   # C7
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62), (1.625, 64), (1.75, 62), (1.875, 60),
    (2.25, 62), (2.375, 64), (2.5, 62), (2.625, 60),
    (3.0, 62), (3.125, 64), (3.25, 62), (3.375, 60),
    (3.75, 62), (3.875, 64), (4.0, 62), (4.125, 60),
    (4.5, 62), (4.625, 64), (4.75, 62), (4.875, 60),
    (5.25, 62), (5.375, 64), (5.5, 62), (5.625, 60)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
