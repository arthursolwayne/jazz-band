
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625),  # D#
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),   # F#
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=5.625, end=6.0),   # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.625),  # C
    # Bar 3: D7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.125),  # C
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=5.25, end=5.625),  # C
]
piano.notes.extend(piano_notes)

# Sax: Melody in bars 2-4
# Short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start, end=bar_start + 0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.1875, end=bar_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.5625, end=bar_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.9375, end=bar_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.5),

drums.notes.extend(drums.notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
