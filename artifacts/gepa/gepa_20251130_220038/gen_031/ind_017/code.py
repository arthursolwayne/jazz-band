
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
    (36, 0.0), (38, 0.375), (42, 0.375), (36, 0.75), (38, 1.125), (42, 1.125), (36, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
# Dm7 -> C -> B -> A -> G -> F -> E -> D -> C -> B -> A -> G -> F -> E -> D -> C
bass_notes = [
    (50, 1.5), (49, 1.875), (48, 2.25), (47, 2.625), (45, 2.875), (44, 3.25), (43, 3.625),
    (50, 3.875), (49, 4.25), (48, 4.625), (47, 5.0), (45, 5.25), (44, 5.625), (43, 6.0)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# G7 = G B D F
# Cm7 = C Eb G Bb
# F7 = F A C E
piano_notes = [
    (50, 1.875), (55, 1.875), (57, 1.875), (60, 1.875),  # Dm7 on 2
    (67, 3.25), (71, 3.25), (69, 3.25), (65, 3.25),     # G7 on 4
    (60, 4.625), (63, 4.625), (67, 4.625), (69, 4.625),  # Cm7 on 2
    (55, 6.0), (58, 6.0), (60, 6.0), (64, 6.0)           # F7 on 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875), (36, 2.25), (38, 2.625), (42, 2.625), (36, 3.0),
    (36, 3.75), (38, 4.125), (42, 4.125), (36, 4.5), (38, 4.875), (42, 4.875), (36, 5.25),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor Sax, one short motif, make it sing
# Dm scale: D F G A Bb C
# Motif: D -> F -> G -> A -> Bb -> A -> G -> F -> D (descending)
sax_notes = [
    (50, 1.5), (52, 1.75), (53, 2.0), (55, 2.25), (57, 2.5), (55, 2.75), (53, 3.0), (52, 3.25), (50, 3.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
