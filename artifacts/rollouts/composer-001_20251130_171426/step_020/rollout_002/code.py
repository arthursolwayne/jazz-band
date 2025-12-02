
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: F (G#) - Bb - A - G (F)
sax_notes = [
    (84, 1.5, 0.375), (81, 1.875, 0.375), (80, 2.25, 0.375), (79, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in F (F - G - A - Bb)
bass_notes = [
    (53, 1.5, 0.375), (55, 1.875, 0.375), (57, 2.25, 0.375), (58, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Bb7 on 2, E7 on 4)
piano_notes = [
    (73, 1.875, 0.375), (71, 1.875, 0.375), (69, 1.875, 0.375), (67, 1.875, 0.375),
    (76, 2.625, 0.375), (74, 2.625, 0.375), (72, 2.625, 0.375), (70, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif with variation (F (G#) - Bb - A - G)
sax_notes = [
    (84, 3.0, 0.375), (81, 3.375, 0.375), (80, 3.75, 0.375), (79, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in F (F - G - A - Bb)
bass_notes = [
    (53, 3.0, 0.375), (55, 3.375, 0.375), (57, 3.75, 0.375), (58, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Bb7 on 2, E7 on 4)
piano_notes = [
    (73, 3.375, 0.375), (71, 3.375, 0.375), (69, 3.375, 0.375), (67, 3.375, 0.375),
    (76, 4.125, 0.375), (74, 4.125, 0.375), (72, 4.125, 0.375), (70, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: complete the motif (F (G#) - Bb - A - G) and hold on G
sax_notes = [
    (84, 4.5, 0.375), (81, 4.875, 0.375), (80, 5.25, 0.375), (79, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in F (F - G - A - Bb)
bass_notes = [
    (53, 4.5, 0.375), (55, 4.875, 0.375), (57, 5.25, 0.375), (58, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Bb7 on 2, E7 on 4)
piano_notes = [
    (73, 4.875, 0.375), (71, 4.875, 0.375), (69, 4.875, 0.375), (67, 4.875, 0.375),
    (76, 5.625, 0.375), (74, 5.625, 0.375), (72, 5.625, 0.375), (70, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (36, 6.0, 0.375), (38, 6.375, 0.375), (42, 6.0, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
