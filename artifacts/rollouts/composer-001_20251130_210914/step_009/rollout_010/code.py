
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

# Bass line: walking chromatic line
bass_notes = [
    (62, 1.5), (63, 1.75), (60, 2.0), (62, 2.25),
    (63, 2.5), (65, 2.75), (67, 3.0), (65, 3.25),
    (63, 3.5), (62, 3.75), (60, 4.0), (62, 4.25),
    (63, 4.5), (65, 4.75), (67, 5.0), (65, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (64, 2.0), (67, 2.0), (72, 2.0), (74, 2.0),  # D7
    # Bar 3
    (64, 3.5), (67, 3.5), (72, 3.5), (74, 3.5),  # D7
    # Bar 4
    (64, 5.0), (67, 5.0), (72, 5.0), (74, 5.0)   # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4
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

# Sax: One short motif, make it sing
sax_notes = [
    (62, 1.5), (65, 1.75), (67, 2.0), (65, 2.25),  # D, F#, G, F#
    (62, 2.5), (60, 2.75), (62, 3.0), (65, 3.25),  # D, C, D, F#
    (67, 3.5), (65, 3.75), (62, 4.0), (60, 4.25),  # G, F#, D, C
    (62, 4.5), (65, 4.75), (67, 5.0), (65, 5.25)   # D, F#, G, F#
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
