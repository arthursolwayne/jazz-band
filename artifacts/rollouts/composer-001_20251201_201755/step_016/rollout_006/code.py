
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
    (42, 1.125, 0.375),   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm (F, Ab, G, Eb)
bass_notes = [
    (38, 1.5, 0.375),     # F2
    (41, 1.875, 0.375),   # Ab2
    (40, 2.25, 0.375),    # G2
    (39, 2.625, 0.375),   # Eb2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Fm7 (F, Ab, C, D) -> Bbm7 (Bb, Db, F, Ab) -> Eb7 (Eb, G, Bb, D) -> Am7 (A, C, E, G)
piano_notes = [
    # Bar 2 (1.5 - 1.875)
    (53, 1.5, 0.375),     # F (F4)
    (60, 1.5, 0.375),     # C (C5)
    (62, 1.5, 0.375),     # D (D5)
    (64, 1.5, 0.375),     # Ab (Ab5)
    # Bar 3 (1.875 - 2.25)
    (58, 1.875, 0.375),   # Bb (Bb4)
    (61, 1.875, 0.375),   # Db (Db5)
    (53, 1.875, 0.375),   # F (F4)
    (64, 1.875, 0.375),   # Ab (Ab5)
    # Bar 4 (2.25 - 2.625)
    (55, 2.25, 0.375),    # Eb (Eb4)
    (58, 2.25, 0.375),    # G (G4)
    (60, 2.25, 0.375),    # Bb (Bb4)
    (62, 2.25, 0.375),    # D (D5)
    # Bar 4 (2.625 - 3.0)
    (65, 2.625, 0.375),   # A (A4)
    (69, 2.625, 0.375),   # C (C5)
    (72, 2.625, 0.375),   # E (E5)
    (74, 2.625, 0.375),   # G (G5)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif (F, Ab, G, Eb)
sax_notes = [
    (53, 1.5, 0.375),     # F (F4)
    (60, 1.875, 0.375),   # Ab (Ab4)
    (62, 2.25, 0.375),    # G (G4)
    (55, 2.625, 0.375),   # Eb (Eb4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Fm (F, Ab, G, Eb)
bass_notes = [
    (38, 3.0, 0.375),     # F2
    (41, 3.375, 0.375),   # Ab2
    (40, 3.75, 0.375),    # G2
    (39, 4.125, 0.375),   # Eb2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Fm7 (F, Ab, C, D) -> Bbm7 (Bb, Db, F, Ab) -> Eb7 (Eb, G, Bb, D) -> Am7 (A, C, E, G)
piano_notes = [
    # Bar 3 (3.0 - 3.375)
    (53, 3.0, 0.375),     # F (F4)
    (60, 3.0, 0.375),     # C (C5)
    (62, 3.0, 0.375),     # D (D5)
    (64, 3.0, 0.375),     # Ab (Ab5)
    # Bar 4 (3.375 - 3.75)
    (58, 3.375, 0.375),   # Bb (Bb4)
    (61, 3.375, 0.375),   # Db (Db5)
    (53, 3.375, 0.375),   # F (F4)
    (64, 3.375, 0.375),   # Ab (Ab5)
    # Bar 4 (3.75 - 4.125)
    (55, 3.75, 0.375),    # Eb (Eb4)
    (58, 3.75, 0.375),    # G (G4)
    (60, 3.75, 0.375),    # Bb (Bb4)
    (62, 3.75, 0.375),    # D (D5)
    # Bar 4 (4.125 - 4.5)
    (65, 4.125, 0.375),   # A (A4)
    (69, 4.125, 0.375),   # C (C5)
    (72, 4.125, 0.375),   # E (E5)
    (74, 4.125, 0.375),   # G (G5)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Rest
# No notes here

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Fm (F, Ab, G, Eb)
bass_notes = [
    (38, 4.5, 0.375),     # F2
    (41, 4.875, 0.375),   # Ab2
    (40, 5.25, 0.375),    # G2
    (39, 5.625, 0.375),   # Eb2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Fm7 (F, Ab, C, D) -> Bbm7 (Bb, Db, F, Ab) -> Eb7 (Eb, G, Bb, D) -> Am7 (A, C, E, G)
piano_notes = [
    # Bar 4 (4.5 - 4.875)
    (53, 4.5, 0.375),     # F (F4)
    (60, 4.5, 0.375),     # C (C5)
    (62, 4.5, 0.375),     # D (D5)
    (64, 4.5, 0.375),     # Ab (Ab5)
    # Bar 4 (4.875 - 5.25)
    (58, 4.875, 0.375),   # Bb (Bb4)
    (61, 4.875, 0.375),   # Db (Db5)
    (53, 4.875, 0.375),   # F (F4)
    (64, 4.875, 0.375),   # Ab (Ab5)
    # Bar 4 (5.25 - 5.625)
    (55, 5.25, 0.375),    # Eb (Eb4)
    (58, 5.25, 0.375),    # G (G4)
    (60, 5.25, 0.375),    # Bb (Bb4)
    (62, 5.25, 0.375),    # D (D5)
    # Bar 4 (5.625 - 6.0)
    (65, 5.625, 0.375),   # A (A4)
    (69, 5.625, 0.375),   # C (C5)
    (72, 5.625, 0.375),   # E (E5)
    (74, 5.625, 0.375),   # G (G5)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Repeat motif with variation (F, Ab, G, Eb)
sax_notes = [
    (53, 4.5, 0.375),     # F (F4)
    (60, 4.875, 0.375),   # Ab (Ab4)
    (62, 5.25, 0.375),    # G (G4)
    (55, 5.625, 0.375),   # Eb (Eb4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    # Bar 2 (1.5 - 3.0)
    (36, 1.5, 0.375),     # Kick on 1
    (42, 1.5, 0.375),     # Hihat on 1
    (38, 1.875, 0.375),   # Snare on 2
    (42, 1.875, 0.375),   # Hihat on 2
    (36, 2.25, 0.375),    # Kick on 3
    (42, 2.25, 0.375),    # Hihat on 3
    (38, 2.625, 0.375),   # Snare on 4
    (42, 2.625, 0.375),   # Hihat on 4
    # Bar 3 (3.0 - 4.5)
    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.0, 0.375),     # Hihat on 1
    (38, 3.375, 0.375),   # Snare on 2
    (42, 3.375, 0.375),   # Hihat on 2
    (36, 3.75, 0.375),    # Kick on 3
    (42, 3.75, 0.375),    # Hihat on 3
    (38, 4.125, 0.375),   # Snare on 4
    (42, 4.125, 0.375),   # Hihat on 4
    # Bar 4 (4.5 - 6.0)
    (36, 4.5, 0.375),     # Kick on 1
    (42, 4.5, 0.375),     # Hihat on 1
    (38, 4.875, 0.375),   # Snare on 2
    (42, 4.875, 0.375),   # Hihat on 2
    (36, 5.25, 0.375),    # Kick on 3
    (42, 5.25, 0.375),    # Hihat on 3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.625, 0.375),   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
