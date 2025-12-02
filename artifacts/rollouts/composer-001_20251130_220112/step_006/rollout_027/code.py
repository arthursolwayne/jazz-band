
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F (F, G, A, Bb, C, D, Eb, F)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=70, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.875, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=70, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.625, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=3.875, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.375),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.375, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.625, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=70, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=5.125, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.375),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=5.375, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=5.5, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=5.625, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=5.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=70, start=5.875, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# F7: F, A, C, Eb
# Bb7: Bb, D, F, Ab
# C7: C, E, G, Bb
# Eb7: Eb, G, Bb, Db
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=70, start=2.0, end=2.125),
    pretty_midi.Note(velocity=95, pitch=72, start=2.0, end=2.125),
    pretty_midi.Note(velocity=95, pitch=74, start=2.0, end=2.125),
    pretty_midi.Note(velocity=95, pitch=69, start=2.0, end=2.125),
    # Bar 2: Bb7 on beat 4
    pretty_midi.Note(velocity=95, pitch=68, start=2.5, end=2.625),
    pretty_midi.Note(velocity=95, pitch=71, start=2.5, end=2.625),
    pretty_midi.Note(velocity=95, pitch=70, start=2.5, end=2.625),
    pretty_midi.Note(velocity=95, pitch=66, start=2.5, end=2.625),
    # Bar 3: C7 on beat 2
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.125),
    pretty_midi.Note(velocity=95, pitch=75, start=3.0, end=3.125),
    pretty_midi.Note(velocity=95, pitch=77, start=3.0, end=3.125),
    pretty_midi.Note(velocity=95, pitch=70, start=3.0, end=3.125),
    # Bar 3: Eb7 on beat 4
    pretty_midi.Note(velocity=95, pitch=69, start=3.5, end=3.625),
    pretty_midi.Note(velocity=95, pitch=72, start=3.5, end=3.625),
    pretty_midi.Note(velocity=95, pitch=70, start=3.5, end=3.625),
    pretty_midi.Note(velocity=95, pitch=65, start=3.5, end=3.625),
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=70, start=4.0, end=4.125),
    pretty_midi.Note(velocity=95, pitch=72, start=4.0, end=4.125),
    pretty_midi.Note(velocity=95, pitch=74, start=4.0, end=4.125),
    pretty_midi.Note(velocity=95, pitch=69, start=4.0, end=4.125),
    # Bar 4: Bb7 on beat 4
    pretty_midi.Note(velocity=95, pitch=68, start=4.5, end=4.625),
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.625),
    pretty_midi.Note(velocity=95, pitch=70, start=4.5, end=4.625),
    pretty_midi.Note(velocity=95, pitch=66, start=4.5, end=4.625),
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax melody (start in bar 2)
# Short motif: F, Bb, C, Eb -> F, Bb, C, Eb (chromatic approach)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0),  # Eb
    # Repeat with variation
    pretty_midi.Note(velocity=110, pitch=70, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=2.875, end=3.0),  # Eb
    # Start again on beat 4 of bar 3
    pretty_midi.Note(velocity=110, pitch=70, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=3.625, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=3.875, end=4.0),  # Eb
    # Final motive in bar 4
    pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=4.625, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0),  # Eb
]
sax.notes.extend(sax_notes)

# Fill the rest of the time with drum fills
# Bar 2: Fill on beat 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Fill on beat 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Fill on beat 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
