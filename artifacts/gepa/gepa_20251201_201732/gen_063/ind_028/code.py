
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 50), (1.875, 53), (2.25, 52), (2.625, 50),
    (3.0, 50), (3.375, 53), (3.75, 52), (4.125, 50),
    (4.5, 50), (4.875, 53), (5.25, 52), (5.625, 50)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, F)
piano_notes = [
    # Bar 2
    (1.5, 62), (1.5, 67), (1.5, 70), (1.5, 62),
    # Bar 3: Gm7 (Bb, D, G, Bb)
    (3.0, 60), (3.0, 65), (3.0, 69), (3.0, 60),
    # Bar 4: Cm7 (E, G, C, E)
    (4.5, 64), (4.5, 67), (4.5, 72), (4.5, 64)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.75))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    (1.5, 62), (1.75, 65), (2.0, 62),
    # Bar 3
    (3.0, 62), (3.25, 65), (3.5, 62),
    # Bar 4
    (4.5, 62), (4.75, 65), (5.0, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
