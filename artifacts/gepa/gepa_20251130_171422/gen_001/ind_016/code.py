
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
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),  # Bar 1
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42),  # Bar 2
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),  # Bar 3
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)   # Bar 4
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 50), (1.875, 49), (2.25, 51), (2.625, 52),
    (3.0, 52), (3.375, 51), (3.75, 49), (4.125, 50),
    (4.5, 50), (4.875, 49), (5.25, 51), (5.625, 52)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 62), (1.875, 67), (1.875, 71), (1.875, 74),  # D7
    # Bar 3
    (3.375, 62), (3.375, 67), (3.375, 71), (3.375, 74),  # D7
    # Bar 4
    (4.875, 62), (4.875, 67), (4.875, 71), (4.875, 74)   # D7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62), (1.625, 65), (1.75, 62), (1.875, 67),  # Motif
    (3.0, 62), (3.125, 65), (3.25, 62), (3.375, 67),  # Return
    (4.5, 62), (4.625, 65), (4.75, 62), (4.875, 67)   # Finish
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
