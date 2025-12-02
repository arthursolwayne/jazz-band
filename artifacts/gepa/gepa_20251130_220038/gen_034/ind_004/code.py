
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),      # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),   # Kick on 3
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Saxophone
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bass (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=2.0, end=2.25),   # D
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.5),   # C
    pretty_midi.Note(velocity=80, pitch=46, start=2.5, end=2.75),   # Eb
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),   # Bb7
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.75),   # G7
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.75),   # F7
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.75),   # Eb7
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),   # Bb7
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.5),   # G7
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.5),   # F7
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.5),   # Eb7
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # A
]
sax.notes.extend(sax_notes)

# Bass (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=80, pitch=43, start=3.25, end=3.5),   # C
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.75),   # Bb
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.25),   # Bb
    pretty_midi.Note(velocity=80, pitch=40, start=4.25, end=4.5),   # Ab
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.25),   # F7
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.25),   # Eb7
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.25),   # D7
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25),   # C7
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.0),   # F7
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.0),   # Eb7
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.0),   # D7
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.0),   # C7
]
piano.notes.extend(piano_notes)

# Drums (Bar 3)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),      # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Saxophone
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=58, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Bass (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.75),   # Ab
    pretty_midi.Note(velocity=80, pitch=39, start=4.75, end=5.0),   # G
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.25),   # Bb
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.5),   # Ab
    pretty_midi.Note(velocity=80, pitch=39, start=5.5, end=5.75),   # G
    pretty_midi.Note(velocity=80, pitch=40, start=5.75, end=6.0),   # Ab
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.75),   # Eb7
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.75),   # D7
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.75),   # C7
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.75),   # Bb7
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.5),   # Eb7
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.5),   # D7
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.5),   # C7
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.5),   # Bb7
]
piano.notes.extend(piano_notes)

# Drums (Bar 4)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),      # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),   # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
