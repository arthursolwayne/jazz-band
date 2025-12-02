
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
# Sax: motif in Dm
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # A
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # F
    # Repeat motif
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Bass: walking line in Dm
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5),  # Gb
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=55, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5),  # B
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0),  # Db
    pretty_midi.Note(velocity=80, pitch=65, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=5.0, end=5.25),  # G#
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=80, pitch=76, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=77, start=5.75, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords comp on 2 and 4
piano_notes = [
    # Bar 2 (2nd beat)
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=2.0, end=2.25),  # G
    # Bar 3 (4th beat)
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.75),  # G
    # Bar 4 (2nd beat)
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.25),  # G
    # Bar 4 (4th beat)
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=5.5, end=5.75),  # G
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    # Bar start
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.1875, end=bar_start + (i + 1) * 0.1875)

drums.notes.extend([note for note in drums.notes if note.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
