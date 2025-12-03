
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

# Drums: Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Marcus (Walking line, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75),    # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=2.0),    # F#2
    pretty_midi.Note(velocity=80, pitch=40, start=2.0, end=2.25),    # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.5),    # A2
    pretty_midi.Note(velocity=80, pitch=38, start=2.5, end=2.75),    # D2
    pretty_midi.Note(velocity=80, pitch=41, start=2.75, end=3.0),    # F#2
]
bass.notes.extend(bass_notes)

# Piano: Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),    # D4
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),    # F4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),    # A4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),    # C4
]
piano.notes.extend(piano_notes)

# Sax: Dante (Motif, haunting, incomplete)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),   # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),   # F4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 4
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Marcus (Walking line, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.25),    # B2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.25, end=3.5),    # C#3
    pretty_midi.Note(velocity=80, pitch=38, start=3.5, end=3.75),    # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.0),    # F2
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.25),    # G2
    pretty_midi.Note(velocity=80, pitch=43, start=4.25, end=4.5),    # A2
]
bass.notes.extend(bass_notes)

# Piano: Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 3: Bm7 (B, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),    # B4
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.25),    # D5
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.25),    # F#5
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.25),    # A5
]
piano.notes.extend(piano_notes)

# Sax: Dante (Motif variation, haunting, incomplete)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # A5
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.0),   # G5
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),   # B4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 3
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Marcus (Walking line, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.75),    # C#3
    pretty_midi.Note(velocity=80, pitch=38, start=4.75, end=5.0),    # D2
    pretty_midi.Note(velocity=80, pitch=40, start=5.0, end=5.25),    # F2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.5),    # G2
    pretty_midi.Note(velocity=80, pitch=38, start=5.5, end=5.75),    # D2
    pretty_midi.Note(velocity=80, pitch=40, start=5.75, end=6.0),    # F2
]
bass.notes.extend(bass_notes)

# Piano: Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 4: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),    # D4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),    # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),    # A4
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),    # C#5
]
piano.notes.extend(piano_notes)

# Sax: Dante (Motif resolution, haunting, incomplete)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),   # G4
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),   # D4
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 4
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
