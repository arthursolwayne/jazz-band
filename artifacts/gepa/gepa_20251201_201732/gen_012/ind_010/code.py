
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
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.375), (42, 0.75), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.875), (42, 2.25), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (D2), walking line with chromatic approaches
# Fm7 -> Bbm7 -> Eb7 -> Am7
bass_notes = [
    (38, 1.5), (39, 1.75), (38, 2.0), (37, 2.25),  # F2 -> Eb -> F2 -> D
    (35, 2.5), (36, 2.75), (35, 3.0), (34, 3.25),  # Bb2 -> A -> Bb2 -> G
    (32, 3.5), (33, 3.75), (32, 4.0), (31, 4.25),  # Eb2 -> D -> Eb2 -> C
    (29, 4.5), (30, 4.75), (29, 5.0), (28, 5.25)   # A2 -> G -> A2 -> F
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, D, C)
    (53, 1.5), (51, 1.5), (55, 1.5), (52, 1.5),
    # Bar 3: Bbm7 (Bb, D, F, Ab)
    (57, 2.5), (55, 2.5), (53, 2.5), (51, 2.5),
    # Bar 4: Eb7 (Eb, G, Bb, D)
    (56, 3.5), (58, 3.5), (57, 3.5), (55, 3.5),
    # Bar 4: Am7 (A, C, E, G)
    (60, 4.5), (62, 4.5), (64, 4.5), (61, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm -> Bb -> Eb -> A
sax_notes = [
    (53, 1.5), (57, 1.75), (56, 2.0), (60, 2.25),
    (53, 2.5), (57, 2.75), (56, 3.0), (60, 3.25),
    (53, 3.5), (57, 3.75), (56, 4.0), (60, 4.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0)
for bar_start in [1.5, 3.0]:
    for beat in [0.0, 1.5]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + beat, end=bar_start + beat + 0.125))
    for beat in [0.375, 1.875]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + beat, end=bar_start + beat + 0.125))
    for beat in [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + beat, end=bar_start + beat + 0.125))

# Bar 3 (3.0 - 4.5)
for bar_start in [3.0, 4.5]:
    for beat in [0.0, 1.5]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + beat, end=bar_start + beat + 0.125))
    for beat in [0.375, 1.875]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + beat, end=bar_start + beat + 0.125))
    for beat in [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + beat, end=bar_start + beat + 0.125))

# Bar 4 (4.5 - 6.0)
for bar_start in [4.5, 6.0]:
    for beat in [0.0, 1.5]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + beat, end=bar_start + beat + 0.125))
    for beat in [0.375, 1.875]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + beat, end=bar_start + beat + 0.125))
    for beat in [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + beat, end=bar_start + beat + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
