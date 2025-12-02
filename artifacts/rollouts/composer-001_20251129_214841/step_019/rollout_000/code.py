
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in C, chromatic approaches
bass_notes = [
    (60, 1.5, 0.375), (61, 1.875, 0.375), (62, 2.25, 0.375), (64, 2.625, 0.375),
    (65, 3.0, 0.375), (64, 3.375, 0.375), (63, 3.75, 0.375), (62, 4.125, 0.375),
    (60, 4.5, 0.375), (61, 4.875, 0.375), (62, 5.25, 0.375), (64, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane: 7th chords on 2 and 4, comping
piano_notes = [
    (60, 1.5, 0.1875), (64, 1.5, 0.1875), (67, 1.5, 0.1875), (71, 1.5, 0.1875),
    (62, 2.25, 0.1875), (66, 2.25, 0.1875), (69, 2.25, 0.1875), (72, 2.25, 0.1875),
    (60, 3.0, 0.1875), (64, 3.0, 0.1875), (67, 3.0, 0.1875), (71, 3.0, 0.1875),
    (62, 3.75, 0.1875), (66, 3.75, 0.1875), (69, 3.75, 0.1875), (72, 3.75, 0.1875)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375), (65, 1.875, 0.375), (67, 2.25, 0.375),
    (65, 2.625, 0.375), (62, 3.0, 0.375), (64, 3.375, 0.375),
    (67, 3.75, 0.375), (65, 4.125, 0.375), (62, 4.5, 0.375),
    (64, 4.875, 0.375), (67, 5.25, 0.375), (65, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
