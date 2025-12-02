
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),  # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),  # Snare on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax takes the melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=37, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=70, pitch=40, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=70, pitch=39, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=70, pitch=41, start=2.25, end=2.5),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.75),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),  # Hihat on 1 & 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.625, end=1.75),  # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=1.75, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),  # Hihat on 3 & 4
    pretty_midi.Note(velocity=90, pitch=36, start=2.0, end=2.375),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.125, end=2.25),  # Hihat on 3 & 4
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375),  # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=38, start=2.375, end=2.75),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax takes the melody again, with variations
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.625, end=3.75),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic passing tones
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=37, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=70, pitch=38, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=70, pitch=40, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=70, pitch=41, start=3.75, end=4.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),  # Hihat on 1 & 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.25),  # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=3.25, end=3.5),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),  # Hihat on 3 & 4
    pretty_midi.Note(velocity=90, pitch=36, start=3.5, end=3.875),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75),  # Hihat on 3 & 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875),  # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=38, start=3.875, end=4.25),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax ends the melody with a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.125),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.125, end=5.25),  # F
]
sax.notes.extend(sax_notes)

# Bass: Chromatic passing tone
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=37, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=70, pitch=38, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=70, pitch=40, start=5.0, end=5.25),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chord on 2
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625),  # Hihat on 1 & 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75),  # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=4.75, end=5.0),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),  # Hihat on 3 & 4
    pretty_midi.Note(velocity=90, pitch=36, start=5.0, end=5.375),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.25),  # Hihat on 3 & 4
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.375),  # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=38, start=5.375, end=5.75),  # Snare on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
