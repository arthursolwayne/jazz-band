
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=3.0),  # F#4
]
sax.notes.extend(sax_notes)

# Bass line (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=2.0),  # Eb3
    pretty_midi.Note(velocity=90, pitch=47, start=2.0, end=2.25),  # E3
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.5),  # G3
    pretty_midi.Note(velocity=90, pitch=50, start=2.5, end=2.75),  # Ab3
    pretty_midi.Note(velocity=90, pitch=51, start=2.75, end=3.0),  # A3
]
bass.notes.extend(bass_notes)

# Piano comp on 2 and 4 (7th chords)
piano_notes = [
    # Bar 2 - 2nd beat (D7)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # C#5
    # Bar 2 - 4th beat (F#7)
    pretty_midi.Note(velocity=90, pitch=66, start=2.75, end=3.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # C#5
    pretty_midi.Note(velocity=90, pitch=73, start=2.75, end=3.0),  # E5
    pretty_midi.Note(velocity=90, pitch=76, start=2.75, end=3.0),  # G#5
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # F4
]
sax.notes.extend(sax_notes)

# Bass line (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.25),  # A3
    pretty_midi.Note(velocity=90, pitch=52, start=3.25, end=3.5),  # Bb3
    pretty_midi.Note(velocity=90, pitch=53, start=3.5, end=3.75),  # B3
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=90, pitch=56, start=4.0, end=4.25),  # Eb4
    pretty_midi.Note(velocity=90, pitch=57, start=4.25, end=4.5),  # E4
]
bass.notes.extend(bass_notes)

# Piano comp on 2 and 4 (7th chords)
piano_notes = [
    # Bar 3 - 2nd beat (G7)
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),  # C5
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),  # D5
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5),  # F#5
    # Bar 3 - 4th beat (B7)
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),  # B4
    pretty_midi.Note(velocity=90, pitch=76, start=4.25, end=4.5),  # F#5
    pretty_midi.Note(velocity=90, pitch=78, start=4.25, end=4.5),  # A5
    pretty_midi.Note(velocity=90, pitch=81, start=4.25, end=4.5),  # C#6
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),  # F#4
]
sax.notes.extend(sax_notes)

# Bass line (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.75),  # E4
    pretty_midi.Note(velocity=90, pitch=58, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=90, pitch=59, start=5.0, end=5.25),  # F#4
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.5),  # A4
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # A#4
    pretty_midi.Note(velocity=90, pitch=63, start=5.75, end=6.0),  # B4
]
bass.notes.extend(bass_notes)

# Piano comp on 2 and 4 (7th chords)
piano_notes = [
    # Bar 4 - 2nd beat (D7)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # C#5
    # Bar 4 - 4th beat (F#7)
    pretty_midi.Note(velocity=90, pitch=66, start=5.75, end=6.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),  # C#5
    pretty_midi.Note(velocity=90, pitch=73, start=5.75, end=6.0),  # E5
    pretty_midi.Note(velocity=90, pitch=76, start=5.75, end=6.0),  # G#5
]
piano.notes.extend(piano_notes)

# Drums in bar 3 and 4 (same pattern as bar 1)
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend(drum_notes.copy())

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
