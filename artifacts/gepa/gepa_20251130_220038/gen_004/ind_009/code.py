
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875), (36, 1.125), (38, 1.5),
    (42, 1.125), (42, 1.25), (42, 1.375), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (Fm7)
    (48, 1.5), (47, 1.875), (49, 2.25), (50, 2.625),
    # Bar 3 (Fm7)
    (48, 2.875), (47, 3.25), (49, 3.625), (50, 4.0),
    # Bar 4 (Fm7)
    (48, 4.25), (47, 4.625), (49, 5.0), (50, 5.375)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (48, 1.875), (50, 1.875), (53, 1.875), (57, 1.875),
    # Bar 3
    (48, 3.25), (50, 3.25), (53, 3.25), (57, 3.25),
    # Bar 4
    (48, 4.625), (50, 4.625), (53, 4.625), (57, 4.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (42, 2.0), (42, 2.125), (42, 2.25), (42, 2.375), (36, 2.625), (38, 3.0),
    (42, 2.625), (42, 2.75), (42, 2.875), (42, 3.0),
    # Bar 3
    (36, 3.25), (38, 3.625), (42, 3.25), (42, 3.375), (42, 3.5), (42, 3.625),
    (42, 3.75), (42, 3.875), (42, 4.0), (42, 4.125), (36, 4.375), (38, 4.75),
    (42, 4.375), (42, 4.5), (42, 4.625), (42, 4.75),
    # Bar 4
    (36, 5.0), (38, 5.375), (42, 5.0), (42, 5.125), (42, 5.25), (42, 5.375),
    (42, 5.5), (42, 5.625), (42, 5.75), (42, 5.875), (36, 6.125), (38, 6.5),
    (42, 6.125), (42, 6.25), (42, 6.375), (42, 6.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (start motif)
    (53, 1.5), (57, 1.875), (55, 2.25),
    # Bar 3 (leave it hanging)
    (57, 2.625), (55, 2.875), (53, 3.125),
    # Bar 4 (come back and finish it)
    (57, 3.5), (55, 3.75), (53, 4.0), (57, 4.375), (55, 4.625), (53, 4.875),
    (57, 5.125), (55, 5.375), (53, 5.625), (57, 5.875), (55, 6.125), (53, 6.375)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
