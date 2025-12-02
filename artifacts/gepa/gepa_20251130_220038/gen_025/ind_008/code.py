
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
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches
bass_notes = [
    (48, 1.5), (49, 1.75), (47, 2.0), (45, 2.25),
    (48, 2.5), (49, 2.75), (47, 3.0), (45, 3.25),
    (48, 3.5), (49, 3.75), (47, 4.0), (45, 4.25),
    (48, 4.5), (49, 4.75), (47, 5.0), (45, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords on 2 and 4, Fm7, Bb7, Fm7, Bb7
piano_notes = [
    # Bar 2
    (45, 2.0), (48, 2.0), (50, 2.0), (52, 2.0),
    # Bar 3
    (48, 3.0), (51, 3.0), (53, 3.0), (55, 3.0),
    # Bar 4
    (45, 4.0), (48, 4.0), (50, 4.0), (52, 4.0),
    # Bar 5
    (48, 5.0), (51, 5.0), (53, 5.0), (55, 5.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.75), (42, 1.75),
    (36, 2.25), (38, 2.5), (42, 2.5),
    (36, 3.0), (38, 3.25), (42, 3.25),
    (36, 3.75), (38, 4.0), (42, 4.0),
    (36, 4.5), (38, 4.75), (42, 4.75),
    (36, 5.25), (38, 5.5), (42, 5.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: One short motif, start it, leave it hanging, come back and finish it
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F, Ab, Bb, C (Fm triad with chromatic tension)
sax_notes = [
    (53, 1.5), (50, 1.75), (51, 2.0), (55, 2.25),
    (53, 3.0), (50, 3.25), (51, 3.5), (55, 3.75),
    (53, 4.5), (50, 4.75), (51, 5.0), (55, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
