
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
# Sax melody: F (G7) -> A (B7) -> B (C#7) -> C (D7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F (G7)
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0),  # A (B7)
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),  # B (C#7)
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.5),  # C (D7)
]
sax.notes.extend(sax_notes)

# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.0, end=2.25),  # G#
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # F7 on 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=68, start=1.75, end=2.0),  # G
    # Bb7 on 4 (2.25 - 2.5)
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody: D (E7) -> E (F#7) -> F (G7) -> G (A7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.25),  # D (E7)
    pretty_midi.Note(velocity=100, pitch=81, start=3.25, end=3.5),  # E (F#7)
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # F (G7)
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0),  # G (A7)
]
sax.notes.extend(sax_notes)

# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=57, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=56, start=3.5, end=3.75),  # D#
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # E7 on 2 (3.25 - 3.5)
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=90, pitch=73, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # F
    # A7 on 4 (3.75 - 4.0)
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=78, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0),  # G
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody: D (E7) -> E (F#7) -> F (G7) -> G (A7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.75),  # D (E7)
    pretty_midi.Note(velocity=100, pitch=81, start=4.75, end=5.0),  # E (F#7)
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # F (G7)
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5),  # G (A7)
]
sax.notes.extend(sax_notes)

# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=57, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=56, start=5.0, end=5.25),  # D#
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # E7 on 2 (4.75 - 5.0)
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=73, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # F
    # A7 on 4 (5.25 - 5.5)
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=78, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.5),  # G
]
piano.notes.extend(piano_notes)

# Bar 4: Drums
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
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
