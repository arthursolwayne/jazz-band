
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
    # Hihat on every eighth
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

# Marcus: Walking bass line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # Bb
]
bass.notes.extend(bass_notes)

# Diane: Comping on 2 and 4 with 7th chords in F
piano_notes = [
    # Bar 2, beat 2: F7
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # D
    # Bar 2, beat 4: F7
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Dante: Saxophone melody
# One short motif, sing it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=2.125, end=2.25), # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Diane: Comping on 2 and 4 with 7th chords in F
piano_notes = [
    # Bar 3, beat 2: F7
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # D
    # Bar 3, beat 4: F7
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),  # D
]
piano.notes.extend(piano_notes)

# Dante: Saxophone melody (continuation and resolution)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: Comping on 2 and 4 with 7th chords in F
piano_notes = [
    # Bar 4, beat 2: F7
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # D
    # Bar 4, beat 4: F7
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Dante: Saxophone melody (closing)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=77, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=77, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
