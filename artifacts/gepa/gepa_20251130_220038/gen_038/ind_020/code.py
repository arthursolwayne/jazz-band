
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # D
    # Bar 3: A7
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0),  # C#
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=3.0),  # G
]
piano.notes.extend(piano_notes)

# Sax: Whisper then cry - minimal notes with rests
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 3: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # D
    # Bar 4: G7
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=78, start=3.75, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.5),  # F
]
piano.notes.extend(piano_notes)

# Sax: Whisper then cry - minimal notes with rests
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 4: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),  # D
    # Bar 4: A7
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=6.0),  # C#
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=6.0),  # E
    pretty_midi.Note(velocity=100, pitch=78, start=5.25, end=6.0),  # G
]
piano.notes.extend(piano_notes)

# Sax: Whisper then cry - minimal notes with rests
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
