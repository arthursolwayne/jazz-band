
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.1875),    # Hihat on 1
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.1875),  # Hihat on 2
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.1875),   # Hihat on 3
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.1875)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (60, 1.5, 0.375),     # C (1)
    (61, 1.875, 0.375),   # C# (2)
    (62, 2.25, 0.375),    # D (3)
    (63, 2.625, 0.375),   # D# (4)
    (64, 3.0, 0.375),     # E (1)
    (65, 3.375, 0.375),   # F (2)
    (66, 3.75, 0.375),    # F# (3)
    (67, 4.125, 0.375),   # G (4)
    (68, 4.5, 0.375),     # G# (1)
    (69, 4.875, 0.375),   # A (2)
    (70, 5.25, 0.375),    # A# (3)
    (71, 5.625, 0.375)    # B (4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano (Diane)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (71, 1.5, 0.375),     # B7
    (69, 1.875, 0.375),   # A7
    (67, 2.25, 0.375),    # G7
    (64, 2.625, 0.375),   # E7
    # Bar 3 (3.0 - 4.5s)
    (71, 3.0, 0.375),     # B7
    (69, 3.375, 0.375),   # A7
    (67, 3.75, 0.375),    # G7
    (64, 4.125, 0.375),   # E7
    # Bar 4 (4.5 - 6.0s)
    (71, 4.5, 0.375),     # B7
    (69, 4.875, 0.375),   # A7
    (67, 5.25, 0.375),    # G7
    (64, 5.625, 0.375)    # E7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante)
sax_notes = [
    (62, 1.5, 0.375),     # D (1)
    (64, 1.875, 0.375),   # E (2)
    (65, 2.25, 0.375),    # F (3)
    (62, 2.625, 0.375),   # D (4)
    (64, 3.0, 0.375),     # E (1)
    (66, 3.375, 0.375),   # F# (2)
    (67, 3.75, 0.375),    # G (3)
    (62, 4.125, 0.375),   # D (4)
    (64, 4.5, 0.375),     # E (1)
    (66, 4.875, 0.375),   # F# (2)
    (67, 5.25, 0.375),    # G (3)
    (62, 5.625, 0.375)    # D (4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (36, 1.5, 0.375),     # Kick on 1
    (42, 1.5, 0.1875),    # Hihat on 1
    (38, 1.875, 0.375),   # Snare on 2
    (42, 1.875, 0.1875),  # Hihat on 2
    (36, 2.25, 0.375),    # Kick on 3
    (42, 2.25, 0.1875),   # Hihat on 3
    (38, 2.625, 0.375),   # Snare on 4
    (42, 2.625, 0.1875),  # Hihat on 4
    # Bar 3 (3.0 - 4.5s)
    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.0, 0.1875),    # Hihat on 1
    (38, 3.375, 0.375),   # Snare on 2
    (42, 3.375, 0.1875),  # Hihat on 2
    (36, 3.75, 0.375),    # Kick on 3
    (42, 3.75, 0.1875),   # Hihat on 3
    (38, 4.125, 0.375),   # Snare on 4
    (42, 4.125, 0.1875),  # Hihat on 4
    # Bar 4 (4.5 - 6.0s)
    (36, 4.5, 0.375),     # Kick on 1
    (42, 4.5, 0.1875),    # Hihat on 1
    (38, 4.875, 0.375),   # Snare on 2
    (42, 4.875, 0.1875),  # Hihat on 2
    (36, 5.25, 0.375),    # Kick on 3
    (42, 5.25, 0.1875),   # Hihat on 3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.625, 0.1875)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
