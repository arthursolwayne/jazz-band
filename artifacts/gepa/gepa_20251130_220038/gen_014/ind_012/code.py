
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.375),    # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.375),   # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus - Bass (walking line)
bass_notes = [
    (62, 1.5, 0.375),    # D4
    (64, 1.875, 0.375),  # Eb4
    (65, 2.25, 0.375),   # E4
    (67, 2.625, 0.375)   # F4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane - Piano (comping on 2 and 4)
piano_notes = [
    # Bar 2: 7th chords on 2 and 4
    # D7 on 2
    (62, 1.875, 0.375),  # D
    (67, 1.875, 0.375),  # F
    (69, 1.875, 0.375),  # A
    (71, 1.875, 0.375),  # C
    # D7 on 4
    (62, 2.625, 0.375),  # D
    (67, 2.625, 0.375),  # F
    (69, 2.625, 0.375),  # A
    (71, 2.625, 0.375)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray - Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.375),    # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.375),   # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante - Sax (motif: D - Eb - E - F, spaced out)
sax_notes = [
    (62, 1.5, 0.375),    # D
    (64, 2.25, 0.375),   # E
    (65, 3.0, 0.375),    # F
    (62, 3.75, 0.375)    # D (hang on the last note)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus - Bass (walking line)
bass_notes = [
    (67, 3.0, 0.375),    # F4
    (69, 3.375, 0.375),  # G4
    (71, 3.75, 0.375),   # A4
    (72, 4.125, 0.375)   # Bb4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane - Piano (comping on 2 and 4)
piano_notes = [
    # D7 on 2
    (62, 3.375, 0.375),  # D
    (67, 3.375, 0.375),  # F
    (69, 3.375, 0.375),  # A
    (71, 3.375, 0.375),  # C
    # D7 on 4
    (62, 4.125, 0.375),  # D
    (67, 4.125, 0.375),  # F
    (69, 4.125, 0.375),  # A
    (71, 4.125, 0.375)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray - Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.375),    # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.375),   # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante - Sax (motif variation: D - F - E - G)
sax_notes = [
    (62, 3.0, 0.375),    # D
    (67, 3.375, 0.375),  # F
    (65, 3.75, 0.375),   # E
    (69, 4.125, 0.375)   # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus - Bass (walking line)
bass_notes = [
    (72, 4.5, 0.375),    # Bb4
    (74, 4.875, 0.375),  # B4
    (76, 5.25, 0.375),   # C5
    (77, 5.625, 0.375)   # Db5
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane - Piano (comping on 2 and 4)
piano_notes = [
    # D7 on 2
    (62, 4.875, 0.375),  # D
    (67, 4.875, 0.375),  # F
    (69, 4.875, 0.375),  # A
    (71, 4.875, 0.375),  # C
    # D7 on 4
    (62, 5.625, 0.375),  # D
    (67, 5.625, 0.375),  # F
    (69, 5.625, 0.375),  # A
    (71, 5.625, 0.375)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray - Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.375),    # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.375),   # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante - Sax (motif finish: D - F - E - D)
sax_notes = [
    (62, 4.5, 0.375),    # D
    (67, 4.875, 0.375),  # F
    (65, 5.25, 0.375),   # E
    (62, 5.625, 0.375)   # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('jazz_intro.mid')
