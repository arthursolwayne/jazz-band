
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F
bass_notes = [
    # F (1st beat)
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),
    # Bb (2nd beat)
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    # D (3rd beat)
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),
    # F (4th beat)
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on 2nd beat (1.875 - 2.25)
    pretty_midi.Note(velocity=95, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=85, pitch=69, start=1.875, end=2.25),
    # F7 on 4th beat (2.625 - 3.0)
    pretty_midi.Note(velocity=95, pitch=70, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=85, pitch=69, start=2.625, end=3.0)
]
piano.notes.extend(piano_notes)

# Sax: Melody in F
sax_notes = [
    # First note: F (1.5 - 1.875)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),
    # Second note: G (1.875 - 2.25)
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),
    # Third note: A (2.25 - 2.625)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),
    # Fourth note: Bb (2.625 - 3.0)
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    # F (3.0)
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),
    # Bb (3.375)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    # D (3.75)
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),
    # F (4.125)
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on 2nd beat (3.375 - 3.75)
    pretty_midi.Note(velocity=95, pitch=70, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=85, pitch=69, start=3.375, end=3.75),
    # F7 on 4th beat (4.125 - 4.5)
    pretty_midi.Note(velocity=95, pitch=70, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=85, pitch=69, start=4.125, end=4.5)
]
piano.notes.extend(piano_notes)

# Sax: Continue the melody
sax_notes = [
    # Fifth note: C (3.0 - 3.375)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    # Sixth note: F (3.375 - 3.75)
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),
    # Seventh note: G (3.75 - 4.125)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),
    # Eighth note: A (4.125 - 4.5)
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    # F (4.5)
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),
    # Bb (4.875)
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    # D (5.25)
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),
    # F (5.625)
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on 2nd beat (4.875 - 5.25)
    pretty_midi.Note(velocity=95, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=85, pitch=69, start=4.875, end=5.25),
    # F7 on 4th beat (5.625 - 6.0)
    pretty_midi.Note(velocity=95, pitch=70, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=85, pitch=69, start=5.625, end=6.0)
]
piano.notes.extend(piano_notes)

# Sax: Final note
sax_notes = [
    # Ninth note: F (4.5 - 4.875)
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),
    # Tenth note: G (4.875 - 5.25)
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),
    # Eleventh note: A (5.25 - 5.625)
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),
    # Twelfth note: F (5.625 - 6.0)
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
