
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (65, 2.25), (67, 2.625),
    (69, 3.0), (67, 3.375), (65, 3.75), (64, 4.125),
    (62, 4.5), (64, 4.875), (66, 5.25), (67, 5.625)
]
for note, time in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bn)

# Piano: 7th chords on 2 and 4, moving
piano_notes = []
# Bar 2
piano_notes.extend([
    (67, 1.5), (71, 1.5), (72, 1.5), (76, 1.5),  # D7
    (69, 2.0), (73, 2.0), (74, 2.0), (78, 2.0),  # F#7
    (67, 2.5), (71, 2.5), (72, 2.5), (76, 2.5),  # D7
    (71, 3.0), (75, 3.0), (76, 3.0), (80, 3.0)   # A7
])
# Bar 3
piano_notes.extend([
    (71, 3.5), (75, 3.5), (76, 3.5), (80, 3.5),  # A7
    (69, 4.0), (73, 4.0), (74, 4.0), (78, 4.0),  # F#7
    (71, 4.5), (75, 4.5), (76, 4.5), (80, 4.5),  # A7
    (67, 5.0), (71, 5.0), (72, 5.0), (76, 5.0)   # D7
])
for note, time in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(pn)

# Drums for bars 2-4
drum_notes = []
# Bar 2
drum_notes.extend([
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125)
])
# Bar 3
drum_notes.extend([
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375),
    (36, 6.75), (38, 7.125), (42, 7.125)
])
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Sax: motif in D, short, melodic, hanging
sax_notes = [
    (67, 1.5), (69, 1.875), (72, 2.25), (72, 2.625),
    (69, 3.0), (67, 3.375), (72, 3.75), (76, 4.125),
    (72, 4.5), (69, 4.875), (67, 5.25), (72, 5.625)
]
for note, time in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
