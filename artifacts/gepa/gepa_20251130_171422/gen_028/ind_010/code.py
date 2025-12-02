
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 3, snare on 2, hihat on every eighth, but with subtle dynamic variation
drum_notes = [
    pretty_midi.Note(velocity=70, pitch=36, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=55, pitch=42, start=0.125, end=1.5),
    pretty_midi.Note(velocity=50, pitch=42, start=0.25, end=1.5),
    pretty_midi.Note(velocity=55, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=0.5, end=1.5),
    pretty_midi.Note(velocity=55, pitch=42, start=0.625, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=50, pitch=42, start=0.875, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody - sparse, expressive, with rests and dynamic variation
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=70, pitch=65, start=2.0, end=2.25),
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=75, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0)
]
sax.notes.extend(sax_notes)

# Bass line - chromatic, walking, with subtle dynamic shifts
bass_notes = [
    pretty_midi.Note(velocity=60, pitch=55, start=1.5, end=1.75),
    pretty_midi.Note(velocity=65, pitch=56, start=1.75, end=2.0),
    pretty_midi.Note(velocity=62, pitch=57, start=2.0, end=2.25),
    pretty_midi.Note(velocity=63, pitch=58, start=2.25, end=2.5),
    pretty_midi.Note(velocity=64, pitch=59, start=2.5, end=2.75),
    pretty_midi.Note(velocity=65, pitch=60, start=2.75, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4, with subtle counterpoint
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=75, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=70, pitch=70, start=1.5, end=1.75),
    pretty_midi.Note(velocity=65, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=75, pitch=70, start=2.25, end=2.5),
    pretty_midi.Note(velocity=70, pitch=72, start=2.25, end=2.5),
    pretty_midi.Note(velocity=65, pitch=64, start=2.25, end=2.5)
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody continues, building tension
sax_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=85, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=75, pitch=65, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=70, pitch=69, start=4.0, end=4.25),
    pretty_midi.Note(velocity=75, pitch=67, start=4.25, end=4.5)
]
sax.notes.extend(sax_notes)

# Bass line - chromatic, walking, with tension
bass_notes = [
    pretty_midi.Note(velocity=60, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=65, pitch=61, start=3.25, end=3.5),
    pretty_midi.Note(velocity=62, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=63, pitch=63, start=3.75, end=4.0),
    pretty_midi.Note(velocity=64, pitch=64, start=4.0, end=4.25),
    pretty_midi.Note(velocity=65, pitch=65, start=4.25, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, with more movement
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=75, pitch=70, start=3.0, end=3.25),
    pretty_midi.Note(velocity=70, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=85, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=70, start=3.5, end=3.75),
    pretty_midi.Note(velocity=75, pitch=72, start=3.5, end=3.75),
    pretty_midi.Note(velocity=70, pitch=64, start=3.5, end=3.75)
]
piano.notes.extend(piano_notes)

# Drums - more energy, kicks on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.125),
    pretty_midi.Note(velocity=95, pitch=38, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.5),
    pretty_midi.Note(velocity=75, pitch=42, start=3.125, end=3.5),
    pretty_midi.Note(velocity=70, pitch=42, start=3.25, end=3.5),
    pretty_midi.Note(velocity=75, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.5),
    pretty_midi.Note(velocity=90, pitch=36, start=3.375, end=3.5),
    pretty_midi.Note(velocity=95, pitch=38, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=4.0),
    pretty_midi.Note(velocity=75, pitch=42, start=3.625, end=4.0),
    pretty_midi.Note(velocity=70, pitch=42, start=3.75, end=4.0),
    pretty_midi.Note(velocity=75, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.0),
    pretty_midi.Note(velocity=90, pitch=36, start=3.875, end=4.0),
    pretty_midi.Note(velocity=95, pitch=38, start=4.0, end=4.125)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody resolves partially, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=85, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=75, pitch=65, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=70, pitch=69, start=5.5, end=5.75),
    pretty_midi.Note(velocity=75, pitch=67, start=5.75, end=6.0)
]
sax.notes.extend(sax_notes)

# Bass line - resolves slightly, but with tension
bass_notes = [
    pretty_midi.Note(velocity=60, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=65, pitch=66, start=4.75, end=5.0),
    pretty_midi.Note(velocity=62, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=63, pitch=68, start=5.25, end=5.5),
    pretty_midi.Note(velocity=64, pitch=69, start=5.5, end=5.75),
    pretty_midi.Note(velocity=65, pitch=70, start=5.75, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, with a hint of resolution
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=75, pitch=70, start=4.5, end=4.75),
    pretty_midi.Note(velocity=70, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=85, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=70, start=5.0, end=5.25),
    pretty_midi.Note(velocity=75, pitch=72, start=5.0, end=5.25),
    pretty_midi.Note(velocity=70, pitch=64, start=5.0, end=5.25)
]
piano.notes.extend(piano_notes)

# Drums - final push, energy at peak
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.625),
    pretty_midi.Note(velocity=105, pitch=38, start=4.625, end=4.75),
    pretty_midi.Note(velocity=85, pitch=42, start=4.5, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=5.0),
    pretty_midi.Note(velocity=75, pitch=42, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=85, pitch=42, start=5.0, end=5.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.0),
    pretty_midi.Note(velocity=105, pitch=38, start=5.0, end=5.125),
    pretty_midi.Note(velocity=85, pitch=42, start=5.0, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.5),
    pretty_midi.Note(velocity=75, pitch=42, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=85, pitch=42, start=5.5, end=5.5),
    pretty_midi.Note(velocity=100, pitch=36, start=5.375, end=5.5),
    pretty_midi.Note(velocity=105, pitch=38, start=5.5, end=5.625)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
