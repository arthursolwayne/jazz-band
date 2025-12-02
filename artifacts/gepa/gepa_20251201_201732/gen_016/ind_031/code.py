
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # G2
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # C3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125), # E3
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),  # D3
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # E3
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # G3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625), # B3
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),  # A3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.25),  # F3
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=2.25),  # A3
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.25),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),  # E4

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=3.0),  # Bb3
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=3.0),  # D3
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=3.0),  # F3
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=3.0),  # Ab3

    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # G3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # B3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # D3
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.75),  # F3
]
piano.notes.extend(piano_notes)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + 1.5)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)

drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (60) - A (65) - C (62) - F (60)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # C4
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # C4
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # C4
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # C4
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # C4
    pretty_midi.Note(velocity=110, pitch=60, start=5.75, end=6.0)   # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
