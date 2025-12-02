
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone: Whispering motif
sax_notes = [
    (65, 1.5), (67, 1.875), (64, 2.25),
    (62, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Bass: Walking line with chromatic approach
bass_notes = [
    (46, 1.5), (48, 1.875), (47, 2.25), (45, 2.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (62, 1.875), (64, 1.875), (67, 1.875), (69, 1.875),
    (60, 2.625), (62, 2.625), (65, 2.625), (67, 2.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.625), (38, 3.0), (42, 3.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone: Development of the motif
sax_notes = [
    (62, 3.0), (64, 3.375), (65, 3.75),
    (67, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Bass: Walking line with chromatic approach
bass_notes = [
    (45, 3.0), (47, 3.375), (49, 3.75), (46, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (60, 3.375), (62, 3.375), (65, 3.375), (67, 3.375),
    (62, 4.125), (64, 4.125), (67, 4.125), (69, 4.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 4.125), (38, 4.5), (42, 4.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone: Cry, resolve the motif
sax_notes = [
    (67, 4.5), (65, 4.875), (64, 5.25),
    (62, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Bass: Walking line with chromatic approach
bass_notes = [
    (46, 4.5), (47, 4.875), (48, 5.25), (45, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (62, 4.875), (64, 4.875), (67, 4.875), (69, 4.875),
    (60, 5.625), (62, 5.625), (65, 5.625), (67, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.625), (38, 6.0), (42, 6.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
