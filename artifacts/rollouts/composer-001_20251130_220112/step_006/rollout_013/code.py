
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

# Bass: walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Db
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=47, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.0),   # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4, Fm7, Bb7, E7, Am7
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=2.8125),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=2.8125),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=2.8125),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=2.8125),  # Ab
    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=3.9375),  # E
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=3.9375),  # G#
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=3.9375),  # B
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=3.9375),  # D
    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.0625),  # A
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.0625),  # C
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.0625),  # E
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.0625),  # G
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53), Ab (50), C (55), F (53)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=1.875, end=2.0625), # C
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=110, pitch=57, start=2.4375, end=2.625), # A (hanging)
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.1875),   # F (return)
    pretty_midi.Note(velocity=110, pitch=55, start=3.1875, end=3.375), # C
    pretty_midi.Note(velocity=110, pitch=53, start=3.375, end=3.5625), # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5s - 3.0s)
for i in range(4):
    kick_start = 1.5 + i * 0.75
    kick_end = kick_start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    if i == 1 or i == 3:
        snare_start = 1.5 + i * 0.75
        snare_end = snare_start + 0.125
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    for j in range(4):
        hihat_start = 1.5 + i * 0.75 + j * 0.1875
        hihat_end = hihat_start + 0.1875
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end))

# Bar 3 (3.0s - 4.5s)
for i in range(4):
    kick_start = 3.0 + i * 0.75
    kick_end = kick_start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    if i == 1 or i == 3:
        snare_start = 3.0 + i * 0.75
        snare_end = snare_start + 0.125
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    for j in range(4):
        hihat_start = 3.0 + i * 0.75 + j * 0.1875
        hihat_end = hihat_start + 0.1875
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end))

# Bar 4 (4.5s - 6.0s)
for i in range(4):
    kick_start = 4.5 + i * 0.75
    kick_end = kick_start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    if i == 1 or i == 3:
        snare_start = 4.5 + i * 0.75
        snare_end = snare_start + 0.125
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    for j in range(4):
        hihat_start = 4.5 + i * 0.75 + j * 0.1875
        hihat_end = hihat_start + 0.1875
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
