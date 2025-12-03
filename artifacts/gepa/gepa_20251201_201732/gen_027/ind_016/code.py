
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625), # F2 (fifth)
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125), # F2 (fifth)
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625), # F2 (fifth)
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),  # E2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings
piano_notes = [
    # Bar 2 (1.5 - 2.25s): Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # C5

    # Bar 3 (2.25 - 3.0s): G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # F5

    # Bar 4 (3.0 - 3.75s): Cmaj7 (C E G B)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # B4

    # Bar 4 (3.75 - 4.5s): Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.5),  # C5

    # Bar 4 (4.5 - 5.25s): G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),  # F5

    # Bar 4 (5.25 - 6.0s): Cmaj7 (C E G B)
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=6.0),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=6.0),  # B4
]
piano.notes.extend(piano_notes)

# Sax: Motif in Dm
sax_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4 (start)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E4 (end)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4 (start)
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # E4
]
sax.notes.extend(sax_notes)

# Drums in Bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 4

    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4

    # Bar 4 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
