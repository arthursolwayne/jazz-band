
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
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=60, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=60, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    # Bar 2: walking line in F minor
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0),   # G
    # Bar 3: chromatic approach
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),   # G#
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # D
    # Bar 4: walking line in F minor
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=95, pitch=76, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=77, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=95, pitch=82, start=1.875, end=2.25),  # E
    # Bar 3: D7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=95, pitch=72, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=95, pitch=73, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=95, pitch=78, start=3.375, end=3.75),  # B
    # Bar 4: F7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=95, pitch=76, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=77, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=95, pitch=82, start=4.875, end=5.25),  # E
]
piano.notes.extend(piano_notes)

# Sax: Dante (melody)
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=105, pitch=71, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=105, pitch=74, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=105, pitch=72, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=105, pitch=76, start=2.625, end=3.0),   # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=105, pitch=72, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=105, pitch=76, start=3.375, end=3.75),  # Bb
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=105, pitch=74, start=4.5, end=4.875),   # A
    pretty_midi.Note(velocity=105, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=105, pitch=72, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=105, pitch=76, start=5.625, end=6.0),   # Bb
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
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
        pretty_midi.Note(velocity=60, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
