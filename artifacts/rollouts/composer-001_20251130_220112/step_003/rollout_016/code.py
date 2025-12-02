
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    (45, 3.0), (46, 3.375), (44, 3.75), (43, 4.125),
    (45, 4.5), (46, 4.875), (44, 5.25), (43, 5.625),
    (45, 6.0)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 3.0), (64, 3.0), (62, 3.0), (61, 3.0),  # F7
    (60, 3.375), (64, 3.375), (62, 3.375), (61, 3.375),  # F7
    # Bar 3
    (63, 4.5), (67, 4.5), (65, 4.5), (64, 4.5),  # Bb7
    (63, 4.875), (67, 4.875), (65, 4.875), (64, 4.875),  # Bb7
    # Bar 4
    (60, 6.0), (64, 6.0), (62, 6.0), (61, 6.0)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, Db, D
sax_notes = [
    (53, 1.5), (51, 1.875), (50, 2.25), (53, 2.625),  # motif
    (53, 3.0), (51, 3.375), (50, 3.75), (53, 4.125),  # repeat
    (53, 4.5), (51, 4.875), (50, 5.25), (53, 5.625)   # complete
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
