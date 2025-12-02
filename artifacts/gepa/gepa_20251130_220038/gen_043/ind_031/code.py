
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
# Bass line - walking line, chromatic approaches
bass_notes = [
    (42, 1.5), (43, 1.75), (41, 2.0), (40, 2.25),
    (42, 2.5), (43, 2.75), (41, 3.0), (40, 3.25),
    (42, 3.5), (43, 3.75), (41, 4.0), (40, 4.25),
    (42, 4.5), (43, 4.75), (41, 5.0), (40, 5.25)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.75), (66, 1.75), (67, 1.75),
    (62, 2.25), (66, 2.25), (67, 2.25),
    # Bar 3 (3.0 - 4.5s)
    (62, 3.25), (66, 3.25), (67, 3.25),
    (62, 3.75), (66, 3.75), (67, 3.75),
    # Bar 4 (4.5 - 6.0s)
    (62, 4.75), (66, 4.75), (67, 4.75),
    (62, 5.25), (66, 5.25), (67, 5.25)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax - melody: one short motif, make it sing
sax_notes = [
    (43, 1.5), (41, 1.75), (43, 2.0),
    (41, 2.5), (42, 2.75), (45, 3.0),
    (43, 3.5), (41, 3.75), (43, 4.0),
    (41, 4.5), (42, 4.75), (45, 5.0),
    (43, 5.5), (41, 5.75), (43, 6.0)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')
