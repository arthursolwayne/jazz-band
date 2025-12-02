
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
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Marcus
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D4 on 1
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0),  # Eb4 on 2
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25),  # F#4 on 3
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # A4 on 4
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=2.75),  # B4 on 1
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # A4 on 2
]
bass.notes.extend(bass_notes)

# Piano: Diane
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # A4 (7th chord)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # B4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # A4 (7th chord)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # E4
]
piano.notes.extend(piano_notes)

# Sax: Dante - first motif (starts on bar 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # E4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums
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

# Bass line: Marcus
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # A4 on 1
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),  # B4 on 2
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.75),  # D5 on 3
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0),  # E4 on 4
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.25),  # D4 on 1
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5),  # A4 on 2
]
bass.notes.extend(bass_notes)

# Piano: Diane
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # B4 (7th chord)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # E5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # B4 (7th chord)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # E5
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # E4
]
piano.notes.extend(piano_notes)

# Sax: Dante - continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bass line: Marcus
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),  # E4 on 1
    pretty_midi.Note(velocity=80, pitch=66, start=4.75, end=5.0),  # G4 on 2
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.25),  # B4 on 3
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),  # A4 on 4
    pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75),  # E4 on 1
    pretty_midi.Note(velocity=80, pitch=66, start=5.75, end=6.0),  # G4 on 2
]
bass.notes.extend(bass_notes)

# Piano: Diane
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # E4 (7th chord)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # E4 (7th chord)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # D5
]
piano.notes.extend(piano_notes)

# Sax: Dante - finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # E4
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # E4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
