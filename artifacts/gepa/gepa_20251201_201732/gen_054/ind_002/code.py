
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.6875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.6875, end=1.875), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.0),   # A2
    pretty_midi.Note(velocity=90, pitch=40, start=2.0, end=2.1875),  # Eb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, resolve on the last bar
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=95, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.75),  # C5
]
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.5),  # Bb4
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.5),  # D5
    pretty_midi.Note(velocity=95, pitch=72, start=2.25, end=2.5),  # F5
])
# Bar 4: Dm7 again (D-F-A-C)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=62, start=2.75, end=3.0),  # D4
    pretty_midi.Note(velocity=95, pitch=65, start=2.75, end=3.0),  # F4
    pretty_midi.Note(velocity=95, pitch=67, start=2.75, end=3.0),  # A4
    pretty_midi.Note(velocity=95, pitch=69, start=2.75, end=3.0),  # C5
])
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
]
# Bar 3 (2.0s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.375, end=2.5),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
])
# Bar 4 (2.5s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
])
drums.notes.extend(drum_notes)

# Dante: Tenor sax - One short motif, start it, leave it hanging
# Bar 2: Start of motif
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=64, start=1.5, end=1.6875),  # E4
    pretty_midi.Note(velocity=105, pitch=66, start=1.6875, end=1.875), # G4
    pretty_midi.Note(velocity=105, pitch=62, start=1.875, end=2.0),   # D4 (rest)
]
# Bar 3: Continue the motif
sax_notes.extend([
    pretty_midi.Note(velocity=105, pitch=67, start=2.25, end=2.4375), # A4
    pretty_midi.Note(velocity=105, pitch=64, start=2.4375, end=2.625), # E4
    pretty_midi.Note(velocity=105, pitch=62, start=2.625, end=2.8125), # D4
])
# Bar 4: End of motif
sax_notes.extend([
    pretty_midi.Note(velocity=105, pitch=65, start=2.75, end=2.9375), # F4
    pretty_midi.Note(velocity=105, pitch=62, start=2.9375, end=3.0),  # D4 (rest)
])
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
