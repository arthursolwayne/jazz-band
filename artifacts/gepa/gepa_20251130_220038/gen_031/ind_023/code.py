
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Sax enters with a whisper (1.5 - 3.0s)
# Motif: F (C4), Bb (E4), B (F#4), rest, then repeat with F (C4), Bb (E4), B (F#4)
sax_notes = [
    pretty_midi.Note(velocity=70, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=72, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=74, pitch=64, start=2.0, end=2.25),
    pretty_midi.Note(velocity=70, pitch=60, start=2.5, end=2.75),
    pretty_midi.Note(velocity=72, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=74, pitch=64, start=3.0, end=3.25),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F minor
# F - Gb - G - Ab
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=65, pitch=66, start=1.75, end=2.0),
    pretty_midi.Note(velocity=68, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=63, pitch=68, start=2.25, end=2.5),
    pretty_midi.Note(velocity=70, pitch=65, start=2.5, end=2.75),
    pretty_midi.Note(velocity=65, pitch=66, start=2.75, end=3.0),
    pretty_midi.Note(velocity=68, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=63, pitch=68, start=3.25, end=3.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=85, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=75, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=75, pitch=65, start=3.0, end=3.25),
]
piano.notes.extend(piano_notes)

# Bar 3: Drum fill
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Sax continues with a cry (3.0 - 4.5s)
# Motif: F (C4), Bb (E4), B (F#4), G (G4), then a rest and a high F# (F#5)
sax_notes = [
    pretty_midi.Note(velocity=70, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=72, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=74, pitch=64, start=3.5, end=3.75),
    pretty_midi.Note(velocity=76, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=70, pitch=60, start=4.25, end=4.5),
    pretty_midi.Note(velocity=72, pitch=62, start=4.25, end=4.5),
    pretty_midi.Note(velocity=74, pitch=64, start=4.25, end=4.5),
    pretty_midi.Note(velocity=78, pitch=76, start=4.5, end=4.75),
]
sax.notes.extend(sax_notes)

# Bass: Walking line continues
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=3.5, end=3.75),
    pretty_midi.Note(velocity=65, pitch=66, start=3.75, end=4.0),
    pretty_midi.Note(velocity=68, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=63, pitch=68, start=4.25, end=4.5),
    pretty_midi.Note(velocity=70, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=65, pitch=66, start=4.5, end=4.75),
    pretty_midi.Note(velocity=68, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=63, pitch=68, start=5.0, end=5.25),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # F7
    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=75, pitch=65, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),
    pretty_midi.Note(velocity=85, pitch=69, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),
    pretty_midi.Note(velocity=75, pitch=65, start=5.0, end=5.25),
]
piano.notes.extend(piano_notes)

# Bar 4: Drum fill
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Sax ends on a high note (4.5 - 6.0s)
sax_notes = [
    pretty_midi.Note(velocity=70, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=72, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=74, pitch=64, start=5.0, end=5.25),
    pretty_midi.Note(velocity=76, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=78, pitch=76, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=76, start=5.75, end=6.0),
]
sax.notes.extend(sax_notes)

# Bass: Walking line ends
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=4.75, end=5.0),
    pretty_midi.Note(velocity=65, pitch=66, start=5.0, end=5.25),
    pretty_midi.Note(velocity=68, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=63, pitch=68, start=5.5, end=5.75),
    pretty_midi.Note(velocity=70, pitch=65, start=5.75, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),  # F7
    pretty_midi.Note(velocity=85, pitch=69, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),
    pretty_midi.Note(velocity=75, pitch=65, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.25),
    pretty_midi.Note(velocity=85, pitch=69, start=6.0, end=6.25),
    pretty_midi.Note(velocity=80, pitch=60, start=6.0, end=6.25),
    pretty_midi.Note(velocity=75, pitch=65, start=6.0, end=6.25),
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
