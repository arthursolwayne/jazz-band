
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
    (36, 0.0, 0.375),     # Kick on 1
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.75, 0.125),    # Hihat on 8
    (42, 0.875, 0.125),   # Hihat on 8
    (36, 1.125, 0.375),   # Kick on 3
    (38, 1.5, 0.375)      # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F - G - Ab - A (walking line with chromatic approach)
bass_notes = [
    (70, 1.5, 0.375),     # F
    (71, 1.875, 0.375),   # G
    (69, 2.25, 0.375),    # Ab
    (71, 2.625, 0.375)    # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Fmaj7 -> Bbm7 -> E7 -> Am7
piano_notes_bar2 = [
    (65, 1.5, 0.375),     # F
    (69, 1.5, 0.375),     # A
    (71, 1.5, 0.375),     # C
    (77, 1.5, 0.375),     # E
    (60, 1.875, 0.375),   # Bb
    (64, 1.875, 0.375),   # D
    (67, 1.875, 0.375),   # F
    (72, 1.875, 0.375),   # A
    (65, 2.25, 0.375),    # E
    (69, 2.25, 0.375),    # G
    (72, 2.25, 0.375),    # B
    (76, 2.25, 0.375),    # D
    (60, 2.625, 0.375),   # A
    (64, 2.625, 0.375),   # C
    (67, 2.625, 0.375),   # E
    (71, 2.625, 0.375)    # G
]
for note, start, duration in piano_notes_bar2:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, start on F, end on Bb, leave it hanging
sax_notes = [
    (87, 1.5, 0.375),     # F
    (89, 1.875, 0.375),   # G
    (84, 2.625, 0.375)    # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Bb - C - Db - D
bass_notes = [
    (70, 3.0, 0.375),     # Bb
    (71, 3.375, 0.375),   # C
    (69, 3.75, 0.375),    # Db
    (71, 4.125, 0.375)    # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Bbmaj7 -> Ebm7 -> Ab7 -> Dm7
piano_notes_bar3 = [
    (60, 3.0, 0.375),     # Bb
    (64, 3.0, 0.375),     # D
    (67, 3.0, 0.375),     # F
    (72, 3.0, 0.375),     # A
    (58, 3.375, 0.375),   # Eb
    (62, 3.375, 0.375),   # G
    (65, 3.375, 0.375),   # Bb
    (70, 3.375, 0.375),   # D
    (62, 3.75, 0.375),    # Ab
    (66, 3.75, 0.375),    # C
    (69, 3.75, 0.375),    # Eb
    (74, 3.75, 0.375),    # G
    (59, 4.125, 0.375),   # D
    (63, 4.125, 0.375),   # F
    (66, 4.125, 0.375),   # A
    (71, 4.125, 0.375)    # C
]
for note, start, duration in piano_notes_bar3:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: continuation of motif, Bb - Ab - D
sax_notes = [
    (84, 3.0, 0.375),     # Bb
    (82, 3.375, 0.375),   # Ab
    (69, 4.125, 0.375)    # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D - Eb - F - G
bass_notes = [
    (71, 4.5, 0.375),     # D
    (72, 4.875, 0.375),   # Eb
    (70, 5.25, 0.375),    # F
    (72, 5.625, 0.375)    # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: D7 -> G7 -> C7 -> F7
piano_notes_bar4 = [
    (69, 4.5, 0.375),     # D
    (72, 4.5, 0.375),     # F
    (74, 4.5, 0.375),     # A
    (77, 4.5, 0.375),     # C
    (72, 4.875, 0.375),   # G
    (76, 4.875, 0.375),   # B
    (79, 4.875, 0.375),   # D
    (82, 4.875, 0.375),   # F
    (77, 5.25, 0.375),    # C
    (80, 5.25, 0.375),    # E
    (83, 5.25, 0.375),    # G
    (86, 5.25, 0.375),    # B
    (70, 5.625, 0.375),   # F
    (74, 5.625, 0.375),   # A
    (77, 5.625, 0.375),   # C
    (80, 5.625, 0.375)    # E
]
for note, start, duration in piano_notes_bar4:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: resolution on F
sax_notes = [
    (87, 4.5, 0.375)      # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for bar 3 and 4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    drum_notes = [
        (36, start + 0.0, 0.375),     # Kick on 1
        (38, start + 0.375, 0.375),   # Snare on 2
        (42, start + 0.75, 0.125),    # Hihat on 8
        (42, start + 0.875, 0.125),   # Hihat on 8
        (36, start + 1.125, 0.375),   # Kick on 3
        (38, start + 1.5, 0.375),     # Snare on 4
        (42, start + 1.875, 0.125),   # Hihat on 8
        (42, start + 1.999, 0.125),   # Hihat on 8
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
