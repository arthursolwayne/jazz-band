
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm (F2, Ab2, Bb2, D2)
bass_notes = [
    (71, 1.5), (70, 1.875), (72, 2.25), (69, 2.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Piano: Fm7 -> Bb7 -> Eb7 -> Am7
# Open voicings, comp on 2 and 4
piano_notes = [
    # Bar 2 - Fm7 (F, Ab, Bb, D)
    (65, 1.5), (63, 1.5), (62, 1.5), (67, 1.5),
    # Bar 3 - Bb7 (Bb, D, F, Ab)
    (62, 2.625), (67, 2.625), (65, 2.625), (63, 2.625),
    # Bar 4 - Eb7 (Eb, G, Bb, D)
    (60, 3.75), (67, 3.75), (62, 3.75), (67, 3.75),
    # Bar 4 - Am7 (A, C, E, G)
    (69, 4.125), (60, 4.125), (64, 4.125), (67, 4.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Motif - F, Ab, Bb, G (start on 1.5, leave it hanging)
sax_notes = [
    (65, 1.5), (63, 1.875), (62, 2.25), (67, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Fm (F2, Ab2, Bb2, D2)
bass_notes = [
    (71, 3.0), (70, 3.375), (72, 3.75), (69, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Piano: Bb7 -> Eb7 -> Am7 -> Dm7
piano_notes = [
    # Bar 3 - Bb7 (Bb, D, F, Ab)
    (62, 3.0), (67, 3.0), (65, 3.0), (63, 3.0),
    # Bar 4 - Eb7 (Eb, G, Bb, D)
    (60, 4.125), (67, 4.125), (62, 4.125), (67, 4.125),
    # Bar 4 - Am7 (A, C, E, G)
    (69, 4.5), (60, 4.5), (64, 4.5), (67, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Fm (F2, Ab2, Bb2, D2)
bass_notes = [
    (71, 4.5), (70, 4.875), (72, 5.25), (69, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Piano: Am7 -> Dm7 -> Gm7 -> Cm7 (resolve on last)
piano_notes = [
    # Bar 4 - Am7 (A, C, E, G)
    (69, 4.5), (60, 4.5), (64, 4.5), (67, 4.5),
    # Bar 4 - Dm7 (D, F, A, C)
    (62, 5.25), (65, 5.25), (69, 5.25), (60, 5.25),
    # Bar 4 - Gm7 (G, Bb, D, F)
    (67, 5.625), (62, 5.625), (62, 5.625), (65, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Finish the motif - F, Ab, Bb, G (start on 4.5, resolve cleanly)
sax_notes = [
    (65, 4.5), (63, 4.875), (62, 5.25), (67, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
