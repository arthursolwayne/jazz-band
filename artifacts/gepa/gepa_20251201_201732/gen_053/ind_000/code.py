
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth note
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: C (root) -> Bb (chromatic approach) -> Ab (fifth) -> G (chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=59, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=64, start=2.0625, end=2.25),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),
]
piano.notes.extend(piano_notes)

# Sax: Melody starts here — one short motif, incomplete
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=63, start=2.0, end=2.25),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Bb (root) -> A (chromatic approach) -> G (fifth) -> F (chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=58, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=63, start=3.5625, end=3.75),
]
bass.notes.extend(bass_notes)

# Piano: Bbm7 (Bb, Db, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif — leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=63, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=110, pitch=61, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F (root) -> Eb (chromatic approach) -> D (fifth) -> C (chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=59, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=61, start=5.0625, end=5.25),
]
bass.notes.extend(bass_notes)

# Piano: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),
]
piano.notes.extend(piano_notes)

# Sax: Return to the motif, finish it — but with tension
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # A
]
sax.notes.extend(sax_notes)

# Drums: Same pattern but with a slight push on the last snare
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    # Hihat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
