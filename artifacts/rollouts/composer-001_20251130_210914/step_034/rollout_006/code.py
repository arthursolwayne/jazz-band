
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
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drums_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drum pattern for bars 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.1875, end=start_time + i * 0.1875 + 0.1875)

# Bass line (Marcus)
bass_notes = [
    # Bar 2: D (D4) -> Eb (E4b) -> F# (F#4) -> G (G4)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb4
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625), # F#4
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G4

    # Bar 3: A (A4) -> Bb (Bb4) -> C# (C#5) -> D (D5)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75), # Bb4
    pretty_midi.Note(velocity=90, pitch=73, start=3.75, end=4.125), # C#5
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),  # D5

    # Bar 4: D (D4) -> Eb (E4b) -> F# (F#4) -> G (G4)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25), # Eb4
    pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.625), # F#4
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # G4
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    # Bar 2: D7 (D4, F#4, A4, C#5)
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=85, pitch=73, start=1.5, end=1.875),  # C#5

    # Bar 3: G7 (G4, B4, D5, F#5)
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=85, pitch=77, start=3.0, end=3.375),  # F#5

    # Bar 4: D7 (D4, F#4, A4, C#5)
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=85, pitch=73, start=4.5, end=4.875),  # C#5
]
piano.notes.extend(piano_notes)

# Sax (Dante) - Main motif: D (D4) -> F# (F#4) -> A (A4) -> D (D5)
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),   # A4
    # Bar 3: Return and finish
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),   # A4
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.875),  # D5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
