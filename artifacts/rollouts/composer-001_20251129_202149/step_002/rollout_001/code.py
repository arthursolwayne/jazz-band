
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif starting on C (60), Bb (58), B (59), C (60)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=58, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=59, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0)
]
sax.notes.extend(sax_notes)

# Bass: walking line in C with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.625, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.125),  # D#
    pretty_midi.Note(velocity=80, pitch=63, start=2.125, end=2.25), # E
    pretty_midi.Note(velocity=80, pitch=61, start=2.25, end=2.375), # D
    pretty_midi.Note(velocity=80, pitch=62, start=2.375, end=2.5),  # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),   # B
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),   # B
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=2.75),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),   # B
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif, but with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=58, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=59, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5)
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.5),   # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.625),   # D#
    pretty_midi.Note(velocity=80, pitch=63, start=3.625, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=3.875, end=4.0),   # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 3 (3.0 - 3.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),   # B
    # Bar 4 (3.5 - 4.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),   # B
    # Bar 4 (4.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),   # B
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish motif, return and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=58, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=59, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0)
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=4.625, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.0),   # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.125),   # D#
    pretty_midi.Note(velocity=80, pitch=63, start=5.125, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=5.375, end=5.5),   # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 4 (4.5 - 5.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),   # B
    # Bar 5 (5.0 - 5.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.25),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.25),   # B
    # Bar 6 (5.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.75),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.75),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75),   # B
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat every eighth
for bar in [2, 3, 4]:
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hi-hat on every eighth
    for i in range(8):
        start = bar_start + i * 0.125
        end = start + 0.125
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
