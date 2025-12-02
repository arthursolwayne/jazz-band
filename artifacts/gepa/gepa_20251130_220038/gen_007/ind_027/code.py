
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

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.875), (47, 2.25), (44, 2.625),
    (45, 3.0), (46, 3.375), (47, 3.75), (44, 4.125),
    (45, 4.5), (46, 4.875), (47, 5.25), (44, 5.625)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.5), (65, 1.5), (67, 1.5), (69, 1.5),  # F7
    (62, 2.25), (65, 2.25), (67, 2.25), (69, 2.25),  # F7
    # Bar 3
    (62, 3.0), (65, 3.0), (67, 3.0), (71, 3.0),  # Fmaj7
    (62, 3.75), (65, 3.75), (67, 3.75), (71, 3.75),  # Fmaj7
    # Bar 4
    (62, 4.5), (65, 4.5), (67, 4.5), (69, 4.5),  # F7
    (62, 5.25), (65, 5.25), (67, 5.25), (69, 5.25)   # F7
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (66, 1.5), (69, 1.875), (67, 2.25),  # motif starts
    (66, 2.625), (69, 2.875), (67, 3.0),  # leave it hanging
    (66, 3.375), (69, 3.75), (67, 4.125),  # come back
    (66, 4.5), (69, 4.875), (67, 5.25)    # finish it
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Drums: continue for bars 2-4
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dantes_intro.mid")
