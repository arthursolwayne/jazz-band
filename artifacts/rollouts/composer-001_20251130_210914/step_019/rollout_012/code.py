
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax starts with short motif (Fm7 -> Bb -> Ab -> G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.0),  # G
]

sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F (root)
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0),  # G (chromatic)
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # Eb (b7)
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.5),  # F (root)
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.75),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=58, start=2.25, end=2.5),
    # Bar 4: Ab7 (Ab, C, Eb, Gb)
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.25),
]

piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax continues with motif variation (Fm7 -> Ab -> G -> Bb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=61, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),  # C (chromatic)
]

sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # G (chromatic)
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),  # F (root)
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.75),  # Eb (b7)
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0),  # F (root)
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Fm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.25),
    # Bar 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.0),
]

piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax finishes motif (Fm7 -> Bb -> Ab -> G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0),  # F
]

sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # G (chromatic)
    pretty_midi.Note(velocity=80, pitch=48, start=4.75, end=5.0),  # F (root)
    pretty_midi.Note(velocity=80, pitch=47, start=5.0, end=5.25),  # Eb (b7)
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.5),  # F (root)
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Fm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.75),
]

piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
