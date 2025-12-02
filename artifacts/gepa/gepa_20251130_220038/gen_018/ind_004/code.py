
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

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.75), (60, 2.0), (62, 2.25),
    (63, 2.5), (64, 2.75), (62, 3.0), (60, 3.25),
    (62, 3.5), (63, 3.75), (64, 4.0), (62, 4.25),
    (63, 4.5), (64, 4.75), (62, 5.0), (60, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (67, 2.0), (69, 2.0), (64, 2.0), (65, 2.0),  # Dm7 at bar 2
    (71, 3.0), (73, 3.0), (68, 3.0), (69, 3.0),  # Gm7 at bar 3
    (74, 4.0), (76, 4.0), (71, 4.0), (72, 4.0),  # Cm7 at bar 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm - D, F, Ab, C
sax_notes = [
    (62, 1.5), (65, 1.75), (67, 2.0), (69, 2.25),  # motif
    (67, 2.75), (69, 3.0), (65, 3.25), (62, 3.5),  # return
    (65, 4.0), (67, 4.25), (69, 4.5), (67, 4.75)   # resolution
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
