
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

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (37, 1.5), (39, 1.875), (36, 2.25), (38, 2.625),
    (40, 3.0), (42, 3.375), (41, 3.75), (43, 4.125),
    (44, 4.5), (46, 4.875), (45, 5.25), (47, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (50, 2.625), (53, 2.625), (57, 2.625), (60, 2.625),  # F7
    (52, 4.125), (55, 4.125), (59, 4.125), (62, 4.125),  # Ab7
    (50, 5.625), (53, 5.625), (57, 5.625), (60, 5.625)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = bar * 1.5
    drum_notes = [
        (36, start_time), (38, start_time + 0.375), (42, start_time + 0.375),
        (36, start_time + 0.75), (38, start_time + 1.125), (42, start_time + 1.125),
        (36, start_time + 1.5), (38, start_time + 1.875), (42, start_time + 1.875)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F, Ab, Bb, F (first bar), then leave it hanging, resolve on the second pass
sax_notes = [
    (53, 1.5), (55, 1.75), (57, 2.0), (53, 2.25),  # First phrase
    (53, 3.0), (55, 3.25), (57, 3.5), (53, 3.75),  # Second phrase
    (53, 4.5), (55, 4.75), (57, 5.0), (53, 5.25)   # Third phrase
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
