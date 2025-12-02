
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
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, chromatic approaches
bass_notes = [
    (1.5, 50), (1.875, 49), (2.25, 50), (2.625, 51),
    (3.0, 52), (3.375, 51), (3.75, 50), (4.125, 49),
    (4.5, 50), (4.875, 51), (5.25, 52), (5.625, 53)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.25, 62), (2.25, 67), (2.25, 69), (2.25, 71),
    # Bar 3
    (3.75, 62), (3.75, 67), (3.75, 69), (3.75, 71),
    # Bar 4
    (5.25, 62), (5.25, 67), (5.25, 69), (5.25, 71)
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(n)

# Sax: Melody in Dm, one short motif, make it sing
sax_notes = [
    (1.5, 62), (1.75, 65), (2.0, 62), (2.25, 60),
    (2.5, 62), (2.75, 65), (3.0, 62), (3.25, 60),
    (3.5, 62), (3.75, 65), (4.0, 62), (4.25, 60),
    (4.5, 62), (4.75, 65), (5.0, 62), (5.25, 60),
    (5.5, 62), (5.75, 65), (6.0, 62)
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
