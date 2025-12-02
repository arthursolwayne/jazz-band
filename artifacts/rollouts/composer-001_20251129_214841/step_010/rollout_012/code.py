
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
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

# Bar 2: Everyone in. Sax starts the motif
# C7 - E7 - Bb7 - D7 (descending chromatic line in 16th notes)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=85, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=83, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=82, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=84, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=85, start=2.125, end=2.25),
    pretty_midi.Note(velocity=100, pitch=83, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=82, start=2.375, end=2.5),
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4, 7th chords
piano_notes = [
    # Bar 2 (1.5 - 2.0s): C7 (C E G B)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0),
    # Bar 3 (2.5 - 3.0s): D7 (D F# A C)
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=66, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
]
drums.notes.extend(drum_notes)

# Bar 4: Sax returns, finishes the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=85, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=83, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=82, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=84, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=85, start=3.625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=83, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=82, start=3.875, end=4.0),
]
sax.notes.extend(sax_notes)

# Bass: Walking line continues
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4
piano_notes = [
    # Bar 4 (3.5 - 4.0s): C7 (C E G B)
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=4.0),
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=4.0),
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=4.0),
]
piano.notes.extend(piano_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
