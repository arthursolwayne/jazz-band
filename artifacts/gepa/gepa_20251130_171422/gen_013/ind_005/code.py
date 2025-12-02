
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
    # Bar 1 (0.0 - 1.5s)
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5), (63, 1.75), (60, 2.0), (62, 2.25),
    (64, 2.5), (65, 2.75), (62, 3.0), (64, 3.25),
    (66, 3.5), (67, 3.75), (64, 4.0), (66, 4.25),
    (68, 4.5), (69, 4.75), (66, 5.0), (68, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (64, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),  # D7
    (64, 2.5), (67, 2.5), (69, 2.5), (71, 2.5),  # D7
    # Bar 3 (3.0 - 4.5s)
    (64, 3.5), (67, 3.5), (71, 3.5), (72, 3.5),  # G7
    (64, 4.0), (67, 4.0), (71, 4.0), (72, 4.0),  # G7
    # Bar 4 (4.5 - 6.0s)
    (64, 5.0), (67, 5.0), (69, 5.0), (71, 5.0),  # D7
    (64, 5.5), (67, 5.5), (69, 5.5), (71, 5.5),  # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0), (64, 2.25),
    (66, 2.5), (64, 2.75), (65, 3.0),
    (67, 3.5), (66, 3.75), (64, 4.0), (65, 4.25),
    (67, 4.5), (65, 4.75), (64, 5.0), (62, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Bar 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.25), (42, 2.375), (42, 2.5), (42, 2.625),
    # Bar 3 (3.0 - 4.5s)
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 3.75), (42, 3.875), (42, 4.0), (42, 4.125),
    # Bar 4 (4.5 - 6.0s)
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.25), (42, 5.375), (42, 5.5), (42, 5.625),
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
