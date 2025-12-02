
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
    (36, 0.0), (38, 0.375), (42, 0.1875),
    (36, 0.75), (38, 1.125), (42, 0.9375),
    (36, 1.5), (38, 1.875), (42, 1.6875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (47, 2.625),
    (48, 3.0), (49, 3.375), (47, 3.75), (50, 4.125),
    (51, 4.5), (52, 4.875), (50, 5.25), (53, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.875), (64, 1.875), (67, 1.875), (71, 1.875),
    # Bar 3
    (62, 3.375), (66, 3.375), (69, 3.375), (72, 3.375),
    # Bar 4
    (60, 4.875), (64, 4.875), (67, 4.875), (71, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0),
    (60, 2.5), (62, 2.75), (64, 3.0),
    (62, 3.5), (64, 3.75), (62, 4.0),
    (60, 4.5), (62, 4.75), (64, 5.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
