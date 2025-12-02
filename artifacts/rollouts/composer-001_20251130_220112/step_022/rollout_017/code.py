
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
drums_notes = [
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
drums.notes.extend(drums_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: F7 - G7 - Bb7 - C7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=100, pitch=85, start=1.875, end=2.25),  # G7
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=2.625),  # Bb7
    pretty_midi.Note(velocity=100, pitch=87, start=2.625, end=3.0)   # C7
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F (F - G - A - Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=3.0)   # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (comp on 2 and 4)
# Bar 2 (1.5 - 3.0s)
# 2: F7 (F, A, C, Eb)
# 4: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.0),  # Eb

    pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=2.75)   # Ab
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: F7 - G7 - Bb7 - C7 (reprise)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=100, pitch=85, start=3.375, end=3.75),  # G7
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.125),  # Bb7
    pretty_midi.Note(velocity=100, pitch=87, start=4.125, end=4.5)   # C7
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F (F - G - A - Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=68, start=4.125, end=4.5)   # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 3 (3.0 - 4.5s)
# 2: F7 (F, A, C, Eb)
# 4: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.5),  # Eb

    pretty_midi.Note(velocity=80, pitch=68, start=4.125, end=4.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.25)   # Ab
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: F7 - G7 - Bb7 - C7 (reprise)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=100, pitch=85, start=4.875, end=5.25),  # G7
    pretty_midi.Note(velocity=100, pitch=81, start=5.25, end=5.625),  # Bb7
    pretty_midi.Note(velocity=100, pitch=87, start=5.625, end=6.0)   # C7
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F (F - G - A - Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=68, start=5.625, end=6.0)   # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 4 (4.5 - 6.0s)
# 2: F7 (F, A, C, Eb)
# 4: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0),  # Eb

    pretty_midi.Note(velocity=80, pitch=68, start=5.625, end=5.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=5.75)   # Ab
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [3.0, 4.5]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar + 0.0, end=bar + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar + 1.125, end=bar + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar + 0.75, end=bar + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar + 1.875, end=bar + 2.0)
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.0, end=bar + 0.1875)
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.1875, end=bar + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.375, end=bar + 0.5625)
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.5625, end=bar + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.75, end=bar + 0.9375)
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.9375, end=bar + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 1.125, end=bar + 1.3125)
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 1.3125, end=bar + 1.5)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),

    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
])

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dantes_introduction.mid')
