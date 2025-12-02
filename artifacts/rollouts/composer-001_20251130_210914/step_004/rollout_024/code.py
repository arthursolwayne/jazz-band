
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, chromatic approach to F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=100, pitch=46, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=47, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=2.125, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.375),  # G#
    pretty_midi.Note(velocity=100, pitch=47, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=2.5, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=44, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=100, pitch=43, start=2.875, end=3.0),  # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4, F7, Bb7, Eb7, Ab7
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.625),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.375),
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.125),
    # Bar 4: Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=48, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=53, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=52, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=57, start=3.125, end=3.25),
]
piano.notes.extend(piano_notes)

# Sax: Short motif, melodic, starting on F, leaving it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=55, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=50, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=55, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=110, pitch=53, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=2.75, end=3.0),  # E
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Same pattern as bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Drums (4.5 - 6.0s)
# Same pattern as bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, chromatic approach to Bb
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=51, start=3.125, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=49, start=3.25, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=3.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=3.625, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=100, pitch=50, start=3.875, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=49, start=4.0, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=4.25, end=4.375),  # G
    pretty_midi.Note(velocity=100, pitch=46, start=4.375, end=4.5),  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4, Bb7, Eb7, Ab7, Db7
piano_notes = [
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.125),
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=3.875),
    # Bar 4: Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.625),
    # Bar 4: Db7 (Db, F, Ab, C)
    pretty_midi.Note(velocity=100, pitch=45, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=53, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=48, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=55, start=4.625, end=4.75),
]
piano.notes.extend(piano_notes)

# Bar 4: Sax (4.5 - 6.0s)
# Full motif, resolving on D (Eb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=55, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=50, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=55, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=110, pitch=53, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=5.75, end=6.0),  # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
