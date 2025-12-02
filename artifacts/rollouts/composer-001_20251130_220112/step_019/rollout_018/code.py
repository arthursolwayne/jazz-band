
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
# Sax: Motif starts here - F, A, Bb, D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.6875, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),    # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.1875),  # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.6875, end=1.875),  # F#
    pretty_midi.Note(velocity=80, pitch=48, start=1.875, end=2.0),    # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.0, end=2.1875),  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=85, pitch=57, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=85, pitch=60, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=85, pitch=62, start=1.875, end=2.0),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=1.875, end=2.0),  # C
    # Bar 3: Bb7 on beat 4
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=85, pitch=65, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.1875),  # E
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.1875),  # F
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.1875, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.5625),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.5625, end=3.75),  # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.1875),  # G#
    pretty_midi.Note(velocity=80, pitch=50, start=3.1875, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.5625),  # A#
    pretty_midi.Note(velocity=80, pitch=52, start=3.5625, end=3.75),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=85, pitch=62, start=3.375, end=3.5625),  # Bb
    pretty_midi.Note(velocity=85, pitch=65, start=3.375, end=3.5625),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=3.375, end=3.5625),  # E
    pretty_midi.Note(velocity=85, pitch=69, start=3.375, end=3.5625),  # F
    # Bar 4: D7 on beat 4
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=85, pitch=70, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=85, pitch=72, start=4.5, end=4.6875),  # A
    pretty_midi.Note(velocity=85, pitch=74, start=4.5, end=4.6875),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif with a trill
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.6875, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.0),    # F
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.1875),  # A
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.6875),  # B
    pretty_midi.Note(velocity=80, pitch=53, start=4.6875, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=54, start=4.875, end=5.0),    # C#
    pretty_midi.Note(velocity=80, pitch=55, start=5.0, end=5.1875),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=85, pitch=67, start=4.875, end=5.0),    # D
    pretty_midi.Note(velocity=85, pitch=70, start=4.875, end=5.0),    # F
    pretty_midi.Note(velocity=85, pitch=72, start=4.875, end=5.0),    # A
    pretty_midi.Note(velocity=85, pitch=74, start=4.875, end=5.0),    # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.8125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.8125, end=6.0),
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
