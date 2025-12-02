
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),# Hihat on 2
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Tenor motif - start with a question, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F# (F#4)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # F# (F#4)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # D (D3)
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),  # Eb (Eb3)
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # E (E3)
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.5),  # G (G3)
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),  # G# (G#3)
    pretty_midi.Note(velocity=80, pitch=52, start=2.75, end=3.0),  # Bb (Bb3)
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, measure 2: D7 (D F# A C)
    pretty_midi.Note(velocity=85, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=85, pitch=65, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=85, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=1.75, end=2.0),  # C
    # Bar 2, measure 4: D7 (D F# A C)
    pretty_midi.Note(velocity=85, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=85, pitch=65, start=2.75, end=3.0),  # F#
    pretty_midi.Note(velocity=85, pitch=69, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=2.75, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F# (F#4)
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F# (F#4)
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D (D4)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.25),  # Bb (Bb3)
    pretty_midi.Note(velocity=80, pitch=53, start=3.25, end=3.5),  # B (B3)
    pretty_midi.Note(velocity=80, pitch=55, start=3.5, end=3.75),  # D (D4)
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.0),  # E (E4)
    pretty_midi.Note(velocity=80, pitch=58, start=4.0, end=4.25),  # F (F4)
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5),  # G (G4)
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 3, measure 2: D7 (D F# A C)
    pretty_midi.Note(velocity=85, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=85, pitch=65, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=85, pitch=69, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=3.25, end=3.5),  # C
    # Bar 3, measure 4: D7 (D F# A C)
    pretty_midi.Note(velocity=85, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=85, pitch=65, start=4.25, end=4.5),  # F#
    pretty_midi.Note(velocity=85, pitch=69, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=4.25, end=4.5),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End with a question, not a statement
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F# (F#4)
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # F# (F#4)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),  # G (G4)
    pretty_midi.Note(velocity=80, pitch=61, start=4.75, end=5.0),  # G# (G#4)
    pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.25),  # A (A4)
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5),  # B (B4)
    pretty_midi.Note(velocity=80, pitch=65, start=5.5, end=5.75),  # B# (C5)
    pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=6.0),  # D (D5)
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 4, measure 2: D7 (D F# A C)
    pretty_midi.Note(velocity=85, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=85, pitch=65, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=85, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=4.75, end=5.0),  # C
    # Bar 4, measure 4: D7 (D F# A C)
    pretty_midi.Note(velocity=85, pitch=62, start=5.75, end=6.0),  # D
    pretty_midi.Note(velocity=85, pitch=65, start=5.75, end=6.0),  # F#
    pretty_midi.Note(velocity=85, pitch=69, start=5.75, end=6.0),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=5.75, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875), # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),# Hihat on 2
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),# Hihat on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875), # Hihat on 4

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875), # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),# Hihat on 2
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),# Hihat on 3
    pretty_midi.Note(velocity=90, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.1875), # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
