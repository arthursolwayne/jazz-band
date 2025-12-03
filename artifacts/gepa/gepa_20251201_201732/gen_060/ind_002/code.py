
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: Dm (D2, F2, A2)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    # Bar 3: Gm (G2, Bb2, D2)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    # Bar 4: Cm (C2, Eb2, G2)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # C2
    # Chromatic approaches
    pretty_midi.Note(velocity=70, pitch=39, start=1.875, end=2.0),  # Eb2 (approach to G2)
    pretty_midi.Note(velocity=70, pitch=42, start=2.625, end=2.75),  # Bb2 (approach to C2)
    pretty_midi.Note(velocity=70, pitch=41, start=3.375, end=3.5),  # F#2 (approach to G2)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # D4 (root)
    pretty_midi.Note(velocity=85, pitch=55, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=85, pitch=58, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=85, pitch=60, start=1.5, end=1.875),  # C5
    # Bar 3: G7 (B, D, F#, G)
    pretty_midi.Note(velocity=90, pitch=58, start=2.25, end=2.625),  # G4 (root)
    pretty_midi.Note(velocity=85, pitch=61, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=85, pitch=65, start=2.25, end=2.625),  # F#5
    # Bar 4: Cm7 (Eb, G, Bb, C)
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # C4 (root)
    pretty_midi.Note(velocity=85, pitch=55, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=85, pitch=58, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=85, pitch=60, start=3.0, end=3.375),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm scale fragment - D, F, Eb, D (D4, F4, Eb4, D4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=100, pitch=63, start=2.0, end=2.25),  # Eb4
    # Leave it hanging, return later
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
