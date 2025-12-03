
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),  # Hihat on &
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on &
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet starts (1.5 - 3.0s)
# Sax: Dm7 (D F A C) -> Fm7 (F A C Eb)
# Bass: D (root), F (5th), Ab (chromatic), A (root)
# Piano: Dm7 (D F A C), Fm7 (F A C Eb), G7 (G B D F), Cm7 (C Eb G Bb)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Sax (Bar 2: Dm7 - Fm7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D (Dm7)
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # A (Fm7)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # Eb (Fm7)
]

# Bass (Bar 2: D - F - Ab - A)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=70, pitch=53, start=1.875, end=2.125),  # F
    pretty_midi.Note(velocity=70, pitch=51, start=2.125, end=2.5),  # Ab
    pretty_midi.Note(velocity=70, pitch=55, start=2.5, end=2.875),  # A
]

# Piano (Bar 2: Dm7 -> Fm7 -> G7 -> Cm7)
piano_notes = [
    # Dm7 - 1
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),  # C
    # Fm7 - 2
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=68, start=1.75, end=2.0),  # Eb
    # G7 - 3
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.25),  # F
    # Cm7 - 4
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),  # Bb
]

# Drums (Bar 2)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.125),  # Hihat on &
    pretty_midi.Note(velocity=90, pitch=38, start=2.125, end=2.375),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.125, end=2.375),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.375, end=2.75),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.75),  # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=3.0),  # Hihat on &
    pretty_midi.Note(velocity=90, pitch=38, start=2.75, end=3.0),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: G7 (G B D F), then Cm7 (C Eb G Bb)
# Bass: G (5th), Bb (chromatic), B (5th), C (root)
# Piano: G7 -> Cm7 -> Dm7 -> Fm7
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Sax (Bar 3: G7 - Cm7)
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G (G7)
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # B (G7)
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # D (Cm7)
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # F (Cm7)
]

# Bass (Bar 3: G - Bb - B - C)
bass_notes += [
    pretty_midi.Note(velocity=70, pitch=55, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=70, pitch=57, start=3.375, end=3.625),  # Bb
    pretty_midi.Note(velocity=70, pitch=59, start=3.625, end=4.0),  # B
    pretty_midi.Note(velocity=70, pitch=60, start=4.0, end=4.375),  # C
]

# Piano (Bar 3: G7 -> Cm7 -> Dm7 -> Fm7)
piano_notes += [
    # G7 - 1
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),  # F
    # Cm7 - 2
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),  # Bb
    # Dm7 - 3
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.75),  # C
    # Fm7 - 4
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=4.0),  # Eb
]

# Drums (Bar 3)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.625),  # Hihat on &
    pretty_midi.Note(velocity=90, pitch=38, start=3.625, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=3.875),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.875, end=4.25),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.25),  # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.5),  # Hihat on &
    pretty_midi.Note(velocity=90, pitch=38, start=4.25, end=4.5),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Dm7 (D F A C) - leave it hanging
# Bass: D (root), F (5th), Ab (chromatic), A (root)
# Piano: Dm7 (D F A C) -> Fm7 (F A C Eb) -> G7 (G B D F) -> Cm7 (C Eb G Bb)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Sax (Bar 4: Dm7)
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D (Dm7)
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # A (Dm7)
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # C (Dm7)
]

# Bass (Bar 4: D - F - Ab - A)
bass_notes += [
    pretty_midi.Note(velocity=70, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=70, pitch=53, start=4.875, end=5.125),  # F
    pretty_midi.Note(velocity=70, pitch=51, start=5.125, end=5.5),  # Ab
    pretty_midi.Note(velocity=70, pitch=55, start=5.5, end=5.875),  # A
]

# Piano (Bar 4: Dm7 -> Fm7 -> G7 -> Cm7)
piano_notes += [
    # Dm7 - 1
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),  # C
    # Fm7 - 2
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=68, start=4.75, end=5.0),  # Eb
    # G7 - 3
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=5.0, end=5.25),  # F
    # Cm7 - 4
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5),  # Bb
]

# Drums (Bar 4)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.125),  # Hihat on &
    pretty_midi.Note(velocity=90, pitch=38, start=5.125, end=5.375),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.375),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.375, end=5.75),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.75),  # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=6.0),  # Hihat on &
    pretty_midi.Note(velocity=90, pitch=38, start=5.75, end=6.0),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
