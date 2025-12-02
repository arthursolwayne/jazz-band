
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

# Marcus: Walking bass line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # F7 - F
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875), # F7 - Bb
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875), # F7 - E
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.875), # F7 - A
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375), # F7 - F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375), # F7 - Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375), # F7 - E
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375), # F7 - A
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875), # F7 - F
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875), # F7 - Bb
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875), # F7 - E
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.875), # F7 - A
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),

# Dante: Your motif - one short phrase, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.6875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),    # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.1875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.1875, end=2.375), # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5625), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.5625, end=2.75), # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.9375), # D
    pretty_midi.Note(velocity=100, pitch=66, start=2.9375, end=3.125), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.3125), # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.3125, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.6875),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.6875, end=3.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.875, end=4.0),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.1875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.1875, end=4.375), # E
    pretty_midi.Note(velocity=100, pitch=66, start=4.375, end=4.5625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5625, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.9375),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.9375, end=5.125), # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.125, end=5.3125), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.3125, end=5.5),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.6875, end=5.875), # E
    pretty_midi.Note(velocity=100, pitch=66, start=5.875, end=6.0),    # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
