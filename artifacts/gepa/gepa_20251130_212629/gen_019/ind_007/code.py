
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
    (36, 0.0, 0.375), (42, 0.0, 0.1875),
    (38, 0.375, 0.375), (42, 0.375, 0.1875),
    (36, 0.75, 0.375), (42, 0.75, 0.1875),
    (38, 1.125, 0.375), (42, 1.125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Fm motif - F, Ab, Bb, rest
sax_notes = [
    (84, 1.5, 0.375), (81, 1.875, 0.375), (82, 2.25, 0.375),
    (84, 2.625, 0.1875), (81, 2.8125, 0.1875), (82, 2.8125, 0.1875)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
bass_notes = [
    (53, 1.5, 0.375), (51, 1.875, 0.375), (52, 2.25, 0.375), (55, 2.625, 0.375),
    (53, 2.625, 0.375), (51, 2.8125, 0.375), (52, 3.0, 0.375), (55, 3.375, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 (C, E, G, Bb)
    (60, 1.875, 0.375), (64, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375),
    # Bar 3: Cm7 (Bb, C, Eb, G)
    (64, 2.625, 0.375), (67, 2.625, 0.375), (69, 2.625, 0.375), (71, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration))

# Drums: Bar 2
drum_notes = [
    (36, 1.5, 0.375), (42, 1.5, 0.1875),
    (38, 1.875, 0.375), (42, 1.875, 0.1875),
    (36, 2.25, 0.375), (42, 2.25, 0.1875),
    (38, 2.625, 0.375), (42, 2.625, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, but with slight variation
sax_notes = [
    (84, 3.0, 0.375), (81, 3.375, 0.375), (82, 3.75, 0.375),
    (84, 4.125, 0.1875), (81, 4.3125, 0.1875), (82, 4.3125, 0.1875)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
bass_notes = [
    (55, 3.0, 0.375), (53, 3.375, 0.375), (51, 3.75, 0.375), (52, 4.125, 0.375),
    (55, 4.125, 0.375), (53, 4.5, 0.375), (51, 4.875, 0.375), (52, 5.25, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Fm7 (E, F, Ab, C)
    (64, 3.375, 0.375), (65, 3.375, 0.375), (69, 3.375, 0.375), (72, 3.375, 0.375),
    # Bar 4: Bb7 (A, Bb, D, F)
    (69, 4.125, 0.375), (71, 4.125, 0.375), (74, 4.125, 0.375), (76, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration))

# Drums: Bar 3
drum_notes = [
    (36, 3.0, 0.375), (42, 3.0, 0.1875),
    (38, 3.375, 0.375), (42, 3.375, 0.1875),
    (36, 3.75, 0.375), (42, 3.75, 0.1875),
    (38, 4.125, 0.375), (42, 4.125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Motif variation - rest, Ab, Bb, F
sax_notes = [
    (81, 4.5, 0.375), (82, 4.875, 0.375), (84, 5.25, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
bass_notes = [
    (52, 4.5, 0.375), (55, 4.875, 0.375), (53, 5.25, 0.375), (51, 5.625, 0.375),
    (52, 5.625, 0.375), (55, 5.8125, 0.375), (53, 6.0, 0.375), (51, 6.375, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Ab7 (G, Ab, C, Eb)
    (71, 4.875, 0.375), (72, 4.875, 0.375), (76, 4.875, 0.375), (78, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 0.375), (42, 4.5, 0.1875),
    (38, 4.875, 0.375), (42, 4.875, 0.1875),
    (36, 5.25, 0.375), (42, 5.25, 0.1875),
    (38, 5.625, 0.375), (42, 5.625, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
