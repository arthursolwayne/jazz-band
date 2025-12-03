
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches, roots and fifths
bass_notes = [
    # Bar 2: D (root) and F# (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25),  # F#2 (fifth)
    # Bar 3: C# (chromatic approach to D)
    pretty_midi.Note(velocity=75, pitch=42, start=2.25, end=2.625),  # C#2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # D2
    # Bar 4: E (chromatic approach to F#)
    pretty_midi.Note(velocity=75, pitch=44, start=3.0, end=3.375),  # E2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75),  # F#2
    # Bar 5: G (fifth of D)
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125),  # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # D2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on last
# Bar 2: D7sus4 -> D7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#5

    # Bar 3: Cm7 -> D7
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # C4
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # F#5

    # Bar 4: A7sus4 -> D7
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # C#5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F#5
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # B5
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # F#5
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # B4

    # Bar 5: D7
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # F#5
]
piano.notes.extend(piano_notes)

# Sax (Dante): Motif that starts and finishes with a question
# Bar 2: Start of motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # B4
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875),  # D5
    # Bar 3: Continue motif
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.4375),  # B4
    pretty_midi.Note(velocity=110, pitch=65, start=2.4375, end=2.625),  # D5
    # Bar 4: Continue motif
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # B4
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375),  # D5
    # Bar 5: Resolve motif
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # F#5
]
sax.notes.extend(sax_notes)

# Final setup
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
