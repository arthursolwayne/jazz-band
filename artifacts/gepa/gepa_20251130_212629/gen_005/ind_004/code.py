
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
    (36, 0.0, 0.375), (38, 0.375, 0.375),
    (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.0, 0.125), (42, 0.125, 0.125), (42, 0.25, 0.125),
    (42, 0.375, 0.125), (42, 0.5, 0.125), (42, 0.625, 0.125),
    (42, 0.75, 0.125), (42, 0.875, 0.125), (42, 1.0, 0.125),
    (42, 1.125, 0.125), (42, 1.25, 0.125), (42, 1.375, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5, 0.375),   # F
    (46, 1.875, 0.375),  # Gb
    (47, 2.25, 0.375),   # G
    (48, 2.625, 0.375),  # Ab
    (45, 2.999, 0.375),  # F
    (47, 3.375, 0.375),  # G
    (48, 3.75, 0.375),   # Ab
    (49, 4.125, 0.375),  # Bb
    (45, 4.5, 0.375),    # F
    (47, 4.875, 0.375),  # G
    (49, 5.25, 0.375),   # Bb
    (50, 5.625, 0.375),  # B
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (53, 1.875, 0.375),  # F
    (57, 1.875, 0.375),  # Bb
    (60, 1.875, 0.375),  # D
    (62, 1.875, 0.375),  # E
    (53, 2.625, 0.375),
    (57, 2.625, 0.375),
    (60, 2.625, 0.375),
    (62, 2.625, 0.375),
    # Bar 3: F7 on 2 and 4
    (53, 3.375, 0.375),
    (57, 3.375, 0.375),
    (60, 3.375, 0.375),
    (62, 3.375, 0.375),
    (53, 4.125, 0.375),
    (57, 4.125, 0.375),
    (60, 4.125, 0.375),
    (62, 4.125, 0.375),
    # Bar 4: F7 on 2 and 4
    (53, 4.875, 0.375),
    (57, 4.875, 0.375),
    (60, 4.875, 0.375),
    (62, 4.875, 0.375),
    (53, 5.625, 0.375),
    (57, 5.625, 0.375),
    (60, 5.625, 0.375),
    (62, 5.625, 0.375),
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), (38, 1.875, 0.375),
    (36, 2.25, 0.375), (38, 2.625, 0.375),
    (42, 1.5, 0.125), (42, 1.625, 0.125), (42, 1.75, 0.125),
    (42, 1.875, 0.125), (42, 2.0, 0.125), (42, 2.125, 0.125),
    (42, 2.25, 0.125), (42, 2.375, 0.125), (42, 2.5, 0.125),
    (42, 2.625, 0.125), (42, 2.75, 0.125), (42, 2.875, 0.125),
    # Bar 3
    (36, 2.999, 0.375), (38, 3.375, 0.375),
    (36, 3.75, 0.375), (38, 4.125, 0.375),
    (42, 3.0, 0.125), (42, 3.125, 0.125), (42, 3.25, 0.125),
    (42, 3.375, 0.125), (42, 3.5, 0.125), (42, 3.625, 0.125),
    (42, 3.75, 0.125), (42, 3.875, 0.125), (42, 4.0, 0.125),
    (42, 4.125, 0.125), (42, 4.25, 0.125), (42, 4.375, 0.125),
    # Bar 4
    (36, 4.5, 0.375), (38, 4.875, 0.375),
    (36, 5.25, 0.375), (38, 5.625, 0.375),
    (42, 4.5, 0.125), (42, 4.625, 0.125), (42, 4.75, 0.125),
    (42, 4.875, 0.125), (42, 5.0, 0.125), (42, 5.125, 0.125),
    (42, 5.25, 0.125), (42, 5.375, 0.125), (42, 5.5, 0.125),
    (42, 5.625, 0.125), (42, 5.75, 0.125), (42, 5.875, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    (65, 1.5, 0.375),  # G7
    (67, 1.875, 0.375), # A
    (65, 2.25, 0.375),  # G
    # Bar 3: Leave it hanging
    (62, 2.625, 0.375),  # F
    (62, 2.999, 0.375),  # F
    # Bar 4: Come back and finish it
    (65, 3.375, 0.375),  # G
    (67, 3.75, 0.375),   # A
    (65, 4.125, 0.375),  # G
    (62, 4.5, 0.375),    # F
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
