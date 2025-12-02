
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
    # Kick on 1 and 3 (0.0s and 0.75s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    # Snare on 2 and 4 (0.375s and 1.125s)
    pretty_midi.Note(velocity=110, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=110, pitch=38, start=1.125, end=1.5),
    # Hihat on every eighth (0.0 - 1.5s)
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=3.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: C - E - G - Bb (1.5s)
# Then rest until 4.5s, then repeat and resolve on G (6.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
    # Rest until 4.5s
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Kick on 1 and 3 for bar 2 (1.5, 2.25)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    # Snare on 2 and 4 for bar 2 (1.875, 2.625)
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=3.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    # Kick on 1 and 3 for bar 3 (3.0, 3.75)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    # Snare on 2 and 4 for bar 3 (3.375, 4.125)
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    # Kick on 1 and 3 for bar 4 (4.5, 5.25)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    # Snare on 2 and 4 for bar 4 (4.875, 5.625)
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=6.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
