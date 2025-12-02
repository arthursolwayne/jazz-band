
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
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.375), (38, 3.75), (42, 3.75)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (53, 1.5), (54, 1.75), (52, 2.0), (51, 2.25),
    (53, 2.5), (54, 2.75), (52, 3.0), (51, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
# Bar 2: F7 on beat 2, Bb7 on beat 4
piano_notes = [
    (64, 1.75), (69, 1.75), (67, 1.75), (62, 1.75),
    (62, 2.25), (67, 2.25), (65, 2.25), (60, 2.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Motif - F, G, Ab, F (start at 1.5s)
sax_notes = [
    (84, 1.5), (85, 1.75), (83, 2.0), (84, 2.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (54, 3.0), (53, 3.25), (55, 3.5), (57, 3.75),
    (54, 4.0), (53, 4.25), (55, 4.5), (57, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
# Bar 3: Bb7 on beat 2, Eb7 on beat 4
piano_notes = [
    (62, 3.25), (67, 3.25), (65, 3.25), (60, 3.25),
    (60, 3.75), (65, 3.75), (63, 3.75), (58, 3.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Motif continuation - Bb, C, D, Bb (start at 3.0s)
sax_notes = [
    (83, 3.0), (85, 3.25), (87, 3.5), (83, 3.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (55, 4.5), (57, 4.75), (54, 5.0), (53, 5.25),
    (55, 5.5), (57, 5.75), (54, 6.0), (53, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
# Bar 4: Eb7 on beat 2, Ab7 on beat 4
piano_notes = [
    (60, 4.75), (65, 4.75), (63, 4.75), (58, 4.75),
    (58, 5.25), (63, 5.25), (61, 5.25), (56, 5.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Motif resolution - D, Eb, F, D (start at 4.5s)
sax_notes = [
    (87, 4.5), (88, 4.75), (84, 5.0), (87, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.625), (38, 6.0), (42, 6.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
