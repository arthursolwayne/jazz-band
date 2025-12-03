
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax enters with a haunting motif
# Time starts at 1.5s
# Fm7 -> Bbm7 -> Eb7 -> Am7
# Diane - Piano
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875),  # D
    # Bar 3: Bbm7 (Bb, Db, F, G)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # Db
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # G
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # D
    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # G
]
piano.notes.extend(piano_notes)

# Bass line: Marcus, walking in Fm7 -> Bbm7 -> Eb7 -> Am7
# Roots: F -> Bb -> Eb -> A (with chromatic approaches)
bass_notes = [
    # Bar 2: F -> Eb -> F -> G
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),  # G
    # Bar 3: Bb -> A -> Bb -> C
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # C
]
bass.notes.extend(bass_notes)

# Sax solo: Dante, haunting motif
# Fm7 -> Bbm7 -> Eb7 -> Am7
# Motif: F, Ab, Bb, D
# Bar 2: F (1.5s) - Ab (1.875s) - Bb (2.25s) - D (2.625s)
# Bar 3: F (3.0s) - Ab (3.375s) - Bb (3.75s) - D (4.125s)
# Bar 4: F (4.5s) - Ab (4.875s) - Bb (5.25s) - D (5.625s)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=76, start=2.625, end=3.0),  # D

    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=76, start=4.125, end=4.5),  # D

    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=76, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 1: Drums only
# No piano, bass, or sax in bar 1

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
