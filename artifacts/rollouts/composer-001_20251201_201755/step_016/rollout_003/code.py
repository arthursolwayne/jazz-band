
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line starting on D2 (MIDI 38)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # D2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),   # A2
]
bass.notes.extend(bass_notes)

# Piano: First chord is Fmaj7 (F, A, C, E) open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # E4 (top of Fmaj7)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F3
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # A3
]
piano.notes.extend(piano_notes)

# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # C5
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=3.0),  # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F (MIDI 43) -> G (MIDI 45) -> A (MIDI 47) -> A (MIDI 47)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),   # F2
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),   # A2
]
bass.notes.extend(bass_notes)

# Piano: Dm7 (D, F, A, C) open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # C4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # D4
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # Bb4
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),  # G4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: A (MIDI 47) -> Bb (MIDI 48) -> C (MIDI 50) -> C (MIDI 50)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),   # A2
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.25),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),  # C2
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),   # C2
]
bass.notes.extend(bass_notes)

# Piano: G7 (G, B, D, F) open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=6.0),  # F4 (top of G7)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # B3
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # G3
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # E4
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),  # G4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
