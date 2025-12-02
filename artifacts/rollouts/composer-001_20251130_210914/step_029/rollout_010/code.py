
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

# Bass: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=68, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.5),  # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # E
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=68, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=5.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # Eb
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
