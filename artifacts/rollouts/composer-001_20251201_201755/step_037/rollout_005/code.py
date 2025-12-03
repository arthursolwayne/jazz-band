
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.125),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.5),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=2.5, end=2.875),  # F#2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.625),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=3.625, end=4.0),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=4.0, end=4.375),  # F#2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.125),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=5.125, end=5.5),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=5.5, end=5.875),  # F#2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0),  # E
    # Bar 3 (3.0 - 4.5s) - Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=4.5),  # F
    # Bar 4 (4.5 - 6.0s) - C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # E
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s) - Motif start
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.125),  # G
    pretty_midi.Note(velocity=110, pitch=76, start=2.125, end=2.5),  # A
    # Bar 3 (3.0 - 4.5s) - Motif continuation
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.625),  # F#
    pretty_midi.Note(velocity=110, pitch=71, start=3.625, end=4.0),  # F
    # Bar 4 (4.5 - 6.0s) - Motif resolution
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.125),  # G
    pretty_midi.Note(velocity=110, pitch=76, start=5.125, end=5.5),  # A
    pretty_midi.Note(velocity=110, pitch=77, start=5.5, end=5.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=79, start=5.875, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
