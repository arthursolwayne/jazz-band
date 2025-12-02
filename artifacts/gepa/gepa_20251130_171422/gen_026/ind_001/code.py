
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=45, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=2.75, end=3.0),  # F#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),  # D

    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5),  # D
]
piano.notes.extend(piano_notes)

# Sax: Melody - sparse, expressive, one motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=2.75, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=44, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=90, pitch=45, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=4.25, end=4.5),  # F#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),  # D

    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Melody - sparse, expressive, one motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # A
]
sax.notes.extend(sax_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=90, pitch=45, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=45, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=5.75, end=6.0),  # F#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),  # D

    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5),  # D
]
piano.notes.extend(piano_notes)

# Sax: Melody - sparse, expressive, one motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
