
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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
drums.notes.extend(drums_notes)

# Bar 2: Everyone in (1.5 - 3.0s)
# Bass: walking line in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (Bar 2, beat 2 and beat 4)
piano_notes = [
    # Bar 2, beat 2: D7
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # B
    # Bar 2, beat 4: G7
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: Motif starts (Bar 2, beat 1)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.125),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.125, end=2.5),  # F#
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=2.875, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drums_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: G7
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),
    # Bar 3, beat 4: C7
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Sax: Motif repeats with variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.375),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.375, end=4.5),  # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drums_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: C7
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),
    # Bar 4, beat 4: D7
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
