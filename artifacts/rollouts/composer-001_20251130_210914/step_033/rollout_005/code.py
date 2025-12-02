
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
# Fm7 chord: F, Ab, Bb, D
# Walking bass line in Fm
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # F (root)
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),  # D (bass note)
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.5),  # Gb (Ab)
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # G (chromatic)
    pretty_midi.Note(velocity=90, pitch=66, start=2.75, end=3.0),  # Gb (Ab)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.25),  # Gb (Ab)
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),  # G (chromatic)
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=4.25, end=4.5),  # Gb (Ab)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.75),  # Gb (Ab)
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),  # G (chromatic)
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=5.75, end=6.0),  # Gb (Ab)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, D
# Comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=95, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=85, pitch=71, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=85, pitch=71, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # D
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=95, pitch=64, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=85, pitch=71, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=85, pitch=71, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Saxophone: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F, Gb, Ab, Bb -> 1st bar, then rest on Bb, resolve on F in bar 4
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # Bb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # Bb (rest)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=6.0),  # F (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.1875, end=bar_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.5625, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.9375, end=bar_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.5),
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
