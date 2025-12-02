
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
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dm motif, start on D, then F, then G, then Bb
sax_notes = [
    (62, 1.5, 0.375), (65, 1.875, 0.375), (67, 2.25, 0.375), (60, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (50, 1.5, 0.375), (51, 1.875, 0.375), (53, 2.25, 0.375), (52, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, Dm7 on beat 2, F7 on beat 4
piano_notes = [
    # Beat 2: Dm7 (D, F, A, C)
    (62, 1.875, 0.125), (65, 1.875, 0.125), (67, 1.875, 0.125), (60, 1.875, 0.125),
    # Beat 4: F7 (F, A, C, E)
    (65, 2.625, 0.125), (67, 2.625, 0.125), (60, 2.625, 0.125), (64, 2.625, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, but with a slight variation on the last note
sax_notes = [
    (62, 3.0, 0.375), (65, 3.375, 0.375), (67, 3.75, 0.375), (62, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (50, 3.0, 0.375), (51, 3.375, 0.375), (52, 3.75, 0.375), (54, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, Dm7 on beat 2, F7 on beat 4
piano_notes = [
    # Beat 2: Dm7 (D, F, A, C)
    (62, 3.375, 0.125), (65, 3.375, 0.125), (67, 3.375, 0.125), (60, 3.375, 0.125),
    # Beat 4: F7 (F, A, C, E)
    (65, 4.125, 0.125), (67, 4.125, 0.125), (60, 4.125, 0.125), (64, 4.125, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif again, but with a resolution on the last note
sax_notes = [
    (62, 4.5, 0.375), (65, 4.875, 0.375), (67, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (50, 4.5, 0.375), (51, 4.875, 0.375), (52, 5.25, 0.375), (50, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, Dm7 on beat 2, F7 on beat 4
piano_notes = [
    # Beat 2: Dm7 (D, F, A, C)
    (62, 4.875, 0.125), (65, 4.875, 0.125), (67, 4.875, 0.125), (60, 4.875, 0.125),
    # Beat 4: F7 (F, A, C, E)
    (65, 5.625, 0.125), (67, 5.625, 0.125), (60, 5.625, 0.125), (64, 5.625, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (42, 4.5, 0.125),
    (38, 4.875, 0.375), (42, 4.875, 0.125),
    (36, 5.25, 0.375), (42, 5.25, 0.125),
    (38, 5.625, 0.375), (42, 5.625, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
