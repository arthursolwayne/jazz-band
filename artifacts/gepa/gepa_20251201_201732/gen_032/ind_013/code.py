
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
# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.75),  # F (root)
    pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=2.0),  # E (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=2.0, end=2.25),  # Ab (fifth)
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.5),  # G (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.75),  # F (root)
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=3.0),  # E (chromatic approach)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.25),  # C (root of Bb7)
    pretty_midi.Note(velocity=90, pitch=47, start=3.25, end=3.5),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=3.5, end=3.75),  # D (fifth of Bb7)
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.0),  # C# (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=4.0, end=4.25),  # C (root of Bb7)
    pretty_midi.Note(velocity=90, pitch=47, start=4.25, end=4.5),  # Bb (chromatic approach)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.75),  # F (root)
    pretty_midi.Note(velocity=90, pitch=44, start=4.75, end=5.0),  # G (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=5.0, end=5.25),  # Ab (fifth)
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.5),  # A (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=5.5, end=5.75),  # Ab (fifth)
    pretty_midi.Note(velocity=90, pitch=46, start=5.75, end=6.0),  # A (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s): Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # C
    # Bar 3 (3.0 - 4.5s): Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # Ab
    # Bar 4 (4.5 - 6.0s): Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), Ab (67), C (69), Bb (62) — 1st bar
# Then pause, then resolve with F (65), Ab (67), C (69), and a trill on F (65) at the end
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # Bb
    # Pause
    pretty_midi.Note(velocity=0, pitch=60, start=2.0, end=3.0),  # Rest
    # Resume with F, Ab, C, and a trill on F
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.625),  # F trill
    pretty_midi.Note(velocity=110, pitch=65, start=3.625, end=3.75),  # F trill
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=3.875),  # F trill
    pretty_midi.Note(velocity=110, pitch=65, start=3.875, end=4.0),  # F trill
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4 (1.5 - 6.0s)
for bar in range(2, 5):
    start_time = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick_start = start_time + 0.0
    kick_end = kick_start + 0.375
    kick_2_start = start_time + 1.125
    kick_2_end = kick_2_start + 0.375
    # Snare on 2 and 4
    snare_start = start_time + 0.75
    snare_end = snare_start + 0.125
    snare_2_start = start_time + 1.875
    snare_2_end = snare_2_start + 0.125
    # Hihat on every eighth
    hihat_notes = [
        (start_time + 0.0, start_time + 0.1875),
        (start_time + 0.1875, start_time + 0.375),
        (start_time + 0.375, start_time + 0.5625),
        (start_time + 0.5625, start_time + 0.75),
        (start_time + 0.75, start_time + 0.9375),
        (start_time + 0.9375, start_time + 1.125),
        (start_time + 1.125, start_time + 1.3125),
        (start_time + 1.3125, start_time + 1.5),
    ]
    for h_start, h_end in hihat_notes:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=h_start, end=h_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_2_start, end=kick_2_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_2_start, end=snare_2_end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
