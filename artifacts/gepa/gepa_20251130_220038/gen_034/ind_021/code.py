
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: D (D4), F# (F#4), A (A4), B (B4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # B4
]
sax.notes.extend(sax_notes)

# Bass line: D (D2), C# (C#2), D (D2), E (E2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=80, pitch=44, start=1.75, end=2.0),  # C#2
    pretty_midi.Note(velocity=80, pitch=45, start=2.0, end=2.25),  # D2
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.5),  # E2
]
bass.notes.extend(bass_notes)

# Piano chords: D7 (D4, F#4, A4, C#5)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # C#5
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody: E (E4), F# (F#4), G (G4), A (A4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # E4
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # A4
]
sax.notes.extend(sax_notes)

# Bass line: E (E2), F# (F#2), G (G2), A (A2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.25),  # E2
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),  # F#2
    pretty_midi.Note(velocity=80, pitch=49, start=3.5, end=3.75),  # G2
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano chords: D7 (D4, F#4, A4, C#5)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # C#5
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody: B (B4), A (A4), G (G4), F# (F#4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),  # F#4
]
sax.notes.extend(sax_notes)

# Bass line: B (B1), A (A1), G (G1), F# (F#1)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.75),  # B1
    pretty_midi.Note(velocity=80, pitch=57, start=4.75, end=5.0),  # A1
    pretty_midi.Note(velocity=80, pitch=55, start=5.0, end=5.25),  # G1
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5),  # F#1
]
bass.notes.extend(bass_notes)

# Piano chords: D7 (D4, F#4, A4, C#5)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # C#5
]
piano.notes.extend(piano_notes)

# Add drum fill for bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.25),  # Hi-hat
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_shorter_intro.mid")
