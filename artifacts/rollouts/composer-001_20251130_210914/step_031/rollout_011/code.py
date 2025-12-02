
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
# Marcus: Walking bass line in F
bass_notes = [
    (53, 1.5, 0.375),   # F
    (55, 1.875, 0.375), # G
    (57, 2.25, 0.375),  # A
    (58, 2.625, 0.375)  # Bb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2
    (53, 1.875, 0.375), # F
    (57, 1.875, 0.375), # A
    (60, 1.875, 0.375), # C
    (62, 1.875, 0.375), # D
    # Bar 3: D7 on 2
    (58, 2.25, 0.375),  # D
    (62, 2.25, 0.375),  # F
    (65, 2.25, 0.375),  # A
    (67, 2.25, 0.375),  # C
    # Bar 4: G7 on 2
    (55, 2.625, 0.375), # G
    (59, 2.625, 0.375), # B
    (62, 2.625, 0.375), # D
    (64, 2.625, 0.375)  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Sax motif (start on 1 of bar 2)
sax_notes = [
    (62, 1.5, 0.375),   # C
    (65, 1.875, 0.375), # E
    (67, 2.25, 0.375),  # G
    (69, 2.625, 0.375)  # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in F
bass_notes = [
    (60, 3.0, 0.375),   # C
    (62, 3.375, 0.375), # D
    (64, 3.75, 0.375),  # E
    (65, 4.125, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: D7 on 2
    (58, 3.375, 0.375), # D
    (62, 3.375, 0.375), # F
    (65, 3.375, 0.375), # A
    (67, 3.375, 0.375), # C
    # Bar 4: G7 on 2
    (55, 3.75, 0.375),  # G
    (59, 3.75, 0.375),  # B
    (62, 3.75, 0.375),  # D
    (64, 3.75, 0.375)   # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Drums
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
# Marcus: Walking bass line in F
bass_notes = [
    (65, 4.5, 0.375),   # F
    (67, 4.875, 0.375), # G
    (69, 5.25, 0.375),  # A
    (71, 5.625, 0.375)  # Bb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on 2
    (53, 4.875, 0.375), # F
    (57, 4.875, 0.375), # A
    (60, 4.875, 0.375), # C
    (62, 4.875, 0.375), # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Sax motif (finish the motif)
sax_notes = [
    (69, 4.5, 0.375),   # A
    (67, 4.875, 0.375), # G
    (65, 5.25, 0.375),  # E
    (62, 5.625, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Little Ray: Drums
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
