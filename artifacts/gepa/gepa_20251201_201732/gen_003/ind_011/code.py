
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

# Bass: Walking line in Fm with chromatic approaches (D2-G2, MIDI 38-43)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # Ab (chromatic)
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # D (octave)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # Ab (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125),  # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),  # D (octave)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # Ab (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),  # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # D (octave)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (Fm7) - 1.5 - 3.0s
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0),  # D
    # Bar 3 (Bbmaj7) - 3.0 - 4.5s
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),  # A
    # Bar 4 (F7) - 4.5 - 6.0s
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Motif: F (60) -> Ab (63) -> Bb (62) -> F (60)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # F (return)
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick_start = start
    kick_end = kick_start + 0.375
    kick_3_start = start + 1.125
    kick_3_end = kick_3_start + 0.375
    drums.notes.extend([
        pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end),
        pretty_midi.Note(velocity=100, pitch=36, start=kick_3_start, end=kick_3_end)
    ])

# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    snare_2_start = start + 0.75
    snare_2_end = snare_2_start + 0.125
    snare_4_start = start + 1.875
    snare_4_end = snare_4_start + 0.125
    drums.notes.extend([
        pretty_midi.Note(velocity=100, pitch=38, start=snare_2_start, end=snare_2_end),
        pretty_midi.Note(velocity=100, pitch=38, start=snare_4_start, end=snare_4_end)
    ])

# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        hihat_start = start + (i * 0.1875)
        hihat_end = hihat_start + 0.1875
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
