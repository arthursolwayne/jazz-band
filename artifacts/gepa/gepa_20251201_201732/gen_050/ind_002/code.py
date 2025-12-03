
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody - a haunting motif, incomplete
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # D5
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=2.75, end=3.0),  # E5
]
sax.notes.extend(sax_notes)

# Bass line - walking with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D3 (root)
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # C#3 (chromatic)
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25),  # F3 (fifth)
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5),  # E3 (chromatic)
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),  # D3 (root)
    pretty_midi.Note(velocity=80, pitch=53, start=2.75, end=3.0),  # G3 (octave)
]
bass.notes.extend(bass_notes)

# Piano comp on 2 and 4
piano_notes = [
    # Bar 2: Open voicing, D7sus4 (D, G, A, C#)
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=2.0),  # Bb4
    pretty_midi.Note(velocity=85, pitch=65, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=2.0),  # F4 (passing tone)

    # Bar 3: Open voicing, Bm7b5 (B, D, F#, A)
    pretty_midi.Note(velocity=85, pitch=66, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=85, pitch=69, start=2.25, end=2.5),  # Bb4 (chromatic)
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.5),  # F4
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.5),  # D4 (passing tone)

    # Bar 4: Open voicing, G7 (G, B, D, F)
    pretty_midi.Note(velocity=85, pitch=67, start=2.75, end=3.0),  # B4
    pretty_midi.Note(velocity=85, pitch=69, start=2.75, end=3.0),  # Bb4 (chromatic)
    pretty_midi.Note(velocity=85, pitch=65, start=2.75, end=3.0),  # G4
    pretty_midi.Note(velocity=85, pitch=62, start=2.75, end=3.0),  # D4
    pretty_midi.Note(velocity=85, pitch=60, start=2.75, end=3.0),  # F4
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax continues the motif, but with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D4
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),  # G3
    pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.5),  # E3
    pretty_midi.Note(velocity=80, pitch=52, start=3.5, end=3.75),  # F3
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # D3
    pretty_midi.Note(velocity=80, pitch=49, start=4.0, end=4.25),  # C#3
    pretty_midi.Note(velocity=80, pitch=50, start=4.25, end=4.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano comp on 2 and 4
piano_notes = [
    # Bar 3: Open voicing, Bm7b5 (B, D, F#, A)
    pretty_midi.Note(velocity=85, pitch=66, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.25),  # Bb4 (chromatic)
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.25),  # D4 (passing tone)

    # Bar 4: Open voicing, G7 (G, B, D, F)
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.0),  # B4
    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.0),  # Bb4 (chromatic)
    pretty_midi.Note(velocity=85, pitch=65, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=85, pitch=62, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=85, pitch=60, start=3.75, end=4.0),  # F4
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue
drum_notes = [
    # Kick on 1 and 3
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
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax finishes the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # D3
    pretty_midi.Note(velocity=80, pitch=51, start=4.75, end=5.0),  # E3
    pretty_midi.Note(velocity=80, pitch=52, start=5.0, end=5.25),  # F3
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5),  # G3
    pretty_midi.Note(velocity=80, pitch=55, start=5.5, end=5.75),  # A3
    pretty_midi.Note(velocity=80, pitch=57, start=5.75, end=6.0),  # B3
]
bass.notes.extend(bass_notes)

# Piano comp on 2 and 4
piano_notes = [
    # Bar 4: Open voicing, D7sus4 (D, G, A, C#)
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=5.0),  # Bb4
    pretty_midi.Note(velocity=85, pitch=65, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=5.0),  # F4 (passing tone)
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
