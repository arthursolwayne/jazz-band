
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

# Marcus: Walking bass line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 chord (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=1.875),  # Eb
    # Bar 3: Bb7 chord (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # Ab
    # Bar 4: C7 chord (C, E, G, Bb)
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # Bb
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),   # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),   # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.75),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),   # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5),
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax line (start at bar 2)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B
    # Bar 3: Continue motif
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    # Bar 4: Resolution
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),   # B
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
