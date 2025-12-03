
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
    # Kick on 1 and 3: 0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),

    # Snare on 2 and 4: 0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),

    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) -> Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),

    # Bar 3: G2 (fifth) -> F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),

    # Bar 4: D2 (root) -> Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),

    # Bar 4: G2 (fifth) -> F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),

    # Bar 4: D2 (root) -> Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),

    # Bar 4: G2 (fifth) -> F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # C4
]
# Bar 3: G7 (G, B, D, F)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),  # F4
]
# Bar 4: Cmaj7 (C, E, G, B)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 -> F4 -> Bb4 (Dm), then resolve on G4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
