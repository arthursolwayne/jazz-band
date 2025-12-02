
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
    (36, 0.0, 0.75),   # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1&
    (42, 0.375, 0.375),# Hihat on 2&
    (38, 0.5, 0.75),   # Snare on 3
    (42, 0.5, 0.375),  # Hihat on 3&
    (42, 0.875, 0.375),# Hihat on 4&
    (36, 1.125, 0.375),# Kick on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    (60, 1.5, 0.5),   # C4
    (62, 2.0, 0.5),   # D4
    (64, 2.5, 0.5),   # E4
    (65, 3.0, 0.5),   # F4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line
bass_notes = [
    (48, 1.5, 0.5),   # C3
    (50, 2.0, 0.5),   # D3
    (52, 2.5, 0.5),   # E3
    (53, 3.0, 0.5),   # F3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano comping (2 and 4)
piano_notes = [
    (71, 2.0, 0.5),   # B3 (C7)
    (69, 3.0, 0.5),   # G3 (F7)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums
drum_notes = [
    (36, 1.5, 0.75),   # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1&
    (42, 1.875, 0.375),# Hihat on 2&
    (38, 2.0, 0.75),   # Snare on 3
    (42, 2.0, 0.375),  # Hihat on 3&
    (42, 2.375, 0.375),# Hihat on 4&
    (36, 2.75, 0.375), # Kick on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody
sax_notes = [
    (65, 3.0, 0.5),   # F4
    (67, 3.5, 0.5),   # G4
    (69, 4.0, 0.5),   # A4
    (71, 4.5, 0.5),   # B4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line
bass_notes = [
    (53, 3.0, 0.5),   # F3
    (55, 3.5, 0.5),   # G3
    (57, 4.0, 0.5),   # A3
    (59, 4.5, 0.5),   # B3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano comping (2 and 4)
piano_notes = [
    (72, 3.5, 0.5),   # C4 (G7)
    (69, 4.5, 0.5),   # G3 (B7)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums
drum_notes = [
    (36, 3.0, 0.75),   # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1&
    (42, 3.375, 0.375),# Hihat on 2&
    (38, 3.5, 0.75),   # Snare on 3
    (42, 3.5, 0.375),  # Hihat on 3&
    (42, 3.875, 0.375),# Hihat on 4&
    (36, 4.25, 0.375), # Kick on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody
sax_notes = [
    (71, 4.5, 0.5),   # B4
    (69, 5.0, 0.5),   # A4
    (67, 5.5, 0.5),   # G4
    (65, 6.0, 0.5),   # F4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line
bass_notes = [
    (59, 4.5, 0.5),   # B3
    (57, 5.0, 0.5),   # A3
    (55, 5.5, 0.5),   # G3
    (53, 6.0, 0.5),   # F3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano comping (2 and 4)
piano_notes = [
    (71, 5.0, 0.5),   # B3 (A7)
    (69, 6.0, 0.5),   # G3 (D7)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums
drum_notes = [
    (36, 4.5, 0.75),   # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1&
    (42, 4.875, 0.375),# Hihat on 2&
    (38, 5.0, 0.75),   # Snare on 3
    (42, 5.0, 0.375),  # Hihat on 3&
    (42, 5.375, 0.375),# Hihat on 4&
    (36, 5.75, 0.375), # Kick on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
