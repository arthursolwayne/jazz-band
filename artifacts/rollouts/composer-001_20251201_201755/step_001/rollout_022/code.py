
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.625),
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

# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F2 (root), G2 (fifth), E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625),
    # Bar 3: C3 (root), D3 (fifth), B2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=62, start=2.875, end=3.25),
    pretty_midi.Note(velocity=90, pitch=59, start=3.25, end=3.625),
    # Bar 4: F2 (root), G2 (fifth), E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=3.625, end=3.875),
    pretty_midi.Note(velocity=90, pitch=55, start=3.875, end=4.25),
    pretty_midi.Note(velocity=90, pitch=52, start=4.25, end=4.625)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),
    # Bar 3: Bm7 (B, D, F#, A)
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=2.875),
    pretty_midi.Note(velocity=95, pitch=64, start=2.625, end=2.875),
    pretty_midi.Note(velocity=95, pitch=66, start=2.625, end=2.875),
    pretty_midi.Note(velocity=95, pitch=69, start=2.625, end=2.875),
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=95, pitch=58, start=3.625, end=3.875),
    pretty_midi.Note(velocity=95, pitch=61, start=3.625, end=3.875),
    pretty_midi.Note(velocity=95, pitch=62, start=3.625, end=3.875),
    pretty_midi.Note(velocity=95, pitch=60, start=3.625, end=3.875),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C - F (over 4 bars, with space in between)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=105, pitch=50, start=2.625, end=2.875),
    pretty_midi.Note(velocity=105, pitch=55, start=3.625, end=3.875),
    pretty_midi.Note(velocity=105, pitch=53, start=4.625, end=4.875)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
