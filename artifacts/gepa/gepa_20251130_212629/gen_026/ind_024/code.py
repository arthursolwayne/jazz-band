
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
    (36, 0.0, 0.75),     # Kick on 1
    (42, 0.0, 0.5),      # Hihat on 1
    (38, 0.5, 0.75),     # Snare on 2
    (42, 0.5, 0.5),      # Hihat on 2
    (36, 1.0, 0.75),     # Kick on 3
    (42, 1.0, 0.5),      # Hihat on 3
    (38, 1.5, 0.75),     # Snare on 4
    (42, 1.5, 0.5)       # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),    # D (root)
    (60, 1.875, 0.375),  # Bb (chromatic)
    (62, 2.25, 0.375),   # D
    (64, 2.625, 0.375)   # F (3rd)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (64, 1.875, 0.125),  # F (Dm7)
    (67, 1.875, 0.125),  # A
    (62, 1.875, 0.125),  # D
    (69, 1.875, 0.125),  # C
    (64, 2.625, 0.125),  # F (Dm7)
    (67, 2.625, 0.125),  # A
    (62, 2.625, 0.125),  # D
    (69, 2.625, 0.125)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.75),     # Kick on 1
    (42, 1.5, 0.5),      # Hihat on 1
    (38, 1.875, 0.75),   # Snare on 2
    (42, 1.875, 0.5),    # Hihat on 2
    (36, 2.25, 0.75),    # Kick on 3
    (42, 2.25, 0.5),     # Hihat on 3
    (38, 2.625, 0.75),   # Snare on 4
    (42, 2.625, 0.5)     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax motif (start at bar 2)
# One short motif, leave it hanging, finish it in bar 4
# Dm scale: D, Eb, F, G, A, Bb, C
sax_notes = [
    (62, 1.875, 0.375),  # D
    (64, 2.25, 0.375),   # F
    (67, 2.625, 0.375),  # A
    (62, 3.0, 0.375)     # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line in Dm, chromatic approaches
bass_notes = [
    (64, 3.0, 0.375),    # F
    (62, 3.375, 0.375),  # D
    (60, 3.75, 0.375),   # Bb
    (62, 4.125, 0.375)   # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (64, 3.375, 0.125),  # F (Dm7)
    (67, 3.375, 0.125),  # A
    (62, 3.375, 0.125),  # D
    (69, 3.375, 0.125),  # C
    (64, 4.125, 0.125),  # F (Dm7)
    (67, 4.125, 0.125),  # A
    (62, 4.125, 0.125),  # D
    (69, 4.125, 0.125)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.75),     # Kick on 1
    (42, 3.0, 0.5),      # Hihat on 1
    (38, 3.375, 0.75),   # Snare on 2
    (42, 3.375, 0.5),    # Hihat on 2
    (36, 3.75, 0.75),    # Kick on 3
    (42, 3.75, 0.5),     # Hihat on 3
    (38, 4.125, 0.75),   # Snare on 4
    (42, 4.125, 0.5)     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line in Dm, chromatic approaches
bass_notes = [
    (60, 4.5, 0.375),    # Bb
    (62, 4.875, 0.375),  # D
    (64, 5.25, 0.375),   # F
    (67, 5.625, 0.375)   # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (64, 4.875, 0.125),  # F (Dm7)
    (67, 4.875, 0.125),  # A
    (62, 4.875, 0.125),  # D
    (69, 4.875, 0.125),  # C
    (64, 5.625, 0.125),  # F (Dm7)
    (67, 5.625, 0.125),  # A
    (62, 5.625, 0.125),  # D
    (69, 5.625, 0.125)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.75),     # Kick on 1
    (42, 4.5, 0.5),      # Hihat on 1
    (38, 4.875, 0.75),   # Snare on 2
    (42, 4.875, 0.5),    # Hihat on 2
    (36, 5.25, 0.75),    # Kick on 3
    (42, 5.25, 0.5),     # Hihat on 3
    (38, 5.625, 0.75),   # Snare on 4
    (42, 5.625, 0.5)     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax motif (finish it in bar 4)
sax_notes = [
    (62, 5.625, 0.375),  # D
    (64, 6.0, 0.375)     # F (end on a question)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_wayne.mid")
