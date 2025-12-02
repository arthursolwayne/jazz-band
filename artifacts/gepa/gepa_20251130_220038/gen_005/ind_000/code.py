
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # E7
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G7
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # A7
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G7
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # E7
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # D7
]
sax.notes.extend(sax_notes)

# Bass (Walking line)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=38, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=36, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=34, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=35, start=2.5, end=2.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=37, start=2.75, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Piano (7th chords on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # F7
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # F7
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # D7
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # F7
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # E7
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # D7
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),  # F7
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # E7
]
sax.notes.extend(sax_notes)

# Bass (Walking line)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=35, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=37, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=36, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=80, pitch=38, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=80, pitch=34, start=4.25, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano (7th chords on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # F7
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25),  # F7
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # D7
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # E7
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G7
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # E7
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # D7
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # F7
]
sax.notes.extend(sax_notes)

# Bass (Walking line)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=34, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=35, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=37, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=36, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=80, pitch=37, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano (7th chords on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # F7
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # F7
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)

    # Hihat on 1, 2, 3, 4
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875)

    # Fill the bar with hihat on every eighth
    for i in range(0, 8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
