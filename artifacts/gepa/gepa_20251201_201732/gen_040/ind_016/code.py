
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
    # Hihat on every eighth
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

# Bass: walking line in Fm, roots and fifths with chromatic approaches
# Fm = F, Ab, C (root, b3, 5)
bass_notes = [
    # Bar 2, measure 1: F (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.6875),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=48, start=1.6875, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.0),   # C (fifth)
    # Bar 2, measure 2: Ab (b3) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.1875),  # G (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=51, start=2.1875, end=2.375),  # Ab (b3)
    pretty_midi.Note(velocity=100, pitch=52, start=2.375, end=2.5),   # C (fifth)
    # Bar 2, measure 3: F (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=47, start=2.5, end=2.6875),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=48, start=2.6875, end=2.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=52, start=2.875, end=3.0),   # C (fifth)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.5 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.5 + 0.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.5 + 0.375),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.5 + 0.375),  # Eb
    # Bar 3: Bbm7 (Bb, Db, F, Ab)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.0 + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.0 + 0.375),  # Db
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.0 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.0 + 0.375),  # Ab
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.5 + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.5 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.375),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.5 + 0.375),  # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    for i in range(0, 8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875),
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, C, Bb (Fm with a chromatic passing tone)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.5 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=1.875 + 0.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.25 + 0.375),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=2.625 + 0.375),  # Bb (hanging)
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.5 + 0.375),  # F (return)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
