
import pretty_midi

midi = pretty_midi.PrettyMIDI(tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet
# Sax melody starts
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # E
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.25),  # D#
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=90, pitch=50, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=2.75, end=3.0),  # C
]
bass.notes.extend(bass_notes)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),  # D
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),  # D
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet
# Sax continues melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=2.75, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 3 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=3.0),  # F
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet
# Sax concludes melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # G
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=3.25, end=3.5),  # A
]
bass.notes.extend(bass_notes)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 4 (3.0 - 3.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # F
]
piano.notes.extend(piano_notes)

# Add drum notes for bar 3 and 4
# Bar 3 (1.5 - 3.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
]
drums.notes.extend(drum_notes)

# Bar 4 (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
