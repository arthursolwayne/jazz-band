
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38), F2 (MIDI 41), A2 (MIDI 45), C3 (MIDI 48)
# Chromatic approach to D2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.875), # C#2
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # D2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # F2
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last beat
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Short motif, sing it, leave it hanging
# D4 (MIDI 62), F4 (MIDI 65), G4 (MIDI 67), D4 (MIDI 62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2 (MIDI 41), A2 (MIDI 45), C3 (MIDI 48), D3 (MIDI 49)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.5),  # F5
]
piano.notes.extend(piano_notes)

# Sax: Repeat and vary the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: A2 (MIDI 45), C3 (MIDI 48), D3 (MIDI 49), E3 (MIDI 50)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.875), # A2
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.25), # C3
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625), # D3
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # E3
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb, D, F, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=5.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.0),  # F5
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=5.0),  # A5
]
piano.notes.extend(piano_notes)

# Sax: Resolve the motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D4
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
