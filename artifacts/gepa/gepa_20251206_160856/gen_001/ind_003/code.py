
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4 (next bar)
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: F (G4) -> A (B4) -> C (D5) -> B (C5) -> F (G4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F (G4)
    pretty_midi.Note(velocity=100, pitch=73, start=1.875, end=2.25), # A (B4)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # C (D5)
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # B (C5)
]

# Bass: walking line (F, Bb, B, Ab, G, C, D, F)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=57, start=1.875, end=2.25),  # Bb (F2)
    pretty_midi.Note(velocity=80, pitch=58, start=2.25, end=2.625),  # B (F#2)
    pretty_midi.Note(velocity=80, pitch=55, start=2.625, end=3.0),   # Ab (D2)
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),   # G (C2)
    pretty_midi.Note(velocity=80, pitch=56, start=3.375, end=3.75),  # C (E2)
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125),  # D (F2)
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5),   # F (D2)
]

# Piano: chord on bar 2 (F7), bar 3 (Bb7), bar 4 (C7)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),   # F (C4)
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=3.0),   # A (E4)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),   # C (G4)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),   # E (B4)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),   # F# (C#5)
]

piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),   # Bb (A3)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),   # D (C4)
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=4.5),   # F (E4)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),   # A (G4)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),   # C (B4)
]

piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),   # C (A3)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),   # E (C4)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),   # G (E4)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),   # B (G4)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),   # D (B4)
]

# Add the notes to instruments
sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes_bar2)
piano.notes.extend(piano_notes_bar3)
piano.notes.extend(piano_notes_bar4)
drums.notes.extend(drum_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Snare on 2 and 4, kick on 1 and 3, hihat on every eighth
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
]

drums.notes.extend(drum_notes_bar3)

# Bar 4: Drums (4.5 - 6.0s)
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]

drums.notes.extend(drum_notes_bar4)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
