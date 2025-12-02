
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

# Bass line - walking line, chromatic approaches
bass_notes = [
    (44, 1.5), (45, 1.875), (43, 2.25), (42, 2.625),
    (44, 3.0), (45, 3.375), (43, 3.75), (42, 4.125),
    (44, 4.5), (45, 4.875), (43, 5.25), (42, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano - 7th chords, comp on 2 and 4
# F7 on 2, Bb7 on 4, F7 on 2, G7 on 4
piano_notes = [
    # Bar 2 - F7 (F, A, C, E)
    (64, 1.5), (68, 1.5), (67, 1.5), (69, 1.5),
    # Bar 2 - Bb7 (Bb, D, F, Ab)
    (62, 2.25), (65, 2.25), (64, 2.25), (67, 2.25),
    # Bar 3 - F7
    (64, 3.0), (68, 3.0), (67, 3.0), (69, 3.0),
    # Bar 3 - G7 (G, B, D, F)
    (67, 3.75), (71, 3.75), (69, 3.75), (67, 3.75),
    # Bar 4 - F7
    (64, 4.5), (68, 4.5), (67, 4.5), (69, 4.5),
    # Bar 4 - C7 (C, E, G, B)
    (67, 5.25), (71, 5.25), (69, 5.25), (72, 5.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Drums again: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Saxophone - your motif: F, G#, B, D, F (F7 arpeggio with a chromatic approach)
sax_notes = [
    (64, 1.5), (67, 1.875), (69, 2.25), (71, 2.625),
    (64, 3.0), (67, 3.375), (69, 3.75), (71, 4.125),
    (64, 4.5), (67, 4.875), (69, 5.25), (71, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
