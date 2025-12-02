
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

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.1875),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=2.1875, end=2.375), # F
    pretty_midi.Note(velocity=90, pitch=65, start=2.375, end=2.5625), # Gb
    pretty_midi.Note(velocity=90, pitch=62, start=2.5625, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=2.9375),  # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=65, start=2.9375, end=3.125), # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=3.125, end=3.3125), # A
    pretty_midi.Note(velocity=90, pitch=65, start=3.3125, end=3.5),   # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.6875),   # A
    pretty_midi.Note(velocity=90, pitch=64, start=3.6875, end=3.875), # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.0),    # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.1875),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.1875, end=4.375), # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.375, end=4.5625), # F
    pretty_midi.Note(velocity=90, pitch=63, start=4.5625, end=4.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=4.9375),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.9375, end=5.125), # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.125, end=5.3125), # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.3125, end=5.5),   # F
    pretty_midi.Note(velocity=90, pitch=65, start=5.5, end=5.6875),   # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=5.6875, end=5.875), # A
    pretty_midi.Note(velocity=90, pitch=65, start=5.875, end=6.0),    # Gb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 chord
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.6875),  # C#
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.6875),  # F
    # Bar 3: Gb7 chord
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.4375), # Gb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.4375), # D
    pretty_midi.Note(velocity=85, pitch=73, start=2.25, end=2.4375), # F
    pretty_midi.Note(velocity=85, pitch=68, start=2.25, end=2.4375), # Bb
    # Bar 4: A7 chord
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.9375), # A
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=3.9375), # E
    pretty_midi.Note(velocity=85, pitch=76, start=3.75, end=3.9375), # G
    pretty_midi.Note(velocity=85, pitch=71, start=3.75, end=3.9375), # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: motif starts
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=110, pitch=71, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0),   # A
    # Bar 3: leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.4375), # Bb
    # Bar 4: come back and finish it
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=3.9375), # A
    pretty_midi.Note(velocity=110, pitch=66, start=3.9375, end=4.125), # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.3125), # D
    pretty_midi.Note(velocity=110, pitch=69, start=4.3125, end=4.5),   # A
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.6875),   # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=110, pitch=66, start=5.0625, end=5.25),   # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.4375), # D
    pretty_midi.Note(velocity=110, pitch=69, start=5.4375, end=5.625), # A
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.4375), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.9375), # Snare on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.1875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.9375),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.25, end=4.4375),  # Snare on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.6875),   # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.4375),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=5.75, end=5.9375),  # Snare on 4
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.9375, end=5.125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.3125, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.6875, end=5.875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
