
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # C
    # F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0), # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0), # C
]
piano.notes.extend(piano_notes)

# Dante: Sax melody
sax_notes = [
    # First note: F (70)
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.875),
    # Second note: Bb (67)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),
    # Third note: D (62)
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75), # C
    # F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125), # C
]
piano.notes.extend(piano_notes)

# Little Ray: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.6875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25), # C
    # F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625), # C
]
piano.notes.extend(piano_notes)

# Little Ray: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.1875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Dante: Sax melody
sax_notes = [
    # First note: F (70)
    pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.875),
    # Second note: Bb (67)
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),
    # Third note: D (62)
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
