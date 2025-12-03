
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
    # Hi-hat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm (F, Ab, Bb, Db) with chromatic approaches
bass_notes = [
    # Bar 2: F (root), Ab (b9), Bb (11), Db (b13)
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=2.0),
    pretty_midi.Note(velocity=80, pitch=63, start=1.5, end=2.0),
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=2.0),
    # Chromatic approach to F
    pretty_midi.Note(velocity=60, pitch=64, start=1.0, end=1.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb), open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=2.0),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif in Fm, one short phrase, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Ab (b9), Bb (11), Db (b13), F (root)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=63, start=3.0, end=3.5),
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.5),
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.5),
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.5),
    # Chromatic approach to Ab
    pretty_midi.Note(velocity=60, pitch=62, start=2.5, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Ab7 (Ab, C, Eb, Gb), open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.5),  # Gb
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # B
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Bb (11), Db (b13), F (root), Ab (b9)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=5.0),
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=5.0),
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=5.0),
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=5.0),
    # Chromatic approach to Bb
    pretty_midi.Note(velocity=60, pitch=61, start=4.0, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Db7 (Db, F, Ab, C), open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0),  # Db
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # A
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
