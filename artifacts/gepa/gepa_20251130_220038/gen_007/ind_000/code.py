
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),    # F
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25),   # Gb
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.625),   # G
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),    # E
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),    # F
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75),   # Gb
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),   # G
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),    # E
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),    # F
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25),   # Gb
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625),   # G
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),    # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),    # F
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.875),    # A
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),    # C
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),    # Eb
    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),   # F
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625),   # A
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),   # C
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),   # Eb
    # Bar 4 (3.0 - 3.75s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),    # F
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.375),    # A
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),    # C
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),    # Eb
    # Bar 5 (3.75 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),   # F
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125),   # A
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125),   # C
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125),   # Eb
    # Bar 6 (4.5 - 5.25s)
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),    # F
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),    # A
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),    # C
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),    # Eb
    # Bar 7 (5.25 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),   # F
    pretty_midi.Note(velocity=100, pitch=47, start=5.25, end=5.625),   # A
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),   # C
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625),   # Eb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.6875),   # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=1.6875, end=1.875), # C
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.0625, end=2.25),  # Ab
    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),     # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.6875),   # C
    pretty_midi.Note(velocity=110, pitch=64, start=2.6875, end=2.875), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),    # Ab
    # Bar 4 (3.0 - 3.75s)
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.1875),   # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=3.1875, end=3.375), # C
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.5625, end=3.75),  # Ab
    # Bar 5 (3.75 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),     # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.1875),   # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=4.1875, end=4.375), # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.375, end=4.5),    # Ab
    # Bar 6 (4.5 - 5.25s)
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.6875),   # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=4.6875, end=4.875), # C
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.0625, end=5.25),  # Ab
    # Bar 7 (5.25 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),     # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.6875),   # C
    pretty_midi.Note(velocity=110, pitch=64, start=5.6875, end=5.875), # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=5.875, end=6.0),    # C
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 7):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
