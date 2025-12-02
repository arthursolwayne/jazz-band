
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
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    # Walking line in Dm
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),  # C
]

bass.notes.extend(bass_notes)

# Piano: Diane
piano_notes = [
    # Comp on 2 and 4 with 7th chords
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=60, start=1.5, end=1.875),

    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=85, pitch=67, start=2.625, end=2.875),
    pretty_midi.Note(velocity=85, pitch=69, start=2.625, end=2.875),
    pretty_midi.Note(velocity=85, pitch=71, start=2.625, end=2.875),
    pretty_midi.Note(velocity=85, pitch=64, start=2.625, end=2.875),

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=85, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=85, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.0),
]

piano.notes.extend(piano_notes)

# Sax: Dante
sax_notes = [
    # Motif: D (62), F (64), Eb (63), D (62)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=63, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),

    # Repeat motif with slight variation
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),

    # Final phrase with resolution
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=63, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
