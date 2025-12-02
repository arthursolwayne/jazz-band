
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

# Bass: Walking line starting on F2 (MIDI 53), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=54, start=1.875, end=2.125),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=58, start=2.125, end=2.5),  # C3 (F2 + 5th)
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=2.875),  # B2 (chromatic approach)
    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.625),  # C#3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=63, start=3.625, end=4.0),  # G3 (C3 + 5th)
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.375),  # F#3 (chromatic approach)
    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # G3
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.125),  # G#3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=68, start=5.125, end=5.5),  # D4 (G3 + 5th)
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.875),  # C#4 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),
    # Bar 3: Bm7b5 (B, D, F, A)
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53) - A (60) - G (62) - F (53), then leave it hanging on A (60)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.5),
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=60, start=2.5, end=2.75),
    # Come back and finish it
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=53, start=5.25, end=5.5),
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5-3.0s)
for bar_start in [1.5, 3.0]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.1875, end=bar_start + i * 0.1875 + 0.1875)
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0),
])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
