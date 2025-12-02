
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.125),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.125),
    (42, 1.25, 0.125), (42, 1.375, 0.125), (42, 1.5, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# SAX: motif starts here, short and singable
sax_notes = [
    (62, 1.5, 0.375), (67, 1.875, 0.375), (65, 2.25, 0.375), (62, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# BASS: walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (61, 2.25, 0.375), (62, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# PIANO: 7th chords, comp on 2 and 4
piano_notes = [
    (72, 1.875, 0.375), (76, 1.875, 0.375), (74, 1.875, 0.375), (70, 1.875, 0.375),
    (72, 2.625, 0.375), (76, 2.625, 0.375), (74, 2.625, 0.375), (70, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# SAX: motif returns, but ends on a different note
sax_notes = [
    (62, 3.0, 0.375), (67, 3.375, 0.375), (65, 3.75, 0.375), (67, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# BASS: walking line
bass_notes = [
    (63, 3.0, 0.375), (64, 3.375, 0.375), (62, 3.75, 0.375), (63, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# PIANO: comp again
piano_notes = [
    (72, 3.375, 0.375), (76, 3.375, 0.375), (74, 3.375, 0.375), (70, 3.375, 0.375),
    (72, 4.125, 0.375), (76, 4.125, 0.375), (74, 4.125, 0.375), (70, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# SAX: motif resolves
sax_notes = [
    (62, 4.5, 0.375), (67, 4.875, 0.375), (65, 5.25, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# BASS: resolves on D
bass_notes = [
    (62, 4.5, 0.375), (63, 4.875, 0.375), (62, 5.25, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# PIANO: last comp
piano_notes = [
    (72, 4.875, 0.375), (76, 4.875, 0.375), (74, 4.875, 0.375), (70, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: same pattern
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.125),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.125),
    (42, 5.375, 0.125), (42, 5.5, 0.125), (42, 5.625, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
