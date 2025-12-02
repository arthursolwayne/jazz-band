
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    
    # Snare on 2 and 4
    pretty_midi.Note(velocity=85, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=85, pitch=38, start=1.875, end=2.0),
    
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=70, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=70, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=70, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=70, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=70, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=70, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=70, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=70, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass (Marcus): Walking line in Fm, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=49, start=2.0, end=2.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=51, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.375),  # A
    pretty_midi.Note(velocity=80, pitch=48, start=2.375, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=2.875, end=3.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.0),
    pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),
    
    # Bar 2, beat 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.75),
    pretty_midi.Note(velocity=95, pitch=68, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75),
    
    # Bar 3, beat 2: F7 again
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.5),
    pretty_midi.Note(velocity=95, pitch=72, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5),
    
    # Bar 3, beat 4: Bb7 again
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.25),
    pretty_midi.Note(velocity=95, pitch=68, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.25)
]
piano.notes.extend(piano_notes)

# Saxophone (Dante): Motif on 1.5s (Bar 2) — start with a question
sax_notes = [
    # Bar 2: F (tenor sax is transposed, so F is played as C)
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.625),
    # Bar 2: Ab (tenor sax is transposed, so Ab is played as D)
    pretty_midi.Note(velocity=100, pitch=62, start=1.625, end=1.75),
    # Bar 3: Eb (tenor sax is transposed, so Eb is played as A)
    pretty_midi.Note(velocity=105, pitch=69, start=2.25, end=2.375),
    # Bar 3: F again
    pretty_midi.Note(velocity=110, pitch=60, start=2.375, end=2.5)
]
sax.notes.extend(sax_notes)

# Bar 3: Drums again (3.0 - 4.5s)
# Same pattern but slightly varied velocities and timing
drum_notes = [
    pretty_midi.Note(velocity=92, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=87, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=70, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=70, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=70, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=70, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=70, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=70, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=70, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=70, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=70, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=70, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=70, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=70, pitch=42, start=4.375, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass (Marcus): Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=80, pitch=48, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=47, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=5.125, end=5.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.375),  # A
    pretty_midi.Note(velocity=80, pitch=51, start=5.375, end=5.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=5.5, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=5.75),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=5.75, end=5.875),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=5.875, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: F7
    pretty_midi.Note(velocity=100, pitch=71, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=74, start=5.375, end=5.5),
    pretty_midi.Note(velocity=95, pitch=72, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=69, start=5.375, end=5.5),
    
    # Bar 4, beat 4: Bb7
    pretty_midi.Note(velocity=100, pitch=71, start=6.125, end=6.25),
    pretty_midi.Note(velocity=95, pitch=68, start=6.125, end=6.25),
    pretty_midi.Note(velocity=90, pitch=71, start=6.125, end=6.25),
    pretty_midi.Note(velocity=90, pitch=69, start=6.125, end=6.25),
]
piano.notes.extend(piano_notes)

# Saxophone (Dante): End on a question, leaving it open
sax_notes = [
    # Bar 4: Play Ab again (tenor sax is transposed, so Ab is D)
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),
    # Bar 4: End with F (tenor sax is transposed, so F is C)
    pretty_midi.Note(velocity=110, pitch=60, start=5.125, end=5.25)
]
sax.notes.extend(sax_notes)

# Drums (Bar 4, 4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=95, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=88, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=70, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=70, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=70, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=70, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=70, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=70, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=70, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=70, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=70, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=70, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=70, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=70, pitch=42, start=5.875, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
