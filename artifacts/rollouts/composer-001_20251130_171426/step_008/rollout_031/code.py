
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),       # Kick on 1
    (42, 0.0, 0.1875),      # Hihat on 1
    (38, 0.375, 0.375),     # Snare on 2
    (42, 0.375, 0.1875),    # Hihat on 2
    (36, 0.75, 0.375),      # Kick on 3
    (42, 0.75, 0.1875),     # Hihat on 3
    (38, 1.125, 0.375),     # Snare on 4
    (42, 1.125, 0.1875)     # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, Dm7 -> G7 -> Cm7 -> F7
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 1.5),         # D
    (61, 1.875, 1.875),     # C#
    (62, 2.25, 2.25),       # D
    (64, 2.625, 2.625),     # E
    # Bar 3 (3.0 - 4.5s)
    (67, 3.0, 3.0),         # G
    (66, 3.375, 3.375),     # F#
    (67, 3.75, 3.75),       # G
    (69, 4.125, 4.125),     # A
    # Bar 4 (4.5 - 6.0s)
    (60, 4.5, 4.5),         # C
    (59, 4.875, 4.875),     # B
    (60, 5.25, 5.25),       # C
    (62, 5.625, 5.625)      # D
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 1.5),         # D7 (D, F#, A, C)
    (66, 1.5, 1.5),
    (69, 1.5, 1.5),
    (60, 1.5, 1.5),
    (62, 2.625, 2.625),
    (66, 2.625, 2.625),
    (69, 2.625, 2.625),
    (60, 2.625, 2.625),
    # Bar 3 (3.0 - 4.5s)
    (67, 3.0, 3.0),         # G7 (G, B, D, F)
    (71, 3.0, 3.0),
    (69, 3.0, 3.0),
    (64, 3.0, 3.0),
    (67, 4.125, 4.125),
    (71, 4.125, 4.125),
    (69, 4.125, 4.125),
    (64, 4.125, 4.125),
    # Bar 4 (4.5 - 6.0s)
    (60, 4.5, 4.5),         # Cm7 (C, Eb, G, Bb)
    (63, 4.5, 4.5),
    (67, 4.5, 4.5),
    (62, 4.5, 4.5),
    (60, 5.625, 5.625),
    (63, 5.625, 5.625),
    (67, 5.625, 5.625),
    (62, 5.625, 5.625)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 1.5),         # D
    (67, 1.875, 1.875),     # G
    (62, 2.25, 2.25),       # D
    # Bar 3 (3.0 - 4.5s)
    (69, 3.75, 3.75),       # A
    (67, 4.125, 4.125),     # G
    (62, 4.5, 4.5),         # D
    # Bar 4 (4.5 - 6.0s)
    (62, 5.25, 5.25),       # D
    (67, 5.625, 5.625)      # G
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Bar 2: 1.5 to 3.0, Bar 3: 3.0 to 4.5, Bar 4: 4.5 to 6.0
    for i in range(4):
        time = bar_start + i * 0.375
        if i == 0 or i == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))
        elif i == 1 or i == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375))
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
