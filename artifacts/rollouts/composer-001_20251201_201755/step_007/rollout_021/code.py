
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
    (0.0, 36, 127), (0.375, 42, 127), (0.75, 36, 127), (1.125, 42, 127),
    (1.5, 38, 127), (1.875, 42, 127), (2.25, 38, 127), (2.625, 42, 127)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: Fm -> Bb -> Ab -> D
    (1.5, 71, 100), (1.875, 68, 100), (2.25, 70, 100), (2.625, 67, 100),
    # Bar 3: Eb -> A -> G -> C
    (3.0, 64, 100), (3.375, 69, 100), (3.75, 67, 100), (4.125, 60, 100),
    # Bar 4: Fm -> Bb -> Ab -> D
    (4.5, 71, 100), (4.875, 68, 100), (5.25, 70, 100), (5.625, 67, 100)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    (1.5, 71, 100), (1.5, 64, 100), (1.5, 67, 100), (1.5, 60, 100),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (3.0, 68, 100), (3.0, 67, 100), (3.0, 71, 100), (3.0, 64, 100),
    # Bar 4: Ab7 (Ab, C, Eb, G)
    (4.5, 70, 100), (4.5, 67, 100), (4.5, 64, 100), (4.5, 69, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it
sax_notes = [
    # Bar 2: Start of motif
    (1.5, 72, 110), (1.875, 70, 110),
    # Bar 3: Leave it hanging
    (3.0, 69, 100),
    # Bar 4: Come back and finish it
    (4.5, 72, 110), (4.875, 70, 110), (5.25, 69, 110)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36, 127), (1.875, 42, 127), (2.25, 36, 127), (2.625, 42, 127),
    (3.0, 38, 127), (3.375, 42, 127), (3.75, 38, 127), (4.125, 42, 127),
    # Bar 3
    (4.5, 36, 127), (4.875, 42, 127), (5.25, 36, 127), (5.625, 42, 127),
    (6.0, 38, 127), (6.375, 42, 127), (6.75, 38, 127), (7.125, 42, 127)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
