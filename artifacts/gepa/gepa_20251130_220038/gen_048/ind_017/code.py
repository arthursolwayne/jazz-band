
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, Dm7 chord
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # D
    # Bar 2, beat 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # D
]
piano.notes.extend(piano_notes)

# Sax: Melody - Whisper at first, then a cry
# Bar 2: start the motif
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # Bb
    # Bar 3: Return and finish the motif
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # Bb
    # Bar 4: Add a cry, avoid repetition
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=60, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=60, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=60, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Bass (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Bar 3: Piano (3.0 - 4.5s)
piano_notes = [
    # Bar 3, beat 2 (3.75 - 4.125)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # D
    # Bar 3, beat 4 (4.875 - 5.25)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),   # D
]
piano.notes.extend(piano_notes)

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=38, start=6.0, end=6.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Bass (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Bar 4: Piano (4.5 - 6.0s)
piano_notes = [
    # Bar 4, beat 2 (5.25 - 5.625)
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # D
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
midi.write("dante_intro.mid")
