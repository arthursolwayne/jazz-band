
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
# Sax: Dm7 -> F -> Bb -> C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, Dm7 -> G7 -> Cm7 -> F7
piano_notes = [
    # Dm7 (beat 2)
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # F
    # G7 (beat 4)
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),  # F
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif but with chromatic approach
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=4.125, end=4.5),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, Cm7 -> F7
piano_notes = [
    # Cm7 (beat 2)
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # Bb
    # F7 (beat 4)
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5),  # D
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif again, but now resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Bass: Walk to the end
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, Bm7 -> E7
piano_notes = [
    # Bm7 (beat 2)
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),  # G
    # E7 (beat 4)
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),  # E
    pretty_midi.Note(velocity=80, pitch=68, start=5.625, end=6.0),  # G#
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hihat on every eighth
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
