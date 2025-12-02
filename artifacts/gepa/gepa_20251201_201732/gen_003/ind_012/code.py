
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

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=37, start=2.25, end=2.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # A2 (root + minor third)
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # Bb2 (fifth)
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125), # A2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),  # A2 (root + minor third)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=37, start=5.25, end=5.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # F2 (root)
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # E4 (chromatic)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # A4 (resolve)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # Bb4
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25), # A4 (chromatic)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # F4 (resolve)

    # Bar 3: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # C5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # B4 (chromatic)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # C5 (resolve)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # A4 (resolve)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # Bb4 (resolve)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # B4 (resolve)

    # Bar 4: Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb4 (chromatic)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75),  # Ab4 (resolve)
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # C5 (resolve)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # Bb4 (resolve)
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # D5 (resolve)
]
piano.notes.extend(piano_notes)

# Sax (Dante)
sax_notes = [
    # Bar 2: Melody starts
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # Eb4

    # Bar 3: Melody continues
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),   # G4

    # Bar 4: Melody ends
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # Eb4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),   # G4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Bar 2
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375),  # Hihat on 1
        pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),  # Snare on 2
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),  # Hihat on 2
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),  # Kick on 3
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),  # Hihat on 3
        pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875),  # Snare on 4
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875),  # Hihat on 4
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
