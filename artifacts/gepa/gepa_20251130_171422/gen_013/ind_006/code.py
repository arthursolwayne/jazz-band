
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
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # Dm7 chord: D, F, A, C
    # Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7: D, F, A, C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # C
    # Dm7 again on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: Motif in Dm, one short phrase, leaves it hanging
sax_notes = [
    # Dm motif: D, F, G, A -> D
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75), # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875), # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0),  # A
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line continues
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # C
    # Dm7 again on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # C
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.875, end=4.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line continues
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=5.625, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # C
    # Dm7 again on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.125, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.375),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.375, end=5.5),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=5.875),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.875, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
