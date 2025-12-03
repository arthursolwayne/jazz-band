
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),   # F2 (chromatic approach)

    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),   # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),   # F2 (chromatic approach)

    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),   # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)    # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 - D F A C
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),   # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),   # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),   # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875)    # C5
]

# Bar 3: G7 - G B D F
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),   # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),   # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625)    # F5
])

# Bar 4: Cm7 - C Eb G Bb
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),    # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),    # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),    # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375)     # Bb4
])

# Add the last bar with a more open voicing resolving to Dm7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),   # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),   # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),   # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875)    # C5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it
# Motif: D4, F4, G4, A4 - then leave it hanging on A4, return on the third bar
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),   # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),   # A4 (leave hanging)

    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.125),   # A4 (return)
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5)    # D4
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)    # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
