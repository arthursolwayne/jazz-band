
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bar 2: Start of the melody (1.5 - 3.0s)
# Sax melody: D - Eb - F - G (Motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # G
]
sax.notes.extend(sax_notes)

# Marcus (Bass) - Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.625),  # D (root)
    pretty_midi.Note(velocity=90, pitch=45, start=1.625, end=1.75),  # Eb (b9)
    pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=1.875),  # F (3)
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.0),  # G (5)
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.125),  # A (7)
    pretty_midi.Note(velocity=90, pitch=48, start=2.125, end=2.25),  # G (5)
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.375),  # F (3)
    pretty_midi.Note(velocity=90, pitch=45, start=2.375, end=2.5),  # Eb (b9)
]
bass.notes.extend(bass_notes)

# Diane (Piano) - Comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),  # D7 (G)
    pretty_midi.Note(velocity=90, pitch=70, start=1.75, end=1.875),  # D7 (B)
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=1.875),  # D7 (A)
    # Bar 2, beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125),  # D7 (G)
    pretty_midi.Note(velocity=90, pitch=70, start=2.0, end=2.125),  # D7 (B)
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125),  # D7 (A)
    # Bar 3, beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=2.875),  # D7 (G)
    pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=2.875),  # D7 (B)
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=2.875),  # D7 (A)
    # Bar 3, beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125),  # D7 (G)
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.125),  # D7 (B)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.125),  # D7 (A)
]
piano.notes.extend(piano_notes)

# Bar 3: Continue the melody (3.0 - 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),  # G
]
sax.notes.extend(sax_notes)

# Marcus (Bass) - Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.125),  # A (7)
    pretty_midi.Note(velocity=90, pitch=48, start=3.125, end=3.25),  # G (5)
    pretty_midi.Note(velocity=90, pitch=46, start=3.25, end=3.375),  # F (3)
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.5),  # Eb (b9)
    pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=3.625),  # D (root)
    pretty_midi.Note(velocity=90, pitch=45, start=3.625, end=3.75),  # Eb (b9)
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=3.875),  # F (3)
    pretty_midi.Note(velocity=90, pitch=48, start=3.875, end=4.0),  # G (5)
]
bass.notes.extend(bass_notes)

# Diane (Piano) - Comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375),  # D7 (G)
    pretty_midi.Note(velocity=90, pitch=70, start=3.25, end=3.375),  # D7 (B)
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.375),  # D7 (A)
    # Bar 3, beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.625),  # D7 (G)
    pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=3.625),  # D7 (B)
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.625),  # D7 (A)
    # Bar 4, beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.375),  # D7 (G)
    pretty_midi.Note(velocity=90, pitch=70, start=4.25, end=4.375),  # D7 (B)
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.375),  # D7 (A)
    # Bar 4, beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.625),  # D7 (G)
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.625),  # D7 (B)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.625),  # D7 (A)
]
piano.notes.extend(piano_notes)

# Bar 4: End of the melody (4.5 - 6.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.625, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),  # G
]
sax.notes.extend(sax_notes)

# Marcus (Bass) - Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.625),  # G (5)
    pretty_midi.Note(velocity=90, pitch=46, start=4.625, end=4.75),  # F (3)
    pretty_midi.Note(velocity=90, pitch=45, start=4.75, end=4.875),  # Eb (b9)
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.0),  # D (root)
]
bass.notes.extend(bass_notes)

# Diane (Piano) - Comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=4.875),  # D7 (G)
    pretty_midi.Note(velocity=90, pitch=70, start=4.75, end=4.875),  # D7 (B)
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=4.875),  # D7 (A)
    # Bar 4, beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.125),  # D7 (G)
    pretty_midi.Note(velocity=90, pitch=70, start=5.0, end=5.125),  # D7 (B)
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.125),  # D7 (A)
]
piano.notes.extend(piano_notes)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
