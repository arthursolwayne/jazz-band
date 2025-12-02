
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in C, chromatic approaches
bass_notes = [
    (60, 1.5), (61, 1.75), (62, 2.0), (63, 2.25),
    (64, 2.5), (65, 2.75), (66, 3.0), (67, 3.25),
    (68, 3.5), (69, 3.75), (70, 4.0), (71, 4.25),
    (72, 4.5), (71, 4.75), (70, 5.0), (69, 5.25)
]
for note, time in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bn)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.75), (67, 1.75), (71, 1.75), (72, 1.75),
    # Bar 3
    (64, 3.25), (67, 3.25), (71, 3.25), (72, 3.25),
    # Bar 4
    (64, 4.75), (67, 4.75), (71, 4.75), (72, 4.75)
]
for note, time in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(pn)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Dante: Tenor sax motif
sax_notes = [
    (62, 1.5), (64, 1.75), (65, 2.0),
    (64, 2.5), (62, 2.75), (60, 3.0),
    (62, 3.5), (64, 3.75), (65, 4.0),
    (64, 4.5), (62, 4.75), (60, 5.0)
]
for note, time in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
