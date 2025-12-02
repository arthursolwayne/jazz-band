
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody starts here - motif: C (60), E (64), B (71), D (62)
sax_notes = [
    (1.5, 60, 0.375), (1.875, 64, 0.375), (2.25, 71, 0.375), (2.625, 62, 0.375)
]
for start, pitch, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in C, chromatic approaches
bass_notes = [
    (1.5, 60, 0.375), (1.875, 61, 0.375), (2.25, 62, 0.375), (2.625, 64, 0.375)
]
for start, pitch, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (1.875, 60, 0.375), (1.875, 64, 0.375), (1.875, 67, 0.375), (1.875, 71, 0.375),
    (2.625, 60, 0.375), (2.625, 64, 0.375), (2.625, 67, 0.375), (2.625, 71, 0.375)
]
for start, pitch, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif starting on E (64)
sax_notes = [
    (3.0, 64, 0.375), (3.375, 67, 0.375), (3.75, 72, 0.375), (4.125, 65, 0.375)
]
for start, pitch, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in C, chromatic approaches
bass_notes = [
    (3.0, 64, 0.375), (3.375, 65, 0.375), (3.75, 67, 0.375), (4.125, 69, 0.375)
]
for start, pitch, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (3.375, 64, 0.375), (3.375, 67, 0.375), (3.375, 71, 0.375), (3.375, 74, 0.375),
    (4.125, 64, 0.375), (4.125, 67, 0.375), (4.125, 71, 0.375), (4.125, 74, 0.375)
]
for start, pitch, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif again, this time resolving to C (60)
sax_notes = [
    (4.5, 65, 0.375), (4.875, 68, 0.375), (5.25, 71, 0.375), (5.625, 60, 0.375)
]
for start, pitch, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in C, chromatic approaches
bass_notes = [
    (4.5, 68, 0.375), (4.875, 69, 0.375), (5.25, 71, 0.375), (5.625, 72, 0.375)
]
for start, pitch, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (4.875, 68, 0.375), (4.875, 71, 0.375), (4.875, 74, 0.375), (4.875, 76, 0.375),
    (5.625, 68, 0.375), (5.625, 71, 0.375), (5.625, 74, 0.375), (5.625, 76, 0.375)
]
for start, pitch, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 38), (7.125, 42)
]
for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
