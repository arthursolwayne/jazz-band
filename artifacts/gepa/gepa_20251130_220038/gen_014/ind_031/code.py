
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
    (36, 0.0), (38, 0.375), (42, 0.375), (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (39, 1.5), (41, 1.875), (40, 2.25), (38, 2.625),
    (40, 3.0), (42, 3.375), (41, 3.75), (39, 4.125),
    (41, 4.5), (43, 4.875), (42, 5.25), (40, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (43, 2.25), (47, 2.25), (49, 2.25), (50, 2.25),
    # Bar 3
    (43, 3.75), (47, 3.75), (49, 3.75), (50, 3.75),
    # Bar 4
    (43, 5.25), (47, 5.25), (49, 5.25), (50, 5.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: short motif, starts on 2nd beat of bar 2, ends on 3rd beat of bar 3
# Fm7 -> Gb -> Bb -> C -> Fm7
sax_notes = [
    (53, 2.0),  # Gb
    (55, 2.375), # Bb
    (57, 2.75),  # C
    (53, 3.125), # Gb
    (55, 3.5),   # Bb
    (57, 3.875), # C
    (53, 4.25),  # Gb
    (55, 4.625), # Bb
    (57, 5.0),   # C
    (53, 5.375)  # Gb
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.125))

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    bar_start = bar * 1.5
    drum_notes = [
        (36, bar_start), (38, bar_start + 0.375), (42, bar_start + 0.375),
        (36, bar_start + 0.75), (38, bar_start + 1.125), (42, bar_start + 1.125),
        (36, bar_start + 1.5)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
