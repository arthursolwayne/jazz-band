
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
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
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (walking line with chromatic approaches)
# D2 (MIDI 38) - G2 (MIDI 43)
# Dm7: D F A C
# Chord progression: Dm7 -> G7 -> Cm7 -> F7
# Roots: D -> G -> C -> F
# Marcus walks with chromatic approaches
bass_notes = [
    # Bar 2: Dm7
    (38, 1.5, 1.5),  # D2
    (40, 1.875, 1.875),  # E2 (chromatic up)
    (38, 2.25, 2.25),  # D2
    (40, 2.625, 2.625),  # E2
    # Bar 3: G7
    (43, 2.625, 2.625),  # G2
    (44, 2.625, 2.625),  # A2 (chromatic up)
    (43, 3.0, 3.0),  # G2
    (44, 3.375, 3.375),  # A2
    # Bar 4: Cm7
    (40, 3.375, 3.375),  # C2
    (41, 3.75, 3.75),  # D2 (chromatic up)
    (40, 4.125, 4.125),  # C2
    (41, 4.5, 4.5),  # D2
    # Bar 4: F7
    (45, 4.5, 4.5),  # F2
    (46, 4.875, 4.875),  # G2 (chromatic up)
    (45, 5.25, 5.25),  # F2
    (46, 5.625, 5.625)  # G2
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Diane on piano (open voicings, resolve on last beat of each bar)
# Bar 2: Dm7 (D F A C)
# Bar 3: G7 (G B D F)
# Bar 4: Cm7 (C Eb G Bb)
# Bar 4: F7 (F A C E)
piano_notes = [
    # Bar 2: Dm7 (D F A C) - open voicing
    (50, 1.5, 1.5),  # D4
    (52, 1.5, 1.5),  # F4
    (55, 1.5, 1.5),  # A4
    (57, 1.5, 1.5),  # C5
    # Bar 2: Comp on 2 and 4
    (61, 2.25, 2.25),  # C6
    (64, 2.625, 2.625),  # E6
    # Bar 3: G7 (G B D F)
    (62, 2.625, 2.625),  # G5
    (65, 2.625, 2.625),  # B5
    (67, 2.625, 2.625),  # D6
    (69, 2.625, 2.625),  # F6
    # Bar 3: Comp on 2 and 4
    (72, 3.375, 3.375),  # G7
    (74, 3.75, 3.75),  # B7
    # Bar 4: Cm7 (C Eb G Bb)
    (60, 3.75, 3.75),  # C5
    (63, 3.75, 3.75),  # Eb5
    (67, 3.75, 3.75),  # G5
    (69, 3.75, 3.75),  # Bb5
    # Bar 4: F7 (F A C E)
    (65, 4.5, 4.5),  # F5
    (68, 4.5, 4.5),  # A5
    (72, 4.5, 4.5),  # C6
    (76, 4.5, 4.5),  # E6
    # Bar 4: Comp on 2 and 4
    (79, 5.25, 5.25),  # G7
    (82, 5.625, 5.625),  # B7
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Dante on sax (short motif, leave it hanging)
# Motif: Dm7 - F, A, D, G (MIDI 62, 65, 67, 69)
# Start, leave it hanging, come back and finish it
# Bar 2: notes on 1, 2, 3, 4
# Bar 3: notes on 1, 2
# Bar 4: notes on 3, 4

sax_notes = [
    (62, 1.5, 1.5),  # F4 on 1
    (65, 1.875, 1.875),  # A4 on 2
    (67, 2.25, 2.25),  # D5 on 3
    (69, 2.625, 2.625),  # G5 on 4

    (62, 3.0, 3.0),  # F4 on 1
    (65, 3.375, 3.375),  # A4 on 2

    (67, 4.125, 4.125),  # D5 on 3
    (69, 4.5, 4.5),  # G5 on 4
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Add drum fills for energy
# Bar 2: Fill on 2
drum_notes = [
    (38, 2.25, 2.25),  # Snare on 2
    (42, 2.25, 2.25),  # Hihat on 2
    (38, 2.625, 2.625),  # Snare on 3
    (42, 2.625, 2.625),  # Hihat on 3
    (36, 3.0, 3.0),  # Kick on 4
    (42, 3.0, 3.0),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Fill on 2
drum_notes = [
    (38, 3.375, 3.375),  # Snare on 2
    (42, 3.375, 3.375),  # Hihat on 2
    (38, 3.75, 3.75),  # Snare on 3
    (42, 3.75, 3.75),  # Hihat on 3
    (36, 4.125, 4.125),  # Kick on 4
    (42, 4.125, 4.125),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Fill on 2
drum_notes = [
    (38, 4.5, 4.5),  # Snare on 2
    (42, 4.5, 4.5),  # Hihat on 2
    (38, 4.875, 4.875),  # Snare on 3
    (42, 4.875, 4.875),  # Hihat on 3
    (36, 5.25, 5.25),  # Kick on 4
    (42, 5.25, 5.25),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
