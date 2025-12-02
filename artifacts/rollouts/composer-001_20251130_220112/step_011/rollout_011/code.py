
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

# Marcus: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5), (60, 1.875), (59, 2.25), (62, 2.625),
    (62, 3.0), (60, 3.375), (59, 3.75), (62, 4.125),
    (62, 4.5), (60, 4.875), (59, 5.25), (62, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (57, 2.0), (60, 2.0), (62, 2.0), (59, 2.0),  # Dm7
    (67, 3.0), (70, 3.0), (72, 3.0), (69, 3.0),  # Gm7
    (67, 4.0), (70, 4.0), (72, 4.0), (69, 4.0)   # Gm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax melody (start at bar 2)
sax_notes = [
    (62, 1.5), (65, 1.75), (67, 2.0), (65, 2.25),  # start with a motif
    (62, 2.5), (65, 2.75), (67, 3.0), (65, 3.25),  # repeat the motif
    (62, 3.5), (65, 3.75), (67, 4.0), (65, 4.25),  # repeat again
    (62, 4.5), (65, 4.75), (67, 5.0), (65, 5.25)   # leave it hanging
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
