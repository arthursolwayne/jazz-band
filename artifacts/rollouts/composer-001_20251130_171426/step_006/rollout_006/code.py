
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38), (1.875, 42),
    (2.25, 36), (2.625, 42), (3.0, 38), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 36), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 53), (1.75, 51), (2.0, 50), (2.25, 52),
    (2.5, 53), (2.75, 51), (3.0, 50), (3.25, 52),
    (3.5, 53), (3.75, 51), (4.0, 50), (4.25, 52),
    (4.5, 53), (4.75, 51), (5.0, 50), (5.25, 52)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 62), (2.0, 67), (2.0, 69), (2.0, 71),
    # Bar 3
    (3.5, 62), (3.5, 67), (3.5, 69), (3.5, 71),
    # Bar 4
    (5.0, 62), (5.0, 67), (5.0, 69), (5.0, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66), (1.75, 69), (2.0, 67), (2.25, 66),
    (3.0, 66), (3.25, 69), (3.5, 67), (3.75, 66),
    (4.5, 66), (4.75, 69), (5.0, 67), (5.25, 66)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
