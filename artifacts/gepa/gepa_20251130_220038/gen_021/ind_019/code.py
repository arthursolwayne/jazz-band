
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
    (42, 0.1875, 0.1875), # Hihat on &1
    (38, 0.75, 0.375),    # Snare on 2
    (42, 0.9375, 0.1875), # Hihat on &2
    (36, 1.125, 0.375),   # Kick on 3
    (42, 1.3125, 0.1875), # Hihat on &3
    (38, 1.875, 0.375),   # Snare on 4
    (42, 2.0625, 0.1875)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4 (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (45, 1.5, 0.375),     # D
    (46, 1.875, 0.375),   # Eb
    (44, 2.25, 0.375),    # C
    (45, 2.625, 0.375),   # D
    (46, 2.999, 0.375),   # Eb
    (44, 3.374, 0.375),   # C
    (45, 3.749, 0.375),   # D
    (46, 4.124, 0.375),   # Eb
    (44, 4.499, 0.375),   # C
    (45, 4.874, 0.375),   # D
    (43, 5.249, 0.375),   # Bb
    (45, 5.624, 0.375)    # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (50, 2.25, 0.375),    # F7 (F, A, C, Eb)
    (52, 2.25, 0.375),
    (53, 2.25, 0.375),
    (55, 2.25, 0.375),
    (50, 3.375, 0.375),
    (52, 3.375, 0.375),
    (53, 3.375, 0.375),
    (55, 3.375, 0.375),
    (50, 4.5, 0.375),
    (52, 4.5, 0.375),
    (53, 4.5, 0.375),
    (55, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Bar 2
    if bar == 2:
        drum_notes = [
            (36, bar_start + 0.0, 0.375),     # Kick on 1
            (42, bar_start + 0.1875, 0.1875), # Hihat on &1
            (38, bar_start + 0.75, 0.375),    # Snare on 2
            (42, bar_start + 0.9375, 0.1875), # Hihat on &2
            (36, bar_start + 1.125, 0.375),   # Kick on 3
            (42, bar_start + 1.3125, 0.1875), # Hihat on &3
            (38, bar_start + 1.875, 0.375),   # Snare on 4
            (42, bar_start + 2.0625, 0.1875)  # Hihat on &4
        ]
    # Bars 3 and 4
    else:
        drum_notes = [
            (36, bar_start + 0.0, 0.375),     # Kick on 1
            (42, bar_start + 0.1875, 0.1875), # Hihat on &1
            (38, bar_start + 0.75, 0.375),    # Snare on 2
            (42, bar_start + 0.9375, 0.1875), # Hihat on &2
            (36, bar_start + 1.125, 0.375),   # Kick on 3
            (42, bar_start + 1.3125, 0.1875), # Hihat on &3
            (38, bar_start + 1.875, 0.375),   # Snare on 4
            (42, bar_start + 2.0625, 0.1875)  # Hihat on &4
        ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (62, 1.5, 0.375),     # G
    (64, 1.875, 0.375),   # A
    (62, 2.25, 0.375),    # G
    (66, 2.625, 0.375),   # Bb
    (62, 3.375, 0.375),   # G
    (64, 3.75, 0.375),    # A
    (62, 4.125, 0.375),   # G
    (66, 4.5, 0.375),     # Bb
    (62, 5.25, 0.375),    # G
    (64, 5.625, 0.375),   # A
    (69, 6.0, 0.375)      # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
