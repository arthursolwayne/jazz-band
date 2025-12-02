
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
    (42, 1.3125, 0.1875), (36, 1.5, 0.375),
    (38, 1.875, 0.375), (42, 1.5, 0.1875), (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875), (42, 2.0625, 0.1875), (42, 2.25, 0.1875),
    (42, 2.4375, 0.1875), (42, 2.625, 0.1875), (42, 2.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full ensemble
# Bass: Walking line, chromatic approaches
bass_notes = [
    (35, 1.5, 0.375), (34, 1.875, 0.375), (36, 2.25, 0.375), (37, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 (Fm substitute) on beat 2
    (60, 1.875, 0.375), (64, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375),
    # Bar 3: Bb7 on beat 2
    (62, 3.375, 0.375), (65, 3.375, 0.375), (67, 3.375, 0.375), (69, 3.375, 0.375),
    # Bar 4: D7 on beat 2
    (62, 4.875, 0.375), (67, 4.875, 0.375), (71, 4.875, 0.375), (72, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody
# Bar 2: Start the motif
sax_notes = [
    (62, 1.5, 0.25),  # G
    (64, 1.75, 0.25),  # A
    (59, 2.0, 0.25),   # D
    (57, 2.25, 0.25),  # Bb
    (59, 2.5, 0.25),   # D
    (60, 2.75, 0.25),  # C
    (57, 3.0, 0.25),   # Bb
    (59, 3.25, 0.25),  # D
    (62, 3.5, 0.25),   # G
    (64, 3.75, 0.25),  # A
    (65, 4.0, 0.25),   # Bb
    (62, 4.25, 0.25),  # G
    (59, 4.5, 0.25),   # D
    (57, 4.75, 0.25),  # Bb
    (59, 5.0, 0.25),   # D
    (62, 5.25, 0.25)   # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875), (36, 3.0, 0.375),
    (38, 3.375, 0.375), (42, 3.0, 0.1875), (42, 3.1875, 0.1875),
    (42, 3.375, 0.1875), (42, 3.5625, 0.1875), (42, 3.75, 0.1875),
    (42, 3.9375, 0.1875), (42, 4.125, 0.1875), (42, 4.3125, 0.1875),
    # Bar 3
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875), (36, 4.5, 0.375),
    (38, 4.875, 0.375), (42, 4.5, 0.1875), (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875), (42, 5.0625, 0.1875), (42, 5.25, 0.1875),
    (42, 5.4375, 0.1875), (42, 5.625, 0.1875), (42, 5.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Bar 3-4
bass_notes = [
    (37, 3.0, 0.375), (38, 3.375, 0.375), (40, 3.75, 0.375), (39, 4.125, 0.375),
    (37, 4.5, 0.375), (38, 4.875, 0.375), (40, 5.25, 0.375), (39, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Bar 3-4
piano_notes = [
    # Bar 3: D7 on beat 4
    (62, 3.75, 0.375), (67, 3.75, 0.375), (71, 3.75, 0.375), (72, 3.75, 0.375),
    # Bar 4: Fm7 on beat 4
    (53, 5.625, 0.375), (57, 5.625, 0.375), (60, 5.625, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Bar 2-4 (Continuation)
sax_notes = [
    (57, 3.0, 0.25),  # Bb
    (59, 3.25, 0.25),  # D
    (62, 3.5, 0.25),   # G
    (64, 3.75, 0.25),  # A
    (65, 4.0, 0.25),   # Bb
    (62, 4.25, 0.25),  # G
    (59, 4.5, 0.25),   # D
    (57, 4.75, 0.25),  # Bb
    (59, 5.0, 0.25),   # D
    (62, 5.25, 0.25),  # G
    (64, 5.5, 0.25),   # A
    (65, 5.75, 0.25)   # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
