
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
    (36, 0.0, 1.0),          # Kick on 1
    (42, 0.25, 0.25),        # Hihat on 2
    (38, 0.5, 1.0),          # Snare on 3
    (42, 0.75, 0.25),        # Hihat on 4
    (42, 1.0, 0.5)           # Hihat fill
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 - Fm (F, C)
    (38, 1.5, 0.375),  # F (D2)
    (40, 1.875, 0.375), # Ab (E2)
    (43, 2.25, 0.375),  # C (G2)
    (41, 2.625, 0.375), # Bb (F2)
    # Bar 3 - Gm7 (G, D)
    (42, 3.0, 0.375),  # G (A2)
    (45, 3.375, 0.375), # B (C3)
    (47, 3.75, 0.375),  # D (D3)
    (44, 4.125, 0.375), # C (B2)
    # Bar 4 - Am7 (A, E)
    (45, 4.5, 0.375),  # A (C3)
    (48, 4.875, 0.375), # C (D3)
    (50, 5.25, 0.375),  # E (F3)
    (47, 5.625, 0.375)  # D (E3)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 - Fm7: F, Ab, C, Eb
    (53, 1.5, 0.5), (55, 1.5, 0.5), (57, 1.5, 0.5), (58, 1.5, 0.5),
    # Bar 3 - Gm7: G, Bb, D, F
    (58, 3.0, 0.5), (60, 3.0, 0.5), (62, 3.0, 0.5), (64, 3.0, 0.5),
    # Bar 4 - Am7: A, C, E, G
    (60, 4.5, 0.5), (62, 4.5, 0.5), (65, 4.5, 0.5), (67, 4.5, 0.5)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Bar 2
    dr = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(dr)
    dr = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    drums.notes.append(dr)
    dr = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.5, end=start + 1.875)
    drums.notes.append(dr)
    dr = pretty_midi.Note(velocity=100, pitch=38, start=start + 2.25, end=start + 2.625)
    drums.notes.append(dr)
    # Hihat on every eighth
    for i in range(0, 4):
        dr = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(dr)

# Sax: Dante - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 - Start motif (F, Ab, Bb, C)
    (53, 1.5, 0.25), (55, 1.75, 0.25), (57, 2.0, 0.25), (58, 2.25, 0.25),
    # Bar 3 - Leave it hanging (G, A)
    (58, 3.0, 0.25), (60, 3.25, 0.25),
    # Bar 4 - Finish it (Bb, C, D, Eb)
    (57, 4.5, 0.25), (58, 4.75, 0.25), (60, 5.0, 0.25), (58, 5.25, 0.25)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
