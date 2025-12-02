
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

# Marcus: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5), (61, 1.875), (60, 2.25), (59, 2.625), # Dm7
    (62, 3.0), (61, 3.375), (60, 3.75), (59, 4.125), # Dm7
    (62, 4.5), (61, 4.875), (60, 5.25), (59, 5.625)  # Dm7
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    (62, 1.875), (65, 1.875), (67, 1.875), (70, 1.875),
    # Bar 3: G7 (G B D F)
    (71, 3.375), (74, 3.375), (76, 3.375), (79, 3.375),
    # Bar 4: Cm7 (C Eb G Bb)
    (60, 4.875), (63, 4.875), (67, 4.875), (71, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

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

# Dante: One short motif, make it sing
# Dm scale: D (62), Eb (63), F (65), G (67), A (69)
sax_notes = [
    (62, 1.5), (65, 1.625), (67, 1.75), (62, 1.875),
    (65, 2.5), (67, 2.625), (69, 2.75), (67, 2.875),
    (65, 3.5), (67, 3.625), (62, 3.75), (65, 3.875),
    (67, 4.5), (69, 4.625), (67, 4.75), (65, 4.875)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
