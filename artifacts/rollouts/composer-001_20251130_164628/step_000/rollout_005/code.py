
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # G
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=85, pitch=71, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25),  # C#
    # Bar 3: G7 on beat 4
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=85, pitch=76, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=80, pitch=77, start=2.625, end=3.0),   # F
]

piano.notes.extend(piano_notes)

# Sax: Motif - short, singable, leaves it hanging
sax_notes = [
    # Bar 2: D (62)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # Bar 3: F# (66)
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625),
    # Bar 4: B (69)
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),
    # Bar 4: D (62), resolves the motif
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass continues the walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # C
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: B7 on beat 2
    pretty_midi.Note(velocity=95, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=85, pitch=78, start=3.375, end=3.75),  # G#
    pretty_midi.Note(velocity=80, pitch=79, start=3.375, end=3.75),  # A
    # Bar 4: F#7 on beat 4
    pretty_midi.Note(velocity=95, pitch=66, start=4.125, end=4.5),   # F#
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # B
    pretty_midi.Note(velocity=85, pitch=75, start=4.125, end=4.5),   # D#
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),   # E
]

piano.notes.extend(piano_notes)

# Sax continues motif, ends on D (62)
sax_notes = [
    # Bar 3: F# (66)
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),
    # Bar 4: B (69)
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),
    # Bar 4: D (62), resolves the motif
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),
]

sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass continues the walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),   # E
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: C7 on beat 2
    pretty_midi.Note(velocity=95, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),  # D
]

piano.notes.extend(piano_notes)

# Sax: Motif resolution
sax_notes = [
    # Bar 4: C (60)
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),
    # Bar 4: D (62), resolves the motif
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
