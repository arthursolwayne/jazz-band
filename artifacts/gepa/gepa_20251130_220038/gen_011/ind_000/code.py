
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25), # Gb (chromatic)
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.625), # Eb (3rd)
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=3.0),  # D (chromatic)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # F (root)
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75), # Gb (chromatic)
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125), # Ab (5th)
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),  # G (chromatic)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25), # Gb (chromatic)
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625), # Ab (5th)
    pretty_midi.Note(velocity=100, pitch=54, start=5.625, end=6.0),  # A (chromatic)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Eb

    # Bar 3 (comp on 2)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F7
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),

    # Bar 4 (comp on 4)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # F

    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875),
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875),
    drums.notes.extend([

    ])

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
