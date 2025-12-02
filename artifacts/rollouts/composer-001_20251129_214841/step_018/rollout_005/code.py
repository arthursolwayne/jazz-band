
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    (42, 1.125, 0.375),  # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    (62, 1.5, 0.375),  # C5
    (67, 1.875, 0.375),  # G5
    (64, 2.25, 0.375),  # E5
    (62, 2.625, 0.375),  # C5
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line (walking, chromatic)
bass_notes = [
    (49, 1.5, 0.375),  # C3
    (50, 1.875, 0.375),  # C#3
    (51, 2.25, 0.375),  # D3
    (52, 2.625, 0.375),  # D#3
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chords (7th chords on 2 and 4)
piano_notes = [
    # Bar 2, beat 2: C7 (C E G B)
    (60, 1.875, 0.375),
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    (71, 1.875, 0.375),
    # Bar 2, beat 4: C7 again
    (60, 2.625, 0.375),
    (64, 2.625, 0.375),
    (67, 2.625, 0.375),
    (71, 2.625, 0.375),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375),  # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody (continuation of motif)
sax_notes = [
    (62, 3.0, 0.375),  # C5
    (67, 3.375, 0.375),  # G5
    (64, 3.75, 0.375),  # E5
    (62, 4.125, 0.375),  # C5
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line (walking, chromatic)
bass_notes = [
    (53, 3.0, 0.375),  # E3
    (54, 3.375, 0.375),  # F3
    (55, 3.75, 0.375),  # F#3
    (57, 4.125, 0.375),  # A3
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chords (7th chords on 2 and 4)
piano_notes = [
    # Bar 3, beat 2: C7
    (60, 3.375, 0.375),
    (64, 3.375, 0.375),
    (67, 3.375, 0.375),
    (71, 3.375, 0.375),
    # Bar 3, beat 4: C7 again
    (60, 4.125, 0.375),
    (64, 4.125, 0.375),
    (67, 4.125, 0.375),
    (71, 4.125, 0.375),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375),  # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody (continuation of motif)
sax_notes = [
    (62, 4.5, 0.375),  # C5
    (67, 4.875, 0.375),  # G5
    (64, 5.25, 0.375),  # E5
    (62, 5.625, 0.375),  # C5
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line (walking, chromatic)
bass_notes = [
    (58, 4.5, 0.375),  # G3
    (59, 4.875, 0.375),  # G#3
    (60, 5.25, 0.375),  # A3
    (62, 5.625, 0.375),  # Bb3
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chords (7th chords on 2 and 4)
piano_notes = [
    # Bar 4, beat 2: C7
    (60, 4.875, 0.375),
    (64, 4.875, 0.375),
    (67, 4.875, 0.375),
    (71, 4.875, 0.375),
    # Bar 4, beat 4: C7 again
    (60, 5.625, 0.375),
    (64, 5.625, 0.375),
    (67, 5.625, 0.375),
    (71, 5.625, 0.375),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375),  # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
