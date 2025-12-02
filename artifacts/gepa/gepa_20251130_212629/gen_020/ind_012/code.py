
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody starts with a short motif, ends on a suspended note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D (1st beat)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.125),  # F# (2nd beat)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A (3rd beat)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F# (4th beat, held)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.625),  # D (1st beat)
    pretty_midi.Note(velocity=80, pitch=49, start=1.625, end=1.75),  # C# (chromatic)
    pretty_midi.Note(velocity=80, pitch=52, start=1.875, end=2.0),  # E
    pretty_midi.Note(velocity=80, pitch=53, start=2.0, end=2.125),  # F (chromatic)
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=80, pitch=54, start=2.375, end=2.5),  # F# (chromatic)
    pretty_midi.Note(velocity=80, pitch=57, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=56, start=2.75, end=2.875),  # G# (chromatic)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, sparse and driving
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.875, end=2.125),  # D7 (2nd beat)
    pretty_midi.Note(velocity=85, pitch=67, start=1.875, end=2.125),
    pretty_midi.Note(velocity=85, pitch=71, start=1.875, end=2.125),
    pretty_midi.Note(velocity=85, pitch=74, start=1.875, end=2.125),
    pretty_midi.Note(velocity=85, pitch=62, start=2.625, end=2.875),  # D7 (4th beat)
    pretty_midi.Note(velocity=85, pitch=67, start=2.625, end=2.875),
    pretty_midi.Note(velocity=85, pitch=71, start=2.625, end=2.875),
    pretty_midi.Note(velocity=85, pitch=74, start=2.625, end=2.875),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Rest, then one note with a slight delay
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F# with slight delay
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.125),  # A (1st beat)
    pretty_midi.Note(velocity=80, pitch=56, start=3.125, end=3.25),  # G# (chromatic)
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.5),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.625),  # C (chromatic)
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=3.875, end=4.0),  # C# (chromatic)
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=4.25, end=4.375),  # E# (chromatic)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, sparse and driving
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=3.375, end=3.625),  # D7 (2nd beat)
    pretty_midi.Note(velocity=85, pitch=67, start=3.375, end=3.625),
    pretty_midi.Note(velocity=85, pitch=71, start=3.375, end=3.625),
    pretty_midi.Note(velocity=85, pitch=74, start=3.375, end=3.625),
    pretty_midi.Note(velocity=85, pitch=62, start=4.125, end=4.375),  # D7 (4th beat)
    pretty_midi.Note(velocity=85, pitch=67, start=4.125, end=4.375),
    pretty_midi.Note(velocity=85, pitch=71, start=4.125, end=4.375),
    pretty_midi.Note(velocity=85, pitch=74, start=4.125, end=4.375),
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Ends with a question — a note that wants to resolve but doesn't
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # A (1st beat)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.125),  # F# (2nd beat)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D (3rd beat)
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F# (4th beat, unresolved)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.625),  # D (1st beat)
    pretty_midi.Note(velocity=80, pitch=61, start=4.625, end=4.75),  # C# (chromatic)
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=5.0, end=5.125),  # E# (chromatic)
    pretty_midi.Note(velocity=80, pitch=66, start=5.25, end=5.375),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=5.375, end=5.5),  # F# (chromatic)
    pretty_midi.Note(velocity=80, pitch=68, start=5.625, end=5.75),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=5.875),  # G# (chromatic)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, sparse and driving
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=4.875, end=5.125),  # D7 (2nd beat)
    pretty_midi.Note(velocity=85, pitch=67, start=4.875, end=5.125),
    pretty_midi.Note(velocity=85, pitch=71, start=4.875, end=5.125),
    pretty_midi.Note(velocity=85, pitch=74, start=4.875, end=5.125),
    pretty_midi.Note(velocity=85, pitch=62, start=5.625, end=5.875),  # D7 (4th beat)
    pretty_midi.Note(velocity=85, pitch=67, start=5.625, end=5.875),
    pretty_midi.Note(velocity=85, pitch=71, start=5.625, end=5.875),
    pretty_midi.Note(velocity=85, pitch=74, start=5.625, end=5.875),
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
