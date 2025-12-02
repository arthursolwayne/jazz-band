
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
for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches
bass_notes = [
    (1.5, 65), (1.875, 66), (2.25, 67), (2.625, 69),
    (3.0, 71), (3.375, 72), (3.75, 74), (4.125, 76),
    (4.5, 77), (4.875, 79), (5.25, 81), (5.625, 83)
]
for start, note in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(n)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    (1.875, 62), (1.875, 67), (1.875, 71), (1.875, 67),
    # Bar 3: G7 (G, B, D, F)
    (3.375, 67), (3.375, 71), (3.375, 74), (3.375, 69),
    # Bar 4: C7 (C, E, G, B)
    (4.875, 60), (4.875, 64), (4.875, 71), (4.875, 74)
]
for start, note in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(n)

# Sax (Dante): motif in D, one short phrase, leave it hanging
sax_notes = [
    # Bar 2 (1.5 - 2.25s): motif
    (1.5, 65), (1.875, 67), (2.25, 65),  # D, E, D
    # Bar 3 (2.625 - 3.375s): repeat and resolve
    (2.625, 65), (3.0, 67), (3.375, 69),  # D, E, F#
    # Bar 4 (3.75 - 5.25s): develop the idea
    (3.75, 69), (4.125, 67), (4.5, 65), (4.875, 67), (5.25, 69)  # F#, E, D, E, F#
]
for start, note in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(n)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.5, end=start + 1.875)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 2.25, end=start + 2.625)
    hihat = [
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        for i in range(4)
    ]
    drums.notes.extend([kick1, snare2, kick3, snare4] + hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('jazz_intro.mid')
