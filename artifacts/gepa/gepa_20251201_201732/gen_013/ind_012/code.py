
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

# Bar 2: Everyone in. Sax melody starts.
# Dm7 -> G7 -> Cm7 -> F7

# Bass: Walking line
bass_notes = [
    (38, 1.5, 1.625),  # D2
    (40, 1.625, 1.875),  # F
    (43, 1.875, 2.0),  # A
    (40, 2.0, 2.125),  # F
    (42, 2.125, 2.375),  # G
    (45, 2.375, 2.5),  # B
    (43, 2.5, 2.625),  # A
    (42, 2.625, 2.875),  # G
    (38, 2.875, 3.0),  # D
    (40, 3.0, 3.125),  # F
    (43, 3.125, 3.375),  # A
    (40, 3.375, 3.5),  # F
    (42, 3.5, 3.625),  # G
    (45, 3.625, 3.875),  # B
    (43, 3.875, 4.0),  # A
    (42, 4.0, 4.125)   # G
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: Open voicings, different chord each bar
# Bar 2: Dm7
piano_notes = [
    # Bar 2 (Dm7)
    (62, 1.5, 1.75),  # D
    (67, 1.5, 1.75),  # G
    (72, 1.5, 1.75),  # C
    (60, 1.5, 1.75),  # F
    # Bar 3 (G7)
    (67, 2.25, 2.5),  # G
    (72, 2.25, 2.5),  # C
    (76, 2.25, 2.5),  # D
    (69, 2.25, 2.5),  # B
    # Bar 4 (Cm7)
    (60, 3.0, 3.25),  # C
    (65, 3.0, 3.25),  # E
    (72, 3.0, 3.25),  # G
    (63, 3.0, 3.25),  # B
    # Bar 4 (F7)
    (65, 3.75, 4.0),  # F
    (72, 3.75, 4.0),  # A
    (77, 3.75, 4.0),  # C
    (69, 3.75, 4.0)   # E
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: Melody
# Bar 2: Dm7 -> F (1.5 - 1.75)
# Bar 3: G7 -> A (2.25 - 2.5)
# Bar 4: Cm7 -> D (3.0 - 3.25)
# Bar 4: F7 -> F (3.75 - 4.0)
sax_notes = [
    (62, 1.5, 1.75),  # D
    (65, 2.25, 2.5),  # F
    (67, 3.0, 3.25),  # A
    (65, 3.75, 4.0)   # F
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Drums (1.5 - 3.0s)
drum_notes = [
    (36, 1.5, 1.875),  # Kick on 1
    (42, 1.5, 1.875),  # Hihat on 1
    (38, 1.875, 2.125),  # Snare on 2
    (42, 1.875, 2.125),  # Hihat on 2
    (36, 2.25, 2.625),  # Kick on 3
    (42, 2.25, 2.625),  # Hihat on 3
    (38, 2.625, 2.875),  # Snare on 4
    (42, 2.625, 2.875)   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Drums (3.0 - 4.5s)
drum_notes = [
    (36, 3.0, 3.375),  # Kick on 1
    (42, 3.0, 3.375),  # Hihat on 1
    (38, 3.375, 3.625),  # Snare on 2
    (42, 3.375, 3.625),  # Hihat on 2
    (36, 3.75, 4.125),  # Kick on 3
    (42, 3.75, 4.125),  # Hihat on 3
    (38, 4.125, 4.5),  # Snare on 4
    (42, 4.125, 4.5)   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
