
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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
    pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.5),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=41, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=40, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=39, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.5),  # Ab
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=37, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=35, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=34, start=4.25, end=4.5),  # Eb
    # Bar 4 continuation
    pretty_midi.Note(velocity=100, pitch=33, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=32, start=4.75, end=5.0),  # Db
    pretty_midi.Note(velocity=100, pitch=31, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=30, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=29, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=28, start=5.75, end=6.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # B
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # B
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # B
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.625),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=2.75, end=2.875),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.875, end=3.0),  # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.625, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),  # Bb
    # Bar 4 continuation
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=59, start=4.625, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=57, start=4.75, end=4.875),  # Db
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.125, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.375, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=59, start=5.75, end=5.875),  # E
    pretty_midi.Note(velocity=100, pitch=57, start=5.875, end=6.0),  # Db
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)

drums.notes.extend([n for n in drums.notes if n not in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
