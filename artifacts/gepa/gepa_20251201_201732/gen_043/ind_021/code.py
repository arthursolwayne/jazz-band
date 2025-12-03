
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
    # Kick on 1 and 3 (0.0, 0.75)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.875),
    # Snare on 2 and 4 (0.375, 1.125)
    pretty_midi.Note(velocity=110, pitch=38, start=0.375, end=0.5),
    pretty_midi.Note(velocity=110, pitch=38, start=1.125, end=1.25),
    # Hi-hat on every eighth (0.0, 0.375, 0.75, 1.125)
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Fm walking line (F2 - Ab2 - D2 - G2)
# Bar 2 (1.5 - 3.0s)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=2.0),  # Ab2
    pretty_midi.Note(velocity=100, pitch=48, start=2.0, end=2.25),  # D2
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.5),  # G2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=3.25, end=3.5),  # Ab2
    pretty_midi.Note(velocity=100, pitch=48, start=3.5, end=3.75),  # D2
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.0),  # G2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=4.75, end=5.0),  # Ab2
    pretty_midi.Note(velocity=100, pitch=48, start=5.0, end=5.25),  # D2
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.5),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, each bar a different chord
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.75),  # D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25),  # Ab
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.75),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, finish it
# Motif: F, G, Ab, D (Fm pentatonic)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.65),  # F
    pretty_midi.Note(velocity=110, pitch=55, start=1.65, end=1.8),  # G
    pretty_midi.Note(velocity=110, pitch=50, start=1.8, end=2.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=48, start=2.0, end=2.15),  # D
    # Repeat motif to finish
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.65),  # F
    pretty_midi.Note(velocity=110, pitch=55, start=4.65, end=4.8),  # G
    pretty_midi.Note(velocity=110, pitch=50, start=4.8, end=4.95),  # Ab
    pretty_midi.Note(velocity=110, pitch=48, start=4.95, end=5.1),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    kick_start = bar_start
    kick_end = kick_start + 0.125
    snare_start = bar_start + 0.375
    snare_end = snare_start + 0.125
    hihat_start = bar_start
    hihat_end = hihat_start + 0.125
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 0.875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.125, end=bar_start + 1.25))
    # Hi-hat on every eighth
    for i in range(8):
        hihat_start = bar_start + (i * 0.375)
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
