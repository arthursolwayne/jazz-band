
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
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, chromatic approaches
bass_notes = [
    (1.5, 62), (1.75, 63), (2.0, 64), (2.25, 62),
    (2.5, 62), (2.75, 63), (3.0, 64), (3.25, 62),
    (3.5, 62), (3.75, 63), (4.0, 64), (4.25, 62),
    (4.5, 62), (4.75, 63), (5.0, 64), (5.25, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 74), (2.0, 71), (2.0, 70), (2.0, 67),
    (2.5, 74), (2.5, 71), (2.5, 70), (2.5, 67),
    # Bar 3
    (3.0, 74), (3.0, 71), (3.0, 70), (3.0, 67),
    (3.5, 74), (3.5, 71), (3.5, 70), (3.5, 67),
    # Bar 4
    (4.0, 74), (4.0, 71), (4.0, 70), (4.0, 67),
    (4.5, 74), (4.5, 71), (4.5, 70), (4.5, 67)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 67), (1.625, 69), (1.75, 71), (1.875, 72),
    (2.0, 67), (2.125, 69), (2.25, 71), (2.375, 72),
    (2.5, 67), (2.625, 69), (2.75, 71), (2.875, 72),
    (3.0, 67), (3.125, 69), (3.25, 71), (3.375, 72),
    (3.5, 67), (3.625, 69), (3.75, 71), (3.875, 72),
    (4.0, 67), (4.125, 69), (4.25, 71), (4.375, 72),
    (4.5, 67), (4.625, 69), (4.75, 71), (4.875, 72),
    (5.0, 67), (5.125, 69), (5.25, 71), (5.375, 72)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
