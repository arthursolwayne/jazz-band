
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.125, end=4.5),   # Eb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, comp on 2 and 4, Dm7, Gm7, Cm7, F7
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),  # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # Bb
]
piano.notes.extend(piano_notes)

# Sax - 4-bar motif starting on bar 2, short, singable, melodic
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # Dm7 - G
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
