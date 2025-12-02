
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
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]

for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 38), (1.875, 40), (2.25, 38), (2.625, 40),
    # Bar 3
    (3.0, 41), (3.375, 38), (3.75, 41), (4.125, 38),
    # Bar 4
    (4.5, 43), (4.875, 41), (5.25, 43), (5.625, 41)
]

for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (1.5, 53), (1.5, 60), (1.5, 65), (1.5, 67),
    # Bar 3: Dm7 (D, F, A, C)
    (3.0, 55), (3.0, 58), (3.0, 62), (3.0, 65),
    # Bar 4: G7 (G, B, D, F)
    (4.5, 62), (4.5, 67), (4.5, 69), (4.5, 65)
]

for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 3
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]

for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) -> G (67) -> A (69) -> F (65) (Bar 2)
# Then repeat (Bar 4)
sax_notes = [
    # Bar 2
    (1.5, 65), (1.75, 67), (2.0, 69), (2.25, 65),
    # Bar 3: Rest
    # Bar 4
    (4.5, 65), (4.75, 67), (5.0, 69), (5.25, 65)
]

for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
