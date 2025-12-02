
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in C, chromatic approaches
bass_notes = [
    # Bar 2
    (60, 1.5, 0.375),    # C
    (61, 1.875, 0.375),  # C#
    (62, 2.25, 0.375),   # D
    (60, 2.625, 0.375),  # C
    # Bar 3
    (63, 3.0, 0.375),    # D#
    (62, 3.375, 0.375),  # D
    (60, 3.75, 0.375),   # C
    (59, 4.125, 0.375),  # B
    # Bar 4
    (60, 4.5, 0.375),    # C
    (62, 4.875, 0.375),  # D
    (64, 5.25, 0.375),   # E
    (62, 5.625, 0.375)   # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (71, 1.875, 0.375),  # B7 (Cmaj7)
    (70, 1.875, 0.375),  # B
    (67, 1.875, 0.375),  # G
    (64, 1.875, 0.375),  # E
    (60, 1.875, 0.375),  # C
    # Bar 3
    (71, 3.375, 0.375),  # B7 (Cmaj7)
    (70, 3.375, 0.375),  # B
    (67, 3.375, 0.375),  # G
    (64, 3.375, 0.375),  # E
    (60, 3.375, 0.375),  # C
    # Bar 4
    (71, 4.875, 0.375),  # B7 (Cmaj7)
    (70, 4.875, 0.375),  # B
    (67, 4.875, 0.375),  # G
    (64, 4.875, 0.375),  # E
    (60, 4.875, 0.375)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax, one short motif
sax_notes = [
    # Bar 2
    (65, 1.5, 0.375),    # E
    (67, 1.875, 0.375),  # G
    (64, 2.25, 0.375),   # E
    (62, 2.625, 0.375),  # D
    # Bar 3
    (65, 3.0, 0.375),    # E
    (67, 3.375, 0.375),  # G
    (64, 3.75, 0.375),   # E
    (62, 4.125, 0.375),  # D
    # Bar 4
    (65, 4.5, 0.375),    # E
    (67, 4.875, 0.375),  # G
    (64, 5.25, 0.375),   # E
    (62, 5.625, 0.375)   # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
