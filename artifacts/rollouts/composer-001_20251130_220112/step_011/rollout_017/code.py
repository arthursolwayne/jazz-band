
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
# Sax melody: F7 - Ab7 - Bb7 - D7 (motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=84, start=1.5, end=1.75),  # F7
    pretty_midi.Note(velocity=110, pitch=81, start=1.75, end=2.0),  # Ab7
    pretty_midi.Note(velocity=110, pitch=82, start=2.0, end=2.25),  # Bb7
    pretty_midi.Note(velocity=110, pitch=86, start=2.25, end=2.5),  # D7
    pretty_midi.Note(velocity=110, pitch=84, start=2.5, end=2.75),  # F7 (return)
    pretty_midi.Note(velocity=110, pitch=81, start=2.75, end=3.0),  # Ab7 (return)
]
sax.notes.extend(sax_notes)

# Bass line: walking chromatic line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=2.75, end=3.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s): F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=85, pitch=76, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=85, pitch=74, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=85, pitch=71, start=1.75, end=2.0),  # Eb
    # Bar 3 (2.0 - 2.5s): Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=85, pitch=70, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=85, pitch=74, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=85, pitch=72, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.5),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif but with slight variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=84, start=3.0, end=3.25),  # F7
    pretty_midi.Note(velocity=110, pitch=81, start=3.25, end=3.5),  # Ab7
    pretty_midi.Note(velocity=110, pitch=82, start=3.5, end=3.75),  # Bb7
    pretty_midi.Note(velocity=110, pitch=86, start=3.75, end=4.0),  # D7
    pretty_midi.Note(velocity=110, pitch=84, start=4.0, end=4.25),  # F7 (return)
    pretty_midi.Note(velocity=110, pitch=81, start=4.25, end=4.5),  # Ab7 (return)
]
sax.notes.extend(sax_notes)

# Bass line: walking chromatic line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=4.25, end=4.5),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 (3.0 - 3.5s): Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=85, pitch=70, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=85, pitch=74, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=85, pitch=72, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=85, pitch=71, start=3.25, end=3.5),  # Ab
    # Bar 4 (3.5 - 4.0s): F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=85, pitch=76, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=85, pitch=74, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=85, pitch=71, start=3.75, end=4.0),  # Eb
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolve motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=84, start=4.5, end=4.75),  # F7
    pretty_midi.Note(velocity=110, pitch=81, start=4.75, end=5.0),  # Ab7
    pretty_midi.Note(velocity=110, pitch=82, start=5.0, end=5.25),  # Bb7
    pretty_midi.Note(velocity=110, pitch=86, start=5.25, end=5.5),  # D7
    pretty_midi.Note(velocity=110, pitch=84, start=5.5, end=5.75),  # F7 (return)
    pretty_midi.Note(velocity=110, pitch=81, start=5.75, end=6.0),  # Ab7 (return)
]
sax.notes.extend(sax_notes)

# Bass line: walking chromatic line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=5.75, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 (4.5 - 5.0s): F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=85, pitch=76, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=85, pitch=74, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=85, pitch=71, start=4.75, end=5.0),  # Eb
    # Bar 4 (5.0 - 5.5s): Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=85, pitch=70, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=85, pitch=74, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=85, pitch=72, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=85, pitch=71, start=5.25, end=5.5),  # Ab
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
