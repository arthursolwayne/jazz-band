
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

# Bass: Walking line, chromatic approaches
bass_notes = [
    (45, 1.5, 0.375), (46, 1.875, 0.375), (44, 2.25, 0.375), (45, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875, 0.375), (64, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375),
    # Bar 3
    (62, 2.625, 0.375), (64, 2.625, 0.375), (67, 2.625, 0.375), (69, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif - start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    (66, 1.5, 0.375), (69, 1.875, 0.375), (66, 2.25, 0.375),
    # Bar 3
    (69, 2.625, 0.375), (66, 2.625, 0.375), (69, 3.0, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (46, 3.0, 0.375), (47, 3.375, 0.375), (45, 3.75, 0.375), (46, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3
    (62, 3.375, 0.375), (64, 3.375, 0.375), (67, 3.375, 0.375), (69, 3.375, 0.375),
    # Bar 4
    (62, 4.125, 0.375), (64, 4.125, 0.375), (67, 4.125, 0.375), (69, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Continue motif
sax_notes = [
    # Bar 3
    (69, 3.0, 0.375), (66, 3.375, 0.375), (69, 3.75, 0.375),
    # Bar 4
    (71, 4.125, 0.375), (69, 4.5, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 4
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875), (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875), (42, 5.0625, 0.1875), (36, 5.25, 0.375), (38, 5.625, 0.375),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875), (42, 5.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line, chromatic approaches
bass_notes = [
    (46, 4.5, 0.375), (47, 4.875, 0.375), (45, 5.25, 0.375), (46, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4
    (62, 4.875, 0.375), (64, 4.875, 0.375), (67, 4.875, 0.375), (69, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Finish motif
sax_notes = [
    (66, 4.5, 0.375), (69, 4.875, 0.375), (66, 5.25, 0.375), (69, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
