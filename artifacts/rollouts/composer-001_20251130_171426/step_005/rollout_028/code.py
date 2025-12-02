
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
    (36, 1.125), (38, 1.5), (42, 1.5),
    (36, 2.0), (38, 2.375), (42, 2.375),
    (36, 3.125), (38, 3.5), (42, 3.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif starts here
sax_notes = [
    (62, 1.5), (67, 1.875), (60, 2.25), (64, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.875), (61, 2.25), (64, 2.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (69, 1.875), (71, 1.875), (72, 1.875), (74, 1.875),
    (72, 2.625), (74, 2.625), (76, 2.625), (77, 2.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: continue
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.875), (38, 4.25), (42, 4.25)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: motif repeats, but with variation
sax_notes = [
    (62, 3.0), (67, 3.375), (60, 3.75), (64, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line, chromatic approaches
bass_notes = [
    (62, 3.0), (63, 3.375), (61, 3.75), (64, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (69, 3.375), (71, 3.375), (72, 3.375), (74, 3.375),
    (72, 4.125), (74, 4.125), (76, 4.125), (77, 4.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: continue
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.375), (38, 5.75), (42, 5.75)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: motif resolves
sax_notes = [
    (62, 4.5), (67, 4.875), (60, 5.25), (64, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line, chromatic approaches
bass_notes = [
    (62, 4.5), (63, 4.875), (61, 5.25), (64, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (69, 4.875), (71, 4.875), (72, 4.875), (74, 4.875),
    (72, 5.625), (74, 5.625), (76, 5.625), (77, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: continue
drum_notes = [
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
