
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
# Sax melody: Fm7 -> Bb -> Eb -> Ab (Fm scale, 1st inversion)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.0625), # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=2.0625, end=2.25), # Ab
]
sax.notes.extend(sax_notes)

# Bass: Walking line (Fm7 -> Bb7 -> Eb7 -> Ab7)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.0625), # D
    pretty_midi.Note(velocity=80, pitch=43, start=2.0625, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=2.4375, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=39, start=2.625, end=2.8125), # C
    pretty_midi.Note(velocity=80, pitch=43, start=2.8125, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, Db, Eb)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.6875),  # Db
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.6875),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.6875),  # Bb
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.4375),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.4375),  # Bb
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.1875),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.1875),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody: Ab -> G -> F -> Bb (Fm scale, 2nd inversion)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.1875),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.5625, end=3.75),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line (Ab7 -> G7 -> F7 -> Bb7)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.1875),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=80, pitch=53, start=3.5625, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=3.9375),  # Ab
    pretty_midi.Note(velocity=80, pitch=49, start=3.9375, end=4.125), # F
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.3125), # E
    pretty_midi.Note(velocity=80, pitch=53, start=4.3125, end=4.5),   # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.1875),  # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.1875),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.1875),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # G
    # Bar 4: G7 (G, Bb, D, F)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.9375),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=3.9375),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=3.9375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.9375),  # F
    # Bar 4: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.6875),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.6875),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.6875),  # Eb
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody: Bb -> Ab -> G -> F (Fm scale, 3rd inversion, resolution)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.6875),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=4.6875, end=4.875), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.0625, end=5.25),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line (Bb7 -> Ab7 -> G7 -> F7)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.6875),  # Bb
    pretty_midi.Note(velocity=80, pitch=53, start=4.6875, end=4.875), # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=80, pitch=64, start=5.0625, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.4375),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.4375, end=5.625), # G
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=5.8125), # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=5.8125, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.6875),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.6875),  # Bb
    # Bar 4: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.4375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.4375),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.4375),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.4375),  # Eb
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
for bar in range(2, 4):
    start = 1.5 * bar
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
