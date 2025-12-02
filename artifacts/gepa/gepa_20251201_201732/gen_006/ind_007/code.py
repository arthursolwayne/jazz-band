
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

# Marcus: Walking bass line in Fm (F - Ab - Bb - Db)
# Root and fifth with chromatic approaches
# Bar 2: F - Eb - F - Gb (approaching F)
# Bar 3: Ab - G - Ab - A
# Bar 4: Bb - A - Bb - B
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.0),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.375),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),  # Gb2
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=45, start=2.5, end=2.875),  # Ab2
    pretty_midi.Note(velocity=80, pitch=44, start=2.875, end=3.0),  # G2
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.5),  # A2
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.875),  # Bb2
    pretty_midi.Note(velocity=80, pitch=46, start=3.875, end=4.0),  # A2
    pretty_midi.Note(velocity=80, pitch=47, start=4.0, end=4.375),  # Bb2
    pretty_midi.Note(velocity=80, pitch=48, start=4.375, end=4.5),  # B2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last.
# Bar 2: Fm7 (F, Ab, Bb, Db)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Ab7 (Ab, C, Db, F)
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.1875),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.5 + 0.1875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.1875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.5 + 0.1875),  # Db4
    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.5 + 0.1875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.5 + 0.1875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.5 + 0.1875),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=2.5, end=2.5 + 0.1875),  # Ab4
    # Bar 4: Ab7
    pretty_midi.Note(velocity=100, pitch=61, start=3.5, end=3.5 + 0.1875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.5 + 0.1875),  # C4
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.5 + 0.1875),  # Db4
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.5 + 0.1875),  # F4
]
piano.notes.extend(piano_notes)

# Dante: Sax solo, short motif, one phrase, leave it hanging, come back.

# Bar 2: Start motif on F (65), D (62), Bb (62), F (65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.5 + 0.1875),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=1.6875, end=1.6875 + 0.1875),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=1.875 + 0.1875),  # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=2.0625, end=2.0625 + 0.1875),  # F4
    # Bar 3: Repeat the motif, but leave it hanging
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.5 + 0.1875),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.6875, end=2.6875 + 0.1875),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=2.875 + 0.1875),  # Bb4
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.5 + 0.1875),  # F4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
# Snare on 2 and 4
# Hihat on every eighth
for bar in [2, 3, 4]:
    bar_start = 1.5 + (bar - 2) * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    hihat = [
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.0, end=bar_start + 0.1875),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.1875, end=bar_start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.5625, end=bar_start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.9375, end=bar_start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.5)
    ]
    drums.notes.extend([kick1, kick2, snare1, snare2] + hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('wayne_moment.mid')
