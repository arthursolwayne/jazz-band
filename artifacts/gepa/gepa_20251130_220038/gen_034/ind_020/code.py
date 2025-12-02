
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 3
    pretty_midi.Note(velocity=95, pitch=38, start=1.125, end=1.5),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D7
    pretty_midi.Note(velocity=75, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=75, pitch=65, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=75, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=2.999), # D7
    pretty_midi.Note(velocity=75, pitch=67, start=2.625, end=2.999), # A
    pretty_midi.Note(velocity=75, pitch=65, start=2.625, end=2.999), # G
    pretty_midi.Note(velocity=75, pitch=60, start=2.625, end=2.999), # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Hihat on 3
    pretty_midi.Note(velocity=95, pitch=38, start=2.625, end=3.0),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax: Melody starts in Bar 2, with a whisper then a cry
sax_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=85, pitch=65, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=85, pitch=62, start=2.0, end=2.25),   # D
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.5),   # G
    pretty_midi.Note(velocity=95, pitch=65, start=2.5, end=2.75),   # F (cry)
    pretty_midi.Note(velocity=95, pitch=62, start=2.75, end=3.0),   # D (fall)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D7
    pretty_midi.Note(velocity=75, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=75, pitch=65, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=75, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D7
    pretty_midi.Note(velocity=75, pitch=67, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=75, pitch=65, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=75, pitch=60, start=4.125, end=4.5),  # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=95, pitch=38, start=4.125, end=4.5),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax: Melody continues
sax_notes = [
    pretty_midi.Note(velocity=85, pitch=60, start=3.0, end=3.25),   # C
    pretty_midi.Note(velocity=85, pitch=62, start=3.25, end=3.5),    # D
    pretty_midi.Note(velocity=85, pitch=64, start=3.5, end=3.75),    # F
    pretty_midi.Note(velocity=85, pitch=62, start=3.75, end=4.0),    # D
    pretty_midi.Note(velocity=95, pitch=64, start=4.0, end=4.25),    # F (cry)
    pretty_midi.Note(velocity=95, pitch=60, start=4.25, end=4.5),    # C (fall)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D7
    pretty_midi.Note(velocity=75, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=75, pitch=65, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=75, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),  # D7
    pretty_midi.Note(velocity=75, pitch=67, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=75, pitch=65, start=5.625, end=6.0),  # G
    pretty_midi.Note(velocity=75, pitch=60, start=5.625, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=95, pitch=38, start=5.625, end=6.0),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax: Melody ends with a whisper
sax_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=85, pitch=64, start=4.75, end=5.0),    # F
    pretty_midi.Note(velocity=85, pitch=62, start=5.0, end=5.25),    # D
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.5),    # G
    pretty_midi.Note(velocity=95, pitch=64, start=5.5, end=5.75),    # F (cry)
    pretty_midi.Note(velocity=95, pitch=62, start=5.75, end=6.0),    # D (fall)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
