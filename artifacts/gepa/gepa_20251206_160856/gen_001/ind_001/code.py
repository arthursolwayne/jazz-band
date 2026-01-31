
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
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drums_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (root) - C (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.125),
    # Bar 3: A (fifth) - Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.875),
    # Bar 4: D (root) - C (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.875, end=3.25),
    pretty_midi.Note(velocity=90, pitch=37, start=3.25, end=3.625),
    # Repeat for next bars
    pretty_midi.Note(velocity=90, pitch=38, start=3.625, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=37, start=3.9375, end=4.25),
    pretty_midi.Note(velocity=90, pitch=43, start=4.25, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.9375),
    pretty_midi.Note(velocity=90, pitch=38, start=4.9375, end=5.3125),
    pretty_midi.Note(velocity=90, pitch=37, start=5.3125, end=5.625),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    # Bar 3: F7 (F-A-C-E)
    pretty_midi.Note(velocity=100, pitch=65, start=2.125, end=2.5),
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.5),
    pretty_midi.Note(velocity=100, pitch=69, start=2.125, end=2.5),
    pretty_midi.Note(velocity=100, pitch=71, start=2.125, end=2.5),
    # Bar 4: Gm7 (G-Bb-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.25),
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
drums_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.125, end=2.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.25),
    # Hi-hats
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),
    # Hi-hats
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0625, end=3.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.4375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=3.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.8125, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.1875, end=4.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.375, end=4.75),
    pretty_midi.Note(velocity=100, pitch=36, start=5.5, end=5.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),
    # Hi-hats
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=4.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.9375, end=5.125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.3125, end=5.5),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.6875, end=5.875),
]
drums.notes.extend(drums_notes)

# Saxophone: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Start motif on D (62), F (65), A (67), rest on bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=105, pitch=67, start=2.0, end=2.25),
    # Rest of bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    # Start again in bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.125),
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.375),
    pretty_midi.Note(velocity=105, pitch=67, start=3.375, end=3.625),
    # Resolve on D in bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=65, start=3.875, end=4.125),
    pretty_midi.Note(velocity=105, pitch=67, start=4.125, end=4.375),
    pretty_midi.Note(velocity=110, pitch=62, start=4.375, end=4.625),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
