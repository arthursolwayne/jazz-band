
import pretty_midi

midi = pretty_midi.PrettyMIDI(tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: chromatic walking line starting on C
bass_notes = [
    (60, 1.5, 1.5), (61, 1.5, 1.5), (62, 1.5, 1.5), (63, 1.5, 1.5),
    (64, 3.0, 1.5), (65, 3.0, 1.5), (66, 3.0, 1.5), (67, 3.0, 1.5)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    (71, 1.5, 1.5), (70, 1.5, 1.5), (67, 1.5, 1.5), (69, 1.5, 1.5),
    (71, 3.0, 1.5), (70, 3.0, 1.5), (67, 3.0, 1.5), (69, 3.0, 1.5)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: short motif starting on C, ending on E, with a suspension
sax_notes = [
    (60, 1.5, 1.75), (62, 1.75, 2.0), (64, 2.0, 2.25), (64, 2.25, 2.5)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: chromatic walking line starting on C
bass_notes = [
    (68, 3.0, 1.5), (69, 3.0, 1.5), (70, 3.0, 1.5), (71, 3.0, 1.5),
    (72, 4.5, 1.5), (73, 4.5, 1.5), (74, 4.5, 1.5), (75, 4.5, 1.5)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    (71, 3.0, 1.5), (70, 3.0, 1.5), (67, 3.0, 1.5), (69, 3.0, 1.5),
    (71, 4.5, 1.5), (70, 4.5, 1.5), (67, 4.5, 1.5), (69, 4.5, 1.5)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: continuation of motif, descending 3rd
sax_notes = [
    (62, 3.0, 3.25), (60, 3.25, 3.5), (59, 3.5, 3.75), (60, 3.75, 4.0)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: chromatic walking line starting on C
bass_notes = [
    (76, 4.5, 1.5), (77, 4.5, 1.5), (78, 4.5, 1.5), (79, 4.5, 1.5),
    (80, 6.0, 1.5), (81, 6.0, 1.5), (82, 6.0, 1.5), (83, 6.0, 1.5)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    (71, 4.5, 1.5), (70, 4.5, 1.5), (67, 4.5, 1.5), (69, 4.5, 1.5),
    (71, 6.0, 1.5), (70, 6.0, 1.5), (67, 6.0, 1.5), (69, 6.0, 1.5)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: resolution of motif, ending on G
sax_notes = [
    (64, 4.5, 4.75), (62, 4.75, 5.0), (60, 5.0, 5.25), (67, 5.25, 5.5)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (36, 6.0, 0.375), (38, 6.375, 0.375), (42, 6.0, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
