
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (36, 1.5, 0.375), (38, 1.875, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F, chromatic approaches, no repeated notes
# F7 chord: F, A, C, E
# Walking bass line: F, Gb, G, A, Bb, B, C, Db, D, Eb, E, F#
bass_notes = [
    (44, 1.5, 0.375), (45, 1.875, 0.375), (46, 2.25, 0.375), (47, 2.625, 0.375),
    (48, 3.0, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, F7 and D7
# F7: F, A, C, E
# D7: D, F#, A, C
piano_notes = [
    # Bar 2: F7 on beat 2 (1.875)
    (53, 1.875, 0.375), (58, 1.875, 0.375), (57, 1.875, 0.375), (55, 1.875, 0.375),
    # Bar 2: D7 on beat 4 (2.625)
    (50, 2.625, 0.375), (55, 2.625, 0.375), (58, 2.625, 0.375), (57, 2.625, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Opening motif - simple but expressive
# F, G#, Bb, F (motif)
sax_notes = [
    (53, 1.5, 0.375), (55, 1.875, 0.375), (52, 2.25, 0.375), (53, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line - F, Gb, G, A, Bb, B, C, Db, D, Eb, E, F#
bass_notes = [
    (44, 3.0, 0.375), (45, 3.375, 0.375), (46, 3.75, 0.375), (47, 4.125, 0.375),
    (48, 4.5, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: F7 and D7 on 2 and 4
piano_notes = [
    # Bar 3: F7 on beat 2 (3.375)
    (53, 3.375, 0.375), (58, 3.375, 0.375), (57, 3.375, 0.375), (55, 3.375, 0.375),
    # Bar 3: D7 on beat 4 (4.125)
    (50, 4.125, 0.375), (55, 4.125, 0.375), (58, 4.125, 0.375), (57, 4.125, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Repeat motif with slight variation - F, G#, Bb, A
sax_notes = [
    (53, 3.0, 0.375), (55, 3.375, 0.375), (52, 3.75, 0.375), (57, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: same pattern
drum_notes = [
    # Bar 4
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875), (36, 6.0, 0.375), (38, 6.375, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line - F, Gb, G, A, Bb, B, C, Db, D, Eb, E, F#
bass_notes = [
    (44, 4.5, 0.375), (45, 4.875, 0.375), (46, 5.25, 0.375), (47, 5.625, 0.375),
    (48, 6.0, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: F7 and D7 on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2 (4.875)
    (53, 4.875, 0.375), (58, 4.875, 0.375), (57, 4.875, 0.375), (55, 4.875, 0.375),
    # Bar 4: D7 on beat 4 (5.625)
    (50, 5.625, 0.375), (55, 5.625, 0.375), (58, 5.625, 0.375), (57, 5.625, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Finish the motif - F, G#, Bb, F
sax_notes = [
    (53, 4.5, 0.375), (55, 4.875, 0.375), (52, 5.25, 0.375), (53, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
