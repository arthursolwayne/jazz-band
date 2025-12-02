
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # D
]
bass.notes.extend(bass_notes)

# Diane: Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, 2nd beat: D7
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.0),   # G
    pretty_midi.Note(velocity=95, pitch=69, start=1.875, end=2.0),   # B
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.0),   # D
    # Bar 2, 4th beat: F7
    pretty_midi.Note(velocity=95, pitch=65, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=95, pitch=73, start=2.625, end=2.75),  # D
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax motif
sax_notes = [
    # Bar 2, beat 1: D (start at 1.5s)
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.625),
    # Bar 2, beat 2: F (start at 1.875s)
    pretty_midi.Note(velocity=105, pitch=65, start=1.875, end=2.0),
    # Bar 3, beat 1: G (start at 3.0s)
    pretty_midi.Note(velocity=105, pitch=67, start=3.0, end=3.125),
    # Bar 3, beat 2: B (start at 3.375s)
    pretty_midi.Note(velocity=105, pitch=69, start=3.375, end=3.5),
    # Bar 4, beat 1: D (start at 4.5s)
    pretty_midi.Note(velocity=105, pitch=62, start=4.5, end=4.625),
    # Bar 4, beat 2: F (start at 4.875s)
    pretty_midi.Note(velocity=105, pitch=65, start=4.875, end=5.0),
    # Bar 4, beat 3: G (start at 5.25s)
    pretty_midi.Note(velocity=105, pitch=67, start=5.25, end=5.375),
    # Bar 4, beat 4: B (start at 5.625s)
    pretty_midi.Note(velocity=105, pitch=69, start=5.625, end=5.75),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D
]
bass.notes.extend(bass_notes)

# Diane: Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 3, 2nd beat: D7
    pretty_midi.Note(velocity=95, pitch=62, start=3.375, end=3.5),   # D
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.5),   # G
    pretty_midi.Note(velocity=95, pitch=69, start=3.375, end=3.5),   # B
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.5),   # D
    # Bar 3, 4th beat: F7
    pretty_midi.Note(velocity=95, pitch=65, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=4.125, end=4.25),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=4.125, end=4.25),  # C
    pretty_midi.Note(velocity=95, pitch=73, start=4.125, end=4.25),  # D
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax motif
sax_notes = [
    # Bar 3, beat 1: D (start at 3.0s)
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.125),
    # Bar 3, beat 2: F (start at 3.375s)
    pretty_midi.Note(velocity=105, pitch=65, start=3.375, end=3.5),
    # Bar 4, beat 1: G (start at 4.5s)
    pretty_midi.Note(velocity=105, pitch=67, start=4.5, end=4.625),
    # Bar 4, beat 2: B (start at 4.875s)
    pretty_midi.Note(velocity=105, pitch=69, start=4.875, end=5.0),
    # Bar 4, beat 3: D (start at 5.25s)
    pretty_midi.Note(velocity=105, pitch=62, start=5.25, end=5.375),
    # Bar 4, beat 4: F (start at 5.625s)
    pretty_midi.Note(velocity=105, pitch=65, start=5.625, end=5.75),
    # Bar 4, beat 3: G (start at 5.25s)
    pretty_midi.Note(velocity=105, pitch=67, start=5.25, end=5.375),
    # Bar 4, beat 4: B (start at 5.625s)
    pretty_midi.Note(velocity=105, pitch=69, start=5.625, end=5.75),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Diane: Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 4, 2nd beat: D7
    pretty_midi.Note(velocity=95, pitch=62, start=4.875, end=5.0),   # D
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.0),   # G
    pretty_midi.Note(velocity=95, pitch=69, start=4.875, end=5.0),   # B
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.0),   # D
    # Bar 4, 4th beat: F7
    pretty_midi.Note(velocity=95, pitch=65, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=5.625, end=5.75),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=5.625, end=5.75),  # C
    pretty_midi.Note(velocity=95, pitch=73, start=5.625, end=5.75),  # D
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax motif
sax_notes = [
    # Bar 4, beat 1: D (start at 4.5s)
    pretty_midi.Note(velocity=105, pitch=62, start=4.5, end=4.625),
    # Bar 4, beat 2: F (start at 4.875s)
    pretty_midi.Note(velocity=105, pitch=65, start=4.875, end=5.0),
    # Bar 4, beat 3: G (start at 5.25s)
    pretty_midi.Note(velocity=105, pitch=67, start=5.25, end=5.375),
    # Bar 4, beat 4: B (start at 5.625s)
    pretty_midi.Note(velocity=105, pitch=69, start=5.625, end=5.75),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
