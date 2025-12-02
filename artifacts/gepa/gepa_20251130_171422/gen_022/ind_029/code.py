
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
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: chromatic approach, searching and melodic
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=85, pitch=64, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=85, pitch=62, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.125, end=2.25),  # E
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=2.375, end=2.5),   # F#
    pretty_midi.Note(velocity=85, pitch=64, start=2.5, end=2.625),   # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=85, pitch=63, start=2.75, end=2.875),  # E
    pretty_midi.Note(velocity=80, pitch=64, start=2.875, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, with emotion and space
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.75),  # F7 (64,67,69,71)
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=1.75),
    pretty_midi.Note(velocity=85, pitch=64, start=2.5, end=2.75),  # F7 again
    pretty_midi.Note(velocity=85, pitch=67, start=2.5, end=2.75),
    pretty_midi.Note(velocity=85, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=85, pitch=71, start=2.5, end=2.75),
]
piano.notes.extend(piano_notes)

# Sax: motif – concise, emotional, haunting
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=36, start=4.125, end=4.5),   # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bass line: chromatic approach again, but with a slight twist
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=3.125, end=3.25),  # F#
    pretty_midi.Note(velocity=85, pitch=64, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.5),   # E
    pretty_midi.Note(velocity=85, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.625, end=3.75),  # E
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=3.875, end=4.0),   # F#
    pretty_midi.Note(velocity=85, pitch=64, start=4.0, end=4.125),   # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.25),  # D
    pretty_midi.Note(velocity=85, pitch=63, start=4.25, end=4.375),  # E
    pretty_midi.Note(velocity=85, pitch=64, start=4.375, end=4.5),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords again, but with a slight shift in rhythm
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.25),  # F7
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=85, pitch=64, start=4.0, end=4.25),  # F7
    pretty_midi.Note(velocity=85, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=85, pitch=69, start=4.0, end=4.25),
    pretty_midi.Note(velocity=85, pitch=71, start=4.0, end=4.25),
]
piano.notes.extend(piano_notes)

# Sax: continuation of motif, with space and tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.25, end=4.5),  # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=36, start=5.625, end=6.0),   # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=38, start=6.0, end=6.375),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bass line: resolves with a chromatic descent
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=4.625, end=4.75),  # E
    pretty_midi.Note(velocity=85, pitch=62, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=4.875, end=5.0),   # C
    pretty_midi.Note(velocity=85, pitch=64, start=5.0, end=5.125),   # F
    pretty_midi.Note(velocity=80, pitch=63, start=5.125, end=5.25),  # E
    pretty_midi.Note(velocity=85, pitch=62, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=5.375, end=5.5),   # C
    pretty_midi.Note(velocity=85, pitch=64, start=5.5, end=5.625),   # F
    pretty_midi.Note(velocity=80, pitch=63, start=5.625, end=5.75),  # E
    pretty_midi.Note(velocity=85, pitch=62, start=5.75, end=5.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=5.875, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: final 7th chord with a slight delay on the last note
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=4.75),  # F7
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=85, pitch=71, start=4.5, end=5.0),   # 71 held longer
]
piano.notes.extend(piano_notes)

# Sax: final note — leave it lingering, unresolved
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=6.0),  # G, held for the full bar
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
