
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
# Walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 65), (1.875, 66), (2.25, 67), (2.625, 64),
    (3.0, 62), (3.375, 63), (3.75, 65), (4.125, 67),
    (4.5, 69), (4.875, 67), (5.25, 65), (5.625, 63)
]
for start, note in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano (Diane)
# 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 64), (1.875, 67), (1.875, 71), (1.875, 76),
    # Bar 3
    (3.375, 64), (3.375, 67), (3.375, 71), (3.375, 76),
    # Bar 4
    (4.875, 64), (4.875, 67), (4.875, 71), (4.875, 76)
]
for start, note in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax (Dante)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 (F, A, C, E) - motif
sax_notes = [
    (1.5, 77), (1.875, 82), (2.25, 87), (2.625, 82),
    (3.0, 77), (3.375, 82), (3.75, 87), (4.125, 82),
    (4.5, 77), (4.875, 82), (5.25, 87), (5.625, 82)
]
for start, note in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
