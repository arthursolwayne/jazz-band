
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

# Bass line: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F2 (chromatic approach), G2 (fifth), D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.125),
    pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.5),
    pretty_midi.Note(velocity=80, pitch=38, start=2.5, end=2.875),
    # Bar 3: G2 (root), A2 (chromatic approach), C3 (fifth), G2 (root)
    pretty_midi.Note(velocity=80, pitch=43, start=2.875, end=3.25),
    pretty_midi.Note(velocity=80, pitch=44, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.875),
    pretty_midi.Note(velocity=80, pitch=43, start=3.875, end=4.25),
    # Bar 4: C3 (root), D3 (chromatic approach), F3 (fifth), C3 (root)
    pretty_midi.Note(velocity=80, pitch=48, start=4.25, end=4.625),
    pretty_midi.Note(velocity=80, pitch=50, start=4.625, end=4.875),
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.0),
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=78, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=82, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=79, start=2.5, end=3.0),
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=79, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=81, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=82, start=3.5, end=4.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.75),
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=110, pitch=72, start=4.0, end=4.25),
    pretty_midi.Note(velocity=110, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Bar 2
for i in range(4):
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i * 0.375, end=1.5 + i * 0.375 + 0.1875)
for i in range(4):
    pretty_midi.Note(velocity=110, pitch=38, start=1.5 + i * 0.375 + 0.375, end=1.5 + i * 0.375 + 0.375 + 0.125)
for i in range(8):
    pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i * 0.1875, end=1.5 + i * 0.1875 + 0.1875)

# Bar 3
for i in range(4):
    pretty_midi.Note(velocity=100, pitch=36, start=2.875 + i * 0.375, end=2.875 + i * 0.375 + 0.1875)
for i in range(4):
    pretty_midi.Note(velocity=110, pitch=38, start=2.875 + i * 0.375 + 0.375, end=2.875 + i * 0.375 + 0.375 + 0.125)
for i in range(8):
    pretty_midi.Note(velocity=80, pitch=42, start=2.875 + i * 0.1875, end=2.875 + i * 0.1875 + 0.1875)

# Bar 4
for i in range(4):
    pretty_midi.Note(velocity=100, pitch=36, start=4.25 + i * 0.375, end=4.25 + i * 0.375 + 0.1875)
for i in range(4):
    pretty_midi.Note(velocity=110, pitch=38, start=4.25 + i * 0.375 + 0.375, end=4.25 + i * 0.375 + 0.375 + 0.125)
for i in range(8):
    pretty_midi.Note(velocity=80, pitch=42, start=4.25 + i * 0.1875, end=4.25 + i * 0.1875 + 0.1875)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
