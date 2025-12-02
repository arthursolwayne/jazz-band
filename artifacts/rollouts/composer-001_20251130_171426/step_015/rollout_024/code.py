
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

# Bass: Walking line, chromatic approaches
bass_notes = [
    (53, 1.5), (55, 1.75), (57, 2.0), (59, 2.25),
    (59, 2.5), (57, 2.75), (55, 3.0), (53, 3.25),
    (53, 3.5), (55, 3.75), (57, 4.0), (59, 4.25),
    (59, 4.5), (57, 4.75), (55, 5.0), (53, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.75), (67, 1.75), (72, 1.75), (74, 1.75),
    # Bar 3
    (62, 3.25), (67, 3.25), (72, 3.25), (74, 3.25),
    # Bar 4
    (62, 4.75), (67, 4.75), (72, 4.75), (74, 4.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F7, Ab7, Bb7, F7
sax_notes = [
    (65, 1.5), (65, 1.75),
    (64, 2.0), (64, 2.25),
    (62, 2.5), (62, 2.75),
    (65, 3.0), (65, 3.25),
    (64, 3.5), (64, 3.75),
    (62, 4.0), (62, 4.25),
    (65, 4.5), (65, 4.75),
    (64, 5.0), (64, 5.25),
    (62, 5.5), (62, 5.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start), (38, start + 0.375), (42, start + 0.375),
        (36, start + 0.75), (38, start + 1.125), (42, start + 1.125),
        (36, start + 1.5), (38, start + 1.875), (42, start + 1.875)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
