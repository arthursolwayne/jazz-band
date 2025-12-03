
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet enters
# Bass line: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),  # G2
    # Bar 3: F#2 (chromatic approach to G), G2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # G2
    # Bar 4: A2 (chromatic approach to Bb), Bb2
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # Bb2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
]
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F
]
# Bar 4: Am7 (A-C-E-G)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F - G - D (Dm scale) but played with rhythm and space
sax_notes = [
    # Bar 2: D (D4), F (F4), G (G4)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.375),  # G4
    # Bar 3: Rest
    # Bar 4: D (D4), F (F4), G (G4)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.5),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.875),  # G4
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
