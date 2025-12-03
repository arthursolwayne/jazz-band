
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Fm: F, Ab, Bb, D, Eb, G
# Bar 2: F -> Ab -> Bb -> Eb
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),   # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # G2 (chromatic approach to Ab)
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.625),  # Ab2
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0),   # Eb2 (chromatic approach to D)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),   # D2
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75),  # Eb2
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125),  # F2 (chromatic approach to Ab)
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5),   # Ab2
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.875),   # Ab2
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # Bb2 (chromatic approach to Bb)
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.625),  # Bb2
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),   # F2 (resolution)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, Bb, D)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    # Bar 2: Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # G2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=49, start=1.5, end=1.875),  # Ab2
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),  # D2
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),  # Ab2
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # Bb2
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.875),  # D2
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - Eb - F
# First bar: F (start), Bb (end of bar 2), Eb (end of bar 3), F (end of bar 4)
sax_notes = [
    # Bar 2: F (start) to Bb (end of bar)
    pretty_midi.Note(velocity=110, pitch=48, start=1.5, end=1.75),  # F2
    pretty_midi.Note(velocity=110, pitch=49, start=2.25, end=2.5),  # Bb2
    # Bar 3: Eb (end of bar)
    pretty_midi.Note(velocity=110, pitch=45, start=3.75, end=4.0),  # Eb2
    # Bar 4: F (end of bar)
    pretty_midi.Note(velocity=110, pitch=48, start=5.625, end=6.0),  # F2
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    for i in range(8):
        start_eighth = start + i * 0.375
        pretty_midi.Note(velocity=80, pitch=42, start=start_eighth, end=start_eighth + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
