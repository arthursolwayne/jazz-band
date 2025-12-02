
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
# Sax: F -> Bb -> D -> F (motif)
sax_notes = [
    (84, 1.5), (78, 1.875), (70, 2.25), (84, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line F -> Gb -> G -> Ab -> A -> Bb -> B -> C
bass_notes = [
    (53, 1.5), (54, 1.875), (55, 2.25), (56, 2.625),
    (57, 3.0), (58, 3.375), (59, 3.75), (60, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 (F, A, C, Eb)
    (53, 1.875), (64, 1.875), (55, 1.875), (60, 1.875),
    # Bar 2, beat 4: Bb7 (Bb, D, F, Ab)
    (58, 2.625), (69, 2.625), (53, 2.625), (60, 2.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: continue pattern
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 4.125), (38, 4.5), (42, 4.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif
sax_notes = [
    (84, 3.0), (78, 3.375), (70, 3.75), (84, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line F -> Gb -> G -> Ab -> A -> Bb -> B -> C
bass_notes = [
    (53, 3.0), (54, 3.375), (55, 3.75), (56, 4.125),
    (57, 4.5), (58, 4.875), (59, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: F7 (F, A, C, Eb)
    (53, 3.375), (64, 3.375), (55, 3.375), (60, 3.375),
    # Bar 3, beat 4: Bb7 (Bb, D, F, Ab)
    (58, 4.125), (69, 4.125), (53, 4.125), (60, 4.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: continue pattern
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.625), (38, 6.0), (42, 6.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: repeat motif
sax_notes = [
    (84, 4.5), (78, 4.875), (70, 5.25), (84, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line F -> Gb -> G -> Ab -> A -> Bb -> B -> C
bass_notes = [
    (53, 4.5), (54, 4.875), (55, 5.25), (56, 5.625),
    (57, 6.0), (58, 6.375), (59, 6.75), (60, 7.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: F7 (F, A, C, Eb)
    (53, 4.875), (64, 4.875), (55, 4.875), (60, 4.875),
    # Bar 4, beat 4: Bb7 (Bb, D, F, Ab)
    (58, 5.625), (69, 5.625), (53, 5.625), (60, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: continue pattern
drum_notes = [
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
