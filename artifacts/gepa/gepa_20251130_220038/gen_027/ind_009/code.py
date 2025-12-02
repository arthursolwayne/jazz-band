
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
    (42, 1.3125, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dm motif, one phrase, leave it hanging
sax_notes = [
    (62, 1.5, 0.375), (65, 1.875, 0.375), (62, 2.25, 0.375),
    (60, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (50, 1.5, 0.375), (49, 1.875, 0.375), (51, 2.25, 0.375), (50, 2.625, 0.375),
    (52, 3.0, 0.375), (51, 3.375, 0.375), (50, 3.75, 0.375), (49, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (50, 1.5, 0.375), (53, 1.5, 0.375), (57, 1.5, 0.375), (60, 1.5, 0.375),
    (52, 2.25, 0.375), (55, 2.25, 0.375), (59, 2.25, 0.375), (62, 2.25, 0.375),
    (50, 3.0, 0.375), (53, 3.0, 0.375), (57, 3.0, 0.375), (60, 3.0, 0.375),
    (52, 3.75, 0.375), (55, 3.75, 0.375), (59, 3.75, 0.375), (62, 3.75, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat the motif, then resolve
sax_notes = [
    (62, 3.0, 0.375), (65, 3.375, 0.375), (62, 3.75, 0.375),
    (60, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (50, 3.0, 0.375), (49, 3.375, 0.375), (51, 3.75, 0.375), (50, 4.125, 0.375),
    (52, 4.5, 0.375), (51, 4.875, 0.375), (50, 5.25, 0.375), (49, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (50, 3.0, 0.375), (53, 3.0, 0.375), (57, 3.0, 0.375), (60, 3.0, 0.375),
    (52, 3.75, 0.375), (55, 3.75, 0.375), (59, 3.75, 0.375), (62, 3.75, 0.375),
    (50, 4.5, 0.375), (53, 4.5, 0.375), (57, 4.5, 0.375), (60, 4.5, 0.375),
    (52, 5.25, 0.375), (55, 5.25, 0.375), (59, 5.25, 0.375), (62, 5.25, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolve the motif
sax_notes = [
    (62, 4.5, 0.375), (65, 4.875, 0.375), (62, 5.25, 0.375),
    (60, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (50, 4.5, 0.375), (49, 4.875, 0.375), (51, 5.25, 0.375), (50, 5.625, 0.375),
    (52, 6.0, 0.375), (51, 6.375, 0.375), (50, 6.75, 0.375), (49, 7.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (50, 4.5, 0.375), (53, 4.5, 0.375), (57, 4.5, 0.375), (60, 4.5, 0.375),
    (52, 5.25, 0.375), (55, 5.25, 0.375), (59, 5.25, 0.375), (62, 5.25, 0.375),
    (50, 6.0, 0.375), (53, 6.0, 0.375), (57, 6.0, 0.375), (60, 6.0, 0.375),
    (52, 6.75, 0.375), (55, 6.75, 0.375), (59, 6.75, 0.375), (62, 6.75, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 4
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875),
    (36, 6.0, 0.375), (38, 6.375, 0.375), (42, 6.0, 0.1875),
    (42, 6.1875, 0.1875), (42, 6.375, 0.1875), (42, 6.5625, 0.1875),
    (42, 6.75, 0.1875), (42, 6.9375, 0.1875), (42, 7.125, 0.1875),
    (42, 7.3125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
