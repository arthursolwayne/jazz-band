
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (1.5, 62), (1.75, 63), (2.0, 60), (2.25, 62),
    # Bar 3
    (2.5, 64), (2.75, 65), (3.0, 62), (3.25, 64),
    # Bar 4
    (3.5, 60), (3.75, 61), (4.0, 59), (4.25, 60),
    # Resolution
    (4.5, 62), (4.75, 63), (5.0, 60), (5.25, 62)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    (2.0, 67), (2.0, 71), (2.0, 74), (2.0, 76),
    # Bar 3: G7 on beat 2
    (3.0, 71), (3.0, 74), (3.0, 77), (3.0, 79),
    # Bar 4: C7 on beat 2
    (4.0, 67), (4.0, 71), (4.0, 74), (4.0, 76),
    # Bar 4: D7 on beat 4
    (5.0, 67), (5.0, 71), (5.0, 74), (5.0, 76)
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    (1.5, 62), (1.75, 65), (2.0, 67), (2.25, 65),
    # Bar 3: Leave it hanging
    (2.5, 67), (2.75, 65), (3.0, 62), (3.25, 60),
    # Bar 4: Come back and finish it
    (3.5, 62), (3.75, 65), (4.0, 67), (4.25, 65),
    (4.5, 67), (4.75, 65), (5.0, 62), (5.25, 60)
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_introduction.mid')
