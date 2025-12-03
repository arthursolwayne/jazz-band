
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
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4 (but out of bar 1)
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.625), # C2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D2 (root)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=90, pitch=56, start=3.75, end=4.125), # Bb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # A2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=90, pitch=54, start=5.25, end=5.625), # G2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # D2
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s): Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # C4

    # Bar 3 (3.0 - 4.5s): Gm7 (G-Bb-D-F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # F4

    # Bar 4 (4.5 - 6.0s): Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0),  # Bb4
]

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s): Motif starts
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # F4

    # Bar 3 (3.0 - 4.5s): Silence, leave it hanging
    # Bar 4 (4.5 - 6.0s): Return and finish
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # F4
]

sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):  # bars 2, 3, 4
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
