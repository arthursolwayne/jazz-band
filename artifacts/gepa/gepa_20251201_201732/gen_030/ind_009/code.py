
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet starts here (1.5 - 3.0s)
# Bass: Walking line in F, roots and fifths with chromatic approaches
# F - G - A - Bb - C - D - E - F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.625), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),  # F2 (root)
]

# Piano: Open voicings, different chord each bar
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=48, start=1.5, end=2.0),
    pretty_midi.Note(velocity=85, pitch=55, start=1.5, end=2.0),
    pretty_midi.Note(velocity=85, pitch=52, start=1.5, end=2.0),
    pretty_midi.Note(velocity=85, pitch=60, start=1.5, end=2.0),
]
piano.notes.extend(piano_notes)

# Sax: Melody starts, one short motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G4 (melody starts)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # G4 (resolve)
]
sax.notes.extend(sax_notes)

# Bar 3 (3.0 - 4.5s)
# Bass: Walking line continues
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125), # Bb2
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # G2
])

# Piano: C7 chord (C, E, G, B)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=55, start=3.0, end=3.5),
    pretty_midi.Note(velocity=85, pitch=58, start=3.0, end=3.5),
    pretty_midi.Note(velocity=85, pitch=60, start=3.0, end=3.5),
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.5),
]
piano.notes.extend(piano_notes)

# Sax: Repeat motif, but vary slightly
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # G4 (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Continue pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
# Bass: Walking line continues
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),  # A2
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25), # Bb2
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # G2
])

# Piano: Fmaj7 again, resolves on the last note
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=48, start=4.5, end=5.0),
    pretty_midi.Note(velocity=85, pitch=55, start=4.5, end=5.0),
    pretty_midi.Note(velocity=85, pitch=52, start=4.5, end=5.0),
    pretty_midi.Note(velocity=85, pitch=60, start=4.5, end=5.0),
]
piano.notes.extend(piano_notes)

# Sax: Repeat motif one last time, full resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # G4 (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Final kick on 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
