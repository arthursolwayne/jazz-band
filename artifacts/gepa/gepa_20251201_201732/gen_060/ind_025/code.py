
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2-4
# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75),    # D2 (root)
    pretty_midi.Note(velocity=80, pitch=43, start=1.75, end=2.0),    # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.25),    # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.5),    # D2 (root)
    pretty_midi.Note(velocity=80, pitch=43, start=2.5, end=2.75),    # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=44, start=2.75, end=3.0),    # A2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.25),    # D2 (root)
    pretty_midi.Note(velocity=80, pitch=43, start=3.25, end=3.5),    # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=3.5, end=3.75),    # C2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.0),    # D2 (root)
    pretty_midi.Note(velocity=80, pitch=43, start=4.0, end=4.25),    # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.5),    # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.75),    # D2 (root)
    pretty_midi.Note(velocity=80, pitch=43, start=4.75, end=5.0),    # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=44, start=5.0, end=5.25),    # A2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.5),    # D2 (root)
    pretty_midi.Note(velocity=80, pitch=43, start=5.5, end=5.75),    # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=5.75, end=6.0),    # C2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=2.0),  # F (4th octave)
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=56, start=1.5, end=2.0),  # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=55, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=2.0, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.5),  # Ab
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=55, start=2.5, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=2.5, end=3.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=58, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.5, end=3.0),  # Bb
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 2.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
]
drums.notes.extend(drum_notes)

# Bar 3 (2.0 - 2.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.375, end=2.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.75),
]
drums.notes.extend(drum_notes)

# Bar 4 (2.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.25),
]
drums.notes.extend(drum_notes)

# Bar 5 (3.0 - 3.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
]
drums.notes.extend(drum_notes)

# Bar 6 (3.5 - 4.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.875, end=4.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=4.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.25),
]
drums.notes.extend(drum_notes)

# Bar 7 (4.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.375, end=4.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.75),
]
drums.notes.extend(drum_notes)

# Bar 8 (4.5 - 5.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
]
drums.notes.extend(drum_notes)

# Bar 9 (5.0 - 5.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.375, end=5.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.75),
]
drums.notes.extend(drum_notes)

# Bar 10 (5.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.5, end=5.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.25),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
