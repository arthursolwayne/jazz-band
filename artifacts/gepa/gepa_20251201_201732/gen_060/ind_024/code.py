
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

# Drums - Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass - Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2 (root)

    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # A2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # D2 (root)

    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Piano - Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: C7 (F7) - F, A, C, E, G
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # G4

    # Bar 3: Bb7 (F7) - F, A, C, Eb, G
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # D#4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G4

    # Bar 4: D7 (F7) - F, A, C, D, G
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # G4
]
piano.notes.extend(piano_notes)

# Drums - Bar 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875)
drums.notes.extend(drums.notes)

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) -> G (67) -> A (69) -> F (65) - ascending, then resolve
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),   # G4
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # F4 (return)
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),   # G4
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),   # G4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
