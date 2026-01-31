
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

# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),  # G
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - D7sus4 (D, G, C, F)
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # F
    # Bar 3 (3.0 - 4.5s) - G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # F
    # Bar 4 (4.5 - 6.0s) - Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # B
]
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),  # C
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5),  # C
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
