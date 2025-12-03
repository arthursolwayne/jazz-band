
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625),  # G (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # F (root)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # F (root)
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.125),  # G (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # F (root)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),  # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625),  # G (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),  # F (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2 - Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),  # D
    # Bar 3 - Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.75),  # Ab
    # Bar 4 - Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.25),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # C
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # G
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
