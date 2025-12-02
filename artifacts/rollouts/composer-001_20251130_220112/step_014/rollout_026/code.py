
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=58, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=57, start=2.625, end=3.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 1 (Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # C
    # Bar 2, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # E
    # Bar 2, beat 3 (Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # C
    # Bar 2, beat 4 (G7)
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),  # F
]
piano.notes.extend(piano_notes)

# Sax: Motif - Dm7 (D, F, A, C) with a chromatic approach
sax_notes = [
    # Bar 2, beat 1 (D)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    # Bar 2, beat 1 (chromatic approach - C#)
    pretty_midi.Note(velocity=100, pitch=61, start=1.625, end=1.75),
    # Bar 2, beat 2 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),
    # Bar 2, beat 2 (A)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),
    # Bar 2, beat 3 (C)
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.125),
    # Bar 2, beat 3 (A)
    pretty_midi.Note(velocity=100, pitch=69, start=2.125, end=2.25),
    # Bar 2, beat 4 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375),
    # Bar 2, beat 4 (D)
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),
    # Bar 3, beat 1 (D)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),
    # Bar 3, beat 1 (chromatic approach - C#)
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=2.75),
    # Bar 3, beat 2 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=2.875),
    # Bar 3, beat 2 (A)
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=4.125, end=4.5),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 1 (Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # C
    # Bar 3, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # E
    # Bar 3, beat 3 (Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # C
    # Bar 3, beat 4 (G7)
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),  # F
]
piano.notes.extend(piano_notes)

# Sax: Motif variation - Dm7 (D, F, A, C) with a chromatic approach
sax_notes = [
    # Bar 3, beat 1 (D)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),
    # Bar 3, beat 1 (chromatic approach - C#)
    pretty_midi.Note(velocity=100, pitch=61, start=3.125, end=3.25),
    # Bar 3, beat 2 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375),
    # Bar 3, beat 2 (A)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),
    # Bar 3, beat 3 (C)
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.625),
    # Bar 3, beat 3 (A)
    pretty_midi.Note(velocity=100, pitch=69, start=3.625, end=3.75),
    # Bar 3, beat 4 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875),
    # Bar 3, beat 4 (D)
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),
    # Bar 4, beat 1 (D)
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125),
    # Bar 4, beat 1 (chromatic approach - C#)
    pretty_midi.Note(velocity=100, pitch=61, start=4.125, end=4.25),
    # Bar 4, beat 2 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.375),
    # Bar 4, beat 2 (A)
    pretty_midi.Note(velocity=100, pitch=69, start=4.375, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 1 (Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # C
    # Bar 4, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # E
    # Bar 4, beat 3 (Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # C
    # Bar 4, beat 4 (G7)
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),  # F
]
piano.notes.extend(piano_notes)

# Sax: Motif variation - Dm7 (D, F, A, C) with a chromatic approach
sax_notes = [
    # Bar 4, beat 1 (D)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),
    # Bar 4, beat 1 (chromatic approach - C#)
    pretty_midi.Note(velocity=100, pitch=61, start=4.625, end=4.75),
    # Bar 4, beat 2 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=4.875),
    # Bar 4, beat 2 (A)
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),
    # Bar 4, beat 3 (C)
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.125),
    # Bar 4, beat 3 (A)
    pretty_midi.Note(velocity=100, pitch=69, start=5.125, end=5.25),
    # Bar 4, beat 4 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.375),
    # Bar 4, beat 4 (D)
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5),
    # Bar 4, beat 4 (chromatic approach - C#)
    pretty_midi.Note(velocity=100, pitch=61, start=5.5, end=5.625),
    # Bar 4, beat 4 (D)
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.75),
    # Bar 4, beat 4 (chromatic approach - C#)
    pretty_midi.Note(velocity=100, pitch=61, start=5.75, end=5.875),
    # Bar 4, beat 4 (D)
    pretty_midi.Note(velocity=100, pitch=62, start=5.875, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
