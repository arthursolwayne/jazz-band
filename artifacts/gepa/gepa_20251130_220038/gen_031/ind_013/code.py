
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (62, 1.5, 0.375),   # D3 on 1
    (64, 1.875, 0.375), # Eb3 on 2
    (65, 2.25, 0.375),  # E3 on 3
    (67, 2.625, 0.375), # F#3 on 4
    (69, 3.0, 0.375),   # G3 on 1
    (71, 3.375, 0.375), # A3 on 2
    (72, 3.75, 0.375),  # Bb3 on 3
    (74, 4.125, 0.375), # B3 on 4
    (76, 4.5, 0.375),   # C4 on 1
    (78, 4.875, 0.375), # D4 on 2
    (79, 5.25, 0.375),  # Eb4 on 3
    (81, 5.625, 0.375)  # F#4 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano chords (Diane)
piano_notes = [
    # Bar 2 (1.5s)
    (67, 1.5, 0.375),  # D7 (F#)
    (72, 1.5, 0.375),  # Bb (D7)
    (74, 1.5, 0.375),  # B (D7)
    (77, 1.5, 0.375),  # D (D7)

    # Bar 3 (2.25s)
    (69, 2.25, 0.375),  # G7 (B)
    (74, 2.25, 0.375),  # B (G7)
    (76, 2.25, 0.375),  # D (G7)
    (79, 2.25, 0.375),  # F# (G7)

    # Bar 4 (3.0s)
    (67, 3.0, 0.375),  # D7 (F#)
    (72, 3.0, 0.375),  # Bb (D7)
    (74, 3.0, 0.375),  # B (D7)
    (77, 3.0, 0.375),  # D (D7)

    # Bar 4 (3.375s)
    (69, 3.375, 0.375),  # G7 (B)
    (74, 3.375, 0.375),  # B (G7)
    (76, 3.375, 0.375),  # D (G7)
    (79, 3.375, 0.375),  # F# (G7)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone line (Dante)
sax_notes = [
    (69, 1.5, 0.375),  # G4 on 1
    (72, 1.875, 0.375),  # Bb4 on 2
    (74, 2.25, 0.375),  # B4 on 3
    (69, 2.625, 0.375),  # G4 on 4
    (67, 3.0, 0.375),  # F#4 on 1
    (72, 3.375, 0.375),  # Bb4 on 2
    (74, 3.75, 0.375),  # B4 on 3
    (69, 4.125, 0.375),  # G4 on 4
    (69, 4.5, 0.375),  # G4 on 1
    (72, 4.875, 0.375),  # Bb4 on 2
    (74, 5.25, 0.375),  # B4 on 3
    (69, 5.625, 0.375)  # G4 on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2 (1.5s)
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.375),   # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.375), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.375), # Hihat on 4

    # Bar 3 (3.0s)
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375), # Hihat on 4

    # Bar 4 (4.5s)
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
