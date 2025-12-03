
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

# Bars 2-4: Full quartet (1.5s - 6.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # F#2
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),  # A2
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75),  # C3
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.125),  # C#3
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # E3
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # E3
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # G3
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.625),  # G#3
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # B3
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # A2
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C3
]
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # D3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F3
])
# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Eb3
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G3
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Bb3
])
piano.notes.extend(piano_notes)

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging, finish it.
# Motif: Dm7 (D-F-A-C) - D, F, A, C (MIDI 50, 53, 55, 57)
# Start on D, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=110, pitch=57, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=55, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=110, pitch=57, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=110, pitch=50, start=5.0, end=5.25),  # D
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.375),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.5),
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
# midi.write disabled
