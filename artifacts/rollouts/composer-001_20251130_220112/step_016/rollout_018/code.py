
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
# Marcus: walking line, chromatic approaches
bass_notes = [
    # F -> Eb -> D -> C
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5),
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # F7 at 1.5s
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.75),
    # G7 at 2.25s
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Dante: melody (start at 1.5s)
sax_notes = [
    # F (1.5s)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),
    # Bb (2.0s)
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.375),
    # D (2.5s)
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.875),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: walking line, chromatic approaches
bass_notes = [
    # E -> D -> C -> Bb
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.0),
]
bass.notes.extend(bass_notes)

# Diane: 7th chords
piano_notes = [
    # E7 at 3.0s
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),
    # C7 at 3.75s
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Dante: melody (start at 3.0s)
sax_notes = [
    # E (3.0s)
    pretty_midi.Note(velocity=110, pitch=61, start=3.0, end=3.375),
    # Bb (3.5s)
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.875),
    # C (4.0s)
    pretty_midi.Note(velocity=110, pitch=60, start=4.0, end=4.375),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: walking line, chromatic approaches
bass_notes = [
    # D -> C -> Bb -> A
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=59, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.5),
]
bass.notes.extend(bass_notes)

# Diane: 7th chords
piano_notes = [
    # D7 at 4.5s
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),
    # F7 at 5.25s
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.5),
]
piano.notes.extend(piano_notes)

# Dante: melody (start at 4.5s)
sax_notes = [
    # D (4.5s)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),
    # Bb (5.0s)
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.375),
    # F (5.5s)
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat
    for i in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
