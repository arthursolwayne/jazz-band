
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.375),    # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.375),   # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F (F, G, Ab, A, Bb, B, C, Db)
bass_notes = [
    (45, 1.5, 1.625),     # F
    (46, 1.625, 1.75),    # G
    (47, 1.75, 1.875),    # Ab
    (48, 1.875, 2.0),     # A
    (49, 2.0, 2.125),     # Bb
    (50, 2.125, 2.25),    # B
    (51, 2.25, 2.375),    # C
    (52, 2.375, 2.5),     # Db
    (45, 2.5, 2.625),     # F
    (46, 2.625, 2.75),    # G
    (47, 2.75, 2.875),    # Ab
    (48, 2.875, 3.0),     # A
    (49, 3.0, 3.125),     # Bb
    (50, 3.125, 3.25),    # B
    (51, 3.25, 3.375),    # C
    (52, 3.375, 3.5),     # Db
    (45, 3.5, 3.625),     # F
    (46, 3.625, 3.75),    # G
    (47, 3.75, 3.875),    # Ab
    (48, 3.875, 4.0),     # A
    (49, 4.0, 4.125),     # Bb
    (50, 4.125, 4.25),    # B
    (51, 4.25, 4.375),    # C
    (52, 4.375, 4.5),     # Db
    (45, 4.5, 4.625),     # F
    (46, 4.625, 4.75),    # G
    (47, 4.75, 4.875),    # Ab
    (48, 4.875, 5.0),     # A
    (49, 5.0, 5.125),     # Bb
    (50, 5.125, 5.25),    # B
    (51, 5.25, 5.375),    # C
    (52, 5.375, 5.5),     # Db
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Diane: 7th chords, comp on 2 and 4
# F7 on 2 (F, A, C, Eb)
# Bb7 on 4 (Bb, D, F, Ab)
piano_notes = [
    (53, 1.625, 1.875),   # F
    (58, 1.625, 1.875),   # A
    (57, 1.625, 1.875),   # C
    (55, 1.625, 1.875),   # Eb
    (50, 2.125, 2.375),   # Bb
    (55, 2.125, 2.375),   # D
    (53, 2.125, 2.375),   # F
    (52, 2.125, 2.375),   # Ab
    (53, 3.125, 3.375),   # F
    (58, 3.125, 3.375),   # A
    (57, 3.125, 3.375),   # C
    (55, 3.125, 3.375),   # Eb
    (50, 3.625, 3.875),   # Bb
    (55, 3.625, 3.875),   # D
    (53, 3.625, 3.875),   # F
    (52, 3.625, 3.875),   # Ab
    (53, 4.625, 4.875),   # F
    (58, 4.625, 4.875),   # A
    (57, 4.625, 4.875),   # C
    (55, 4.625, 4.875),   # Eb
    (50, 5.125, 5.375),   # Bb
    (55, 5.125, 5.375),   # D
    (53, 5.125, 5.375),   # F
    (52, 5.125, 5.375),   # Ab
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar2 = [
    (36, 1.5, 1.625),    # Kick on 1
    (42, 1.5, 1.625),    # Hihat on 1
    (38, 1.625, 1.75),   # Snare on 2
    (42, 1.625, 1.75),   # Hihat on 2
    (36, 1.875, 2.0),    # Kick on 3
    (42, 1.875, 2.0),    # Hihat on 3
    (38, 2.0, 2.125),    # Snare on 4
    (42, 2.0, 2.125),    # Hihat on 4
    (36, 2.5, 2.625),    # Kick on 1
    (42, 2.5, 2.625),    # Hihat on 1
    (38, 2.625, 2.75),   # Snare on 2
    (42, 2.625, 2.75),   # Hihat on 2
    (36, 2.875, 3.0),    # Kick on 3
    (42, 2.875, 3.0),    # Hihat on 3
    (38, 3.0, 3.125),    # Snare on 4
    (42, 3.0, 3.125),    # Hihat on 4
    (36, 3.5, 3.625),    # Kick on 1
    (42, 3.5, 3.625),    # Hihat on 1
    (38, 3.625, 3.75),   # Snare on 2
    (42, 3.625, 3.75),   # Hihat on 2
    (36, 3.875, 4.0),    # Kick on 3
    (42, 3.875, 4.0),    # Hihat on 3
    (38, 4.0, 4.125),    # Snare on 4
    (42, 4.0, 4.125),    # Hihat on 4
    (36, 4.5, 4.625),    # Kick on 1
    (42, 4.5, 4.625),    # Hihat on 1
    (38, 4.625, 4.75),   # Snare on 2
    (42, 4.625, 4.75),   # Hihat on 2
    (36, 4.875, 5.0),    # Kick on 3
    (42, 4.875, 5.0),    # Hihat on 3
    (38, 5.0, 5.125),    # Snare on 4
    (42, 5.0, 5.125),    # Hihat on 4
]
for note in drum_notes_bar2:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Dante: Saxophone motif (short, singing, leaves it hanging)
# F (53), Bb (50), D (55), F (53)
sax_notes = [
    (53, 1.5, 1.625),    # F
    (50, 1.625, 1.75),   # Bb
    (55, 1.75, 1.875),   # D
    (53, 1.875, 2.0),    # F
    (53, 2.0, 2.125),    # F
    (50, 2.125, 2.25),   # Bb
    (55, 2.25, 2.375),   # D
    (53, 2.375, 2.5),    # F
]
sax.notes.extend([pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]) for note in sax_notes])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
