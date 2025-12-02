
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
    (36, 0.0, 0.375), (38, 0.375, 0.375),
    (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.0, 0.125), (42, 0.125, 0.125),
    (42, 0.25, 0.125), (42, 0.375, 0.125),
    (42, 0.5, 0.125), (42, 0.625, 0.125),
    (42, 0.75, 0.125), (42, 0.875, 0.125),
    (42, 1.0, 0.125), (42, 1.125, 0.125),
    (42, 1.25, 0.125), (42, 1.375, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    (64, 1.5, 0.375), (65, 1.875, 0.375),
    (63, 2.25, 0.375), (62, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: C7 (C E G B)
    (60, 2.25, 0.375), (64, 2.25, 0.375), (67, 2.25, 0.375), (71, 2.25, 0.375),
    # Bar 2, beat 4: D7 (D F# A C)
    (62, 2.625, 0.375), (66, 2.625, 0.375), (69, 2.625, 0.375), (72, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif (D F# A D)
sax_notes = [
    (62, 1.5, 0.375), (66, 1.875, 0.375), (69, 2.25, 0.375), (62, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass_notes = [
    (64, 3.0, 0.375), (65, 3.375, 0.375),
    (63, 3.75, 0.375), (62, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: B7 (B D# F# A)
    (71, 3.75, 0.375), (74, 3.75, 0.375), (76, 3.75, 0.375), (79, 3.75, 0.375),
    # Bar 3, beat 4: C7 (C E G B)
    (60, 4.125, 0.375), (64, 4.125, 0.375), (67, 4.125, 0.375), (71, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Repeat motif (D F# A D)
sax_notes = [
    (62, 3.0, 0.375), (66, 3.375, 0.375), (69, 3.75, 0.375), (62, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    (64, 4.5, 0.375), (65, 4.875, 0.375),
    (63, 5.25, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: G7 (G B D F)
    (67, 5.25, 0.375), (71, 5.25, 0.375), (69, 5.25, 0.375), (64, 5.25, 0.375),
    # Bar 4, beat 4: D7 (D F# A C)
    (62, 5.625, 0.375), (66, 5.625, 0.375), (69, 5.625, 0.375), (72, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif but ends on F# instead of D to create tension
sax_notes = [
    (62, 4.5, 0.375), (66, 4.875, 0.375), (69, 5.25, 0.375), (66, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375),
    (36, 5.25, 0.375), (38, 5.625, 0.375),
    (42, 4.5, 0.125), (42, 4.625, 0.125),
    (42, 4.75, 0.125), (42, 4.875, 0.125),
    (42, 5.0, 0.125), (42, 5.125, 0.125),
    (42, 5.25, 0.125), (42, 5.375, 0.125),
    (42, 5.5, 0.125), (42, 5.625, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
