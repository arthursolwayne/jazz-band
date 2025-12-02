
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
    (42, 0.0, 0.1875),    # Hihat on 1&
    (42, 0.1875, 0.1875), # Hihat on 2&
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.1875),  # Hihat on 2&
    (42, 0.5625, 0.1875), # Hihat on 3&
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.1875),   # Hihat on 3&
    (42, 0.9375, 0.1875), # Hihat on 4&
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.1875),  # Hihat on 4&
    (42, 1.3125, 0.1875)  # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums for bars 2-4
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    for beat in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + beat * 0.75, end=bar_start + beat * 0.75 + 0.375))
    # Snare on 2 and 4
    for beat in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + beat * 0.75, end=bar_start + beat * 0.75 + 0.375))
    # Hihat on every eighth
    for beat in range(8):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=bar_start + beat * 0.375, end=bar_start + beat * 0.375 + 0.1875))

# Bass line (Marcus)
# Walking line with chromatic approaches
bass_notes = [
    # Bar 2
    (62, 1.5, 0.375),     # D
    (63, 1.875, 0.375),   # Eb
    (60, 2.25, 0.375),    # C
    (62, 2.625, 0.375),   # D
    # Bar 3
    (64, 3.0, 0.375),     # E
    (62, 3.375, 0.375),   # D
    (63, 3.75, 0.375),    # Eb
    (65, 4.125, 0.375),   # F
    # Bar 4
    (62, 4.5, 0.375),     # D
    (63, 4.875, 0.375),   # Eb
    (60, 5.25, 0.375),    # C
    (62, 5.625, 0.375)    # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane)
# 7th chords on beats 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.875, 0.375),   # G7 (G, B, D, F)
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    (69, 1.875, 0.375),
    (62, 1.875, 0.375),
    # Bar 3
    (64, 3.375, 0.375),
    (67, 3.375, 0.375),
    (69, 3.375, 0.375),
    (62, 3.375, 0.375),
    # Bar 4
    (64, 4.875, 0.375),
    (67, 4.875, 0.375),
    (69, 4.875, 0.375),
    (62, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone (Dante)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),     # D
    (65, 1.875, 0.375),   # F
    (67, 2.25, 0.375),    # G
    (62, 2.625, 0.375),   # D (leaving it hanging)
    (62, 4.5, 0.375),     # D (returning)
    (65, 4.875, 0.375),   # F
    (67, 5.25, 0.375),    # G
    (62, 5.625, 0.375)    # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
