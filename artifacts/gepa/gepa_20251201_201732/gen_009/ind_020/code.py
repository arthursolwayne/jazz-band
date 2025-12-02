
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Fm7 -> Bbm7 -> Eb7 -> Am7
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Fm7: F, C, Ab, D
        root = 53  # F
        fifth = 58  # C
        chromatic = 51  # Eb
        # Walking line: F -> Eb -> F -> G
        notes = [pretty_midi.Note(velocity=100, pitch=53, start=start, end=start + 0.375),
                 pretty_midi.Note(velocity=100, pitch=51, start=start + 0.375, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=53, start=start + 0.75, end=start + 1.125),
                 pretty_midi.Note(velocity=100, pitch=55, start=start + 1.125, end=start + 1.5)]
    elif bar == 3:
        # Bbm7: Bb, F, Db, G
        root = 50  # Bb
        fifth = 55  # F
        chromatic = 48  # Ab
        # Walking line: Bb -> Ab -> Bb -> C
        notes = [pretty_midi.Note(velocity=100, pitch=50, start=start, end=start + 0.375),
                 pretty_midi.Note(velocity=100, pitch=48, start=start + 0.375, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=50, start=start + 0.75, end=start + 1.125),
                 pretty_midi.Note(velocity=100, pitch=52, start=start + 1.125, end=start + 1.5)]
    elif bar == 4:
        # Eb7: Eb, Bb, G, D
        root = 51  # Eb
        fifth = 56  # Bb
        chromatic = 49  # Db
        # Walking line: Eb -> Db -> Eb -> F
        notes = [pretty_midi.Note(velocity=100, pitch=51, start=start, end=start + 0.375),
                 pretty_midi.Note(velocity=100, pitch=49, start=start + 0.375, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=51, start=start + 0.75, end=start + 1.125),
                 pretty_midi.Note(velocity=100, pitch=53, start=start + 1.125, end=start + 1.5)]
    bass.notes.extend(notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Bbm7 (Bb, Db, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, D)
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        chord = [pretty_midi.Note(velocity=100, pitch=53, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=51, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=58, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=55, start=start, end=start + 0.75)]
    elif bar == 3:
        chord = [pretty_midi.Note(velocity=100, pitch=50, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=48, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=55, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=51, start=start, end=start + 0.75)]
    elif bar == 4:
        chord = [pretty_midi.Note(velocity=100, pitch=51, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=56, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=58, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=55, start=start, end=start + 0.75)]
    piano.notes.extend(chord)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm7 -> Bbm7 -> Eb7 -> Am7 (Ab7 in Fm key)
# Motif: F (53) -> Eb (51) -> F (53) -> G (55) -> Ab (52) -> G (55) -> Ab (52) -> Bb (50)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5)
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
