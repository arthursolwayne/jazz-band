
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: Motif
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # A
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # A
    # Bar 5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # Bb
    # Bar 6
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # A
    # Bar 7
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # Bb
    # Bar 8
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # A
    # Bar 9
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # Bb
    # Bar 10
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0)   # A
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # G
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5),  # Bb
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.75, end=3.0),  # Bb
    # Bar 5 (3.0 - 3.5s)
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=49, start=3.25, end=3.5),  # G
    # Bar 6 (3.5 - 4.0s)
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0),  # G
    # Bar 7 (4.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=50, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=51, start=4.25, end=4.5),  # Bb
    # Bar 8 (4.5 - 5.0s)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=4.75, end=5.0),  # Bb
    # Bar 9 (5.0 - 5.5s)
    pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.5),  # G
    # Bar 10 (5.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=47, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=5.75, end=6.0)   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # F7: F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # F7: Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # F7: E
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75),  # F7: F
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # A7: A
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),  # A7: C
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.25),  # A7: E
    pretty_midi.Note(velocity=90, pitch=74, start=2.0, end=2.25),  # A7: G
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.75),  # F7: F
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # F7: Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # F7: E
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.75),  # F7: F
    # Bar 5 (3.0 - 3.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # A7: A
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # A7: C
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # A7: E
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # A7: G
    # Bar 6 (3.5 - 4.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # F7: F
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # F7: Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # F7: E
    pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.75),  # F7: F
    # Bar 7 (4.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),  # A7: A
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),  # A7: C
    pretty_midi.Note(velocity=90, pitch=72, start=4.0, end=4.25),  # A7: E
    pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.25),  # A7: G
    # Bar 8 (4.5 - 5.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # F7: F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # F7: Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # F7: E
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # F7: F
    # Bar 9 (5.0 - 5.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),  # A7: A
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.25),  # A7: C
    pretty_midi.Note(velocity=90, pitch=72, start=5.0, end=5.25),  # A7: E
    pretty_midi.Note(velocity=90, pitch=74, start=5.0, end=5.25),  # A7: G
    # Bar 10 (5.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # F7: F
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),  # F7: Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75),  # F7: E
    pretty_midi.Note(velocity=90, pitch=72, start=5.5, end=5.75)   # F7: F
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hihat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.125)

drums.notes.extend([n for n in drums.notes if n.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro_wayne.mid")
