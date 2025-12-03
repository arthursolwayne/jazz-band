
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # F (root) with chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),
    # C (fifth) with chromatic approach from C#
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),
    # Ab (b9) with chromatic approach from G
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625),
    # F (root) with chromatic approach from F#
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),
    # Bar 4: Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Motif starts
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # G (Fm7 9)
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0),  # E (Fm7 7)
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),  # A (Bb7 9)
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=3.0),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=5.75, end=6.0),  # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
