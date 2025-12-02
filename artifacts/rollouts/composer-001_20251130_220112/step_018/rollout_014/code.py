
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.75, 0.125),
    (42, 0.875, 0.125), (42, 1.0, 0.125), (42, 1.125, 0.125),
    (42, 1.25, 0.125), (42, 1.375, 0.125),
    (36, 1.5, 0.375),
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F minor, chromatic approaches, no repeated notes
bass_notes = [
    (53, 1.5, 0.375),   # F
    (54, 1.875, 0.375),  # Gb
    (55, 2.25, 0.375),   # G
    (52, 2.625, 0.375),  # E
    (55, 2.875, 0.125),  # G
    (57, 3.0, 0.375),    # A
    (58, 3.375, 0.375),  # Bb
    (56, 3.75, 0.375),   # Ab
    (58, 4.125, 0.125),  # Bb
    (60, 4.25, 0.375),   # C
    (61, 4.625, 0.375),  # Db
    (59, 5.0, 0.375),    # B
    (61, 5.375, 0.125),  # Db
    (63, 5.5, 0.375),    # D
    (64, 5.875, 0.375),  # Eb
    (62, 6.25, 0.375),   # D
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.875, 0.125),  # C7
    (62, 1.875, 0.125),
    (64, 1.875, 0.125),
    (67, 1.875, 0.125),
    # Bar 3
    (65, 3.375, 0.125),  # D7
    (67, 3.375, 0.125),
    (69, 3.375, 0.125),
    (72, 3.375, 0.125),
    # Bar 4
    (60, 4.625, 0.125),  # C7
    (62, 4.625, 0.125),
    (64, 4.625, 0.125),
    (67, 4.625, 0.125),
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.25),     # G
    (64, 1.75, 0.25),    # A
    (65, 2.0, 0.25),     # Bb
    (67, 2.25, 0.25),    # B
    (65, 2.5, 0.25),     # Bb
    (64, 2.75, 0.25),    # A
    (62, 3.0, 0.25),     # G
    (60, 3.25, 0.25),    # F
    (62, 3.5, 0.25),     # G
    (64, 3.75, 0.25),    # A
    (65, 4.0, 0.25),     # Bb
    (67, 4.25, 0.25),    # B
    (65, 4.5, 0.25),     # Bb
    (64, 4.75, 0.25),    # A
    (62, 5.0, 0.25),     # G
    (60, 5.25, 0.25),    # F
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Drums: Fill the bar
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 2.25, 0.125),
    (42, 2.375, 0.125), (42, 2.5, 0.125), (42, 2.625, 0.125),
    (42, 2.75, 0.125), (42, 2.875, 0.125),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.75, 0.125),
    (42, 3.875, 0.125), (42, 4.0, 0.125), (42, 4.125, 0.125),
    (42, 4.25, 0.125), (42, 4.375, 0.125),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 5.25, 0.125),
    (42, 5.375, 0.125), (42, 5.5, 0.125), (42, 5.625, 0.125),
    (42, 5.75, 0.125), (42, 5.875, 0.125),
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
