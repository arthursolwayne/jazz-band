
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # Hi-hat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hi-hat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),   # Hi-hat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hi-hat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # A7
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # E7
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # C7
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A7
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # Eb7
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # D7
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # A7
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # A7
]
piano.notes.extend(piano_notes)

# Sax (Dante)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # A7
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # E7
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # C7
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # A7
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # Eb7
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # D7
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # A7
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # A7
]
piano.notes.extend(piano_notes)

# Sax (Dante)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums (Little Ray)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0),    # Hi-hat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0),  # Hi-hat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.375),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.5),    # Hi-hat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.375, end=5.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.375, end=5.5),  # Hi-hat on 4
]
drums.notes.extend(drum_notes)

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # A7
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # E7
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # C7
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # A7
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # Eb7
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # D7
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # A7
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # A7
]
piano.notes.extend(piano_notes)

# Sax (Dante)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
