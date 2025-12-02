
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.75),    # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.75, 0.75),   # Snare on 2
    (42, 0.75, 0.375),  # Hihat on 2
    (36, 1.125, 0.75),  # Kick on 3
    (42, 1.125, 0.375), # Hihat on 3
    (38, 1.5, 0.75),    # Snare on 4
    (42, 1.5, 0.375)    # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: C (60) - E (64) - G (67) - C (60)
sax_notes = [
    (60, 1.5, 0.375),  # C
    (64, 1.875, 0.375), # E
    (67, 2.25, 0.375),  # G
    (60, 2.625, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line with chromatic approaches
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375)  # D#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (60, 1.875, 0.375),  # C7
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    (71, 1.875, 0.375),
    (60, 2.625, 0.375),  # C7
    (64, 2.625, 0.375),
    (67, 2.625, 0.375),
    (71, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Bb (58) - D (62) - F (65) - Bb (58)
sax_notes = [
    (58, 3.0, 0.375),  # Bb
    (62, 3.375, 0.375), # D
    (65, 3.75, 0.375),  # F
    (58, 4.125, 0.375)  # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line with chromatic approaches
bass_notes = [
    (64, 3.0, 0.375),  # D
    (65, 3.375, 0.375), # D#
    (66, 3.75, 0.375),  # E
    (67, 4.125, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (62, 3.375, 0.375),  # D7
    (65, 3.375, 0.375),
    (67, 3.375, 0.375),
    (71, 3.375, 0.375),
    (62, 4.125, 0.375),  # D7
    (65, 4.125, 0.375),
    (67, 4.125, 0.375),
    (71, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: C (60) - E (64) - G (67) - C (60)
sax_notes = [
    (60, 4.5, 0.375),  # C
    (64, 4.875, 0.375), # E
    (67, 5.25, 0.375),  # G
    (60, 5.625, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line with chromatic approaches
bass_notes = [
    (66, 4.5, 0.375),  # E
    (67, 4.875, 0.375), # F
    (68, 5.25, 0.375),  # F#
    (69, 5.625, 0.375)  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (64, 4.875, 0.375),  # E7
    (67, 4.875, 0.375),
    (71, 4.875, 0.375),
    (74, 4.875, 0.375),
    (64, 5.625, 0.375),  # E7
    (67, 5.625, 0.375),
    (71, 5.625, 0.375),
    (74, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Bar 3 and 4
drum_notes = [
    (36, 3.0, 0.75),    # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (38, 3.75, 0.75),   # Snare on 2
    (42, 3.75, 0.375),  # Hihat on 2
    (36, 4.125, 0.75),  # Kick on 3
    (42, 4.125, 0.375), # Hihat on 3
    (38, 4.875, 0.75),  # Snare on 4
    (42, 4.875, 0.375), # Hihat on 4
    (36, 5.25, 0.75),   # Kick on 1
    (42, 5.25, 0.375),  # Hihat on 1
    (38, 6.0, 0.75),    # Snare on 4
    (42, 6.0, 0.375)    # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
