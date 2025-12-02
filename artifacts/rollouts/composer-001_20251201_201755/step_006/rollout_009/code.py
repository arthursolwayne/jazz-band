
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
    (36, 0.0), (38, 0.375), (42, 0.375),  # 1
    (36, 0.75), (38, 1.125), (42, 1.125), # 2
    (36, 1.5), (38, 1.875), (42, 1.875),  # 3
    (36, 2.25), (38, 2.625), (42, 2.625)  # 4
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    (43, 1.5), (41, 1.875), (42, 2.25), (43, 2.625)  # Dm -> F -> Eb -> Dm
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
piano_notes = [
    (62, 1.5), (64, 1.5), (67, 1.5), (71, 1.5),
    (64, 1.875), (67, 1.875), (71, 1.875),
    (62, 2.25), (64, 2.25), (67, 2.25), (71, 2.25),
    (64, 2.625), (67, 2.625), (71, 2.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (65, 1.875), (67, 2.25), (65, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    (43, 3.0), (41, 3.375), (42, 3.75), (43, 4.125)  # Dm -> F -> Eb -> Dm
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (B, D, G, D)
piano_notes = [
    (71, 3.0), (74, 3.0), (76, 3.0), (74, 3.0),
    (74, 3.375), (76, 3.375),
    (71, 3.75), (74, 3.75), (76, 3.75), (74, 3.75),
    (74, 4.125), (76, 4.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Continue motif, leave it hanging
sax_notes = [
    (71, 3.0), (69, 3.375), (67, 3.75), (69, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    (43, 4.5), (41, 4.875), (42, 5.25), (43, 5.625)  # Dm -> F -> Eb -> Dm
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (E, G, C, F)
piano_notes = [
    (64, 4.5), (67, 4.5), (72, 4.5), (76, 4.5),
    (67, 4.875), (72, 4.875), (76, 4.875),
    (64, 5.25), (67, 5.25), (72, 5.25), (76, 5.25),
    (67, 5.625), (72, 5.625), (76, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Finish the motif
sax_notes = [
    (62, 4.5), (65, 4.875), (67, 5.25), (65, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),  # 1
    (36, 5.25), (38, 5.625), (42, 5.625), # 2
    (36, 5.625), (38, 5.875), (42, 5.875),  # 3
    (36, 6.0), (38, 6.125), (42, 6.125)  # 4
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
