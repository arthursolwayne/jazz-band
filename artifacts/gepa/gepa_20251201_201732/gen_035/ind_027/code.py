
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # F#5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G5
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # D5
]
sax.notes.extend(sax_notes)

# Bass (walking line: D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # E2 (chromatic up)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),   # F#2 (chromatic down)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D3
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F#3
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # A3
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C#4,

    # Bar 3: Bm7 (B-D-F#-A)
    pretty_midi.Note(velocity=100, pitch=56, start=2.25, end=2.625),  # B3
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # A4

    # Bar 4: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # F5
]
piano.notes.extend(piano_notes)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.875, end=2.25),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),   # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),   # Kick on 3
]
drums.notes.extend(drum_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
