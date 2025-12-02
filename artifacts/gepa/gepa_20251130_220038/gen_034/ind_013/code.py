
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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
# Sax melody: Dm7 -> G7 -> Cm7 -> F7
# Motif: D (E) -> F -> G -> A -> G -> F -> E -> D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.375, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),  # D
]
sax.notes.extend(sax_notes)

# Bass line: Dm7 -> G7 -> Cm7 -> F7
# Walking line with chromatic approaches
bass_notes = [
    # Dm7: D -> C -> B -> C -> D
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=60, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=59, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.125),
    # G7: G -> F -> E -> F -> G
    pretty_midi.Note(velocity=80, pitch=67, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=64, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=2.75),
    # Cm7: C -> B -> A -> B -> C
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=59, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=59, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.375),
    # F7: F -> E -> D -> E -> F
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=64, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=62, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=65, start=3.875, end=4.0)
]
bass.notes.extend(bass_notes)

# Piano comping on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (2nd beat)
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    # Bar 3: G7 (2nd beat)
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=74, start=2.75, end=3.0),
    # Bar 4: Cm7 (2nd beat)
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    # Bar 4: F7 (4th beat)
    pretty_midi.Note(velocity=90, pitch=65, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=69, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=72, start=3.875, end=4.0)
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody: Dm7 -> G7 -> Cm7 -> F7
# Motif: D (E) -> F -> G -> A -> G -> F -> E -> D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=64, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125),
]
sax.notes.extend(sax_notes)

# Bass line: Dm7 -> G7 -> Cm7 -> F7
# Walking line with chromatic approaches
bass_notes = [
    # Dm7: D -> C -> B -> C -> D
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=60, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=59, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.625),
    # G7: G -> F -> E -> F -> G
    pretty_midi.Note(velocity=80, pitch=67, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=64, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=65, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.25),
    # Cm7: C -> B -> A -> B -> C
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=59, start=4.375, end=4.5),
    pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=59, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=4.875),
    # F7: F -> E -> D -> E -> F
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=62, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=65, start=5.375, end=5.5)
]
bass.notes.extend(bass_notes)

# Piano comping on 2 and 4
piano_notes = [
    # Bar 3: Dm7 (2nd beat)
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    # Bar 4: G7 (2nd beat)
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=74, start=4.25, end=4.5),
    # Bar 4: Cm7 (4th beat)
    pretty_midi.Note(velocity=90, pitch=60, start=4.375, end=4.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.375, end=4.5),
    pretty_midi.Note(velocity=90, pitch=64, start=4.375, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.375, end=4.5),
    # Bar 4: F7 (4th beat)
    pretty_midi.Note(velocity=90, pitch=65, start=4.375, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.375, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=4.375, end=4.5),
    pretty_midi.Note(velocity=90, pitch=72, start=4.375, end=4.5)
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody: Dm7 -> G7 -> Cm7 -> F7
# Motif: D (E) -> F -> G -> A -> G -> F -> E -> D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=67, start=5.125, end=5.25),
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=64, start=5.375, end=5.5),
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.625),
]
sax.notes.extend(sax_notes)

# Bass line: Dm7 -> G7 -> Cm7 -> F7
# Walking line with chromatic approaches
bass_notes = [
    # Dm7: D -> C -> B -> C -> D
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=60, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=59, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.125),
    # G7: G -> F -> E -> F -> G
    pretty_midi.Note(velocity=80, pitch=67, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=64, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=65, start=5.5, end=5.625),
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=5.75),
    # Cm7: C -> B -> A -> B -> C
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=5.875),
    pretty_midi.Note(velocity=80, pitch=59, start=5.875, end=6.0),
    pretty_midi.Note(velocity=80, pitch=58, start=6.0, end=6.125),
    pretty_midi.Note(velocity=80, pitch=59, start=6.125, end=6.25),
    pretty_midi.Note(velocity=80, pitch=60, start=6.25, end=6.375),
    # F7: F -> E -> D -> E -> F
    pretty_midi.Note(velocity=80, pitch=65, start=6.375, end=6.5),
    pretty_midi.Note(velocity=80, pitch=64, start=6.5, end=6.625),
    pretty_midi.Note(velocity=80, pitch=62, start=6.625, end=6.75),
    pretty_midi.Note(velocity=80, pitch=64, start=6.75, end=6.875),
    pretty_midi.Note(velocity=80, pitch=65, start=6.875, end=7.0)
]
bass.notes.extend(bass_notes)

# Piano comping on 2 and 4
piano_notes = [
    # Bar 4: Dm7 (2nd beat)
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    # Bar 4: G7 (2nd beat)
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=74, start=5.75, end=6.0),
    # Bar 4: Cm7 (4th beat)
    pretty_midi.Note(velocity=90, pitch=60, start=5.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=62, start=5.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.875, end=6.0),
    # Bar 4: F7 (4th beat)
    pretty_midi.Note(velocity=90, pitch=65, start=5.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=72, start=5.875, end=6.0)
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
