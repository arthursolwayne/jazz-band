
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 37), (1.75, 40), (2.0, 41), (2.25, 43),
    (2.5, 45), (2.75, 48), (3.0, 49), (3.25, 51),
    (3.5, 53), (3.75, 56), (4.0, 57), (4.25, 59),
    (4.5, 60), (4.75, 63), (5.0, 64), (5.25, 66)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (1.5, 65), (1.5, 70), (1.5, 69), (1.5, 74),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (2.5, 62), (2.5, 67), (2.5, 69), (2.5, 65),
    # Bar 4: Gm7 (G, Bb, D, F)
    (3.5, 71), (3.5, 67), (3.5, 69), (3.5, 69),
    # Resolving chords
    (4.5, 74), (4.5, 70), (4.5, 69), (4.5, 65)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 72), (1.625, 76), (1.75, 72), (1.875, 76),
    (2.0, 72), (2.125, 76), (2.25, 72), (2.375, 76),
    (2.5, 76), (2.625, 81), (2.75, 76), (2.875, 81),
    (3.0, 76), (3.125, 81), (3.25, 76), (3.375, 81),
    (3.5, 76), (3.625, 81), (3.75, 76), (3.875, 81),
    (4.0, 76), (4.125, 81), (4.25, 76), (4.375, 81),
    (4.5, 76), (4.625, 81), (4.75, 76), (4.875, 81),
    (5.0, 76), (5.125, 81), (5.25, 76), (5.375, 81)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
