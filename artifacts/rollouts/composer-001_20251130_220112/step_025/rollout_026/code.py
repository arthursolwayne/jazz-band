
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Dm7
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F7
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # Cm7
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # Dm7
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # F7
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # Cm7
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=2.75, end=3.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),  # C
    # Bar 3: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),  # Eb
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.25),  # Bb
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # Dm7
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # F7
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # Cm7
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # Dm7
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # F7
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # Cm7
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=4.25, end=4.5),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),  # Eb
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=58, start=3.75, end=4.0),  # Bb
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # Dm7
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F7
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # Cm7
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # Dm7
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # F7
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # Cm7
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=5.75, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=4.75),  # Bb
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
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
