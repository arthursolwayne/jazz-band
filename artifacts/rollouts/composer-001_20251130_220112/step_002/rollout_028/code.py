
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
    (36, 2.25), (38, 2.625), (42, 2.625),
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches, never the same note twice
bass_notes = [
    (37, 1.5), (38, 1.875), (39, 2.25), (40, 2.625),
    (41, 3.0), (42, 3.375), (43, 3.75), (44, 4.125),
    (45, 4.5), (46, 4.875), (47, 5.25), (48, 5.625),
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (60, 1.75), (64, 1.75), (67, 1.75), (71, 1.75),
    (61, 2.125), (65, 2.125), (68, 2.125), (72, 2.125),
    # Bar 3 (3.0 - 4.5s)
    (60, 3.25), (64, 3.25), (67, 3.25), (71, 3.25),
    (61, 3.625), (65, 3.625), (68, 3.625), (72, 3.625),
    # Bar 4 (4.5 - 6.0s)
    (60, 4.75), (64, 4.75), (67, 4.75), (71, 4.75),
    (61, 5.125), (65, 5.125), (68, 5.125), (72, 5.125),
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Drums continue (Bar 2-4)
bar_2_3_4_drums = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
]
for note, time in bar_2_3_4_drums:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Saxophone (Dante): short motif, sing it, leave it hanging, come back and finish it
# F7 chord: F, A, C, E
# Motif: F -> Bb -> C -> F, with some space
sax_notes = [
    (65, 1.5), (69, 1.875), (67, 2.25), (65, 2.625),  # Bar 2
    (65, 3.0), (69, 3.375), (67, 3.75), (65, 4.125),  # Bar 3
    (65, 4.5), (69, 4.875), (67, 5.25), (65, 5.625),  # Bar 4
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
