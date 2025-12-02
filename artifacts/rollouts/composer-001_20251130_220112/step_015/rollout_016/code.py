
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
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line in Dm - Dm7 chord: D, F, A, C
# Walking bass line: D, F, G, A, Bb, C, D, Eb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.125, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.375, end=2.5),   # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# Dm7: D, F, A, C
# Ab7: Ab, Cb, Eb, Gb
piano_notes = [
    # Bar 2 - 2nd beat: Dm7
    pretty_midi.Note(velocity=85, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=85, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=85, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=1.75, end=2.0),  # C
    # Bar 2 - 4th beat: Ab7
    pretty_midi.Note(velocity=85, pitch=68, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=85, pitch=60, start=2.25, end=2.5),  # Cb
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.5),  # Gb
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line in Dm - D, F, G, A, Bb, C, D, Eb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.125, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5),   # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.625, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.875, end=4.0),   # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# Dm7: D, F, A, C
# Ab7: Ab, Cb, Eb, Gb
piano_notes = [
    # Bar 3 - 2nd beat: Dm7
    pretty_midi.Note(velocity=85, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=85, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=85, pitch=69, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=3.25, end=3.5),  # C
    # Bar 3 - 4th beat: Ab7
    pretty_midi.Note(velocity=85, pitch=68, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=85, pitch=60, start=3.75, end=4.0),  # Cb
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.0),  # Gb
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line in Dm - D, F, G, A, Bb, C, D, Eb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0),   # A
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=5.125, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.375, end=5.5),   # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# Dm7: D, F, A, C
# Ab7: Ab, Cb, Eb, Gb
piano_notes = [
    # Bar 4 - 2nd beat: Dm7
    pretty_midi.Note(velocity=85, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=85, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=85, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=4.75, end=5.0),  # C
    # Bar 4 - 4th beat: Ab7
    pretty_midi.Note(velocity=85, pitch=68, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=85, pitch=60, start=5.25, end=5.5),  # Cb
    pretty_midi.Note(velocity=85, pitch=64, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.5),  # Gb
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
]
drums.notes.extend(drum_notes)

# Sax: Your motif. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D -> Eb -> F -> G (half note each, 3/4 of a bar) then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=2.25),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=3.0),  # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.5),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
