
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # Eb2
    pretty_midi.Note(velocity=80, pitch=55, start=2.625, end=3.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C5
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F4
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Motif in Dm
# Start with a quarter note D (D4) on beat 1
# Then a quarter note Bb (Bb4) on beat 2
# Then a half note C (C4) on beat 3 and 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=3.0),   # Bb4
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # C4 (half note start)
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75), # C4 (half note end)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # D2
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125),  # Eb2
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5),   # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings
piano_notes = [
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F4
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.125),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # Bb4
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # D2
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625),  # Eb2
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=6.0),   # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings
piano_notes = [
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Bb4
]
piano.notes.extend(piano_notes)

# SAX: Repeat motif but with a slight variation
# D4 (beat 1), Bb4 (beat 2), half note C4 (beats 3-4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=5.25),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=6.0),   # Bb4
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),  # C4 (half note start)
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),  # C4 (half note end)
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
