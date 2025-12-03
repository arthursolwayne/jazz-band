
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start_time = bar * 1.5
    kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.0, end=start_time + 0.375),
                  pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)]
    snare_notes = [pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 1.125),
                   pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.5, end=start_time + 1.875)]
    hihat_notes = []
    for i in range(0, 8):
        hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.125))
    drums.notes.extend(kick_notes)
    drums.notes.extend(snare_notes)
    drums.notes.extend(hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Fm7 -> Bb7 -> Eb7 -> Am7
# Roots: F, Bb, Eb, A (MIDI 53, 58, 61, 65)
# Walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=55, start=2.625, end=3.0),  # G

    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=56, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=58, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),  # B

    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=80, pitch=63, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=3.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=3.0),  # Ab
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=4.5),  # Ab
])

# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),  # D
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm7 -> Eb7 -> Am7 -> Dm7
# Motif: F, Ab, G, Eb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: continue for bars 2-4
for bar in range(2, 4):
    start_time = bar * 1.5
    kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.0, end=start_time + 0.375),
                  pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)]
    snare_notes = [pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 1.125),
                   pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.5, end=start_time + 1.875)]
    hihat_notes = []
    for i in range(0, 8):
        hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.125))
    drums.notes.extend(kick_notes)
    drums.notes.extend(snare_notes)
    drums.notes.extend(hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
