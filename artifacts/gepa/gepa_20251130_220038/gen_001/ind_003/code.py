
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
    (42, 0.0, 0.1875),    # Hihat on 1 & 2
    (42, 0.375, 0.1875),  # Hihat on 2
    (38, 0.75, 0.375),    # Snare on 3
    (42, 0.75, 0.1875),   # Hihat on 3 & 4
    (42, 1.125, 0.1875),  # Hihat on 4
    (36, 1.5, 0.375)      # Kick on 4
]

for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in D
bass_notes = [
    (49, 1.5, 0.375),     # D (root)
    (50, 1.875, 0.375),   # Eb (chromatic)
    (51, 2.25, 0.375),    # E (3rd)
    (52, 2.625, 0.375)    # F (4th)
]

for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    (55, 1.875, 0.375),   # C7 (Bb)
    (57, 1.875, 0.375),   # D7 (C)
    (59, 1.875, 0.375),   # E7 (D)
    (60, 1.875, 0.375),   # F7 (E)
    (55, 2.625, 0.375),   # C7 (Bb)
    (57, 2.625, 0.375),   # D7 (C)
    (59, 2.625, 0.375),   # E7 (D)
    (60, 2.625, 0.375)    # F7 (E)
]

for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Dante: Tenor sax motif
sax_notes = [
    (62, 1.5, 0.75),      # E
    (64, 2.25, 0.75),     # G
    (63, 3.0, 0.75)       # F#
]

for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in D
bass_notes = [
    (53, 3.0, 0.375),     # F (5th)
    (54, 3.375, 0.375),   # F# (b6)
    (55, 3.75, 0.375),    # G (b7)
    (56, 4.125, 0.375)    # G# (octave)
]

for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    (55, 3.375, 0.375),   # C7 (Bb)
    (57, 3.375, 0.375),   # D7 (C)
    (59, 3.375, 0.375),   # E7 (D)
    (60, 3.375, 0.375),   # F7 (E)
    (55, 4.125, 0.375),   # C7 (Bb)
    (57, 4.125, 0.375),   # D7 (C)
    (59, 4.125, 0.375),   # E7 (D)
    (60, 4.125, 0.375)    # F7 (E)
]

for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Dante: Tenor sax motif (echo)
sax_notes = [
    (62, 3.0, 0.75),      # E
    (64, 3.75, 0.75),     # G
    (63, 4.5, 0.75)       # F#
]

for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in D
bass_notes = [
    (52, 4.5, 0.375),     # F (5th)
    (53, 4.875, 0.375),   # F# (b6)
    (54, 5.25, 0.375),    # G (b7)
    (55, 5.625, 0.375)    # G# (octave)
]

for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    (55, 4.875, 0.375),   # C7 (Bb)
    (57, 4.875, 0.375),   # D7 (C)
    (59, 4.875, 0.375),   # E7 (D)
    (60, 4.875, 0.375),   # F7 (E)
    (55, 5.625, 0.375),   # C7 (Bb)
    (57, 5.625, 0.375),   # D7 (C)
    (59, 5.625, 0.375),   # E7 (D)
    (60, 5.625, 0.375)    # F7 (E)
]

for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Dante: Tenor sax motif (finish)
sax_notes = [
    (62, 4.5, 0.75),      # E
    (64, 5.25, 0.75),     # G
    (63, 6.0, 0.75)       # F#
]

for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),     # Kick on 1
    (42, 1.5, 0.1875),    # Hihat on 1 & 2
    (42, 1.875, 0.1875),  # Hihat on 2
    (38, 2.25, 0.375),    # Snare on 3
    (42, 2.25, 0.1875),   # Hihat on 3 & 4
    (42, 2.625, 0.1875),  # Hihat on 4
    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.0, 0.1875),    # Hihat on 1 & 2
    (42, 3.375, 0.1875),  # Hihat on 2
    (38, 3.75, 0.375),    # Snare on 3
    (42, 3.75, 0.1875),   # Hihat on 3 & 4
    (42, 4.125, 0.1875),  # Hihat on 4
    (36, 4.5, 0.375),     # Kick on 1
    (42, 4.5, 0.1875),    # Hihat on 1 & 2
    (42, 4.875, 0.1875),  # Hihat on 2
    (38, 5.25, 0.375),    # Snare on 3
    (42, 5.25, 0.1875),   # Hihat on 3 & 4
    (42, 5.625, 0.1875),  # Hihat on 4
    (36, 6.0, 0.375)      # Kick on 4
]

for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
