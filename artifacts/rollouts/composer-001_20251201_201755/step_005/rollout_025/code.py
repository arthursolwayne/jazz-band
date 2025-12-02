
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
bar_length = 1.5

# Bass line: Marcus
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=2.0),   # F2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=2.0, end=2.5),   # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.5, end=3.0),   # C3 (fifth)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.5),   # F2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=3.5, end=4.0),   # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=4.0, end=4.5),   # C3 (fifth)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=5.0),   # F2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=5.0, end=5.5),   # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=5.5, end=6.0),   # C3 (fifth)
]
bass.notes.extend(bass_notes)

# Piano: Diane
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E) open voicing
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),  # E4
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0),  # C5

    # Bar 3: Bbmaj7 (Bb, D, F, Ab) open voicing
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.5),  # Ab4
    pretty_midi.Note(velocity=100, pitch=52, start=2.0, end=2.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=57, start=2.0, end=2.5),  # F4

    # Bar 4: Dm7 (D, F, A, C) open voicing
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=52, start=2.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=55, start=2.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=3.0),  # A4
]
piano.notes.extend(piano_notes)

# Drums: Full bar with kick, snare, hihat
for i in range(3):
    bar_start = 1.5 + i * bar_length
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    for j in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + j * 0.375, end=bar_start + j * 0.375 + 0.1875)

# Sax: Dante's motif
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # G4

    # Bar 3: No sax until the end
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # G4

    # Bar 4: End of motif
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
