
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=3.0)
]
piano.notes.extend(piano_notes)

# Sax: motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),   # G
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Bass
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # G
]
bass.notes.extend(bass_notes)

# Bar 3: Piano
piano_notes = [
    # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),
    # G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=3.0)
]
piano.notes.extend(piano_notes)

# Bar 3: Sax
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),   # G
]
sax.notes.extend(sax_notes)

# Bar 4: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Bass
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # G#
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # B
]
bass.notes.extend(bass_notes)

# Bar 4: Piano
piano_notes = [
    # G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),
    # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.5)
]
piano.notes.extend(piano_notes)

# Bar 4: Sax
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),   # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
