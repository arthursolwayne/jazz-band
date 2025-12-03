
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Sax enters with motif, bass walks, piano comps
# Sax motif: F (G4) -> G (A4) -> A (B4) -> B (C#5) -> F (G4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.6875),  # F (G4)
    pretty_midi.Note(velocity=100, pitch=69, start=1.6875, end=1.875),  # G (A4)
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0625),  # A (B4)
    pretty_midi.Note(velocity=100, pitch=74, start=2.0625, end=2.25),  # B (C#5)
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.4375),  # F (G4)
]
sax.notes.extend(sax_notes)

# Bass: walking line in F (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (D2) -> G (E2) -> A (F2) -> Bb (G2)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.6875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=40, start=1.6875, end=1.875),  # G (E2)
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),  # A (F2)
    pretty_midi.Note(velocity=80, pitch=43, start=2.0625, end=2.25),  # Bb (G2)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: Dm7 (D, F, A, C)
# Bar 4: G7 (G, B, D, F)
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),  # F (F4)
    pretty_midi.Note(velocity=80, pitch=58, start=1.5, end=1.75),  # A (A4)
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),  # C (C5)
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),  # E (E5)
    
    # Bar 3: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5),  # D (D4)
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5),  # F (F4)
    pretty_midi.Note(velocity=80, pitch=58, start=2.25, end=2.5),  # A (A4)
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5),  # C (C5)
    
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=80, pitch=55, start=2.75, end=3.0),  # G (G4)
    pretty_midi.Note(velocity=80, pitch=59, start=2.75, end=3.0),  # B (B4)
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0),  # D (D5)
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0),  # F (F5)
]
piano.notes.extend(piano_notes)

# Bar 3: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Sax continues motif, bass continues walking line, piano resolves
# Sax: F (G4) -> G (A4) -> A (B4) -> B (C#5) -> F (G4) -> G (A4) -> A (B4) -> B (C#5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=2.4375, end=2.625),  # F (G4)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.8125),  # G (A4)
    pretty_midi.Note(velocity=100, pitch=71, start=2.8125, end=3.0),  # A (B4)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.1875),  # B (C#5)
    pretty_midi.Note(velocity=100, pitch=66, start=3.1875, end=3.375),  # F (G4)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5625),  # G (A4)
    pretty_midi.Note(velocity=100, pitch=71, start=3.5625, end=3.75),  # A (B4)
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=3.9375),  # B (C#5)
]
sax.notes.extend(sax_notes)

# Bass: walking line in F (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 3: F (D2) -> G (E2) -> A (F2) -> Bb (G2)
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.4375),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=40, start=2.4375, end=2.625),  # G (E2)
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),  # A (F2)
    pretty_midi.Note(velocity=80, pitch=43, start=2.8125, end=3.0),  # Bb (G2)
    
    # Bar 4: F (D2) -> G (E2) -> A (F2) -> Bb (G2)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.1875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=40, start=3.1875, end=3.375),  # G (E2)
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),  # A (F2)
    pretty_midi.Note(velocity=80, pitch=43, start=3.5625, end=3.75),  # Bb (G2)
]
bass.notes.extend(bass_notes)

# Bar 4: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
