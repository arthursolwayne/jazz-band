
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
    # Bar 2: D2 (MIDI 38)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to G2 (MIDI 43)
    pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.375),
    # Bar 3: G2 (MIDI 43)
    pretty_midi.Note(velocity=80, pitch=43, start=2.375, end=2.75),
    # Chromatic approach to C3 (MIDI 48)
    pretty_midi.Note(velocity=70, pitch=47, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),
    # Bar 4: C3 (MIDI 48)
    pretty_midi.Note(velocity=80, pitch=48, start=3.375, end=3.75),
    # Chromatic approach to F3 (MIDI 53)
    pretty_midi.Note(velocity=70, pitch=52, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=53, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=80, pitch=58, start=1.5, end=1.875),  # A3
    pretty_midi.Note(velocity=70, pitch=60, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=60, pitch=64, start=1.5, end=1.875),  # E4

    # Bar 3: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=55, start=2.375, end=2.75),  # D3
    pretty_midi.Note(velocity=80, pitch=58, start=2.375, end=2.75),  # F3
    pretty_midi.Note(velocity=70, pitch=62, start=2.375, end=2.75),  # A3
    pretty_midi.Note(velocity=60, pitch=60, start=2.375, end=2.75),  # C4

    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75),  # G3
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),  # B3
    pretty_midi.Note(velocity=70, pitch=65, start=3.375, end=3.75),  # D4
    pretty_midi.Note(velocity=60, pitch=53, start=3.375, end=3.75),  # F3
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + (i * 0.1875), end=start + (i * 0.1875) + 0.1875)
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
])

# Saxophone: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # C#5
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # A4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=2.75),  # C4
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # C#5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
