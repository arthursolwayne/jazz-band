
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
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=70, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=70, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Sax: short motif starting on beat 1 of bar 2
sax_notes = [
    # Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),   # Ab
    # Leave it hanging
    # Come back on beat 3 of bar 3
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.625, end=3.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=76, start=3.875, end=4.125),  # Bb
    pretty_midi.Note(velocity=70, pitch=69, start=4.125, end=4.375),  # D
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches
bass_notes = [
    # Bar 2: F -> Gb -> G -> Ab
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5),  # Ab
    # Bar 3: Bb -> B -> C -> C#
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=54, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=56, start=3.25, end=3.5),  # C#
    # Bar 4: D -> Eb -> E -> F
    pretty_midi.Note(velocity=80, pitch=57, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=58, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5),  # F
    # Bar 4: Repeat the last four notes
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=58, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=70, pitch=76, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=60, pitch=69, start=2.0, end=2.25),  # D
    # Bar 3: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=70, pitch=76, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=60, pitch=69, start=3.0, end=3.25),  # D
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=70, pitch=76, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=60, pitch=69, start=4.0, end=4.25),  # D
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=70, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
