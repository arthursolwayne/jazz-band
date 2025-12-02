
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

# Bass line: walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5), (64, 1.875), (61, 2.25), (60, 2.625),
    (62, 3.0), (64, 3.375), (61, 3.75), (60, 4.125),
    (62, 4.5), (64, 4.875), (61, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Dm7 = D F A C
piano_notes = [
    (62, 3.0), (65, 3.0), (67, 3.0), (69, 3.0),  # Dm7
    (65, 3.375), (67, 3.375), (69, 3.375), (71, 3.375),  # F7
    (62, 4.5), (65, 4.5), (67, 4.5), (69, 4.5),  # Dm7
    (65, 4.875), (67, 4.875), (69, 4.875), (71, 4.875)  # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: D - F - A - C
sax_notes = [
    (62, 1.5), (65, 1.875), (67, 2.25), (69, 2.625),  # start the motif
    (62, 3.0), (65, 3.375), (67, 3.75), (69, 4.125),  # repeat it
    (62, 4.5), (65, 4.875), (67, 5.25), (69, 5.625)   # finish it
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
