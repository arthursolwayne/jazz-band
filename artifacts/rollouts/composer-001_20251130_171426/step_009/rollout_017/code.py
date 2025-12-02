
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Snare on 2 and 4, hihat on every eighth, kick on 1 and 3
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375), (38, 0.75, 0.375), (42, 0.0, 0.125),
    (42, 0.125, 0.125), (42, 0.25, 0.125), (42, 0.375, 0.125),
    (42, 0.5, 0.125), (42, 0.625, 0.125), (42, 0.75, 0.125),
    (42, 0.875, 0.125), (36, 1.125, 0.375), (38, 1.5, 0.375),
    (42, 1.5, 0.125), (42, 1.625, 0.125), (42, 1.75, 0.125),
    (42, 1.875, 0.125), (42, 2.0, 0.125), (42, 2.125, 0.125),
    (42, 2.25, 0.125), (42, 2.375, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dm melody - D, Eb, F, G, F, Eb, D, C
sax_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (65, 2.25, 0.375),
    (67, 2.625, 0.375), (65, 2.625, 0.375), (63, 2.625, 0.375),
    (62, 2.625, 0.375), (60, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Dm - D, Eb, F, G
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (65, 2.25, 0.375),
    (67, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 - Dm7 on 2, F7 on 4
piano_notes = [
    # Dm7 on 2 (1.875)
    (62, 1.875, 0.375), (64, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375),
    # F7 on 4 (2.625)
    (65, 2.625, 0.375), (67, 2.625, 0.375), (70, 2.625, 0.375), (72, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif but with variation - D, Eb, F
sax_notes = [
    (62, 3.0, 0.375), (63, 3.375, 0.375), (65, 3.75, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Dm - G, A, Bb, C
bass_notes = [
    (67, 3.0, 0.375), (69, 3.375, 0.375), (70, 3.75, 0.375),
    (72, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 - Dm7 on 2, F7 on 4
piano_notes = [
    # Dm7 on 2 (3.375)
    (62, 3.375, 0.375), (64, 3.375, 0.375), (67, 3.375, 0.375), (69, 3.375, 0.375),
    # F7 on 4 (4.125)
    (65, 4.125, 0.375), (67, 4.125, 0.375), (70, 4.125, 0.375), (72, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.125),
    (42, 3.125, 0.125), (42, 3.25, 0.125), (42, 3.375, 0.125),
    (42, 3.5, 0.125), (42, 3.625, 0.125), (42, 3.75, 0.125),
    (42, 3.875, 0.125), (36, 4.125, 0.375), (38, 4.5, 0.375),
    (42, 4.5, 0.125), (42, 4.625, 0.125), (42, 4.75, 0.125),
    (42, 4.875, 0.125), (42, 5.0, 0.125), (42, 5.125, 0.125),
    (42, 5.25, 0.125), (42, 5.375, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Resolve motif - D, C, Bb, A
sax_notes = [
    (62, 4.5, 0.375), (60, 4.875, 0.375), (70, 5.25, 0.375),
    (69, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Dm - C, D, Eb, F
bass_notes = [
    (72, 4.5, 0.375), (62, 4.875, 0.375), (63, 5.25, 0.375),
    (65, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 - Dm7 on 2, F7 on 4
piano_notes = [
    # Dm7 on 2 (4.875)
    (62, 4.875, 0.375), (64, 4.875, 0.375), (67, 4.875, 0.375), (69, 4.875, 0.375),
    # F7 on 4 (5.625)
    (65, 5.625, 0.375), (67, 5.625, 0.375), (70, 5.625, 0.375), (72, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 4
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.125),
    (42, 4.625, 0.125), (42, 4.75, 0.125), (42, 4.875, 0.125),
    (42, 5.0, 0.125), (42, 5.125, 0.125), (42, 5.25, 0.125),
    (42, 5.375, 0.125), (36, 5.625, 0.375), (38, 6.0, 0.375),
    (42, 6.0, 0.125), (42, 6.125, 0.125), (42, 6.25, 0.125),
    (42, 6.375, 0.125), (42, 6.5, 0.125), (42, 6.625, 0.125),
    (42, 6.75, 0.125), (42, 6.875, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
