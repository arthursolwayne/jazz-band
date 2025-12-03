
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
    # Hi-hat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.625),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.625, end=1.75),  # F2
    pretty_midi.Note(velocity=90, pitch=39, start=1.75, end=1.875),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.0),  # A2 (fifth of D)
    pretty_midi.Note(velocity=90, pitch=41, start=2.0, end=2.125),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.25),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.375),  # Bb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=38, start=2.375, end=2.5),  # D2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F Ab C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),  # Ab4 (MIDI 60)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # C4
]
piano.notes.extend(piano_notes)

# Bar 3: Gm7 (G Bb D F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.75),  # Bb4
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # F4
]
piano.notes.extend(piano_notes)

# Bar 4: Cm7 (C Eb G Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # Bb4
]
piano.notes.extend(piano_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Bb4 - D4 - F4 - G4, then repeat with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75),  # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=4.25, end=4.5),  # A4 (slight variation)
]
sax.notes.extend(sax_notes)

# Bar 2: Drums continue
# Kick on 1 and 3 of bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4 of bar 2
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Drums continue
# Kick on 1 and 3 of bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4 of bar 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Drums continue
# Kick on 1 and 3 of bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4 of bar 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Bass continues (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.125),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.125, end=3.25),  # F2
    pretty_midi.Note(velocity=90, pitch=39, start=3.25, end=3.375),  # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.5),  # A2
    pretty_midi.Note(velocity=90, pitch=41, start=3.5, end=3.625),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=3.625, end=3.75),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.875),  # Bb2
    pretty_midi.Note(velocity=90, pitch=38, start=3.875, end=4.0),  # D2
    pretty_midi.Note(velocity=90, pitch=38, start=4.0, end=4.125),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.25),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=4.25, end=4.375),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=4.375, end=4.5),  # A2
]
bass.notes.extend(bass_notes)

# Bar 4: Bass continues (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.625),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.625, end=4.75),  # F2
    pretty_midi.Note(velocity=90, pitch=39, start=4.75, end=4.875),  # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.0),  # A2
    pretty_midi.Note(velocity=90, pitch=41, start=5.0, end=5.125),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=5.125, end=5.25),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=38, start=5.375, end=5.5),  # D2
    pretty_midi.Note(velocity=90, pitch=38, start=5.5, end=5.625),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=5.75),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=5.75, end=5.875),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=5.875, end=6.0),  # A2
]
bass.notes.extend(bass_notes)

# Bar 3: Piano continues (3.0 - 4.5s)
# Gm7 (G Bb D F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # Bb4
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # F4
]
piano.notes.extend(piano_notes)

# Bar 4: Piano continues (4.5 - 6.0s)
# Cm7 (C Eb G Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # Bb4
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
