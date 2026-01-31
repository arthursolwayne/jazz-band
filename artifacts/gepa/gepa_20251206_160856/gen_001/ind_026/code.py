
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales.
bass_notes = [
    # Bar 2: D2
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Bar 2: F2 (chromatic approach to G2)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.125),
    # Bar 2: G2
    pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.5),
    # Bar 3: A2
    pretty_midi.Note(velocity=100, pitch=45, start=2.5, end=2.875),
    # Bar 3: C3 (chromatic approach to B2)
    pretty_midi.Note(velocity=100, pitch=48, start=2.875, end=3.125),
    # Bar 3: B2
    pretty_midi.Note(velocity=100, pitch=46, start=3.125, end=3.5),
    # Bar 4: D2
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875),
    # Bar 4: F2 (chromatic approach to G2)
    pretty_midi.Note(velocity=100, pitch=41, start=3.875, end=4.125),
    # Bar 4: G2
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),
    # Bar 4: A2
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.875),
    # Bar 4: C3 (chromatic approach to B2)
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.125),
    # Bar 4: B2
    pretty_midi.Note(velocity=100, pitch=46, start=5.125, end=5.5),
    # Bar 4: D2
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=55, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=58, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.875),
    # Bar 4: Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=3.875),
    # Bar 4: Dm7 (D-F-A-C) resolution
    pretty_midi.Note(velocity=100, pitch=50, start=5.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=53, start=5.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=57, start=5.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif begins
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875),  # G4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.6875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.6875, end=2.875),  # B4
    # Bar 4: Finish it
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.6875),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=3.6875, end=3.875),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0625),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.0625, end=4.25),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.4375),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=4.4375, end=4.625),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.8125),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.8125, end=5.0),  # B4
]
sax.notes.extend(sax_notes)

# Drums: continue for bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start_time = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)

# Snare on 2 and 4
for bar in range(2, 5):
    start_time = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.0)

# Hihat on every eighth
for bar in range(2, 5):
    start_time = bar * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
