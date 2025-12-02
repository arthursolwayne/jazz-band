
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.1875), (42, 0.375), (42, 0.5625),
    (42, 0.75), (42, 0.9375), (42, 1.125), (42, 1.3125), (36, 1.5), (38, 1.875),
    (42, 1.5), (42, 1.6875), (42, 1.875), (42, 2.0625), (42, 2.25), (42, 2.4375),
    (42, 2.625), (42, 2.8125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (65, 1.5), (66, 1.875), (64, 2.25), (62, 2.625), (63, 3.0), (65, 3.375),
    (66, 3.75), (64, 4.125), (62, 4.5), (63, 4.875), (65, 5.25), (66, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 2.0), (71, 2.0), (74, 2.0), (69, 2.0),  # D7
    (67, 3.0), (71, 3.0), (74, 3.0), (69, 3.0),  # D7
    (67, 4.0), (71, 4.0), (74, 4.0), (69, 4.0)   # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (64, 1.875), (65, 2.25), (64, 2.625),  # D, E, F#, E
    (62, 3.0), (64, 3.375), (65, 3.75), (64, 4.125),  # D, E, F#, E
    (62, 4.5), (64, 4.875), (65, 5.25), (64, 5.625)   # D, E, F#, E
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
