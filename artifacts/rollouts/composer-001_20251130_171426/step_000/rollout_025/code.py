
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: Dm melody (D, F, G, Bb) - short motif, start it, leave it hanging
# Bar 2: D (D4), F (F4), G (G4), Bb (Bb4)
sax_notes = [
    (62, 1.5), (65, 1.75), (67, 2.0), (69, 2.25),  # Bar 2
    (62, 2.5), (65, 2.75), (67, 3.0), (69, 3.25),  # Bar 3
    (62, 3.5), (65, 3.75), (67, 4.0), (69, 4.25),  # Bar 4
    (62, 4.5), (65, 4.75), (67, 5.0)               # End on G, leave it hanging
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2
    (50, 1.5), (51, 1.75), (52, 2.0), (50, 2.25),
    # Bar 3
    (50, 2.5), (51, 2.75), (52, 3.0), (50, 3.25),
    # Bar 4
    (50, 3.5), (51, 3.75), (52, 4.0), (50, 4.25),
    # Bar 4 (extension)
    (50, 4.5), (51, 4.75), (52, 5.0)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, Dm7, F7, Bb7
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (62, 1.75), (65, 1.75), (69, 1.75), (67, 1.75),
    # Bar 3: F7 (F, A, C, E)
    (65, 2.75), (69, 2.75), (67, 2.75), (71, 2.75),
    # Bar 4: Bb7 (Bb, D, F, A)
    (69, 3.75), (72, 3.75), (67, 3.75), (69, 3.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 0.875))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.5))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.25))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.125, end=bar_start + i * 0.125 + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
