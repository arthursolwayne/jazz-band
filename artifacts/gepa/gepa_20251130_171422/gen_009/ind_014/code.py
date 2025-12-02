
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
    # Hi-hat on every eighth
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
# Sax: Motif in F, ascending with chromatic tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0625), # F#
    pretty_midi.Note(velocity=100, pitch=68, start=2.0625, end=2.25), # G#
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.4375, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.8125), # F#
    pretty_midi.Note(velocity=100, pitch=68, start=2.8125, end=3.0),  # G#
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1875),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.5625), # F#
    pretty_midi.Note(velocity=100, pitch=68, start=3.5625, end=3.75),  # G#
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.9375, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.3125), # F#
    pretty_midi.Note(velocity=100, pitch=68, start=4.3125, end=4.5),   # G#
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.6875),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.0625), # F#
    pretty_midi.Note(velocity=100, pitch=68, start=5.0625, end=5.25),  # G#
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.4375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.4375, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=5.8125), # F#
    pretty_midi.Note(velocity=100, pitch=68, start=5.8125, end=6.0),   # G#
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.0625, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.4375),  # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=2.8125), # F
    pretty_midi.Note(velocity=80, pitch=44, start=2.8125, end=3.0),   # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.1875),   # G
    pretty_midi.Note(velocity=80, pitch=43, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.5625), # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=3.9375, end=4.125), # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.3125), # G
    pretty_midi.Note(velocity=80, pitch=43, start=4.3125, end=4.5),   # F
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.6875),   # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875), # E
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=80, pitch=44, start=5.0625, end=5.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.4375),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=5.4375, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=5.8125), # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),   # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping with tension
piano_notes = [
    # Bar 2 - 2nd beat: F7 chord
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0625),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0625),  # E
    # Bar 2 - 4th beat: F7 chord
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.8125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.8125),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.8125),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=2.8125),  # E
    # Bar 3 - 2nd beat: F7 chord
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.5625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5625),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.5625),  # E
    # Bar 3 - 4th beat: F7 chord
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.3125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.3125),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.3125),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.3125),  # E
    # Bar 4 - 2nd beat: F7 chord
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.0625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0625),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.0625),  # E
    # Bar 4 - 4th beat: F7 chord
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=5.8125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.8125),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=5.8125),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=5.8125),  # E
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hi-hat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(0, 8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + (i * 0.1875), end=start + (i * 0.1875) + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
