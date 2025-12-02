
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
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root), G (fifth), E (chromatic approach down)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    # Bar 3: C (root), D (fifth), B (chromatic approach down)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.625),
    # Bar 4: G (root), A (fifth), F# (chromatic approach down)
    pretty_midi.Note(velocity=100, pitch=72, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=74, start=3.875, end=4.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.625)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    # Bar 3: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.875),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=72, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=74, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=76, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=70, start=3.625, end=3.875)
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: First motif (F, A, G)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    # Bar 3: Leave it hanging (no notes)
    # Bar 4: Come back and finish it (F, A, G)
    pretty_midi.Note(velocity=100, pitch=70, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=72, start=3.875, end=4.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.625)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
