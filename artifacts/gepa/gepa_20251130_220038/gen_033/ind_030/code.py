
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approach to D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.625),  # C#
    pretty_midi.Note(velocity=80, pitch=67, start=1.625, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=1.875),  # D#
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.125),   # D#
    pretty_midi.Note(velocity=80, pitch=67, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.375),  # C#
    pretty_midi.Note(velocity=80, pitch=64, start=2.375, end=2.5),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625),  # F#
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375),  # F#
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.375),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.375),  # C
]
piano.notes.extend(piano_notes)

# Sax: Melody - a whisper at first, then a cry
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # B
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=2.0),   # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.25),   # C
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),   # D#
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75),   # D
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0),   # B
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approach to D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=3.125, end=3.25),  # D#
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.5),   # F
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.625),   # E
    pretty_midi.Note(velocity=80, pitch=69, start=3.625, end=3.75),  # D#
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=3.875, end=4.0),   # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.125),  # F#
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.875),  # F#
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=3.875),  # C
]
piano.notes.extend(piano_notes)

# Sax: Melody continues, builds
sax_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),   # D#
    pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=80, pitch=74, start=3.5, end=3.75),   # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # D#
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approach to D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.625),  # C#
    pretty_midi.Note(velocity=80, pitch=67, start=4.625, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=4.875),  # D#
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.0),   # E
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.125),   # D#
    pretty_midi.Note(velocity=80, pitch=67, start=5.125, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.375),  # C#
    pretty_midi.Note(velocity=80, pitch=64, start=5.375, end=5.5),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.625),  # F#
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.375),  # F#
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.375),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.375),  # C
]
piano.notes.extend(piano_notes)

# Sax: Melody ends with a cry
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),   # D#
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),   # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.5, end=5.75),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),   # D
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
