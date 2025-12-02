
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=54, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 (C, E, B, D)
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    # Bar 3: F7 (F, A, C, E)
    pretty_midi.Note(velocity=95, pitch=53, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=58, start=2.25, end=2.625),
    pretty_midi.Note(velocity=85, pitch=57, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625),
    # Bar 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=95, pitch=52, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=56, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=53, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),
]
piano.notes.extend(piano_notes)

# Sax: Dante, melody. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: G (start 1.5) -> rest
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.6875),
    # Bar 3: Bb (start 2.25) -> rest
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375),
    # Bar 4: A (start 3.0) -> rest
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.1875),
    # Bar 4: F (start 4.5) -> rest
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.6875),
    # Bar 4: G (start 5.25) -> rest
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.4375),
    # Bar 4: A (start 5.625) -> resolves
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_sax_intro.mid")
