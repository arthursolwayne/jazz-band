
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass: Walking line in Fm (F2, Bb2, Eb2, Ab2, etc.) with chromatic approaches
bass_notes = [
    # Bar 2: F2 -> Gb2 -> Bb2 -> Ab2
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=78, start=1.875, end=2.125),  # Gb2
    pretty_midi.Note(velocity=100, pitch=75, start=2.125, end=2.5),   # Bb2
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.875),   # Ab2

    # Bar 3: Eb2 -> D2 -> F2 -> Gb2
    pretty_midi.Note(velocity=100, pitch=72, start=2.875, end=3.25),  # Eb2
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.625),  # D2
    pretty_midi.Note(velocity=100, pitch=77, start=3.625, end=4.0),   # F2
    pretty_midi.Note(velocity=100, pitch=78, start=4.0, end=4.375),   # Gb2

    # Bar 4: Bb2 -> A2 -> C2 -> Db2
    pretty_midi.Note(velocity=100, pitch=75, start=4.375, end=4.75),  # Bb2
    pretty_midi.Note(velocity=100, pitch=73, start=4.75, end=5.125),  # A2
    pretty_midi.Note(velocity=100, pitch=69, start=5.125, end=5.5),   # C2
    pretty_midi.Note(velocity=100, pitch=70, start=5.5, end=5.875)    # Db2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C
]
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=75, start=2.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=2.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=3.0),  # Ab
])
# Bar 4: Am7 (A, C, E, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=73, start=3.5, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0),  # G
])
# Resolve on last chord
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=75, start=4.5, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.0),  # Ab
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Gb, Bb, Ab, F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=78, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=110, pitch=75, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=3.0, end=3.125)   # F (return)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 4):
    start = bar * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hi-hat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
