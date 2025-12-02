
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.375),     # Hihat on 1
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.375),   # Hihat on 2
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.375),    # Hihat on 3
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.375)    # Hihat on 4
]
for pitch, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone: short motif
sax_notes = [
    (62, 1.5, 0.375),     # D4
    (66, 1.875, 0.375),   # F#4
    (64, 2.25, 0.375),    # G4
    (62, 2.625, 0.375)    # D4
]
for pitch, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Bass: walking line
bass_notes = [
    (45, 1.5, 0.375),     # D3
    (47, 1.875, 0.375),   # E3
    (46, 2.25, 0.375),    # F3
    (45, 2.625, 0.375)    # D3
]
for pitch, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (62, 1.875, 0.375),   # D4
    (67, 1.875, 0.375),   # G4 (D7)
    (64, 1.875, 0.375),   # Bb4 (D7)
    (69, 1.875, 0.375),   # C#5 (D7)
    (62, 2.625, 0.375),   # D4
    (67, 2.625, 0.375),   # G4 (D7)
    (64, 2.625, 0.375),   # Bb4 (D7)
    (69, 2.625, 0.375)    # C#5 (D7)
]
for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Drums: keep the pattern
for pitch, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 1.5, end=start + 1.5 + duration)
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone: repeat motif with slight variation
sax_notes = [
    (62, 3.0, 0.375),     # D4
    (66, 3.375, 0.375),   # F#4
    (64, 3.75, 0.375),    # G4
    (62, 4.125, 0.375)    # D4
]
for pitch, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Bass: walking line
bass_notes = [
    (45, 3.0, 0.375),     # D3
    (47, 3.375, 0.375),   # E3
    (46, 3.75, 0.375),    # F3
    (45, 4.125, 0.375)    # D3
]
for pitch, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (62, 3.375, 0.375),   # D4
    (67, 3.375, 0.375),   # G4 (D7)
    (64, 3.375, 0.375),   # Bb4 (D7)
    (69, 3.375, 0.375),   # C#5 (D7)
    (62, 4.125, 0.375),   # D4
    (67, 4.125, 0.375),   # G4 (D7)
    (64, 4.125, 0.375),   # Bb4 (D7)
    (69, 4.125, 0.375)    # C#5 (D7)
]
for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Drums: keep the pattern
for pitch, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 3.0, end=start + 3.0 + duration)
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone: finish motif with resolution
sax_notes = [
    (62, 4.5, 0.375),     # D4
    (66, 4.875, 0.375),   # F#4
    (64, 5.25, 0.375),    # G4
    (62, 5.625, 0.375)    # D4
]
for pitch, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Bass: walking line
bass_notes = [
    (45, 4.5, 0.375),     # D3
    (47, 4.875, 0.375),   # E3
    (46, 5.25, 0.375),    # F3
    (45, 5.625, 0.375)    # D3
]
for pitch, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (62, 4.875, 0.375),   # D4
    (67, 4.875, 0.375),   # G4 (D7)
    (64, 4.875, 0.375),   # Bb4 (D7)
    (69, 4.875, 0.375),   # C#5 (D7)
    (62, 5.625, 0.375),   # D4
    (67, 5.625, 0.375),   # G4 (D7)
    (64, 5.625, 0.375),   # Bb4 (D7)
    (69, 5.625, 0.375)    # C#5 (D7)
]
for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Drums: keep the pattern
for pitch, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 4.5, end=start + 4.5 + duration)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
