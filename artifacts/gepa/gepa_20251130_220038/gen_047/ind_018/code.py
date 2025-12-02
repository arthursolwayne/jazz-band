
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.375, 0.125),  # Hihat on &1
    (38, 0.75, 0.375),  # Snare on 2
    (42, 0.875, 0.125),  # Hihat on &2
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.5, 0.125)     # Hihat on &3
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (44, 1.5, 0.375),  # D
    (45, 1.875, 0.375),  # Eb
    (46, 2.25, 0.375),  # E
    (48, 2.625, 0.375),  # G
    (47, 2.875, 0.375),  # F
    (46, 3.25, 0.375),  # E
    (44, 3.625, 0.375),  # D
    (45, 4.0, 0.375),  # Eb
    (47, 4.375, 0.375),  # F
    (49, 4.75, 0.375),  # G#
    (48, 5.125, 0.375),  # G
    (46, 5.5, 0.375),  # E
    (44, 5.875, 0.375)  # D
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (50, 1.875, 0.125),  # B7 on 2
    (52, 1.875, 0.125),
    (55, 1.875, 0.125),
    (57, 1.875, 0.125),
    (50, 2.625, 0.125),  # B7 on 4
    (52, 2.625, 0.125),
    (55, 2.625, 0.125),
    (57, 2.625, 0.125),
    (57, 3.875, 0.125),  # B7 on 2 (bar 3)
    (59, 3.875, 0.125),
    (62, 3.875, 0.125),
    (64, 3.875, 0.125),
    (57, 4.625, 0.125),  # B7 on 4 (bar 3)
    (59, 4.625, 0.125),
    (62, 4.625, 0.125),
    (64, 4.625, 0.125)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Bar 1
    dr = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(dr)
    dr = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    drums.notes.append(dr)
    # Hihat on every eighth
    for i in range(0, 4):
        dr = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(dr)
    # Bar 2
    dr = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.5, end=start + 1.875)
    drums.notes.append(dr)
    dr = pretty_midi.Note(velocity=100, pitch=38, start=start + 2.25, end=start + 2.625)
    drums.notes.append(dr)
    for i in range(0, 4):
        dr = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5 + i * 0.375, end=start + 1.5 + i * 0.375 + 0.125)
        drums.notes.append(dr)

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (52, 1.5, 0.125),  # F
    (54, 1.625, 0.125),  # G
    (55, 1.75, 0.125),  # A
    (52, 1.875, 0.125),  # F
    (54, 2.0, 0.125),  # G
    (55, 2.125, 0.125),  # A
    (52, 2.25, 0.125),  # F
    (54, 2.375, 0.125),  # G
    (56, 2.5, 0.125),  # Bb
    (54, 2.625, 0.125),  # G
    (52, 2.75, 0.125),  # F
    (50, 2.875, 0.125),  # D
    (52, 3.0, 0.125),  # F
    (54, 3.125, 0.125),  # G
    (55, 3.25, 0.125),  # A
    (52, 3.375, 0.125),  # F
    (54, 3.5, 0.125),  # G
    (55, 3.625, 0.125),  # A
    (52, 3.75, 0.125),  # F
    (54, 3.875, 0.125),  # G
    (56, 4.0, 0.125),  # Bb
    (54, 4.125, 0.125),  # G
    (52, 4.25, 0.125),  # F
    (50, 4.375, 0.125),  # D
    (52, 4.5, 0.125),  # F
    (54, 4.625, 0.125),  # G
    (55, 4.75, 0.125),  # A
    (52, 4.875, 0.125),  # F
    (54, 5.0, 0.125),  # G
    (55, 5.125, 0.125),  # A
    (52, 5.25, 0.125),  # F
    (54, 5.375, 0.125),  # G
    (56, 5.5, 0.125),  # Bb
    (54, 5.625, 0.125),  # G
    (52, 5.75, 0.125),  # F
    (50, 5.875, 0.125)   # D
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
