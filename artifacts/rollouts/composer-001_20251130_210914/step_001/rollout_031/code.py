
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
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches
# Dm7: D F A C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [
    (50, 1.5), (51, 1.875), (52, 2.25), (53, 2.625),
    (55, 3.0), (54, 3.375), (56, 3.75), (57, 4.125),
    (50, 4.5), (51, 4.875), (52, 5.25), (53, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords, comp on 2 and 4
# Dm7: D F A C
# G7: G B D F
# Cm7: C Eb G Bb
# F7: F A C Eb
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    (50, 2.25), (53, 2.25), (55, 2.25), (57, 2.25),
    (50, 2.625), (53, 2.625), (55, 2.625), (57, 2.625),
    # Bar 3: G7 on 2 and 4
    (55, 3.375), (58, 3.375), (60, 3.375), (62, 3.375),
    (55, 3.75), (58, 3.75), (60, 3.75), (62, 3.75),
    # Bar 4: Cm7 on 2 and 4
    (52, 4.125), (55, 4.125), (57, 4.125), (59, 4.125),
    (52, 4.5), (55, 4.5), (57, 4.5), (59, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

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

# Dante: Tenor sax. Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D -> Eb -> F -> D
# Bar 2: Start motif
sax_notes = [
    (50, 2.0), (51, 2.125), (52, 2.25),  # D -> Eb -> F
    (50, 4.5), (51, 4.625), (52, 4.75)   # D -> Eb -> F
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
