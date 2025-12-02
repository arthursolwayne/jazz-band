
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
# Fm7 = F, Ab, Bb, D
# Walking bass line in Fm: F, Gb, G, Ab, Bb, B, C, Db, D, Eb, E, F
bass_notes = [
    (53, 1.5), (52, 1.875), (54, 2.25), (55, 2.625),
    (55, 3.0), (56, 3.375), (57, 3.75), (54, 4.125),
    (55, 4.5), (56, 4.875), (57, 5.25), (53, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
# Fm7 on 1, Ab7 on 2, Bb7 on 3, D7 on 4
piano_notes = [
    # Bar 2
    (53, 1.5), (60, 1.5), (62, 1.5), (67, 1.5),  # Fm7
    (60, 1.875), (62, 1.875), (64, 1.875), (69, 1.875),  # Ab7
    (53, 2.25), (60, 2.25), (62, 2.25), (67, 2.25),  # Fm7
    (60, 2.625), (62, 2.625), (64, 2.625), (69, 2.625),  # Ab7

    # Bar 3
    (53, 3.0), (60, 3.0), (62, 3.0), (67, 3.0),  # Fm7
    (60, 3.375), (62, 3.375), (64, 3.375), (69, 3.375),  # Ab7
    (53, 3.75), (60, 3.75), (62, 3.75), (67, 3.75),  # Fm7
    (60, 4.125), (62, 4.125), (64, 4.125), (69, 4.125),  # Ab7

    # Bar 4
    (53, 4.5), (60, 4.5), (62, 4.5), (67, 4.5),  # Fm7
    (60, 4.875), (62, 4.875), (64, 4.875), (69, 4.875),  # Ab7
    (53, 5.25), (60, 5.25), (62, 5.25), (67, 5.25),  # Fm7
    (60, 5.625), (62, 5.625), (64, 5.625), (69, 5.625)   # Ab7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax motif - short, singable, leave it hanging
# F, Ab, Bb, Eb (motif), then repeat and end on Eb
sax_notes = [
    (53, 1.5), (55, 1.875), (57, 2.25), (63, 2.625),
    (53, 3.0), (55, 3.375), (57, 3.75), (63, 4.125),
    (63, 4.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
