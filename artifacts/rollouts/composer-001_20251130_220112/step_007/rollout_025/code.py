
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
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

# Bar 2: Start of the melody (1.5 - 3.0s)
# Sax: Fm7 -> Ab7 -> Bb7 -> Cm7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.6875, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.0625, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.4375, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.8125), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.8125, end=3.0),  # A
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.0625, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.4375),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.4375, end=2.625), # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=2.8125), # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=2.8125, end=3.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - 2nd beat: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0625),

    # Bar 2 - 4th beat: Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.8125),
]
piano.notes.extend(piano_notes)

# Bar 3: Continue melody (3.0 - 4.5s)
# Sax: Fm7 -> Ab7 -> Bb7 -> Cm7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.5625, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.9375, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.3125), # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.3125, end=4.5),  # A
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=80, pitch=48, start=3.5625, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=3.9375),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=3.9375, end=4.125), # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.3125), # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=4.3125, end=4.5),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 - 2nd beat: Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5625),

    # Bar 3 - 4th beat: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.3125),
]
piano.notes.extend(piano_notes)

# Bar 4: Continue melody (4.5 - 6.0s)
# Sax: Fm7 -> Ab7 -> Bb7 -> Cm7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.6875, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.0625, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.4375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.4375, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.8125), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.8125, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=80, pitch=48, start=5.0625, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.4375),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=5.4375, end=5.625), # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=5.8125), # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=5.8125, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 - 2nd beat: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0625),

    # Bar 4 - 4th beat: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=5.8125),
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hats on every eighth
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
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
