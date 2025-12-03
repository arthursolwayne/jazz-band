
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
    # Bar 1: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Roots and fifths with chromatic approaches
# Dm7 -> G7 -> Cmaj7 -> F7
# Roots: D (2), G (3), C (1), F (2)
# Fifths: A (2), D (3), G (1), Bb (2)
# Chromatic approaches: C# (before D), F (before G), Bb (before C), E (before F)
bass_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # A2 (fifth)
    pretty_midi.Note(velocity=80, pitch=37, start=1.125, end=1.5),  # C#2 (approach to D)
    # Bar 3: G7
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),  # G2 (root)
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.25),  # D3 (fifth)
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # F2 (approach to G)
    # Bar 4: Cmaj7
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),  # C3 (root)
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625),  # G3 (fifth)
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),  # Bb3 (approach to C)
    # Bar 5: F7
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # F3 (root)
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0),  # Bb3 (fifth)
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),  # E3 (approach to F)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
# Bar 3: G7 (G-B-D-F)
# Bar 4: Cmaj7 (C-E-G-B)
# Bar 5: F7 (F-A-C-Eb)
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
    # Bar 3: G7
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # F5
    # Bar 4: Cmaj7
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    # Bar 5: F7
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),  # Eb5
]
piano.notes.extend(piano_notes)

# Sax: One short motif (D-F#-G), start it, leave it hanging, come back and finish it
# Bar 2: Start motif (D-F#-G)
# Bar 3: Leave it hanging (no notes)
# Bar 4: Restate motif (D-F#-G)
sax_notes = [
    # Bar 2: D-F#-G
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.625, end=1.75),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # G4
    # Bar 4: D-F#-G
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=2.75, end=2.875),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=2.875, end=3.0),  # G4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
