
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.375, 0.75),   # Hihat on 2
    (36, 0.75, 1.125),   # Kick on 3
    (42, 1.125, 1.5)     # Hihat on 4
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches, not scales
bass_notes = [
    (53, 1.5, 1.875),    # F2 on 1
    (55, 1.875, 2.25),   # A2 on 2
    (53, 2.25, 2.625),   # F2 on 3
    (57, 2.625, 3.0),    # C3 on 4
    (55, 3.0, 3.375),    # A2 on 1
    (57, 3.375, 3.75),   # C3 on 2
    (53, 3.75, 4.125),   # F2 on 3
    (56, 4.125, 4.5),    # Bb2 on 4
    (57, 4.5, 4.875),    # C3 on 1
    (55, 4.875, 5.25),   # A2 on 2
    (53, 5.25, 5.625),   # F2 on 3
    (57, 5.625, 6.0)     # C3 on 4
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Piano: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 1.5, 1.875),    # F
    (60, 1.5, 1.875),    # C
    (64, 1.5, 1.875),    # D
    (62, 1.5, 1.875),    # Ab

    # Bar 3: Bb7 (Bb, D, F, Ab)
    (57, 3.0, 3.375),    # Bb
    (62, 3.0, 3.375),    # Ab
    (53, 3.0, 3.375),    # F
    (65, 3.0, 3.375),    # D

    # Bar 4: Cm7 (C, Eb, G, Bb)
    (60, 4.5, 4.875),    # C
    (63, 4.5, 4.875),    # Eb
    (67, 4.5, 4.875),    # G
    (57, 4.5, 4.875),    # Bb
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    drum_notes = [
        (36, start + 0.0, start + 0.375),    # Kick on 1
        (42, start + 0.375, start + 0.75),   # Hihat on 2
        (38, start + 0.75, start + 1.125),   # Snare on 2
        (36, start + 0.75, start + 1.125),   # Kick on 3
        (42, start + 1.125, start + 1.5),    # Hihat on 3
        (38, start + 1.5, start + 1.875),    # Snare on 4
        (42, start + 1.5, start + 1.875),    # Hihat on 4
        (36, start + 1.5, start + 1.875),    # Kick on 4?
    ]
    for note, start, end in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Motif: F - Ab - D - F (sax in F, transposition considered)
sax_notes = [
    (66, 1.5, 1.875),    # F (Dante's F)
    (61, 1.875, 2.25),   # Ab
    (71, 2.25, 2.625),   # D
    (66, 2.625, 3.0),    # F
    (66, 4.5, 4.875),    # F (return)
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
# midi.write disabled
