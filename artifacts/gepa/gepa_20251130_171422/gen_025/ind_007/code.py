
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
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Everybody in (1.5 - 3.0s)
# Sax: F7 -> G7 -> A7 -> G7 (start it, leave it hanging)
sax_notes = [
    (113, 1.5), (115, 1.75), (117, 2.0), (115, 2.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line in F (F -> G -> A -> Bb -> C -> D -> Eb -> F)
bass_notes = [
    (84, 1.5), (85, 1.75), (87, 2.0), (88, 2.25),
    (90, 2.5), (91, 2.75), (92, 3.0), (84, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4 (F7, A7)
piano_notes = [
    # F7: F, A, C, Eb
    (84, 1.75), (87, 1.75), (90, 1.75), (92, 1.75),
    # A7: A, C#, E, G
    (87, 2.25), (90, 2.25), (94, 2.25), (97, 2.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Bar 3: Everybody in (3.0 - 4.5s)
# Sax: Repeat the motif, finish it
sax_notes = [
    (115, 3.0), (117, 3.25), (115, 3.5), (113, 3.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line in F (F -> G -> A -> Bb -> C -> D -> Eb -> F)
bass_notes = [
    (84, 3.0), (85, 3.25), (87, 3.5), (88, 3.75),
    (90, 4.0), (91, 4.25), (92, 4.5), (84, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4 (F7, A7)
piano_notes = [
    # F7: F, A, C, Eb
    (84, 3.25), (87, 3.25), (90, 3.25), (92, 3.25),
    # A7: A, C#, E, G
    (87, 3.75), (90, 3.75), (94, 3.75), (97, 3.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Bar 4: Everybody in (4.5 - 6.0s)
# Sax: End with a Bb7 on the last beat
sax_notes = [
    (110, 4.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line in F (F -> G -> A -> Bb -> C -> D -> Eb -> F)
bass_notes = [
    (84, 4.5), (85, 4.75), (87, 5.0), (88, 5.25),
    (90, 5.5), (91, 5.75), (92, 6.0), (84, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4 (F7, A7)
piano_notes = [
    # F7: F, A, C, Eb
    (84, 4.75), (87, 4.75), (90, 4.75), (92, 4.75),
    # A7: A, C#, E, G
    (87, 5.25), (90, 5.25), (94, 5.25), (97, 5.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
