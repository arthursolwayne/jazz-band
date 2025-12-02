
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

# Bass: Walking line in Fm (F, Ab, D, C), with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # F#2 (chromatic approach)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75), # C2
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125), # Eb2
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),  # Db2 (chromatic approach)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25), # Eb2
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),  # F#2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last beat of each bar
piano_notes = [
    # Bar 2 (1.5 - 3.0s): Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),   # F2
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=3.0),   # Eb2
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),   # G2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),   # D2 (C in Fm7)

    # Bar 3 (3.0 - 4.5s): Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),   # Bb2
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),   # G2
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),   # F2
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=4.5),   # Eb2

    # Bar 4 (4.5 - 6.0s): Fm7 again, but with a diminished chord on the last beat
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),   # F2
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=6.0),   # Eb2
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),   # G2
    pretty_midi.Note(velocity=100, pitch=49, start=5.625, end=6.0), # Db2 (diminished approach)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # Ab3 (start of motif)
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # C4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # F3
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),  # C4 (hanging)

    # Bar 3 (3.0 - 4.5s) - leave empty

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # Ab3 (return)
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25), # C4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625), # F3
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # C4 (resolve)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    kick_start = start + 0.0
    kick_end = start + 0.375
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(kick)
    kick_start = start + 1.125
    kick_end = start + 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(kick)

# Snare on 2 and 4
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    snare_start = start + 0.75
    snare_end = start + 0.875
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare)
    snare_start = start + 1.875
    snare_end = start + 2.0
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare)

# Hihat on every eighth
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    for i in range(0, 8):
        hihat_start = start + i * 0.1875
        hihat_end = hihat_start + 0.1875
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
