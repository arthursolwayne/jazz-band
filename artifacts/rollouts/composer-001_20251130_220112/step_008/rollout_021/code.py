
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.75, 0.125),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.875, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),
    (65, 3.0, 0.375), (64, 3.375, 0.375), (62, 3.75, 0.375), (60, 4.125, 0.375),
    (62, 4.5, 0.375), (63, 4.875, 0.375), (60, 5.25, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    (62, 1.5, 0.375), (67, 1.5, 0.375), (69, 1.5, 0.375), (72, 1.5, 0.375),
    # Bar 3: G7
    (67, 3.0, 0.375), (72, 3.0, 0.375), (74, 3.0, 0.375), (76, 3.0, 0.375),
    # Bar 4: Cm7
    (60, 4.5, 0.375), (65, 4.5, 0.375), (67, 4.5, 0.375), (72, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 2.25, 0.125),
    (36, 2.625, 0.375), (38, 3.0, 0.375), (42, 3.375, 0.125),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 4.5, 0.125),
    (36, 4.875, 0.375), (38, 5.25, 0.375), (42, 5.625, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Dante on sax: short motif, make it sing
sax_notes = [
    (62, 1.5, 0.75),  # Start the motif on D
    (65, 2.25, 0.375),  # Move to G
    (62, 2.625, 0.375),  # Back to D
    (60, 3.0, 0.375),   # Descend to C
    (62, 3.375, 0.375),  # Back to D
    (65, 3.75, 0.375),  # G again
    (62, 4.125, 0.375),  # D
    (60, 4.5, 0.375),   # C
    (62, 4.875, 0.375),  # D
    (65, 5.25, 0.375),  # G
    (62, 5.625, 0.375)  # D
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
