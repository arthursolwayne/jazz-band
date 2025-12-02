
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.125, end=2.5),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.875),   # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=2.875, end=3.125),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.5),    # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.875),    # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.25),   # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),     # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),    # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0)     # E
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=83, start=1.5, end=1.875),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=83, start=3.0, end=3.375),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=83, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): Motif, short, singable, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),   # E
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),   # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),   # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75),   # E
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),   # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),   # E
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.25),   # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5),   # G
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),   # E
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),   # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),   # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),   # E
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0)    # G
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)

drums.notes.extend([note for note in drums.notes if note not in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
