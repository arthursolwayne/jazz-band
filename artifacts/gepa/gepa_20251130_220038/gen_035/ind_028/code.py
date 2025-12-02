
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in F
bass_notes = [
    (45, 1.5, 0.375),  # F3
    (46, 1.875, 0.375),  # G3
    (47, 2.25, 0.375),  # Ab3
    (48, 2.625, 0.375)   # Bb3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (57, 1.875, 0.375),  # F7 (F, A, C, Eb)
    (60, 1.875, 0.375),  # A
    (62, 1.875, 0.375),  # C
    (64, 1.875, 0.375),  # Eb
    (57, 2.625, 0.375),  # F7 again
    (60, 2.625, 0.375),
    (62, 2.625, 0.375),
    (64, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax melody in F
sax_notes = [
    (62, 1.5, 0.375),  # F4
    (64, 1.875, 0.375),  # G4
    (66, 2.25, 0.375),  # A4
    (62, 2.625, 0.375)   # F4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass
bass_notes = [
    (48, 3.0, 0.375),  # Bb3
    (45, 3.375, 0.375),  # F3
    (46, 3.75, 0.375),  # G3
    (47, 4.125, 0.375)   # Ab3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (57, 3.375, 0.375),  # F7
    (60, 3.375, 0.375),
    (62, 3.375, 0.375),
    (64, 3.375, 0.375),
    (57, 4.125, 0.375),  # F7 again
    (60, 4.125, 0.375),
    (62, 4.125, 0.375),
    (64, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Continue the melody
sax_notes = [
    (64, 3.0, 0.375),  # G4 (overlap with bar 2)
    (67, 3.375, 0.375),  # Bb4
    (69, 3.75, 0.375),  # C5
    (67, 4.125, 0.375)   # Bb4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass
bass_notes = [
    (47, 4.5, 0.375),  # Ab3
    (48, 4.875, 0.375),  # Bb3
    (45, 5.25, 0.375),  # F3
    (46, 5.625, 0.375)   # G3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (57, 4.875, 0.375),  # F7
    (60, 4.875, 0.375),
    (62, 4.875, 0.375),
    (64, 4.875, 0.375),
    (57, 5.625, 0.375),  # F7 again
    (60, 5.625, 0.375),
    (62, 5.625, 0.375),
    (64, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Finish the motif
sax_notes = [
    (62, 4.5, 0.375),  # F4 (overlap with bar 3)
    (66, 4.875, 0.375),  # A4
    (68, 5.25, 0.375),  # Bb4
    (62, 5.625, 0.375)   # F4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_shorter_moment.mid')
