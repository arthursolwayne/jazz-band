
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
    (36, 0.0), (38, 0.375), (42, 0.375), (36, 0.75), (38, 1.125), (42, 1.125), (36, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Fm7 (F, Ab, Bb, D) -> F, Ab, Bb, D
sax_notes = [
    (84, 1.5), (80, 1.625), (81, 1.75), (82, 1.875)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    (78, 1.5), (77, 1.625), (80, 1.75), (81, 1.875)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Piano: F7 on 2 and 4
piano_notes = [
    (84, 1.625), (80, 1.625), (81, 1.625), (82, 1.625),
    (84, 1.875), (80, 1.875), (81, 1.875), (82, 1.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875), (36, 2.25), (38, 2.625), (42, 2.625), (36, 3.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Fm7 -> Ab, Bb, D, F
sax_notes = [
    (80, 3.0), (81, 3.125), (82, 3.25), (84, 3.375)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    (78, 3.0), (77, 3.125), (80, 3.25), (81, 3.375)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Piano: F7 on 2 and 4
piano_notes = [
    (84, 3.125), (80, 3.125), (81, 3.125), (82, 3.125),
    (84, 3.375), (80, 3.375), (81, 3.375), (82, 3.375)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375), (36, 3.75), (38, 4.125), (42, 4.125), (36, 4.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Fm7 -> Bb, D, F, Ab
sax_notes = [
    (81, 4.5), (82, 4.625), (84, 4.75), (80, 4.875)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    (78, 4.5), (77, 4.625), (80, 4.75), (81, 4.875)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Piano: F7 on 2 and 4
piano_notes = [
    (84, 4.625), (80, 4.625), (81, 4.625), (82, 4.625),
    (84, 4.875), (80, 4.875), (81, 4.875), (82, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875), (36, 5.25), (38, 5.625), (42, 5.625), (36, 6.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
