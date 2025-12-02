
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
    (42, 0.375, 0.75),    # Hihat on 2
    (36, 0.75, 1.125),    # Kick on 3
    (42, 1.125, 1.5),     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums: kick=36, snare=38, hihat=42
# Bar 2
drum_notes = [
    (36, 1.5, 0.375),     # Kick on 1
    (42, 1.5, 0.75),      # Hihat on 2
    (38, 1.875, 0.375),   # Snare on 3
    (42, 1.875, 2.25),    # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3
drum_notes = [
    (36, 2.25, 0.375),    # Kick on 1
    (42, 2.25, 2.625),   # Hihat on 2
    (38, 2.625, 0.375),  # Snare on 3
    (42, 2.625, 3.0),    # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4
drum_notes = [
    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.0, 3.375),    # Hihat on 2
    (38, 3.375, 0.375),  # Snare on 3
    (42, 3.375, 3.75),   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Marcus on bass: walking line in F, chromatic approaches, no repeated notes
# Bar 2
bass_notes = [
    (45, 1.5, 0.375),    # F
    (46, 1.875, 0.375),  # G
    (44, 2.25, 0.375),   # E
    (45, 2.625, 0.375),  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Bar 3
bass_notes = [
    (46, 3.0, 0.375),    # G
    (47, 3.375, 0.375),  # A
    (45, 3.75, 0.375),   # F
    (46, 4.125, 0.375),  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Bar 4
bass_notes = [
    (47, 4.5, 0.375),    # A
    (48, 4.875, 0.375),  # Bb
    (47, 5.25, 0.375),   # A
    (45, 5.625, 0.375),  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords, comp on 2 and 4
# Bar 2
piano_notes = [
    (62, 1.875, 0.375),  # F7 - Bb
    (64, 1.875, 0.375),  # F7 - D
    (65, 1.875, 0.375),  # F7 - E
    (60, 1.875, 0.375),  # F7 - F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3
piano_notes = [
    (62, 3.375, 0.375),  # F7 - Bb
    (64, 3.375, 0.375),  # F7 - D
    (65, 3.375, 0.375),  # F7 - E
    (60, 3.375, 0.375),  # F7 - F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4
piano_notes = [
    (62, 4.875, 0.375),  # F7 - Bb
    (64, 4.875, 0.375),  # F7 - D
    (65, 4.875, 0.375),  # F7 - E
    (60, 4.875, 0.375),  # F7 - F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Dante on sax: Motif in F, short, singable, no scale runs
# Bar 2
sax_notes = [
    (66, 1.5, 0.375),    # F
    (69, 1.875, 0.375),  # A
    (66, 2.25, 0.375),   # F
    (64, 2.625, 0.375),  # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3
sax_notes = [
    (66, 3.0, 0.375),    # F
    (69, 3.375, 0.375),  # A
    (66, 3.75, 0.375),   # F
    (64, 4.125, 0.375),  # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4
sax_notes = [
    (66, 4.5, 0.375),    # F
    (69, 4.875, 0.375),  # A
    (66, 5.25, 0.375),   # F
    (64, 5.625, 0.375),  # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
