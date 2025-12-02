
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
    (42, 0.1875, 0.1875), # Hihat on 1&
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.5625, 0.1875), # Hihat on 2&
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.9375, 0.1875), # Hihat on 3&
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.3125, 0.1875), # Hihat on 4&
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F minor, chromatic approaches
bass_notes = [
    (48, 1.5, 0.375),   # F
    (49, 1.875, 0.375),  # Gb
    (50, 2.25, 0.375),   # G
    (51, 2.625, 0.375),  # Ab
    (53, 3.0, 0.375),    # Bb
    (54, 3.375, 0.375),  # B
    (55, 3.75, 0.375),   # C
    (56, 4.125, 0.375),  # C#
    (57, 4.5, 0.375),    # D
    (58, 4.875, 0.375),  # Eb
    (60, 5.25, 0.375),   # F
    (61, 5.625, 0.375),  # Gb
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.875, 0.1875), # F7 (F, A, C, Eb)
    (69, 1.875, 0.1875),
    (71, 1.875, 0.1875),
    (67, 1.875, 0.1875),
    # Bar 3
    (64, 3.375, 0.1875), # F7 (F, A, C, Eb)
    (69, 3.375, 0.1875),
    (71, 3.375, 0.1875),
    (67, 3.375, 0.1875),
    # Bar 4
    (64, 5.625, 0.1875), # F7 (F, A, C, Eb)
    (69, 5.625, 0.1875),
    (71, 5.625, 0.1875),
    (67, 5.625, 0.1875),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.5 + 0.375))
    # Hihat on every eighth
    for i in range(4):
        hihat_start = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.1875))

# Dante: Tenor sax motif (start on bar 2)
sax_notes = [
    (62, 1.5, 0.375),   # G
    (66, 1.875, 0.375),  # Bb
    (67, 2.25, 0.375),   # B
    (62, 2.625, 0.375),  # G
    (60, 3.0, 0.375),    # F
    (64, 3.375, 0.375),  # A
    (66, 3.75, 0.375),   # Bb
    (62, 4.125, 0.375),  # G
    (60, 4.5, 0.375),    # F
    (64, 4.875, 0.375),  # A
    (62, 5.25, 0.375),   # G
    (66, 5.625, 0.375)   # Bb
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
