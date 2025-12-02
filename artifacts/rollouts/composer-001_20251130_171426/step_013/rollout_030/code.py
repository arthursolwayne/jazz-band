
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
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
# Bass line (Marcus)
bass_notes = [
    (62, 1.5, 0.375),  # F (Dm7) chromatic approach
    (60, 1.875, 0.375),  # D
    (62, 2.25, 0.375),  # F
    (64, 2.625, 0.375)   # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - comp on 2 and 4
piano_notes = [
    (62, 1.875, 0.375),  # F7 chord (F, A, C, D)
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    (69, 1.875, 0.375),
    (62, 2.625, 0.375),
    (64, 2.625, 0.375),
    (67, 2.625, 0.375),
    (69, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums (Little Ray)
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

# Sax (Dante) - motif: D - F - G - Eb (Dm, F, G, Eb)
sax_notes = [
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375),  # F
    (67, 2.25, 0.375),  # G
    (64, 2.625, 0.375)   # Eb (F)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line (Marcus)
bass_notes = [
    (64, 3.0, 0.375),  # G
    (62, 3.375, 0.375),  # F
    (60, 3.75, 0.375),  # D
    (62, 4.125, 0.375)   # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - comp on 2 and 4
piano_notes = [
    (62, 3.375, 0.375),  # F7 chord
    (64, 3.375, 0.375),
    (67, 3.375, 0.375),
    (69, 3.375, 0.375),
    (62, 4.125, 0.375),
    (64, 4.125, 0.375),
    (67, 4.125, 0.375),
    (69, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums (Little Ray)
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

# Sax (Dante) - continue motif with variation
sax_notes = [
    (62, 3.0, 0.375),  # D
    (64, 3.375, 0.375),  # F
    (67, 3.75, 0.375),  # G
    (64, 4.125, 0.375)   # Eb (F)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line (Marcus)
bass_notes = [
    (62, 4.5, 0.375),  # F
    (60, 4.875, 0.375),  # D
    (62, 5.25, 0.375),  # F
    (64, 5.625, 0.375)   # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - comp on 2 and 4
piano_notes = [
    (62, 4.875, 0.375),  # F7 chord
    (64, 4.875, 0.375),
    (67, 4.875, 0.375),
    (69, 4.875, 0.375),
    (62, 5.625, 0.375),
    (64, 5.625, 0.375),
    (67, 5.625, 0.375),
    (69, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums (Little Ray)
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

# Sax (Dante) - finish the motif with tension
sax_notes = [
    (62, 4.5, 0.375),  # D
    (64, 4.875, 0.375),  # F
    (67, 5.25, 0.375),  # G
    (64, 5.625, 0.375)   # Eb (F)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
