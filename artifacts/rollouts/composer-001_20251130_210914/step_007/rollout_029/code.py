
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line by Marcus (walking line in Fm, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano by Diane (7th chords on 2 and 4, comping)
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # D
    # Bar 3: Bb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),   # G
]
piano.notes.extend(piano_notes)

# Sax by Dante: short motif, 2 notes, then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # D (Fm7)
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),   # Bb (Fm7)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line by Marcus (walking line in Fm, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # F
]
bass.notes.extend(bass_notes)

# Piano by Diane (7th chords on 2 and 4, comping)
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),  # D
    # Bar 4: Bb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),   # G
]
piano.notes.extend(piano_notes)

# Sax by Dante: return to finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # G (Fm7)
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),   # D (Fm7)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),   # Bb (Fm7)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),   # D (Fm7)
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.25),   # G (Fm7)
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),   # F (Fm7)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.75),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=100, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=100, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

# Bass line by Marcus (walking line in Fm, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano by Diane (7th chords on 2 and 4, comping)
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax by Dante: leave it open
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # D (Fm7)
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),   # G (Fm7)
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),   # C (Fm7)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
