
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.375, 0.125),  # Hihat on 1 &
    (38, 0.75, 0.375),   # Snare on 2
    (42, 0.75, 0.125),   # Hihat on 2 &
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.125, 0.125),  # Hihat on 3 &
    (38, 1.5, 0.375),    # Snare on 4
    (42, 1.5, 0.125)     # Hihat on 4 &
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F, Eb, D, C, Bb, A, G, F)
bass_notes = [
    (36, 1.5, 0.375),    # F
    (34, 1.875, 0.375),  # Eb
    (33, 2.25, 0.375),   # D
    (31, 2.625, 0.375),  # C
    (30, 2.875, 0.375),  # Bb
    (29, 3.25, 0.375),   # A
    (28, 3.625, 0.375),  # G
    (36, 4.0, 0.375),    # F
    (34, 4.375, 0.375),  # Eb
    (33, 4.75, 0.375),   # D
    (31, 5.125, 0.375),  # C
    (30, 5.375, 0.375),  # Bb
    (29, 5.75, 0.375),   # A
    (28, 6.0, 0.375)     # G
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane: 7th chords on 2 and 4, comping in Fm (F7, Bb7, Eb7, Ab7)
piano_notes = [
    # Bar 2
    (64, 1.875, 0.125),  # F7: F
    (69, 1.875, 0.125),  # F7: Bb
    (66, 1.875, 0.125),  # F7: E
    (61, 1.875, 0.125),  # F7: A
    # Bar 3
    (69, 3.125, 0.125),  # Bb7: Bb
    (71, 3.125, 0.125),  # Bb7: D
    (66, 3.125, 0.125),  # Bb7: F
    (64, 3.125, 0.125),  # Bb7: Ab
    # Bar 4
    (64, 4.375, 0.125),  # Eb7: Eb
    (69, 4.375, 0.125),  # Eb7: G
    (66, 4.375, 0.125),  # Eb7: Bb
    (61, 4.375, 0.125),  # Eb7: D
    # Bar 4 (2nd half)
    (69, 5.375, 0.125),  # Ab7: Ab
    (71, 5.375, 0.125),  # Ab7: C
    (66, 5.375, 0.125),  # Ab7: Eb
    (64, 5.375, 0.125)   # Ab7: G
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.125),    # Hihat on 1 &
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.125),  # Hihat on 2 &
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.125),   # Hihat on 3 &
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.125),  # Hihat on 4 &
    # Bar 3
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.125),    # Hihat on 1 &
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.125),  # Hihat on 2 &
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.125),   # Hihat on 3 &
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.125),  # Hihat on 4 &
    # Bar 4
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.125),    # Hihat on 1 &
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.125),  # Hihat on 2 &
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.125),   # Hihat on 3 &
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.125)   # Hihat on 4 &
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Dante: Tenor sax melody (Fm, one short motif, leave it hanging, then finish it)
# Melody: F -> Ab -> Bb -> C -> D -> Eb -> F (starts on bar 2, ends on bar 4)
sax_notes = [
    (65, 1.875, 0.375),   # Ab
    (62, 2.25, 0.375),    # Bb
    (60, 2.625, 0.375),   # C
    (59, 3.0, 0.375),     # D
    (57, 3.375, 0.375),   # Eb
    (53, 3.75, 0.375),    # F
    (57, 4.125, 0.375),   # Eb
    (60, 4.5, 0.375),     # C
    (62, 4.875, 0.375),   # Bb
    (65, 5.25, 0.375),    # Ab
    (62, 5.625, 0.375),   # Bb
    (60, 6.0, 0.375)      # C
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
