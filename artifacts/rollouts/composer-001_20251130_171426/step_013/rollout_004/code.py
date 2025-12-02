
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=39, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=100, pitch=37, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=35, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=39, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 (2.25s)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),   # Eb

    # Bar 3: D7 on 2 (3.75s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),   # D

    # Bar 4: F7 on 2 (5.25s)
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),   # D
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.5),   # Eb
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax - short motif, start on bar 2, leave it hanging, finish on bar 4
# Fm scale: F, Gb, Ab, A, Bb, C, Db
sax_notes = [
    # Bar 2: F -> Ab -> Bb (start=1.875)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=69, start=2.125, end=2.25),

    # Bar 3: C -> Db -> F (start=3.0)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=71, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),

    # Bar 4: F -> Gb -> Ab -> Bb (finish on 6.0)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=69, start=5.125, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=69, start=5.375, end=5.5),
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.625),
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=5.875),
    pretty_midi.Note(velocity=100, pitch=69, start=5.875, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 5):
    bar_start = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hi-hat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.125),
    # Fill on 3rd beat
    pretty_midi.Note(velocity=80, pitch=46, start=bar_start + 1.125, end=bar_start + 1.25)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
