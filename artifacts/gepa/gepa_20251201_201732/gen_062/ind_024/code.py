
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: D4 (62) -> F#4 (66) -> D5 (72) -> G4 (67) (hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0), # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25), # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5), # G4
]
sax.notes.extend(sax_notes)

# Bass: D2 (38) -> A2 (45) -> D2 (38) -> E2 (41)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75), # D2
    pretty_midi.Note(velocity=100, pitch=45, start=1.75, end=2.0), # A2
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.25), # D2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.5), # E2
]
bass.notes.extend(bass_notes)

# Piano: Dmaj7 (D4, F#4, A4, C#5) -> G7 (G4, B4, D5, F4) -> D7 (D4, F#4, A4, C#5) -> C7 (C4, E4, G4, B4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=2.0), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0), # C#5
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5), # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5), # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.5), # F4
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif: D4 (62) -> F#4 (66) -> D5 (72) -> G4 (67) (hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5), # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75), # D5
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0), # G4
]
sax.notes.extend(sax_notes)

# Bass: D2 (38) -> A2 (45) -> D2 (38) -> E2 (41)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.25), # D2
    pretty_midi.Note(velocity=100, pitch=45, start=3.25, end=3.5), # A2
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.75), # D2
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.0), # E2
]
bass.notes.extend(bass_notes)

# Piano: Dmaj7 (D4, F#4, A4, C#5) -> G7 (G4, B4, D5, F4) -> D7 (D4, F#4, A4, C#5) -> C7 (C4, E4, G4, B4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.5), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5), # C#5
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0), # B4
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=4.0), # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=4.0), # F4
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif: D4 (62) -> F#4 (66) -> D5 (72) -> G4 (67) (hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0), # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25), # D5
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5), # G4
]
sax.notes.extend(sax_notes)

# Bass: D2 (38) -> A2 (45) -> D2 (38) -> E2 (41)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.75), # D2
    pretty_midi.Note(velocity=100, pitch=45, start=4.75, end=5.0), # A2
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.25), # D2
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.5), # E2
]
bass.notes.extend(bass_notes)

# Piano: Dmaj7 (D4, F#4, A4, C#5) -> G7 (G4, B4, D5, F4) -> D7 (D4, F#4, A4, C#5) -> C7 (C4, E4, G4, B4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=5.0), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0), # C#5
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.5), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.5), # B4
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.5), # D5
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.5), # F4
]
piano.notes.extend(piano_notes)

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
