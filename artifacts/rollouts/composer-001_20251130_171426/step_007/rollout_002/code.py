
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 42), (1.125, 42),
    (1.5, 36), (1.875, 38), (2.25, 42), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 42), (4.125, 42),
    (4.5, 36), (4.875, 38), (5.25, 42), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line, chromatic approaches, never same note twice
bass_notes = [
    (1.5, 50), (1.875, 48), (2.25, 49), (2.625, 50),
    (3.0, 52), (3.375, 51), (3.75, 50), (4.125, 49),
    (4.5, 48), (4.875, 47), (5.25, 48), (5.625, 49)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (1.875, 62), (1.875, 67), (1.875, 69), (1.875, 71),
    (3.375, 62), (3.375, 67), (3.375, 69), (3.375, 71),
    (4.875, 62), (4.875, 67), (4.875, 69), (4.875, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62), (1.875, 67), (2.25, 69), (2.625, 67),
    (3.0, 62), (3.375, 67), (3.75, 69), (4.125, 67),
    (4.5, 62), (4.875, 67), (5.25, 69), (5.625, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
