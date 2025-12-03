
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
    # Hi-hat on every eighth
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
    # Bar 2: F root (43) -> E chromatic approach (42)
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25),
    # Bar 3: C root (48) -> B chromatic approach (47)
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),
    # Bar 4: G root (49) -> A chromatic approach (50)
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=2.25),
    # Bar 3: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=3.0),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.125),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.5),   # F
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75),   # F
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
