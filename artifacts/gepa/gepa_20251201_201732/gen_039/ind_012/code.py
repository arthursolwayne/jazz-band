
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
bar_length = 1.5
for bar in range(1):
    start = bar * bar_length
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) -> Eb2 (39) -> G2 (43) -> A2 (45)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),
    # Bar 3: G2 (43) -> Ab2 (44) -> Bb2 (42) -> C3 (48)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5),
    # Bar 4: C3 (48) -> Db3 (49) -> E3 (50) -> F3 (53)
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # C5
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # F5
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # Bb4
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 4):
    start = bar * bar_length
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # A4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A4
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # A4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
