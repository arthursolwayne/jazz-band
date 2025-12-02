
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.1875), (42, 0.375), (42, 0.5625),
    (42, 0.75), (42, 0.9375), (42, 1.125), (42, 1.3125), (36, 1.5),
    (38, 1.875), (42, 1.5), (42, 1.6875), (42, 1.875), (42, 2.0625),
    (42, 2.25), (42, 2.4375), (42, 2.625), (42, 2.8125), (42, 3.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, Fm7 -> Bb7 -> Eb7 -> Am7
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (64, 1.5), (65, 1.875), (64, 2.25), (62, 2.625),
    # Bar 3 (3.0 - 4.5s)
    (60, 3.0), (61, 3.375), (62, 3.75), (64, 4.125),
    # Bar 4 (4.5 - 6.0s)
    (65, 4.5), (67, 4.875), (69, 5.25), (71, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (48, 1.75), (50, 1.75), (53, 1.75), (55, 1.75),  # Fm7
    (48, 2.25), (50, 2.25), (53, 2.25), (57, 2.25),  # Bb7
    # Bar 3 (3.0 - 4.5s)
    (53, 3.25), (55, 3.25), (57, 3.25), (60, 3.25),  # Eb7
    (48, 3.75), (50, 3.75), (53, 3.75), (57, 3.75),  # Bb7
    # Bar 4 (4.5 - 6.0s)
    (53, 4.75), (55, 4.75), (57, 4.75), (60, 4.75),  # Eb7
    (48, 5.25), (50, 5.25), (53, 5.25), (57, 5.25)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (72, 1.5), (68, 1.75), (67, 2.0), (68, 2.25),  # motif
    (67, 2.5), (64, 2.75), (65, 3.0), (66, 3.25),  # continuation
    (67, 3.5), (68, 3.75), (69, 4.0), (70, 4.25),  # resolution
    (69, 4.5), (67, 4.75), (64, 5.0), (65, 5.25),  # echo
    (66, 5.5), (67, 5.75)                          # final
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
