
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25), # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Motif (start on first beat of bar 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings - Bb7 (Bb D F A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=4.5),  # F5
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # A5
]
piano.notes.extend(piano_notes)

# Sax: Motif variation - repeat and resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),   # G4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25), # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings - G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # F5
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution - finish the first motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),   # G4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
