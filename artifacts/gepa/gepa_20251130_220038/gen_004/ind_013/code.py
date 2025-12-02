
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
    # Bar 1 (0.0 - 1.5s)
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (36, 1.5, 0.375),
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Dm (D F A C)
# D (2), F (3), Ab (4), C (5), D (6), F (7), Ab (8), C (9)
bass_notes = [
    (49, 1.5, 0.375), (51, 1.875, 0.375), (53, 2.25, 0.375), (55, 2.625, 0.375),
    (49, 3.0, 0.375), (51, 3.375, 0.375), (53, 3.75, 0.375), (55, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4 (Dm7 = D F A C)
# Comp on beat 2 and 4 of bar 2 (1.875 and 2.625)
diane_notes = [
    # Bar 2 (1.5 - 3.0s)
    (50, 1.875, 0.375), (53, 1.875, 0.375), (57, 1.875, 0.375), (60, 1.875, 0.375),
    (50, 2.625, 0.375), (53, 2.625, 0.375), (57, 2.625, 0.375), (60, 2.625, 0.375)
]
for note, start, duration in diane_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875), (42, 3.0, 0.1875), (36, 3.0, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax motif (Dm scale)
# Start on D (C# in Dm, A# in Ab, etc)
# Motif: D, F, Ab, C (1.5 - 2.0s)
# Leave it hanging at C (2.0 - 2.625s)
# Come back at 3.0s with the same motif
sax_notes = [
    (50, 1.5, 0.375), (52, 1.875, 0.375), (55, 2.25, 0.375), (57, 2.625, 0.375),
    (57, 3.0, 0.375), (55, 3.375, 0.375), (52, 3.75, 0.375), (50, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line in Dm (D F A C)
# D (2), F (3), Ab (4), C (5), D (6), F (7), Ab (8), C (9)
bass_notes = [
    (49, 3.0, 0.375), (51, 3.375, 0.375), (53, 3.75, 0.375), (55, 4.125, 0.375),
    (49, 4.5, 0.375), (51, 4.875, 0.375), (53, 5.25, 0.375), (55, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4 (Dm7 = D F A C)
# Comp on beat 2 and 4 of bar 3 (3.375 and 4.125)
diane_notes = [
    (50, 3.375, 0.375), (53, 3.375, 0.375), (57, 3.375, 0.375), (60, 3.375, 0.375),
    (50, 4.125, 0.375), (53, 4.125, 0.375), (57, 4.125, 0.375), (60, 4.125, 0.375)
]
for note, start, duration in diane_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875), (42, 4.5, 0.1875), (36, 4.5, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax motif (Dm scale)
# Motif: D, F, Ab, C (3.0 - 3.5s)
# Leave it hanging at C (3.5 - 4.125s)
# Come back at 4.5s with the same motif
sax_notes = [
    (50, 3.0, 0.375), (52, 3.375, 0.375), (55, 3.75, 0.375), (57, 4.125, 0.375),
    (57, 4.5, 0.375), (55, 4.875, 0.375), (52, 5.25, 0.375), (50, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line in Dm (D F A C)
# D (2), F (3), Ab (4), C (5), D (6), F (7), Ab (8), C (9)
bass_notes = [
    (49, 4.5, 0.375), (51, 4.875, 0.375), (53, 5.25, 0.375), (55, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4 (Dm7 = D F A C)
# Comp on beat 2 and 4 of bar 4 (4.875 and 5.625)
diane_notes = [
    (50, 4.875, 0.375), (53, 4.875, 0.375), (57, 4.875, 0.375), (60, 4.875, 0.375),
    (50, 5.625, 0.375), (53, 5.625, 0.375), (57, 5.625, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in diane_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875), (42, 6.0, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax motif (Dm scale)
# Motif: D, F, Ab, C (4.5 - 5.0s)
# Leave it hanging at C (5.0 - 5.625s)
# Come back at 6.0s with the same motif
sax_notes = [
    (50, 4.5, 0.375), (52, 4.875, 0.375), (55, 5.25, 0.375), (57, 5.625, 0.375),
    (57, 6.0, 0.375), (55, 6.375, 0.375), (52, 6.75, 0.375), (50, 7.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
