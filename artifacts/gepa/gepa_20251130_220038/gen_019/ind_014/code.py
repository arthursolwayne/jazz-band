
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
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
# Bass line: walking, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2 (start=1.875)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # B
    # Bar 3: F7 on beat 2 (start=3.375)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # B
    # Bar 4: F7 on beat 2 (start=4.875)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # B
]
piano.notes.extend(piano_notes)

# Sax: Melody - short motif, start on bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 4: Bass and Piano continue
# Bass line: walking, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=54, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=58, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2 (start=4.875)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # B
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
