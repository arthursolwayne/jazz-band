
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

# Bass line: walking line, chromatic approaches, never the same note twice
# Fm7 chord: F, Ab, C, Eb
bass_notes = [
    # Bar 2: F (1.5s), Gb (1.875s), Eb (2.25s), D (2.625s)
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=61, start=2.625, end=3.0),
    # Bar 3: Ab (3.0s), G (3.375s), F (3.75s), E (4.125s)
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),
    # Bar 4: C (4.5s), B (4.875s), Ab (5.25s), G (5.625s)
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=68, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
piano_notes = [
    # Bar 2: Comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    # Bar 3: Comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=65, start=3.875, end=4.25),
    pretty_midi.Note(velocity=90, pitch=68, start=3.875, end=4.25),
    pretty_midi.Note(velocity=90, pitch=71, start=3.875, end=4.25),
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.25),
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Sax: Motif (start at 1.5s)
# F (1.5s), Ab (1.875s), Eb (2.25s), F (2.625s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),
    # Come back and finish it
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
