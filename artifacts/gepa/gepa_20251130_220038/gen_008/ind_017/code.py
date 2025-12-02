
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5), # Hihat on &
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: D (62) -> F# (67) -> A (69) -> D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.0625, end=2.25), # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on 2 (beat 2)
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.0625),
    # D7 on 4 (beat 4)
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.4375),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: D (62) -> Bb (62-1) = 61 -> F# (67) -> D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=61, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.1875), # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=3.5625, end=3.75), # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on 2 (beat 2)
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.5625),
    # D7 on 4 (beat 4)
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=3.9375),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: D (62) -> Bb (61) -> F# (67) -> G (67)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=61, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=67, start=5.0625, end=5.25),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.6875), # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=80, pitch=69, start=5.0625, end=5.25), # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on 2 (beat 2)
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.0625),
    # D7 on 4 (beat 4)
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.4375),
]
piano.notes.extend(piano_notes)

# Drums: Fill in bar 4 with more energy
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.6875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.6875, end=5.0625),  # Snare on &
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.0625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.0625, end=5.4375),  # Snare on &
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.4375),  # Kick on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
