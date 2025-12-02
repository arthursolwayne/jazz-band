
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0),  # Eb (chromatic)
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),  # F (chromatic)
    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.0),  # Bb
    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=4.75, end=5.0),  # C#
    pretty_midi.Note(velocity=90, pitch=74, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=75, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=76, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=90, pitch=77, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=79, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=84, start=1.75, end=2.0),  # B
    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=78, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=100, pitch=81, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=86, start=3.25, end=3.5),  # C#
    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=79, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=84, start=4.75, end=5.0),  # B
]
piano.notes.extend(piano_notes)

# Saxophone (Dante)
sax_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=2.0),  # C
    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=110, pitch=74, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75),  # C
    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=5.0),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.5),  # E
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=1.9375),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.4375),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.6875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.1875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.4375),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.9375),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.1875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.6875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=4.9375),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.4375),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.6875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
