
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif
sax_notes = [
    (60, 1.5, 0.375),  # C4
    (62, 1.875, 0.375), # D4
    (64, 2.25, 0.375),  # E4
    (62, 2.625, 0.375), # D4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line: walking in Fm
bass_notes = [
    (48, 1.5, 0.375),   # F3
    (50, 1.875, 0.375), # G3
    (48, 2.25, 0.375),  # F3
    (51, 2.625, 0.375)  # Ab3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (53, 1.875, 0.375),  # Bb4 (F7)
    (50, 1.875, 0.375),  # G4
    (48, 1.875, 0.375),  # F4
    (51, 1.875, 0.375),  # Ab4
    (53, 2.625, 0.375),  # Bb4 (F7)
    (50, 2.625, 0.375),  # G4
    (48, 2.625, 0.375),  # F4
    (51, 2.625, 0.375)   # Ab4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.375),   # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.375), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone motif again
sax_notes = [
    (60, 3.0, 0.375),  # C4
    (62, 3.375, 0.375), # D4
    (64, 3.75, 0.375),  # E4
    (62, 4.125, 0.375), # D4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line: walking in Fm
bass_notes = [
    (51, 3.0, 0.375),   # Ab3
    (53, 3.375, 0.375), # Bb3
    (51, 3.75, 0.375),  # Ab3
    (50, 4.125, 0.375)  # G3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (53, 3.375, 0.375),  # Bb4 (F7)
    (50, 3.375, 0.375),  # G4
    (48, 3.375, 0.375),  # F4
    (51, 3.375, 0.375),  # Ab4
    (53, 4.125, 0.375),  # Bb4 (F7)
    (50, 4.125, 0.375),  # G4
    (48, 4.125, 0.375),  # F4
    (51, 4.125, 0.375)   # Ab4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone motif with resolution
sax_notes = [
    (60, 4.5, 0.375),  # C4
    (62, 4.875, 0.375), # D4
    (64, 5.25, 0.375),  # E4
    (62, 5.625, 0.375), # D4
    (64, 5.625, 0.375)  # E4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line: walking in Fm
bass_notes = [
    (50, 4.5, 0.375),   # G3
    (51, 4.875, 0.375), # Ab3
    (50, 5.25, 0.375),  # G3
    (48, 5.625, 0.375)  # F3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (53, 4.875, 0.375),  # Bb4 (F7)
    (50, 4.875, 0.375),  # G4
    (48, 4.875, 0.375),  # F4
    (51, 4.875, 0.375),  # Ab4
    (53, 5.625, 0.375),  # Bb4 (F7)
    (50, 5.625, 0.375),  # G4
    (48, 5.625, 0.375),  # F4
    (51, 5.625, 0.375)   # Ab4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.375),   # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.375), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
