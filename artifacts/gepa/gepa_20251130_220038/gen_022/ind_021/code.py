
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
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
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),   # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - 2nd beat (Fm7)
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # F
    # Bar 2 - 4th beat (Fm7)
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=37, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),   # F
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax motif (start on beat 1)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=61, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=59, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=110, pitch=61, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=110, pitch=57, start=2.625, end=3.0),   # C
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),   # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 - 2nd beat (Fm7)
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # F
    # Bar 3 - 4th beat (Fm7)
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=37, start=4.125, end=4.5),   # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),   # F
]
piano.notes.extend(piano_notes)

# Dante: Sax continues motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=61, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=110, pitch=59, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=61, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=110, pitch=57, start=4.125, end=4.5),   # C
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 - 2nd beat (Fm7)
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # F
    # Bar 4 - 4th beat (Fm7)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=100, pitch=37, start=5.625, end=6.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),   # F
]
piano.notes.extend(piano_notes)

# Dante: Sax completes the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=61, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=110, pitch=59, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=61, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=110, pitch=57, start=5.625, end=6.0),   # C
]
sax.notes.extend(sax_notes)

# Add the drum pattern for bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.375),
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

midi.write("dante_intro.mid")
