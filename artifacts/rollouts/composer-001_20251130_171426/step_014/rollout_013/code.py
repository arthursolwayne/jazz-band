
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

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (45, 1.5, 0.375),  # F
    (46, 1.875, 0.375),  # Gb
    (47, 2.25, 0.375),  # G
    (49, 2.625, 0.375),  # A
    (50, 3.0, 0.375),  # Bb
    (51, 3.375, 0.375),  # B
    (53, 3.75, 0.375),  # C
    (55, 4.125, 0.375),  # D
    (56, 4.5, 0.375),  # Eb
    (57, 4.875, 0.375),  # E
    (59, 5.25, 0.375),  # F
    (60, 5.625, 0.375)  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (50, 1.5, 0.375),  # Bb7 (F7)
    (52, 1.5, 0.375),
    (53, 1.5, 0.375),
    (57, 1.5, 0.375),
    (50, 2.25, 0.375),  # Bb7
    (52, 2.25, 0.375),
    (53, 2.25, 0.375),
    (57, 2.25, 0.375),
    (50, 3.0, 0.375),  # Bb7
    (52, 3.0, 0.375),
    (53, 3.0, 0.375),
    (57, 3.0, 0.375),
    (50, 3.75, 0.375),  # Bb7
    (52, 3.75, 0.375),
    (53, 3.75, 0.375),
    (57, 3.75, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G - Bb - F (first bar), then G - A - C - G (second bar), then Bb - C - Eb - Bb (third bar), then F (final bar)
sax_notes = [
    (53, 1.5, 0.375),  # F
    (55, 1.875, 0.375),  # G
    (57, 2.25, 0.375),  # Bb
    (53, 2.625, 0.375),  # F (end of first bar)
    (55, 3.0, 0.375),  # G
    (57, 3.375, 0.375),  # A
    (60, 3.75, 0.375),  # C
    (55, 4.125, 0.375),  # G (end of second bar)
    (57, 4.5, 0.375),  # Bb
    (60, 4.875, 0.375),  # C
    (63, 5.25, 0.375),  # Eb
    (57, 5.625, 0.375)  # Bb (end of third bar)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
