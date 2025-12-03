
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# SAX: Melody starts - short motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # D
]
sax.notes.extend(sax_notes)

# BASS: Walking line in Dm - roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=1.75, end=2.0),  # F2
    pretty_midi.Note(velocity=100, pitch=51, start=2.0, end=2.25),  # Eb2
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5),  # D2
]
bass.notes.extend(bass_notes)

# PIANO: Open voicings, resolve on the last bar
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # C5
]
piano.notes.extend(piano_notes)

# Bar 3: F7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=73, start=2.5, end=3.0),  # D5
]
piano.notes.extend(piano_notes)

# Bar 4: Gm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.5),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5),  # D5
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# SAX: Melody continues - finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # D
]
sax.notes.extend(sax_notes)

# BASS: Walking line in Dm - roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=3.25, end=3.5),  # D2
    pretty_midi.Note(velocity=100, pitch=52, start=3.5, end=3.75),  # Eb2
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.0),  # D2
]
bass.notes.extend(bass_notes)

# PIANO: Open voicings, resolve on the last bar
# Bar 3: F7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # C5
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.5),  # D5
]
piano.notes.extend(piano_notes)

# Bar 4: Gm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=4.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=4.0),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=4.0),  # D5
]
piano.notes.extend(piano_notes)

# Bar 4: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Sax continues with the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # E
]
sax.notes.extend(sax_notes)

# BASS: Walking line in Dm - roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=4.0, end=4.25),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=4.25, end=4.5),  # F2
]
bass.notes.extend(bass_notes)

# PIANO: Resolve on the last bar
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.5),  # C5
]
piano.notes.extend(piano_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
