
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.1875), (42, 0.375),
    (42, 0.5625), (42, 0.75), (42, 0.9375), (42, 1.125), (42, 1.3125),
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.6875), (42, 1.875),
    (42, 2.0625), (42, 2.25), (42, 2.4375), (42, 2.625), (42, 2.8125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, never the same note twice
bass_notes = [
    (48, 1.5), (49, 1.875), (50, 2.25), (51, 2.625),
    (52, 2.875), (53, 3.25), (54, 3.625), (55, 4.0),
    (53, 4.375), (52, 4.75), (51, 5.125), (50, 5.5)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25): Fm7
    (53, 1.5), (50, 1.5), (52, 1.5), (55, 1.5),
    # Bar 3 (2.875 - 3.625): Bbm7
    (57, 2.875), (54, 2.875), (56, 2.875), (59, 2.875),
    # Bar 4 (4.375 - 5.125): Ebm7
    (58, 4.375), (55, 4.375), (57, 4.375), (60, 4.375)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (59, 1.5), (62, 1.875), (60, 2.25), (58, 2.625),
    (59, 3.0), (62, 3.375), (60, 3.75), (58, 4.125),
    (60, 4.5), (62, 4.875), (60, 5.25), (58, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
