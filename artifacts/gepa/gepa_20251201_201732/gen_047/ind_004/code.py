
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F minor, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25),  # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.5, end=2.75),  # D (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=2.75, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7sus4 (F, Bb, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.75),  # D
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5),  # F
    # Bar 4: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=57, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=58, start=2.75, end=3.0),  # G
]
piano.notes.extend(piano_notes)

# Sax: Short motif, start it, leave it hanging, come back and finish it
# Motif: F - Bb - D (F7sus4), leave it on D, then come back with F - Bb - C (F7)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=57, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=58, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=110, pitch=57, start=2.875, end=3.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=55, start=3.0, end=3.125),  # C
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in F minor, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=56, start=3.25, end=3.5),  # G (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=4.0, end=4.25),  # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=4.25, end=4.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # F
    # Bar 4: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.0),  # G
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in F minor, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=52, start=5.0, end=5.25),  # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=5.5, end=5.75),  # D (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: A7 (A, C#, E, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.75),  # G
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, resolve on C
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=55, start=4.875, end=5.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.dump()
