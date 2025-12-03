
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

# Bass - Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D2 (38) -> C#2 (37) -> G2 (43) -> D2 (38)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),
]
# Bar 3: G2 (43) -> F#2 (42) -> D2 (38) -> G2 (43)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),
])
# Bar 4: D2 (38) -> C#2 (37) -> G2 (43) -> D2 (38)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=37, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),
])
bass.notes.extend(bass_notes)

# Piano - Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4 (62)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),   # F4 (65)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),   # A4 (69)
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.0),   # C4 (67)
]
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4 (67)
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.5),   # Bb4 (71)
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.5),   # D4 (69)
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.5),   # F4 (65)
])
# Bar 4: Dm7 (D-F-A-C) again, resolving
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # D4 (62)
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=3.0),   # F4 (65)
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=3.0),   # A4 (69)
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=3.0),   # C4 (67)
])
piano.notes.extend(piano_notes)

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62) -> F4 (65) -> A4 (69) -> D4 (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75), # F4
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875), # A4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.75), # D4 (come back)
]
sax.notes.extend(sax_notes)

# Drums - Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 4
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 4
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),   # Hihat on 4
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
