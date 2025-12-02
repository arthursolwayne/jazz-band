
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
    (36, 0.0), (38, 0.375), (42, 0.0),
    (36, 1.125), (38, 1.5), (42, 1.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (62, 1.5, 1.625), (64, 1.625, 1.75), (60, 1.75, 1.875), (62, 1.875, 2.0),
    # Bar 3
    (64, 2.0, 2.125), (65, 2.125, 2.25), (62, 2.25, 2.375), (64, 2.375, 2.5),
    # Bar 4
    (65, 2.5, 2.625), (67, 2.625, 2.75), (64, 2.75, 2.875), (65, 2.875, 3.0)
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.625, 1.75), (67, 1.625, 1.75), (69, 1.625, 1.75), (71, 1.625, 1.75),
    # Bar 3
    (62, 2.25, 2.375), (67, 2.25, 2.375), (69, 2.25, 2.375), (71, 2.25, 2.375),
    # Bar 4
    (62, 2.625, 2.75), (67, 2.625, 2.75), (69, 2.625, 2.75), (71, 2.625, 2.75)
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    (62, 1.5, 1.625), (64, 1.625, 1.75),
    # Bar 3
    (65, 2.0, 2.125), (62, 2.125, 2.25),
    # Bar 4
    (64, 2.5, 2.625), (62, 2.625, 2.75), (64, 2.75, 2.875), (65, 2.875, 3.0)
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# Drums: continue for bars 2-4
drum_notes = [
    (36, 1.5, 1.625), (38, 1.625, 1.75), (42, 1.5, 2.0),
    (36, 2.375, 2.5), (38, 2.5, 2.625), (42, 2.375, 2.875),
    (36, 3.0, 3.125), (38, 3.125, 3.25), (42, 3.0, 3.5)
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
