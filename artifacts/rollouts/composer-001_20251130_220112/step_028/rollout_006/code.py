
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on 2 (1.875)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # D
    # Dm7 on 4 (2.625)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # D
]
piano.notes.extend(piano_notes)

# Sax: Short motif (start at 1.5)
# Dm scale: D, Eb, F, G, A, Bb, C, D
# Motif: D, Eb, F, G (up a 3rd, then a tritone)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),   # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),   # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on 2 (3.375)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # D
    # Dm7 on 4 (4.125)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # D
]
piano.notes.extend(piano_notes)

# Sax: Return of the motif (start at 3.0)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.5),   # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),   # B
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=74, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on 2 (4.875)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # D
    # Dm7 on 4 (5.625)
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # D
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif (start at 4.5)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.625, end=4.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0),   # G
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 (3.0 - 4.5s)
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
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
