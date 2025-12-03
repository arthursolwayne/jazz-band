
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm
# Fm chord: F, Ab, C, D
# Roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root), Gb (chromatic approach to F)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.125),  # Gb2
    # Bar 3: Ab (fifth of Fm), A (chromatic approach to Ab)
    pretty_midi.Note(velocity=100, pitch=58, start=2.125, end=2.5),  # Ab2
    pretty_midi.Note(velocity=100, pitch=59, start=2.5, end=2.875),  # A2
    # Bar 4: C (root of Ab), B (chromatic approach to C)
    pretty_midi.Note(velocity=100, pitch=60, start=2.875, end=3.25),  # C2
    pretty_midi.Note(velocity=100, pitch=61, start=3.25, end=3.625),  # B2
    # Bar 5: D (fifth of Cm), D# (chromatic approach to D)
    pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=4.0),  # D2
    pretty_midi.Note(velocity=100, pitch=63, start=4.0, end=4.375),  # D#2
    # Bar 6: F (root of Dm), E (chromatic approach to F)
    pretty_midi.Note(velocity=100, pitch=53, start=4.375, end=4.75),  # F2
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.125),  # E2
    # Bar 7: Ab (fifth of Fm), G (chromatic approach to Ab)
    pretty_midi.Note(velocity=100, pitch=58, start=5.125, end=5.5),  # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=5.5, end=5.875),  # G2
    # Bar 8: C (root of Ab), B (chromatic approach to C)
    pretty_midi.Note(velocity=100, pitch=60, start=5.875, end=6.25),  # C2
    pretty_midi.Note(velocity=100, pitch=61, start=6.25, end=6.625),  # B2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),  # F2
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=2.0),  # Ab2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0),  # C2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # Eb2
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=57, start=2.0, end=2.5),  # Bb2
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=2.0, end=2.5),  # F2
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.5),  # Ab2
]
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),  # C2
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # Eb2
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0),  # G2
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=3.0),  # Bb2
]
# Bar 5: D7 (D, F#, A, C)
piano_notes_bar5 = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # D2
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # F#2
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),  # A2
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),  # C2
]
# Bar 6: Eb7 (Eb, G, Bb, D)
piano_notes_bar6 = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=4.0),  # Eb2
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # G2
    pretty_midi.Note(velocity=100, pitch=57, start=3.5, end=4.0),  # Bb2
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=4.0),  # D2
]
# Bar 7: Fm7 (F, Ab, C, Eb)
piano_notes_bar7 = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.0, end=4.5),  # F2
    pretty_midi.Note(velocity=100, pitch=58, start=4.0, end=4.5),  # Ab2
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.5),  # C2
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.5),  # Eb2
]
# Bar 8: G7 (G, B, D, F)
piano_notes_bar8 = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0),  # G2
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # B2
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=5.0),  # F2
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4 + piano_notes_bar5 + piano_notes_bar6 + piano_notes_bar7 + piano_notes_bar8)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, C, F (Fm scale), but played with space and tension
sax_notes = [
    # Bar 2: F, Ab, C
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F2
    pretty_midi.Note(velocity=100, pitch=58, start=1.75, end=2.0),  # Ab2
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # C2
    # Bar 3: leave it hanging, rest
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5),  # F2
    # Bar 4: come back, finish the motif
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # F2
    pretty_midi.Note(velocity=100, pitch=58, start=3.25, end=3.5),  # Ab2
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # C2
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.0),  # F2
    # Bar 5: end with a question
    pretty_midi.Note(velocity=100, pitch=53, start=4.0, end=4.25),  # F2
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 2.0s)
for i in range(1, 5):
    kick_time = 1.5 + (i - 1) * 0.375
    if i % 2 == 1:
        pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    snare_time = 1.5 + (i - 1) * 0.375 + 0.375
    if i % 2 == 0:
        pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1875)
    for j in range(0, 4):
        hihat_time = 1.5 + (i - 1) * 0.375 + j * 0.1875
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.1875)

# Bar 3 (2.0 - 2.5s)
for i in range(1, 5):
    kick_time = 2.0 + (i - 1) * 0.375
    if i % 2 == 1:
        pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    snare_time = 2.0 + (i - 1) * 0.375 + 0.375
    if i % 2 == 0:
        pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1875)
    for j in range(0, 4):
        hihat_time = 2.0 + (i - 1) * 0.375 + j * 0.1875
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.1875)

# Bar 4 (2.5 - 3.0s)
for i in range(1, 5):
    kick_time = 2.5 + (i - 1) * 0.375
    if i % 2 == 1:
        pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    snare_time = 2.5 + (i - 1) * 0.375 + 0.375
    if i % 2 == 0:
        pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1875)
    for j in range(0, 4):
        hihat_time = 2.5 + (i - 1) * 0.375 + j * 0.1875
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.1875)

# Bar 5 (3.0 - 3.5s)
for i in range(1, 5):
    kick_time = 3.0 + (i - 1) * 0.375
    if i % 2 == 1:
        pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    snare_time = 3.0 + (i - 1) * 0.375 + 0.375
    if i % 2 == 0:
        pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1875)
    for j in range(0, 4):
        hihat_time = 3.0 + (i - 1) * 0.375 + j * 0.1875
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.1875)

# Bar 6 (3.5 - 4.0s)
for i in range(1, 5):
    kick_time = 3.5 + (i - 1) * 0.375
    if i % 2 == 1:
        pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    snare_time = 3.5 + (i - 1) * 0.375 + 0.375
    if i % 2 == 0:
        pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1875)
    for j in range(0, 4):
        hihat_time = 3.5 + (i - 1) * 0.375 + j * 0.1875
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.1875)

# Bar 7 (4.0 - 4.5s)
for i in range(1, 5):
    kick_time = 4.0 + (i - 1) * 0.375
    if i % 2 == 1:
        pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    snare_time = 4.0 + (i - 1) * 0.375 + 0.375
    if i % 2 == 0:
        pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1875)
    for j in range(0, 4):
        hihat_time = 4.0 + (i - 1) * 0.375 + j * 0.1875
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.1875)

# Bar 8 (4.5 - 5.0s)
for i in range(1, 5):
    kick_time = 4.5 + (i - 1) * 0.375
    if i % 2 == 1:
        pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    snare_time = 4.5 + (i - 1) * 0.375 + 0.375
    if i % 2 == 0:
        pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1875)
    for j in range(0, 4):
        hihat_time = 4.5 + (i - 1) * 0.375 + j * 0.1875
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.1875)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
