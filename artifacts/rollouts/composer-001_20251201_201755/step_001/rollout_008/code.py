
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (walking line, roots and fifths with chromatic approaches)
# Dm7 -> Gm7 -> Cm7 -> Fm7 (roots on 1, 2, 3, 4)
# D2 (D) -> F# (chromatic approach) -> G (G) -> Bb (chromatic) -> C (C) -> Eb (chromatic) -> D (D) -> F# (chromatic)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),   # F#
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),   # F#
]
bass.notes.extend(bass_notes)

# Piano voicings
# Bar 2: Dm7 (D-F-A-C) -> open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
]
# Bar 3: Gm7 (G-Bb-D-F) -> open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # F5
])
# Bar 4: Cm7 (C-Eb-G-Bb) -> open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb4
])
# Bar 4: Fm7 (F-Ab-C-Eb) -> open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),  # Eb5
])
piano.notes.extend(piano_notes)

# Sax melody: short motif, start it, leave it hanging, come back and finish it
# Dm7 - Gm7 - Cm7 - Fm7
# Motif: D (D4), F (F4), A (A4), leave it hanging on A, come back with D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.4375),  # A4 (return)
    pretty_midi.Note(velocity=100, pitch=62, start=2.4375, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.8125),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.8125, end=3.0),   # D4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
