
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums
drum_notes = [
    # Kick on 1 & 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 & 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.5, end=1.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full Quartet (1.5 - 3.0s)
# Bass - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Piano - open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7sus4 (D, G, C, F#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F#
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),  # F
    # Bar 4: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # C#
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # G
]
piano.notes.extend(piano_notes)

# Sax - short motif, haunting, incomplete
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),  # F#
]
sax.notes.extend(sax_notes)

# Bar 3: Full Quartet (3.0 - 4.5s)
# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bass
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # G
]
piano.notes.extend(piano_notes)

# Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full Quartet (4.5 - 6.0s)
# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bass
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # G
]
piano.notes.extend(piano_notes)

# Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
