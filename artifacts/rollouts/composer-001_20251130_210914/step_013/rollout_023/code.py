
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: F, Ab, Bb, C (motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0)   # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=80, pitch=45, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=80, pitch=48, start=2.0, end=2.125),   # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.125, end=2.25),  # G#
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.375, end=2.5),   # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.5, end=2.625),   # G#
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=51, start=2.75, end=2.875),  # A#
    pretty_midi.Note(velocity=80, pitch=50, start=2.875, end=3.0)    # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on 2
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=80, pitch=74, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=80, pitch=76, start=1.875, end=2.0),   # G
    pretty_midi.Note(velocity=80, pitch=79, start=1.875, end=2.0),   # Bb
    # Bar 3: D7 on 2
    pretty_midi.Note(velocity=90, pitch=74, start=2.875, end=3.0),   # D
    pretty_midi.Note(velocity=80, pitch=76, start=2.875, end=3.0),   # F#
    pretty_midi.Note(velocity=80, pitch=78, start=2.875, end=3.0),   # A
    pretty_midi.Note(velocity=80, pitch=81, start=2.875, end=3.0),   # C
]
piano.notes.extend(piano_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Same pattern as bar 1
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif, but shift up a half step
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=73, start=5.625, end=6.0)   # Db
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.625),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=4.625, end=4.75),  # G#
    pretty_midi.Note(velocity=80, pitch=47, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=4.875, end=5.0),   # G
    pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.125),   # A
    pretty_midi.Note(velocity=80, pitch=51, start=5.125, end=5.25),  # A#
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.375),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=5.375, end=5.5),   # A
    pretty_midi.Note(velocity=80, pitch=51, start=5.5, end=5.625),   # A#
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=5.75),  # B
    pretty_midi.Note(velocity=80, pitch=53, start=5.75, end=5.875),  # B#
    pretty_midi.Note(velocity=80, pitch=52, start=5.875, end=6.0)    # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: G7 on 2
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.0),   # G
    pretty_midi.Note(velocity=80, pitch=78, start=4.875, end=5.0),   # B
    pretty_midi.Note(velocity=80, pitch=80, start=4.875, end=5.0),   # D
    pretty_midi.Note(velocity=80, pitch=83, start=4.875, end=5.0),   # F#
]
piano.notes.extend(piano_notes)

# Bar 4: Drums (4.5 - 6.0s) - same pattern as bar 1
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo.mid")
