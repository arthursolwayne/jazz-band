
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
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875), (42, 1.125), (42, 1.25), 
    (42, 1.375), (42, 1.5)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb
# Walking bass line: F, Gb, Ab, Bb, B, Db, Eb, F
bass_notes = [
    (53, 1.5), (52, 1.875), (55, 2.25), (57, 2.625), (58, 2.875), (50, 3.125), (52, 3.375), (53, 3.75),
    (53, 3.75), (52, 4.125), (55, 4.5), (57, 4.875), (58, 5.125), (50, 5.375), (52, 5.625), (53, 6.0)
]
for note, time in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bn)

# Diane: 7th chords, comp on 2 and 4
# Fm7, Bb7, Eb7, Ab7
piano_notes = [
    # Bar 2: Fm7
    (53, 1.5), (50, 1.5), (57, 1.5), (60, 1.5),
    # Bar 3: Bb7
    (58, 2.875), (55, 2.875), (62, 2.875), (65, 2.875),
    # Bar 4: Eb7
    (52, 4.125), (49, 4.125), (56, 4.125), (59, 4.125),
    # Bar 4: Ab7
    (55, 5.375), (52, 5.375), (59, 5.375), (62, 5.375)
]
for note, time in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(pn)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875), 
    (36, 2.25), (38, 2.625), (42, 2.25), (42, 2.375), (42, 2.5), (42, 2.625), 
    (36, 2.875), (38, 3.125), (42, 2.875), (42, 3.0), (42, 3.125), (42, 3.25), 
    (36, 3.375), (38, 3.75), (42, 3.375), (42, 3.5), (42, 3.625), (42, 3.75), 
    (36, 4.125), (38, 4.5), (42, 4.125), (42, 4.25), (42, 4.375), (42, 4.5), 
    (36, 4.875), (38, 5.25), (42, 4.875), (42, 5.0), (42, 5.125), (42, 5.25), 
    (36, 5.375), (38, 5.75), (42, 5.375), (42, 5.5), (42, 5.625), (42, 5.75), 
    (42, 6.0)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Dante: Tenor sax melody (one short motif, make it sing)
# Motif: F, Gb, Ab, Bb
# Start it, leave it hanging, come back and finish it
sax_notes = [
    (66, 1.5), (64, 1.875), (62, 2.25), (57, 2.625),
    (66, 2.875), (64, 3.25), (62, 3.625), (57, 4.0),
    (66, 4.375), (64, 4.75), (62, 5.125), (57, 5.5),
    (66, 5.875), (64, 6.25), (62, 6.625), (57, 7.0)
]
for note, time in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
