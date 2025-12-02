
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
    (38, 0.375, 0.75),  # Snare on 2
    (42, 0.375, 0.75),  # Hihat on 2
    (36, 0.75, 1.125),  # Kick on 3
    (42, 0.75, 1.125),  # Hihat on 3
    (38, 1.125, 1.5),   # Snare on 4
    (42, 1.125, 1.5)    # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums for bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    for beat in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375))
    # Snare on 2 and 4
    for beat in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375))
    # Hihat on every eighth
    for beat in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1875))

# Bass line (Marcus)
# Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (59, 1.5, 0.375),    # D (root)
    (60, 1.875, 0.375),  # Eb (chromatic up)
    (62, 2.25, 0.375),   # F (third)
    (60, 2.625, 0.375),  # Eb (chromatic down)
    (59, 3.0, 0.375),    # D (root)
    (61, 3.375, 0.375),  # E (chromatic up)
    (62, 3.75, 0.375),   # F (third)
    (61, 4.125, 0.375),  # E (chromatic down)
    (59, 4.5, 0.375),    # D (root)
    (60, 4.875, 0.375),  # Eb (chromatic up)
    (62, 5.25, 0.375),   # F (third)
    (60, 5.625, 0.375)   # Eb (chromatic down)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.5, 0.375),    # F7 (F, A, C, Eb) - root
    (67, 1.5, 0.375),
    (69, 1.5, 0.375),
    (64, 1.5, 0.375),
    (62, 1.875, 0.375),  # F7 on 2
    (67, 1.875, 0.375),
    (69, 1.875, 0.375),
    (64, 1.875, 0.375),
    (62, 2.25, 0.375),   # F7 on 3
    (67, 2.25, 0.375),
    (69, 2.25, 0.375),
    (64, 2.25, 0.375),
    (62, 2.625, 0.375),  # F7 on 4
    (67, 2.625, 0.375),
    (69, 2.625, 0.375),
    (64, 2.625, 0.375),
    (62, 3.0, 0.375),    # F7 (root)
    (67, 3.0, 0.375),
    (69, 3.0, 0.375),
    (64, 3.0, 0.375),
    (62, 3.375, 0.375),  # F7 on 2
    (67, 3.375, 0.375),
    (69, 3.375, 0.375),
    (64, 3.375, 0.375),
    (62, 3.75, 0.375),   # F7 on 3
    (67, 3.75, 0.375),
    (69, 3.75, 0.375),
    (64, 3.75, 0.375),
    (62, 4.125, 0.375),  # F7 on 4
    (67, 4.125, 0.375),
    (69, 4.125, 0.375),
    (64, 4.125, 0.375),
    (62, 4.5, 0.375),    # F7 (root)
    (67, 4.5, 0.375),
    (69, 4.5, 0.375),
    (64, 4.5, 0.375),
    (62, 4.875, 0.375),  # F7 on 2
    (67, 4.875, 0.375),
    (69, 4.875, 0.375),
    (64, 4.875, 0.375),
    (62, 5.25, 0.375),   # F7 on 3
    (67, 5.25, 0.375),
    (69, 5.25, 0.375),
    (64, 5.25, 0.375),
    (62, 5.625, 0.375)  # F7 on 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante) - brief motif, start, leave it hanging, return and finish
# Motif: D, F, Eb, D (bars 2-4 with space in between)
sax_notes = [
    (59, 1.5, 0.375),    # D
    (62, 1.875, 0.375),  # F
    (60, 2.25, 0.375),   # Eb
    (59, 2.625, 0.375),  # D
    (62, 3.0, 0.375),    # F
    (60, 3.375, 0.375),  # Eb
    (59, 3.75, 0.375)    # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
