
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: Fm melody (F, Ab, Bb, D)
sax_notes = [
    (65, 1.5, 0.375),    # F
    (60, 1.875, 0.375),  # Ab
    (62, 2.25, 0.375),   # Bb
    (67, 2.625, 0.375),  # D
    (65, 3.0, 0.375),    # F
    (60, 3.375, 0.375),  # Ab
    (62, 3.75, 0.375),   # Bb
    (67, 4.125, 0.375),  # D
    (65, 4.5, 0.375),    # F
    (60, 4.875, 0.375),  # Ab
    (62, 5.25, 0.375),   # Bb
    (67, 5.625, 0.375)   # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    (53, 1.5, 0.375),    # F
    (52, 1.875, 0.375),  # Gb
    (51, 2.25, 0.375),   # Ab
    (50, 2.625, 0.375),  # A
    (53, 3.0, 0.375),    # F
    (52, 3.375, 0.375),  # Gb
    (51, 3.75, 0.375),   # Ab
    (50, 4.125, 0.375),  # A
    (53, 4.5, 0.375),    # F
    (52, 4.875, 0.375),  # Gb
    (51, 5.25, 0.375),   # Ab
    (50, 5.625, 0.375)   # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (53, 1.875, 0.375),  # F7 (F, A, C, Eb)
    (50, 1.875, 0.375),
    (52, 1.875, 0.375),
    (51, 1.875, 0.375),
    (53, 3.375, 0.375),  # F7 again
    (50, 3.375, 0.375),
    (52, 3.375, 0.375),
    (51, 3.375, 0.375),
    (53, 4.875, 0.375),  # F7 again
    (50, 4.875, 0.375),
    (52, 4.875, 0.375),
    (51, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    bar_start = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (36, bar_start + 0.0, 0.375), (38, bar_start + 0.375, 0.375), (42, bar_start + 0.0, 0.1875),
        (36, bar_start + 0.75, 0.375), (38, bar_start + 1.125, 0.375), (42, bar_start + 0.75, 0.1875),
        (42, bar_start + 1.5, 0.1875)
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
