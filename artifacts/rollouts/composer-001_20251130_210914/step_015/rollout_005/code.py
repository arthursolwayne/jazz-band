
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
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875),
    (36, 1.125), (38, 1.5), (42, 1.125), (42, 1.25), (42, 1.375), (42, 1.5)
]

for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: F, Bb, D, Eb
note_lengths = [0.375, 0.375, 0.375, 0.375]
sax_notes = [
    (84, 1.5), (78, 1.875), (71, 2.25), (69, 2.625)
]
for pitch, time in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + note_lengths[i])
    sax.notes.append(n)
i = 0

# Bass: Walking line in F (F, G, A, Bb), chromatic approach to F
bass_notes = [
    (53, 1.5), (55, 1.875), (57, 2.25), (58, 2.625)
]
for pitch, time in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    # F7 on beat 2 (1.875)
    (53, 1.875), (57, 1.875), (60, 1.875), (62, 1.875),
    # Bb7 on beat 4 (2.625)
    (58, 2.625), (62, 2.625), (65, 2.625), (67, 2.625)
]
for pitch, time in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif starting on Bb
sax_notes = [
    (78, 3.0), (71, 3.375), (69, 3.75), (66, 4.125)
]
for pitch, time in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + note_lengths[i])
    sax.notes.append(n)
i = 0

# Bass: Walking line in F (F, G, A, Bb)
bass_notes = [
    (53, 3.0), (55, 3.375), (57, 3.75), (58, 4.125)
]
for pitch, time in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    (53, 3.375), (57, 3.375), (60, 3.375), (62, 3.375),
    (58, 4.125), (62, 4.125), (65, 4.125), (67, 4.125)
]
for pitch, time in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif starting on D
sax_notes = [
    (71, 4.5), (69, 4.875), (66, 5.25), (64, 5.625)
]
for pitch, time in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + note_lengths[i])
    sax.notes.append(n)
i = 0

# Bass: Walking line in F (F, G, A, Bb)
bass_notes = [
    (53, 4.5), (55, 4.875), (57, 5.25), (58, 5.625)
]
for pitch, time in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    (53, 4.875), (57, 4.875), (60, 4.875), (62, 4.875),
    (58, 5.625), (62, 5.625), (65, 5.625), (67, 5.625)
]
for pitch, time in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(n)

# Drums: Bar 3 and 4
drum_notes = [
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (42, 3.5), (42, 3.625), (42, 3.75), (42, 3.875),
    (36, 4.125), (38, 4.5), (42, 4.125), (42, 4.25), (42, 4.375), (42, 4.5),
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (42, 5.0), (42, 5.125), (42, 5.25), (42, 5.375),
    (36, 5.625), (38, 6.0), (42, 5.625), (42, 5.75), (42, 5.875), (42, 6.0)
]

for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
