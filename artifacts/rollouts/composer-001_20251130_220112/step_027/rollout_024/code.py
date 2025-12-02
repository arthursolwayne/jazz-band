
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line - walking, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),  # E
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=78, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.875),  # E
    # Bar 3: leave empty
    # Bar 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=75, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=73, start=3.0, end=3.375),  # Ab
]
piano.notes.extend(piano_notes)

# Sax - your motif, short and singable
# First note: F (71)
# Second note: Bb (70)
# Third note: D (75)
# Leave it hanging on D (75), then come back with F (71) in bar 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=75, start=3.0, end=3.375),  # D (return)
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # F (resolve)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line - walking, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # G#
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 3: leave empty
    # Bar 4: Bb7 (Bb, D, F, Ab)
    # Already added in bar 2
]
piano.notes.extend(piano_notes)

# Drums - Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line - walking, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),  # G#
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 4: F7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=78, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.875),  # E
]
piano.notes.extend(piano_notes)

# Drums - Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
