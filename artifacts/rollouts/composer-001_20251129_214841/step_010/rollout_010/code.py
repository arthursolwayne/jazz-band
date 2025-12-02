
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # C
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=90, pitch=53, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=2.75, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: C7 (C, E, B, D)
    pretty_midi.Note(velocity=95, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=85, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),

    # Bar 2, beat 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=95, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=85, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: motif variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # C
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=58, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: D7 (D, F#, C, E)
    pretty_midi.Note(velocity=95, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=85, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),

    # Bar 3, beat 4: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=95, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=74, start=4.25, end=4.5),
    pretty_midi.Note(velocity=85, pitch=72, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: motif resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=95, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=85, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),

    # Bar 4, beat 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=95, pitch=62, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),
    pretty_midi.Note(velocity=85, pitch=64, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
