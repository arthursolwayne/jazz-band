
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in F minor, roots and fifths with chromatic approaches
# Bar 2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # C3 (F5)
    pretty_midi.Note(velocity=80, pitch=39, start=2.25, end=2.625),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # Ab2 (chromatic approach)
]
# Bar 3
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75),  # D3 (F7)
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Eb3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),  # C3 (chromatic approach)
])
# Bar 4
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # G3 (F7)
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625),  # Ab3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # Eb3 (chromatic approach)
])
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: F minor 7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Eb4
]
# Bar 3: Bb7 (Bb D F Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Ab4
])
# Bar 4: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=75, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # F5
])
piano.notes.extend(piano_notes)

# Sax: one short motif, haunting, incomplete
# Bar 2: F, Eb, D, rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # D4
]
# Bar 3: rest, rest, rest, rest
# Bar 4: F, Bb, C, rest
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # C5
])
sax.notes.extend(sax_notes)

# Drums in bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
for i in range(4):
    kick_start = 1.5 + i * 0.75
    kick_end = kick_start + 0.375
    if i in [0, 2]:
        pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    snare_start = 1.5 + 0.75 * (i + 1)
    snare_end = snare_start + 0.125
    if i in [1, 3]:
        pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)
    for j in range(8):
        hihat_start = 1.5 + 0.1875 * j
        hihat_end = hihat_start + 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end)

# Bar 3
for i in range(4):
    kick_start = 3.0 + i * 0.75
    kick_end = kick_start + 0.375
    if i in [0, 2]:
        pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    snare_start = 3.0 + 0.75 * (i + 1)
    snare_end = snare_start + 0.125
    if i in [1, 3]:
        pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)
    for j in range(8):
        hihat_start = 3.0 + 0.1875 * j
        hihat_end = hihat_start + 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end)

# Bar 4
for i in range(4):
    kick_start = 4.5 + i * 0.75
    kick_end = kick_start + 0.375
    if i in [0, 2]:
        pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    snare_start = 4.5 + 0.75 * (i + 1)
    snare_end = snare_start + 0.125
    if i in [1, 3]:
        pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)
    for j in range(8):
        hihat_start = 4.5 + 0.1875 * j
        hihat_end = hihat_start + 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end)

drums.notes.extend([pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end) for kick_start, kick_end in [(1.5, 1.875), (2.625, 2.999), (3.0, 3.375), (4.125, 4.5), (4.5, 4.875), (5.625, 6.0)]])
drums.notes.extend([pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end) for snare_start, snare_end in [(2.25, 2.375), (3.75, 3.875), (4.875, 5.0), (5.25, 5.375)]])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
