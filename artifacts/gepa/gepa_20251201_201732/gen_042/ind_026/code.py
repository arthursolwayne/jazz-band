
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.625),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.625, end=1.75),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=1.75, end=1.875),  # A2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.0),  # G2
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.125),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=2.125, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.375),  # A2
    pretty_midi.Note(velocity=100, pitch=41, start=2.375, end=2.5),  # G2
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.625),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=2.75),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.75, end=2.875),  # A2
    pretty_midi.Note(velocity=100, pitch=41, start=2.875, end=3.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # D5
]
piano.notes.extend(piano_notes)

# Bar 3: F7 (from Dm to Gm to Cm to F7)
# Bar 3: 1.5-3.0 seconds (bar 2), 3.0-4.5 seconds (bar 3)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # E5
]
piano.notes.extend(piano_notes)

# Bar 4: Gm7
# Bar 4: 4.5-6.0 seconds
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # F5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G4
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # Bb4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.75),  # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=42, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25),  # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=100, pitch=42, start=4.375, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75),  # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=100, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=100, pitch=42, start=5.875, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
