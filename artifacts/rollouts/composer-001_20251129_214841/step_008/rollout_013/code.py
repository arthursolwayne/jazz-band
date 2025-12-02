
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: C (60), E (64), G (67), B (71)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),
]
sax.notes.extend(sax_notes)

# Bass line: walking in C, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=1.625, end=1.75),  # C#
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.0),  # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # C7 (C, E, G, B) on beat 2 (1.625 - 1.75)
    pretty_midi.Note(velocity=90, pitch=60, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=64, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=67, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=71, start=1.625, end=1.75),
    # E7 (E, G#, B, D) on beat 4 (1.875 - 2.0)
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat the motif but with a variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.5),
]
sax.notes.extend(sax_notes)

# Bass line: walking in C, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.125),  # D#
    pretty_midi.Note(velocity=90, pitch=53, start=3.125, end=3.25),  # E
    pretty_midi.Note(velocity=90, pitch=55, start=3.25, end=3.375),  # F#
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # C7 (C, E, G, B) on beat 2 (3.125 - 3.25)
    pretty_midi.Note(velocity=90, pitch=60, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=64, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=67, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=71, start=3.125, end=3.25),
    # F7 (F, A, C, E) on beat 4 (3.375 - 3.5)
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.5),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif, resolve to C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),
]
sax.notes.extend(sax_notes)

# Bass line: walking in C, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.625),  # G
    pretty_midi.Note(velocity=90, pitch=59, start=4.625, end=4.75),  # G#
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0),  # A#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # C7 (C, E, G, B) on beat 2 (4.625 - 4.75)
    pretty_midi.Note(velocity=90, pitch=60, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=64, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=67, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=71, start=4.625, end=4.75),
    # G7 (G, B, D, F) on beat 4 (4.875 - 5.0)
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.0),
]
piano.notes.extend(piano_notes)

# Drums for bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
