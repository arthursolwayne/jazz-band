
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line, roots and fifths with chromatic approaches
# Bar 2: F - G♭ - G - A♭
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # G♭
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),  # A♭
    # Bar 3: A - B♭ - B - C
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # B♭
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),  # C
    # Bar 4: C - D♭ - D - E♭
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),  # D♭
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # E♭
]
bass.notes.extend(bass_notes)

# Piano: Diane, open voicings, resolve on last beat of each bar
# Bar 2: Fmaj7 (F A C E) - comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5),  # E
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.25),  # E
    # Bar 3: Am7 (A C E G) - comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.75),  # G
    # Bar 4: Dm7 (D F A C) - comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.25),  # C
]
piano.notes.extend(piano_notes)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G - A♭ - F (muted, then open, then leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.125),  # A♭
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.625),  # A♭
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.125),  # A♭
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.375),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
