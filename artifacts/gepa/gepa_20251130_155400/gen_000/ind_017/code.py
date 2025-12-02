
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.375, 0.375), (38, 3.75, 0.375), (42, 3.375, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (37, 1.5, 0.375), (38, 1.875, 0.375), (36, 2.25, 0.375), (34, 2.625, 0.375),
    (37, 3.0, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (59, 1.875, 0.375), (57, 1.875, 0.375), (55, 1.875, 0.375), (50, 1.875, 0.375),
    (59, 3.0, 0.375), (57, 3.0, 0.375), (55, 3.0, 0.375), (50, 3.0, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Short motif, start on Fm, leave it hanging
sax_notes = [
    (64, 1.5, 0.375), (66, 1.875, 0.375), (62, 2.25, 0.375), (64, 2.625, 0.375),
    (64, 3.0, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (37, 3.0, 0.375), (38, 3.375, 0.375), (36, 3.75, 0.375), (34, 4.125, 0.375),
    (37, 4.5, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (59, 3.375, 0.375), (57, 3.375, 0.375), (55, 3.375, 0.375), (50, 3.375, 0.375),
    (59, 4.5, 0.375), (57, 4.5, 0.375), (55, 4.5, 0.375), (50, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif continues and resolves
sax_notes = [
    (64, 3.0, 0.375), (66, 3.375, 0.375), (62, 3.75, 0.375), (60, 4.125, 0.375),
    (58, 4.5, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 4.125, 0.375), (38, 4.5, 0.375), (42, 4.125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (37, 4.5, 0.375), (38, 4.875, 0.375), (36, 5.25, 0.375), (34, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (59, 4.875, 0.375), (57, 4.875, 0.375), (55, 4.875, 0.375), (50, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Resolution
sax_notes = [
    (58, 4.5, 0.375), (60, 4.875, 0.375), (58, 5.25, 0.375), (57, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.625, 0.375), (38, 6.0, 0.375), (42, 5.625, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
