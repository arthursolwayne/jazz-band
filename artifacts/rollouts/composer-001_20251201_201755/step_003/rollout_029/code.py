
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F2, Ab2, D2, G2, etc.)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),   # F2 (root)
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # Ab2 (b9)
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # Ab2 (b9)
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),   # D2 (5)
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),   # G2 (7)
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125),  # Ab2 (b9)
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),   # Ab2 (b9)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),   # D2 (5)
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25),  # G2 (7)
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),   # Ab2 (b9)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Eb

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # Ab

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),   # Eb
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),   # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53) - G (55) - Ab (50) - F (53)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625),   # F
    pretty_midi.Note(velocity=110, pitch=55, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=50, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=53, start=3.375, end=3.5),   # F
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar (Bars 2-4)
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
