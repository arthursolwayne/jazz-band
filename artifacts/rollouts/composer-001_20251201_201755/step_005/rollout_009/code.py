
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (root) -> C# (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),
    # Bar 3: A (fifth) -> Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=66, start=2.625, end=3.0),
    # Bar 4: D (root) -> C# (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.875),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.625),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=95, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=63, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=66, start=3.0, end=3.375),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=105, pitch=66, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=105, pitch=69, start=1.6875, end=1.875),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=105, pitch=66, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=105, pitch=69, start=2.4375, end=2.625),
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=105, pitch=66, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=105, pitch=69, start=3.1875, end=3.375),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
