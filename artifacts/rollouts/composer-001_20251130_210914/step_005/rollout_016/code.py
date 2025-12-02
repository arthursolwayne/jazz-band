
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.125),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.125),
    (42, 1.25, 0.125), (42, 1.375, 0.125), (42, 1.5, 0.125)
]
for note, start, dur in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass - walking line, chromatic approaches
bass_notes = [
    (21, 1.5, 0.25), (22, 1.75, 0.25), (20, 2.0, 0.25), (21, 2.25, 0.25),
    (23, 2.5, 0.25), (24, 2.75, 0.25), (22, 3.0, 0.25), (23, 3.25, 0.25),
    (25, 3.5, 0.25), (26, 3.75, 0.25), (24, 4.0, 0.25), (25, 4.25, 0.25),
    (27, 4.5, 0.25), (28, 4.75, 0.25), (26, 5.0, 0.25), (27, 5.25, 0.25)
]
for note, start, dur in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    bass.notes.append(bn)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    (60, 1.75, 0.25), (64, 1.75, 0.25), (67, 1.75, 0.25),
    (62, 2.25, 0.25), (65, 2.25, 0.25), (68, 2.25, 0.25),
    (60, 3.25, 0.25), (64, 3.25, 0.25), (67, 3.25, 0.25),
    (62, 3.75, 0.25), (65, 3.75, 0.25), (68, 3.75, 0.25)
]
for note, start, dur in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    piano.notes.append(pn)

# Little Ray on drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.125),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.125),
    (42, 2.375, 0.125), (42, 2.5, 0.125), (42, 2.625, 0.125),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.125),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.125),
    (42, 3.875, 0.125), (42, 4.0, 0.125), (42, 4.125, 0.125),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.125),
    (42, 4.625, 0.125), (42, 4.75, 0.125), (42, 4.875, 0.125)
]
for note, start, dur in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    drums.notes.append(dr)

# Dante on sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm7: F, Ab, Bb, D
sax_notes = [
    (65, 1.5, 0.375), (63, 1.875, 0.375), (62, 2.25, 0.375),
    (60, 2.625, 0.375), (62, 3.0, 0.375), (63, 3.375, 0.375),
    (65, 3.75, 0.375), (63, 4.125, 0.375), (62, 4.5, 0.375),
    (60, 4.875, 0.375)
]
for note, start, dur in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
