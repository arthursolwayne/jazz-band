
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),   # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet starts here (1.5 - 3.0s)

# Marcus: Walking bass line (F - Bb - B - C), with chromatic approaches
# F (D2), Bb (F3), B (G3), C (A3)
# Bar 2: F -> Bb -> B -> C
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=38, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=70, pitch=41, start=1.875, end=2.25),  # Bb (F3)
    pretty_midi.Note(velocity=70, pitch=43, start=2.25, end=2.625),  # B (G3)
    pretty_midi.Note(velocity=70, pitch=45, start=2.625, end=3.0),  # C (A3)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb) -> Bm7b5 (B D F A) -> E7 (E G# B D) -> Am7 (A C E G)
# Comp on 2 and 4
piano_notes = [
    # F7 on 1
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F (F4)
    pretty_midi.Note(velocity=80, pitch=68, start=1.5, end=1.875),  # A (A4)
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),  # C (C5)
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # Eb (Eb4)

    # Bm7b5 on 2
    pretty_midi.Note(velocity=85, pitch=69, start=1.875, end=2.25),  # B (B4)
    pretty_midi.Note(velocity=75, pitch=72, start=1.875, end=2.25),  # D (D5)
    pretty_midi.Note(velocity=65, pitch=67, start=1.875, end=2.25),  # F (F4)
    pretty_midi.Note(velocity=65, pitch=76, start=1.875, end=2.25),  # A (A5)

    # E7 on 3
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.625),  # E (E4)
    pretty_midi.Note(velocity=75, pitch=69, start=2.25, end=2.625),  # G# (G#4)
    pretty_midi.Note(velocity=70, pitch=72, start=2.25, end=2.625),  # B (B4)
    pretty_midi.Note(velocity=65, pitch=67, start=2.25, end=2.625),  # D (D4)

    # Am7 on 4
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # A (A4)
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),   # C (C5)
    pretty_midi.Note(velocity=70, pitch=76, start=2.625, end=3.0),   # E (E5)
    pretty_midi.Note(velocity=60, pitch=71, start=2.625, end=3.0),   # G (G4)
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: F -> Eb -> D -> Eb -> F (in the first bar), then F -> Eb -> D -> C
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.625),  # F (F5)
    pretty_midi.Note(velocity=95, pitch=74, start=1.625, end=1.75),  # Eb (Eb5)
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=1.875),  # D (D5)
    pretty_midi.Note(velocity=95, pitch=74, start=1.875, end=2.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.125),  # F

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.375),  # F (F5)
    pretty_midi.Note(velocity=95, pitch=74, start=2.375, end=2.5),    # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.625),    # D
    pretty_midi.Note(velocity=85, pitch=71, start=2.625, end=2.75),   # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums continue (3.0 - 4.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat
    pretty_midi.Note(velocity=90, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),   # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Continue bass, piano, sax
# Marcus: F -> Bb -> B -> C
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=38, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=70, pitch=41, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=70, pitch=43, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=70, pitch=45, start=4.125, end=4.5),   # C
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: F7 (F A C Eb) -> Bm7b5 (B D F A) -> E7 (E G# B D) -> Am7 (A C E G)
# Comp on 2 and 4
piano_notes = [
    # F7 on 1
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),   # F (F4)
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.375),   # A (A4)
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375),   # C (C5)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),   # Eb (Eb4)

    # Bm7b5 on 2
    pretty_midi.Note(velocity=85, pitch=69, start=3.375, end=3.75),  # B (B4)
    pretty_midi.Note(velocity=75, pitch=72, start=3.375, end=3.75),  # D (D5)
    pretty_midi.Note(velocity=65, pitch=67, start=3.375, end=3.75),  # F (F4)
    pretty_midi.Note(velocity=65, pitch=76, start=3.375, end=3.75),  # A (A5)

    # E7 on 3
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=4.125),  # E (E4)
    pretty_midi.Note(velocity=75, pitch=69, start=3.75, end=4.125),  # G# (G#4)
    pretty_midi.Note(velocity=70, pitch=72, start=3.75, end=4.125),  # B (B4)
    pretty_midi.Note(velocity=65, pitch=67, start=3.75, end=4.125),  # D (D4)

    # Am7 on 4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.5),    # A (A4)
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.5),    # C (C5)
    pretty_midi.Note(velocity=70, pitch=76, start=3.75, end=4.5),    # E (E5)
    pretty_midi.Note(velocity=60, pitch=71, start=3.75, end=4.5),    # G (G4)
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Continue sax melody
# Bar 4: F -> Eb -> D -> C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=95, pitch=74, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=85, pitch=71, start=3.375, end=3.5),   # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat
    pretty_midi.Note(velocity=90, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),   # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Continue bass, piano, sax

# Marcus: F -> Bb -> B -> C
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=38, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=70, pitch=41, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=70, pitch=43, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=70, pitch=45, start=5.625, end=6.0),   # C
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: F7 (F A C Eb) -> Bm7b5 (B D F A) -> E7 (E G# B D) -> Am7 (A C E G)
# Comp on 2 and 4
piano_notes = [
    # F7 on 1
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),   # F (F4)
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),   # A (A4)
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),   # C (C5)
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),   # Eb (Eb4)

    # Bm7b5 on 2
    pretty_midi.Note(velocity=85, pitch=69, start=4.875, end=5.25),  # B (B4)
    pretty_midi.Note(velocity=75, pitch=72, start=4.875, end=5.25),  # D (D5)
    pretty_midi.Note(velocity=65, pitch=67, start=4.875, end=5.25),  # F (F4)
    pretty_midi.Note(velocity=65, pitch=76, start=4.875, end=5.25),  # A (A5)

    # E7 on 3
    pretty_midi.Note(velocity=85, pitch=64, start=5.25, end=5.625),  # E (E4)
    pretty_midi.Note(velocity=75, pitch=69, start=5.25, end=5.625),  # G# (G#4)
    pretty_midi.Note(velocity=70, pitch=72, start=5.25, end=5.625),  # B (B4)
    pretty_midi.Note(velocity=65, pitch=67, start=5.25, end=5.625),  # D (D4)

    # Am7 on 4
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=6.0),    # A (A4)
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=6.0),    # C (C5)
    pretty_midi.Note(velocity=70, pitch=76, start=5.25, end=6.0),    # E (E5)
    pretty_midi.Note(velocity=60, pitch=71, start=5.25, end=6.0),    # G (G4)
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Continue sax melody
# Bar 4: F -> Eb -> D -> C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=95, pitch=74, start=4.625, end=4.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=85, pitch=71, start=4.875, end=5.0),   # C
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
