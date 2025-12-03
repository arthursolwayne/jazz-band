
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
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=60, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=60, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm
# Fm: F, Ab, D, C
# Roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (1.5-1.875), chromatic approach from E
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),
    pretty_midi.Note(velocity=60, pitch=69, start=1.125, end=1.5),  # E (approach)
    # Ab (1.875-2.25), chromatic approach from G#
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=60, pitch=68, start=1.5, end=1.875),  # G#
    # Bar 3: D (2.25-2.625), chromatic approach from C#
    pretty_midi.Note(velocity=80, pitch=61, start=2.25, end=2.625),
    pretty_midi.Note(velocity=60, pitch=60, start=1.875, end=2.25),  # C#
    # C (2.625-3.0), chromatic approach from B
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=60, pitch=59, start=2.25, end=2.625),  # B
    # Bar 4: F (3.0-3.375), chromatic approach from E
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=60, pitch=69, start=2.625, end=3.0),  # E
    # Ab (3.375-3.75), chromatic approach from G#
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=60, pitch=68, start=3.0, end=3.375),  # G#
    # Bar 5: D (3.75-4.125), chromatic approach from C#
    pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=4.125),
    pretty_midi.Note(velocity=60, pitch=60, start=3.375, end=3.75),  # C#
    # C (4.125-4.5), chromatic approach from B
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=60, pitch=59, start=3.75, end=4.125),  # B
    # Bar 6: F (4.5-4.875), chromatic approach from E
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.875),
    pretty_midi.Note(velocity=60, pitch=69, start=4.125, end=4.5),  # E
    # Ab (4.875-5.25), chromatic approach from G#
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=60, pitch=68, start=4.5, end=4.875),  # G#
    # Bar 7: D (5.25-5.625), chromatic approach from C#
    pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.625),
    pretty_midi.Note(velocity=60, pitch=60, start=4.875, end=5.25),  # C#
    # C (5.625-6.0), chromatic approach from B
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=60, pitch=59, start=5.25, end=5.625),  # B
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bars 2-4: Fm7, Bbm7, Eb7, Am7
# Voicings: 7th with 9th, 11th, etc.
piano_notes = []
# Bar 2: Fm7 (F, Ab, C, Eb, G)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=63, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G (9th)
])
# Bar 3: Bbm7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # A (11th)
])
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.375),  # E (13th)
])
# Bar 5: Am7 (A, C, E, G)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # B (11th)
])
# Bar 6: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # D (13th)
])
# Bar 7: Fm7 (F, Ab, C, Eb, G)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # G (9th)
])
# Bar 8: Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=61, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0),  # E (11th)
])
piano.notes.extend(piano_notes)

# Dante: Motif. Start it, leave it hanging. Come back and finish it.
# Fm: F, Ab, D, C
# F - Ab - D - C
# Start on F, leave it hanging on Ab, then resolve with D and C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5),
    pretty_midi.Note(velocity=100, pitch=61, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=61, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=61, start=4.0, end=4.125),
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.25),
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=67, start=5.375, end=5.5),
    pretty_midi.Note(velocity=100, pitch=61, start=5.5, end=5.625),
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=70, start=5.75, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
# Snare on 2 and 4
# Hi-hat on every eighth
for bar in range(2, 5):
    time = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=time + 1.125, end=time + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=time + 0.75, end=time + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=time + 1.875, end=time + 2.0)
    # Hi-hat
    for i in range(8):
        pretty_midi.Note(velocity=60, pitch=42, start=time + i*0.1875, end=time + i*0.1875 + 0.1875)
drums.notes.extend([n for n in drums.notes if n.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
