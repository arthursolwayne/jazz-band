
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
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (42, 1.25), (42, 1.375), (42, 1.5)
]

for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (36, 1.5, 100), (38, 1.875, 100), (39, 2.25, 100), (40, 2.625, 100),
    # Bar 3
    (41, 3.0, 100), (42, 3.375, 100), (43, 3.75, 100), (44, 4.125, 100),
    # Bar 4
    (45, 4.5, 100), (46, 4.875, 100), (47, 5.25, 100), (48, 5.625, 100)
]
for pitch, time, vel in bass_notes:
    n = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(n)

# Diane on piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bar 2: comp on beat 2
piano_notes = [
    # Bar 2
    (53, 1.875, 100), (50, 1.875, 100), (55, 1.875, 100), (52, 1.875, 100),
    # Bar 3
    (53, 3.375, 100), (50, 3.375, 100), (55, 3.375, 100), (52, 3.375, 100),
    # Bar 4
    (53, 4.875, 100), (50, 4.875, 100), (55, 4.875, 100), (52, 4.875, 100)
]
for pitch, time, vel in piano_notes:
    n = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(n)

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.25), (42, 2.375), (42, 2.5), (42, 2.625),
    (42, 2.75), (42, 2.875), (42, 3.0),
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 3.75), (42, 3.875), (42, 4.0), (42, 4.125),
    (42, 4.25), (42, 4.375), (42, 4.5),
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.25), (42, 5.375), (42, 5.5), (42, 5.625),
    (42, 5.75), (42, 5.875), (42, 6.0)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Dante on sax: short motif, leave it hanging
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F, Gb, Ab, A (1.5 - 2.25s)
# Then leave it hanging (2.25 - 2.625s)
# Come back and finish it (3.0 - 3.75s)
sax_notes = [
    # First motif
    (53, 1.5, 110), (54, 1.875, 110), (56, 2.25, 110), (57, 2.625, 110),
    # Leave it hanging
    (57, 2.625, 110), (57, 2.75, 110), (57, 2.875, 110), (57, 3.0, 110),
    # Finish the motif
    (56, 3.0, 110), (54, 3.375, 110), (53, 3.75, 110)
]
for pitch, time, vel in sax_notes:
    n = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
