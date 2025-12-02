
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875), (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875), (42, 0.5625, 0.1875), (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875), (42, 1.3125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approach to F
bass_notes = [
    (48, 1.5, 0.375), (49, 1.875, 0.375), (50, 2.25, 0.375), (51, 2.625, 0.375),
    (52, 3.0, 0.375)  # Start of bar 3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on bar 2
piano_notes = [
    # Bar 2
    (64, 1.5, 0.1875), (67, 1.5, 0.1875), (69, 1.5, 0.1875), (71, 1.5, 0.1875),  # F7
    (64, 1.875, 0.1875), (67, 1.875, 0.1875), (69, 1.875, 0.1875), (71, 1.875, 0.1875),  # F7
    (64, 2.25, 0.1875), (67, 2.25, 0.1875), (69, 2.25, 0.1875), (71, 2.25, 0.1875),  # F7
    (64, 2.625, 0.1875), (67, 2.625, 0.1875), (69, 2.625, 0.1875), (71, 2.625, 0.1875)  # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif (starts on 1.5s)
sax_notes = [
    (66, 1.5, 0.375), (68, 1.875, 0.375), (69, 2.25, 0.375), (67, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approach to Bb
bass_notes = [
    (52, 3.0, 0.375), (53, 3.375, 0.375), (54, 3.75, 0.375), (55, 4.125, 0.375),
    (56, 4.5, 0.375)  # Start of bar 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on bar 3
piano_notes = [
    # Bar 3
    (64, 3.0, 0.1875), (67, 3.0, 0.1875), (69, 3.0, 0.1875), (71, 3.0, 0.1875),  # F7
    (64, 3.375, 0.1875), (67, 3.375, 0.1875), (69, 3.375, 0.1875), (71, 3.375, 0.1875),  # F7
    (64, 3.75, 0.1875), (67, 3.75, 0.1875), (69, 3.75, 0.1875), (71, 3.75, 0.1875),  # F7
    (64, 4.125, 0.1875), (67, 4.125, 0.1875), (69, 4.125, 0.1875), (71, 4.125, 0.1875)  # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif (continuation)
sax_notes = [
    (66, 3.0, 0.375), (68, 3.375, 0.375), (69, 3.75, 0.375), (67, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 3
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875), (42, 3.1875, 0.1875),
    (42, 3.375, 0.1875), (42, 3.5625, 0.1875), (36, 3.75, 0.375), (38, 4.125, 0.375),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875), (42, 4.3125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approach to C
bass_notes = [
    (56, 4.5, 0.375), (57, 4.875, 0.375), (58, 5.25, 0.375), (59, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on bar 4
piano_notes = [
    # Bar 4
    (64, 4.5, 0.1875), (67, 4.5, 0.1875), (69, 4.5, 0.1875), (71, 4.5, 0.1875),  # F7
    (64, 4.875, 0.1875), (67, 4.875, 0.1875), (69, 4.875, 0.1875), (71, 4.875, 0.1875),  # F7
    (64, 5.25, 0.1875), (67, 5.25, 0.1875), (69, 5.25, 0.1875), (71, 5.25, 0.1875),  # F7
    (64, 5.625, 0.1875), (67, 5.625, 0.1875), (69, 5.625, 0.1875), (71, 5.625, 0.1875)  # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif (finish)
sax_notes = [
    (66, 4.5, 0.375), (68, 4.875, 0.375), (69, 5.25, 0.375), (67, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875), (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875), (42, 5.0625, 0.1875), (36, 5.25, 0.375), (38, 5.625, 0.375),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875), (42, 5.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
