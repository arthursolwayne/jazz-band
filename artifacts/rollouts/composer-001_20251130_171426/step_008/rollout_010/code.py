
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet starts (1.5 - 3.0s)

# Sax: Motif starts here - Dm7 chord tones with a chromatic approach
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=2.75, end=3.0)   # C#
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),   # C
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25),   # F
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5),   # E
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),   # D
    pretty_midi.Note(velocity=80, pitch=48, start=2.75, end=3.0)    # Bb
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),   # D7
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0),   # D7
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=72, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0)
]
piano.notes.extend(piano_notes)

# Bar 3: Drums continue (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 3: Sax continues the motif (3.0 - 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5)   # D
]
sax.notes.extend(sax_notes)

# Bar 3: Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=80, pitch=50, start=3.25, end=3.5),   # D
    pretty_midi.Note(velocity=80, pitch=52, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=4.0, end=4.25),   # D
    pretty_midi.Note(velocity=80, pitch=47, start=4.25, end=4.5)    # Ab
]
bass.notes.extend(bass_notes)

# Bar 3: Piano continues comping
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=57, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),   # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5)
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 4: Sax ends the motif with a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0)   # C
]
sax.notes.extend(sax_notes)

# Bar 4: Bass finishes walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=80, pitch=48, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.25),   # D
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.5),   # C
    pretty_midi.Note(velocity=80, pitch=50, start=5.5, end=5.75),   # D
    pretty_midi.Note(velocity=80, pitch=52, start=5.75, end=6.0)    # F
]
bass.notes.extend(bass_notes)

# Bar 4: Piano resolves with a final D7 chord
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=6.0),   # D7
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=6.0),
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=6.0)
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
