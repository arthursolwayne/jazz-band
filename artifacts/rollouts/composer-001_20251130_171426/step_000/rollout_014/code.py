
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
    (36, 1.125), (38, 1.5), (42, 1.125),
    (36, 2.25), (38, 2.625), (42, 2.25),
    (36, 3.375), (38, 3.75), (42, 3.375)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.75), (60, 2.0), (61, 2.25),
    (62, 2.5), (63, 2.75), (60, 3.0), (61, 3.25)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords comping on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.75), (67, 1.75), (69, 1.75), (71, 1.75),
    (62, 2.25), (67, 2.25), (69, 2.25), (71, 2.25),
    # Bar 3
    (62, 2.75), (67, 2.75), (69, 2.75), (71, 2.75),
    (62, 3.25), (67, 3.25), (69, 3.25), (71, 3.25)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: Motif - Dm7 -> Dm9 -> Gm7 -> Bbm7 (start at 1.5s)
sax_notes = [
    (62, 1.5), (62, 1.5), (64, 1.75), (67, 2.0),
    (62, 2.25), (62, 2.25), (64, 2.5), (67, 2.75),
    (65, 3.0), (65, 3.0), (67, 3.25), (70, 3.5),
    (62, 3.75), (62, 3.75), (64, 4.0), (67, 4.25)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Dm, chromatic approaches
bass_notes = [
    (62, 3.0), (63, 3.25), (60, 3.5), (61, 3.75),
    (62, 4.0), (63, 4.25), (60, 4.5), (61, 4.75)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords comping on 2 and 4
piano_notes = [
    # Bar 3
    (62, 3.25), (67, 3.25), (69, 3.25), (71, 3.25),
    (62, 3.75), (67, 3.75), (69, 3.75), (71, 3.75),
    # Bar 4
    (62, 4.25), (67, 4.25), (69, 4.25), (71, 4.25),
    (62, 4.75), (67, 4.75), (69, 4.75), (71, 4.75)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: Leave it hanging (no resolution in bar 3)
sax_notes = [
    (62, 3.0), (62, 3.0), (64, 3.25), (67, 3.5),
    (62, 3.75), (62, 3.75), (64, 4.0), (67, 4.25),
    (65, 4.5), (65, 4.5), (67, 4.75), (70, 5.0)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Dm, chromatic approaches
bass_notes = [
    (62, 4.5), (63, 4.75), (60, 5.0), (61, 5.25),
    (62, 5.5), (63, 5.75), (60, 6.0), (61, 6.25)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords comping on 2 and 4
piano_notes = [
    # Bar 4
    (62, 4.75), (67, 4.75), (69, 4.75), (71, 4.75),
    (62, 5.25), (67, 5.25), (69, 5.25), (71, 5.25),
    (62, 5.75), (67, 5.75), (69, 5.75), (71, 5.75),
    (62, 6.25), (67, 6.25), (69, 6.25), (71, 6.25)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: Finish the motif with a resolution to Gm7
sax_notes = [
    (65, 4.5), (65, 4.5), (67, 4.75), (70, 5.0),
    (65, 5.25), (65, 5.25), (67, 5.5), (70, 5.75),
    (62, 6.0), (62, 6.0), (64, 6.25), (67, 6.5)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.75), (42, 4.5),
    (36, 5.625), (38, 5.875), (42, 5.625),
    (36, 6.75), (38, 7.0), (42, 6.75)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
