
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
# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    # D2 (root)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to G2 (MIDI 43)
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # Chromatic approach to A2 (MIDI 45)
    pretty_midi.Note(velocity=80, pitch=44, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=45, start=2.5625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Motif (D4, F4, G4, D4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 (MIDI 43) walking line with chromatic approaches
bass_notes = [
    # G2 (root)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    # Chromatic approach to Bb2 (MIDI 46)
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=46, start=3.5625, end=3.875),
    # Chromatic approach to D2 (MIDI 38)
    pretty_midi.Note(velocity=80, pitch=41, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=90, pitch=38, start=4.0625, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb D F A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5),  # F5
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5),  # A5
]
piano.notes.extend(piano_notes)

# Sax: Motif (G4, Bb4, C4, G4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=57, start=3.25, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: A2 (MIDI 45) walking line with chromatic approaches
bass_notes = [
    # A2 (root)
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875),
    # Chromatic approach to D2 (MIDI 38)
    pretty_midi.Note(velocity=80, pitch=44, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=38, start=5.0625, end=5.375),
    # Chromatic approach to F2 (MIDI 41)
    pretty_midi.Note(velocity=80, pitch=40, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=90, pitch=41, start=5.5625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=5.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=5.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Motif (A4, C4, D4, A4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # A4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
