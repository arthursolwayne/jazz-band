
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in D, chromatic approaches
bass_notes = [
    # Bar 2: D (root), F# (b3), G (4), C# (b7)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # C#
    # Bar 3: C# (b7), B (7), D (root), F# (b3)
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75),  # C#
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # F#
    # Bar 4: G (4), C# (b7), B (7), D (root)
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),  # C#
    pretty_midi.Note(velocity=80, pitch=69, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # C#
    # Bar 3: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # F#
    # Bar 4: C#7 (C#, E#, G#, B)
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # C#
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # E#
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # G#
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.0),  # B
]
piano.notes.extend(piano_notes)

# Sax: motif (D, F#, C#, D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # C#
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # D
    # Echo with space
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # C#
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.25),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo.mid")
