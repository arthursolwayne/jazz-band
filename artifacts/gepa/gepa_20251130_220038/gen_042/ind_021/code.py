
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Sax starts with a whisper, then builds
# D7 - G7 - A7 - Bm7
# Melody: D - F# - G - A - B - D - C - B
sax_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=85, pitch=66, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=85, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=95, pitch=71, start=2.0, end=2.125),   # B
    pretty_midi.Note(velocity=90, pitch=62, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=85, pitch=60, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=2.375, end=2.5),   # B
]

# Bar 2: Bass line (D - F# - G - A)
bass_notes = [
    pretty_midi.Note(velocity=60, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=65, pitch=66, start=1.625, end=1.75),
    pretty_midi.Note(velocity=65, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=65, pitch=69, start=1.875, end=2.0),
]

# Bar 2: Piano comp (D7 on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.625),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.625),  # C#
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.625),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=1.625, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=1.625, end=1.75),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=1.625, end=1.75),  # C#
    pretty_midi.Note(velocity=80, pitch=69, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.375),  # C#
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.375),  # G
]

# Bar 3: Sax continues, building tension
# G7 - A7 - Bm7 - D7
# Melody: G - A - B - D - C - B - A - G
sax_notes += [
    pretty_midi.Note(velocity=85, pitch=67, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=2.75, end=2.875),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=2.875, end=3.0),   # D
    pretty_midi.Note(velocity=85, pitch=60, start=3.0, end=3.125),   # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.125, end=3.25),  # B
    pretty_midi.Note(velocity=85, pitch=69, start=3.25, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.5),   # G
]

# Bar 3: Bass line (G - A - B - D)
bass_notes += [
    pretty_midi.Note(velocity=65, pitch=67, start=2.5, end=2.625),
    pretty_midi.Note(velocity=65, pitch=69, start=2.625, end=2.75),
    pretty_midi.Note(velocity=65, pitch=71, start=2.75, end=2.875),
    pretty_midi.Note(velocity=65, pitch=62, start=2.875, end=3.0),
]

# Bar 3: Piano comp (G7 on 2 and 4)
piano_notes += [
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.5, end=2.625),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=2.5, end=2.625),  # C#
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=2.75),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=2.75),  # C#
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.375),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.375),  # C#
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.375),  # D
]

# Bar 4: Sax resolves, a cry
# Bm7 - D7 - G7 - A7
# Melody: B - D - C - B - A - G - F# - D
sax_notes += [
    pretty_midi.Note(velocity=95, pitch=71, start=3.5, end=3.625),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=3.625, end=3.75),  # D
    pretty_midi.Note(velocity=85, pitch=60, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.875, end=4.0),   # B
    pretty_midi.Note(velocity=85, pitch=69, start=4.0, end=4.125),   # A
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.25),  # G
    pretty_midi.Note(velocity=75, pitch=66, start=4.25, end=4.375),  # F#
    pretty_midi.Note(velocity=80, pitch=62, start=4.375, end=4.5),   # D
]

# Bar 4: Bass line (B - D - G - A)
bass_notes += [
    pretty_midi.Note(velocity=65, pitch=71, start=3.5, end=3.625),
    pretty_midi.Note(velocity=65, pitch=62, start=3.625, end=3.75),
    pretty_midi.Note(velocity=65, pitch=67, start=3.75, end=3.875),
    pretty_midi.Note(velocity=65, pitch=69, start=3.875, end=4.0),
]

# Bar 4: Piano comp (Bm7 on 2 and 4)
piano_notes += [
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.625),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.625),  # C#
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.625),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.625, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=3.625, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=72, start=3.625, end=3.75),  # C#
    pretty_midi.Note(velocity=80, pitch=69, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.25),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.25),  # C#
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.25),  # G
]

# Add notes to instruments
sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
