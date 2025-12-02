
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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
# Bass line: walking with chromatic approaches
# Dm7 -> G7 -> Cmaj7 -> F7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.625, end=1.75),  # C#
    pretty_midi.Note(velocity=90, pitch=66, start=1.75, end=1.875),  # D#
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=2.125, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.375, end=2.5),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.625),   # E
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.875, end=3.0),   # Bb
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),  # D7
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.5),   # G7
    pretty_midi.Note(velocity=90, pitch=73, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=78, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.25),   # Cmaj7
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=82, start=3.0, end=3.25),
]
piano.notes.extend(piano_notes)

# Sax: your motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: walking with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.25, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5),   # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.625),   # E
    pretty_midi.Note(velocity=90, pitch=68, start=3.625, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=3.875, end=4.0),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.125),   # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.25, end=4.375),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.375, end=4.5),   # D
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # D7
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0),   # G7
    pretty_midi.Note(velocity=90, pitch=73, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=78, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=81, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.75),   # Cmaj7
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=82, start=4.5, end=4.75),
]
piano.notes.extend(piano_notes)

# Sax: continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: walking with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=90, pitch=75, start=4.625, end=4.75),  # C#
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=4.875),  # D#
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.0),   # E
    pretty_midi.Note(velocity=90, pitch=78, start=5.0, end=5.125),  # G
    pretty_midi.Note(velocity=90, pitch=77, start=5.125, end=5.25),  # F#
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.375),  # E
    pretty_midi.Note(velocity=90, pitch=74, start=5.375, end=5.5),   # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.5, end=5.625),   # E
    pretty_midi.Note(velocity=90, pitch=78, start=5.625, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=5.75, end=5.875),  # A
    pretty_midi.Note(velocity=90, pitch=81, start=5.875, end=6.0),   # Bb
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),  # D7
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.5),   # G7
    pretty_midi.Note(velocity=90, pitch=73, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=78, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=81, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=76, start=5.75, end=6.0),   # Cmaj7
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=78, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=82, start=5.75, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # G
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
