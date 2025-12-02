
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
# Bass: D2 (38) -> F (43), chromatic approach to F
bass_notes = [
    (38, 1.5), (39, 1.625), (43, 1.75),
    (43, 2.0), (42, 2.125), (43, 2.25),
    (38, 2.5), (39, 2.625), (43, 2.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (65, 1.5), (68, 1.5), (69, 1.5), (72, 1.5),
    # Bar 3: Gm7 (G, Bb, D, F)
    (67, 2.0), (70, 2.0), (71, 2.0), (72, 2.0),
    # Bar 4: C7 (C, E, G, Bb)
    (69, 2.5), (72, 2.5), (74, 2.5), (71, 2.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F -> G -> Bb -> F (motif)
sax_notes = [
    (69, 1.5), (71, 1.75), (70, 2.0), (69, 2.25),
    (71, 2.5), (70, 2.75), (69, 3.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F (43) -> A (46), chromatic approach to A
bass_notes = [
    (43, 3.0), (44, 3.125), (46, 3.25),
    (46, 3.5), (45, 3.625), (46, 3.75),
    (43, 4.0), (44, 4.125), (46, 4.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Piano: Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    (67, 3.0), (70, 3.0), (71, 3.0), (72, 3.0),
    # Bar 4: C7 (C, E, G, Bb)
    (69, 3.5), (72, 3.5), (74, 3.5), (71, 3.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: A (46) -> C (49), chromatic approach to C
bass_notes = [
    (46, 4.5), (47, 4.625), (49, 4.75),
    (49, 5.0), (48, 5.125), (49, 5.25),
    (46, 5.5), (47, 5.625), (49, 5.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Piano: Bar 4: C7 (C, E, G, Bb)
piano_notes = [
    (69, 5.0), (72, 5.0), (74, 5.0), (71, 5.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.125))

# Sax: Finish the motif
sax_notes = [
    (71, 5.0), (70, 5.25), (69, 5.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
