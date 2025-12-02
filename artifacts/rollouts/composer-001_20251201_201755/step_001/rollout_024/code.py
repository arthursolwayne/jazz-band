
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # C3 (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),  # Bb2 (chromatic approach)
    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # C3 (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # Bb2 (chromatic approach)
    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # C3 (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),  # Bb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # C5
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Ab4
    # Bar 4: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F - Gb - Ab - A (hanging on A), then F - Ab - Bb - C (resolution)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625),  # F5
    pretty_midi.Note(velocity=110, pitch=63, start=1.625, end=1.75),  # Gb5
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875),  # Ab5
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0),  # A5 (hanging)
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.125),  # F5
    pretty_midi.Note(velocity=110, pitch=62, start=2.125, end=2.25),  # Ab5
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.375),  # Bb5
    pretty_midi.Note(velocity=110, pitch=67, start=2.375, end=2.5),  # C6 (resolution)
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.625),  # A5 (sustain)
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.75),  # Ab5
    pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=2.875),  # Bb5
    pretty_midi.Note(velocity=110, pitch=67, start=2.875, end=3.0),  # C6 (resolution)
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.125),  # F5
    pretty_midi.Note(velocity=110, pitch=62, start=3.125, end=3.25),  # Ab5
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.375),  # Bb5
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5),  # C6
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
