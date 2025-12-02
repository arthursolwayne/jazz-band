
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

# Marcus: Walking line in Dm, chromatic approaches
# Dm7 = D F A C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Dm7: D F A C
# Comp on 2 and 4: 2nd beat (0.75s) and 4th beat (2.25s)
piano_notes = [
    # Dm7 on 2nd beat (0.75s)
    pretty_midi.Note(velocity=100, pitch=62, start=0.75, end=1.125),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=0.75, end=1.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=0.75, end=1.125),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=0.75, end=1.125),  # C
    # Dm7 on 4th beat (2.25s)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # C
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax - short motif, make it sing
# Dm7 - D F A C
# Motif: D -> Eb -> F -> D (half note, then rest)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=3.0),  # D (half note)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line continues
# A -> Bb -> B -> C -> D -> Eb -> F -> G -> A
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Dm7 on 2nd beat (3.75s)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # C
]
piano.notes.extend(piano_notes)

# Dante: repeat the motif on the 3rd bar
# D -> Eb -> F -> D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=4.5),  # D (half note)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line continues
# D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Dm7 on 2nd beat (5.25s)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # C
]
piano.notes.extend(piano_notes)

# Dante: repeat the motif on the 4th bar, but end it
# D -> Eb -> F -> D (half note, then rest)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=6.0),  # D (half note)
]
sax.notes.extend(sax_notes)

# Add the drum pattern for bar 3 and 4
# Bar 3: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),  # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
