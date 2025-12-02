
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
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (57, 1.5), (58, 1.75), (59, 2.0), (60, 2.25),
    (60, 2.5), (59, 2.75), (58, 3.0), (57, 3.25),
    (56, 3.5), (57, 3.75), (58, 4.0), (59, 4.25),
    (59, 4.5), (58, 4.75), (57, 5.0), (56, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 1.75), (64, 1.75), (67, 1.75), (69, 1.75),
    (60, 3.25), (64, 3.25), (67, 3.25), (69, 3.25),
    (60, 4.75), (64, 4.75), (67, 4.75), (69, 4.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (65, 1.75), (62, 2.0),
    (65, 2.25), (62, 2.5), (65, 2.75),
    (62, 3.0), (65, 3.25), (62, 3.5),
    (65, 3.75), (62, 4.0), (65, 4.25),
    (62, 4.5), (65, 4.75), (62, 5.0), (65, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
