
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

# Drums - Bar 1 (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.5, end=1.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line (Bar 2): Walking line with chromatic approaches
bass_notes = [
    # D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # F#2 (fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),
    # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),
    # G2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano (Bar 2): Open voicing on D7, resolve on bar 4
piano_notes = [
    # D7 (open voicing)
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=3.0),  # D5
    pretty_midi.Note(velocity=85, pitch=70, start=1.5, end=3.0),  # B4
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=3.0),  # D4
    # Next bar: G7 (open voicing)
    pretty_midi.Note(velocity=85, pitch=76, start=3.0, end=4.5),  # G5
    pretty_midi.Note(velocity=85, pitch=74, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=4.5),  # F#4
    # Next bar: A7 (open voicing)
    pretty_midi.Note(velocity=85, pitch=77, start=4.5, end=6.0),  # A5
    pretty_midi.Note(velocity=85, pitch=74, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=85, pitch=71, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=6.0),  # F#4
]
piano.notes.extend(piano_notes)

# Drums - Bar 2 (1.5 - 3.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Sax - Bar 2: Melody (D to G to A to D)
sax_notes = [
    # D4 (start of motif)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    # G4 (rising)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    # A4 (peak)
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),
    # Rest (space)
    pretty_midi.Note(velocity=0, pitch=62, start=2.25, end=2.5),
    # D5 (return)
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),
    # Rest (space)
    pretty_midi.Note(velocity=0, pitch=62, start=2.75, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line (Bar 3): Walking line with chromatic approaches
bass_notes = [
    # A2 (root)
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),
    # C#3 (fifth)
    pretty_midi.Note(velocity=80, pitch=48, start=3.375, end=3.75),
    # B2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125),
    # D3 (root)
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Drums - Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Sax - Bar 3: Melody (rest and release)
sax_notes = [
    # Rest (space)
    pretty_midi.Note(velocity=0, pitch=62, start=3.0, end=3.25),
    # G4 (return)
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    # A4 (peak)
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),
    # Rest
    pretty_midi.Note(velocity=0, pitch=62, start=3.75, end=4.0),
    # D5 (return)
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.25),
    # Rest
    pretty_midi.Note(velocity=0, pitch=62, start=4.25, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line (Bar 4): Walking line with chromatic approaches
bass_notes = [
    # D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),
    # F#2 (fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25),
    # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625),
    # G2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Drums - Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Sax - Bar 4: Melody (rest and close)
sax_notes = [
    # Rest
    pretty_midi.Note(velocity=0, pitch=62, start=4.5, end=4.75),
    # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),
    # A4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),
    # Rest
    pretty_midi.Note(velocity=0, pitch=62, start=5.25, end=5.5),
    # D5
    pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=5.75),
    # Rest
    pretty_midi.Note(velocity=0, pitch=62, start=5.75, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
