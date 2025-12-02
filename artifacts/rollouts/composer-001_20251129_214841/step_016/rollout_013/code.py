
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line (Walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.5),  # D#
    pretty_midi.Note(velocity=90, pitch=52, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=90, pitch=53, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=54, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=90, pitch=55, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.0),  # A#
    pretty_midi.Note(velocity=90, pitch=59, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.75),  # C#
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=5.0, end=5.25),  # D#
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=5.75, end=6.0),  # F#
]
bass.notes.extend(bass_notes)

# Diane - Piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2: C7 (C, E, B, D)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    # Bar 3: F7 (F, A, E, G)
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.5),
    # Bar 4: G7 (G, B, F#, A)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),
]
piano.notes.extend(piano_notes)

# Little Ray - Drums (Kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0),
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0),
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
])
drums.notes.extend(drum_notes)

# Dante - Tenor Sax (Melody)
# Short motif: C - E - B - D (C7 arpeggio, but not played as a scale)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # Return to C
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=70, pitch=60, start=5.5, end=5.75),
    pretty_midi.Note(velocity=70, pitch=64, start=5.75, end=6.0),
    pretty_midi.Note(velocity=70, pitch=67, start=6.0, end=6.25),
    pretty_midi.Note(velocity=70, pitch=62, start=6.25, end=6.5),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")
