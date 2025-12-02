
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking in F, chromatic approach
bass_notes = [
    # Bar 2: F -> Gb -> G -> A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.0),  # A
    # Bar 3: Bb -> B -> C -> D
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.125, end=2.25),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=2.375, end=2.5),  # D
    # Bar 4: Eb -> E -> F -> G
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=2.875, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=71, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=1.625, end=1.75),  # C
    # Bar 3: Bb7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=69, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=2.125, end=2.25),  # Ab
    # Bar 4: Eb7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=2.75),  # C
]
piano.notes.extend(piano_notes)

# Sax: motif in F, short and singing
sax_notes = [
    # Bar 2: F -> G -> A -> F (motif)
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=72, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),
    # Bar 3: G -> A -> Bb -> G (variation)
    pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=74, start=2.125, end=2.25),
    pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=72, start=2.375, end=2.5),
    # Bar 4: A -> Bb -> C -> A (finish the motif)
    pretty_midi.Note(velocity=110, pitch=74, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=70, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=72, start=2.75, end=2.875),
    pretty_midi.Note(velocity=110, pitch=74, start=2.875, end=3.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
