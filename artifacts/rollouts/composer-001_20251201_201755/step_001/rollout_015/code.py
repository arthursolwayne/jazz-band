
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) -> Eb2 (39) -> G2 (43) -> A2 (45)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),
    # Bar 3: A2 (45) -> Bb2 (46) -> D3 (50) -> Eb3 (51)
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=51, start=4.125, end=4.5),
    # Bar 4: Eb3 (51) -> F3 (53) -> A3 (57) -> Bb3 (58)
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=58, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: Dm7 (D - F - A - C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),
    # Bar 3: G7 (G - B - D - F)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),
    # Bar 4: Cm7 (C - Eb - G - Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),
    # Bar 3: Motif continues
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125),
    # Bar 4: Motif finishes
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
