
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (Dm7)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    # Bar 3 (Gm7)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),
    # Bar 4 (Cm7)
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # F5
])
# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb4
])
piano.notes.extend(piano_notes)

# Sax: Motif, start it, leave it hanging, come back and finish it
# Dm7 - D (62), F (64), A (67), C (69)
# Motif: D - F - A, leave it hanging on A
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75), # A4 (return)
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # C4 (resolve)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
]
drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.25, end=6.5),  # Slightly beyond to emphasize the end
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Slightly beyond to emphasize the end
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
