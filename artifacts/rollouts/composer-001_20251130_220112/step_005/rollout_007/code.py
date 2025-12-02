
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
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F, with chromatic approaches
bass_notes = [
    (45, 1.5), (47, 1.875), (46, 2.25), (44, 2.625),
    (45, 3.0), (47, 3.375), (46, 3.75), (44, 4.125),
    (45, 4.5), (47, 4.875), (46, 5.25), (44, 5.625)
]
for note, time in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.875), (64, 1.875), (65, 1.875), (67, 1.875), # F7
    # Bar 3 (3.0 - 4.5s)
    (62, 3.375), (64, 3.375), (66, 3.375), (67, 3.375), # Fm7
    # Bar 4 (4.5 - 6.0s)
    (62, 4.875), (64, 4.875), (65, 4.875), (67, 4.875)  # F7
]
for note, time in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(pn)

# Sax: short motif, start at 1.5s
# F (61), A (65), B (62), F (61) - ascending then descending
sax_notes = [
    (61, 1.5), (65, 1.875), (62, 2.25), (61, 2.625),
    (61, 3.0), (65, 3.375), (62, 3.75), (61, 4.125),
    (61, 4.5), (65, 4.875), (62, 5.25), (61, 5.625)
]
for note, time in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
