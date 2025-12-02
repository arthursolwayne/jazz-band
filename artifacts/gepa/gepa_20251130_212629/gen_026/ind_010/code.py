
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# -- Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),     # Kick on 1
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.0, 0.1875),    # Hihat on 1 & 2
    (42, 0.1875, 0.1875),
    (36, 0.75, 0.375),    # Kick on 3
    (38, 1.125, 0.375),   # Snare on 4
    (42, 0.75, 0.1875),   # Hihat on 3 & 4
    (42, 0.9375, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# -- Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line starting on F
bass_notes = [
    (47, 1.5, 0.25),  # F
    (48, 1.75, 0.25), # G
    (46, 2.0, 0.25),  # E
    (45, 2.25, 0.25), # D
    (47, 2.5, 0.25),  # F
    (48, 2.75, 0.25), # G
    (46, 3.0, 0.25),  # E
    (45, 3.25, 0.25)  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 1.5, 0.25),   # C7 (C, E, B) on 1
    (64, 1.75, 0.25),  # E7 on 2
    (62, 2.0, 0.25),   # D7 on 3
    (67, 2.25, 0.25),  # F7 on 4
    (60, 2.5, 0.25),   # C7 on 1
    (64, 2.75, 0.25),  # E7 on 2
    (62, 3.0, 0.25),   # D7 on 3
    (67, 3.25, 0.25)   # F7 on 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax - simple motif with space
sax_notes = [
    (66, 1.5, 0.375),  # A (start of motif)
    (69, 1.875, 0.375), # C
    (67, 2.25, 0.375),  # Bb
    (66, 2.625, 0.375), # A
    (69, 3.0, 0.375),   # C (end of motif)
    (67, 3.375, 0.375), # Bb
    (66, 3.75, 0.375)   # A (repeat with space)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# -- Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line
bass_notes = [
    (47, 3.0, 0.25),  # F
    (48, 3.25, 0.25), # G
    (46, 3.5, 0.25),  # E
    (45, 3.75, 0.25), # D
    (47, 4.0, 0.25),  # F
    (48, 4.25, 0.25), # G
    (46, 4.5, 0.25),  # E
    (45, 4.75, 0.25)  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords
piano_notes = [
    (60, 3.0, 0.25),   # C7 on 1
    (64, 3.25, 0.25),  # E7 on 2
    (62, 3.5, 0.25),   # D7 on 3
    (67, 3.75, 0.25),  # F7 on 4
    (60, 4.0, 0.25),   # C7 on 1
    (64, 4.25, 0.25),  # E7 on 2
    (62, 4.5, 0.25),   # D7 on 3
    (67, 4.75, 0.25)   # F7 on 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax - motif variation
sax_notes = [
    (66, 3.0, 0.375),  # A
    (69, 3.375, 0.375), # C
    (67, 3.75, 0.375),  # Bb
    (66, 4.125, 0.375), # A
    (69, 4.5, 0.375),   # C
    (67, 4.875, 0.375)  # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# -- Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line
bass_notes = [
    (47, 4.5, 0.25),  # F
    (48, 4.75, 0.25), # G
    (46, 5.0, 0.25),  # E
    (45, 5.25, 0.25), # D
    (47, 5.5, 0.25),  # F
    (48, 5.75, 0.25), # G
    (46, 6.0, 0.25),  # E
    (45, 6.25, 0.25)  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords
piano_notes = [
    (60, 4.5, 0.25),   # C7 on 1
    (64, 4.75, 0.25),  # E7 on 2
    (62, 5.0, 0.25),   # D7 on 3
    (67, 5.25, 0.25),  # F7 on 4
    (60, 5.5, 0.25),   # C7 on 1
    (64, 5.75, 0.25),  # E7 on 2
    (62, 6.0, 0.25),   # D7 on 3
    (67, 6.25, 0.25)   # F7 on 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax - leave it hanging
sax_notes = [
    (66, 4.5, 0.375),  # A
    (69, 4.875, 0.375), # C
    (67, 5.25, 0.375),  # Bb
    (66, 5.625, 0.375), # A
    (69, 6.0, 0.375),   # C
    (67, 6.375, 0.375)  # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),     # Kick on 1
    (38, 4.875, 0.375),   # Snare on 2
    (42, 4.5, 0.1875),    # Hihat on 1 & 2
    (42, 4.6875, 0.1875),
    (36, 5.25, 0.375),    # Kick on 3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.25, 0.1875),   # Hihat on 3 & 4
    (42, 5.4375, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
