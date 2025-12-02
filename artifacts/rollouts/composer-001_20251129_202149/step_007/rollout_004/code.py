
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375),  # C#
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375),  # D#
    (64, 3.0, 0.375),  # E
    (65, 3.375, 0.375),  # F
    (66, 3.75, 0.375),  # F#
    (67, 4.125, 0.375),  # G
    (68, 4.5, 0.375),  # G#
    (69, 4.875, 0.375),  # A
    (70, 5.25, 0.375),  # A#
    (71, 5.625, 0.375)  # B
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 1.5, 0.375),  # C
    (64, 1.5, 0.375),  # E
    (67, 1.5, 0.375),  # G
    (71, 1.5, 0.375),  # B
    (62, 1.875, 0.375),  # D
    (65, 1.875, 0.375),  # F
    (68, 1.875, 0.375),  # A
    (72, 1.875, 0.375),  # C
    (60, 2.625, 0.375),  # C
    (64, 2.625, 0.375),  # E
    (67, 2.625, 0.375),  # G
    (71, 2.625, 0.375),  # B
    (62, 3.375, 0.375),  # D
    (65, 3.375, 0.375),  # F
    (68, 3.375, 0.375),  # A
    (72, 3.375, 0.375),  # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875))

# You: This is your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Bar 2: Motif starts
sax_notes = [
    (67, 1.5, 0.375),  # G
    (71, 1.875, 0.375),  # B
    (69, 2.25, 0.375),  # A
    (67, 2.625, 0.375),  # G
    (64, 3.0, 0.375),  # E
    (67, 3.375, 0.375),  # G
    (69, 3.75, 0.375),  # A
    (71, 4.125, 0.375),  # B
    (67, 4.5, 0.375),  # G
    (69, 4.875, 0.375),  # A
    (67, 5.25, 0.375),  # G
    (64, 5.625, 0.375)  # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
