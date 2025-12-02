
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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
# Sax: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # E (C7)
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875),  # F# (C7)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0625),  # G (C7)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25),  # E (C7)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.4375),  # A (C7)
    pretty_midi.Note(velocity=100, pitch=69, start=2.4375, end=2.625),  # B (C7)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.8125),  # D (C7)
    pretty_midi.Note(velocity=100, pitch=69, start=2.8125, end=3.0),  # B (C7)
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=1.5, end=1.6875),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=1.6875, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=1.875, end=2.0625),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=2.0625, end=2.25),  # B
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.4375),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=2.4375, end=2.625),  # C#
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=2.8125),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=2.8125, end=3.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.6875),  # D7
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.6875),  # B7
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.6875),  # A7
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.6875),  # F#7
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.8125),  # D7
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.8125),  # B7
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.8125),  # A7
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=2.8125),  # F#7
]
piano.notes.extend(piano_notes)

# Bar 3: Continue the motif and full ensemble
# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),  # B (C7)
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375),  # A (C7)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625),  # G (C7)
    pretty_midi.Note(velocity=100, pitch=64, start=3.5625, end=3.75),  # F# (C7)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9375),  # E (C7)
    pretty_midi.Note(velocity=100, pitch=60, start=3.9375, end=4.125),  # D (C7)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.3125),  # E (C7)
    pretty_midi.Note(velocity=100, pitch=64, start=4.3125, end=4.5),  # F# (C7)
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.1875),  # B
    pretty_midi.Note(velocity=80, pitch=48, start=3.1875, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.5625),  # B
    pretty_midi.Note(velocity=80, pitch=52, start=3.5625, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=3.9375),  # C#
    pretty_midi.Note(velocity=80, pitch=51, start=3.9375, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.3125),  # B
    pretty_midi.Note(velocity=80, pitch=48, start=4.3125, end=4.5),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.1875),  # D7
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.1875),  # B7
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.1875),  # A7
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.1875),  # F#7
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.3125),  # D7
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.3125),  # B7
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.3125),  # A7
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.3125),  # F#7
]
piano.notes.extend(piano_notes)

# Bar 4: Continue the motif and full ensemble
# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.6875),  # D (C7)
    pretty_midi.Note(velocity=100, pitch=69, start=4.6875, end=4.875),  # B (C7)
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625),  # A (C7)
    pretty_midi.Note(velocity=100, pitch=64, start=5.0625, end=5.25),  # F# (C7)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.4375),  # E (C7)
    pretty_midi.Note(velocity=100, pitch=60, start=5.4375, end=5.625),  # D (C7)
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.8125),  # E (C7)
    pretty_midi.Note(velocity=100, pitch=64, start=5.8125, end=6.0),  # F# (C7)
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.6875),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=4.6875, end=4.875),  # C#
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.0625),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=5.0625, end=5.25),  # B
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.4375),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=5.4375, end=5.625),  # C#
    pretty_midi.Note(velocity=80, pitch=51, start=5.625, end=5.8125),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=5.8125, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.6875),  # D7
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.6875),  # B7
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.6875),  # A7
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.6875),  # F#7
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=5.8125),  # D7
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=5.8125),  # B7
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.8125),  # A7
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=5.8125),  # F#7
]
piano.notes.extend(piano_notes)

# Drums: Bar 3-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
