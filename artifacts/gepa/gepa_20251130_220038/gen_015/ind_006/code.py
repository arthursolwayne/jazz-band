
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=35, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=34, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=33, start=1.875, end=2.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=32, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=31, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=30, start=2.25, end=2.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=29, start=2.375, end=2.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=28, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=27, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=26, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=90, pitch=33, start=2.875, end=3.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0),  # Db
    pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=2.0),  # D
    # Bar 3: F7 on 2 and 4
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.75, end=3.0),  # Db
    pretty_midi.Note(velocity=80, pitch=72, start=2.75, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Dante: Your motif
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875),  # A
    # Bar 3: Continue
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.125, end=2.25),  # F
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.6875),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.6875, end=2.875),  # F
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.75, end=1.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375),  # Snare on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.25, end=4.375),  # Snare on 4
]
# Add hihat on every eighth
for i in range(0, 6, 1):
    start = 1.5 + i * 0.375
    end = start + 0.1875
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
for i in range(0, 6, 1):
    start = 2.0 + i * 0.375
    end = start + 0.1875
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
for i in range(0, 6, 1):
    start = 2.5 + i * 0.375
    end = start + 0.1875
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
for i in range(0, 6, 1):
    start = 3.0 + i * 0.375
    end = start + 0.1875
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
for i in range(0, 6, 1):
    start = 3.5 + i * 0.375
    end = start + 0.1875
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
for i in range(0, 6, 1):
    start = 4.0 + i * 0.375
    end = start + 0.1875
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
