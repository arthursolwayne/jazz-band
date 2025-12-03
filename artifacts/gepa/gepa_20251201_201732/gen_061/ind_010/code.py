
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0),   # C2
]

# Piano: Open voicings, each bar resolves on the last chord
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # Eb
]

# Sax: Motif starts here
# Fm7 -> Bb7 -> Eb7 -> Amaj7
# F (64), Ab (60), Bb (62), Eb (62), F (64)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),   # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.125),  # F
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm (F, Ab, D, C)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),   # C2
])

# Piano: Open voicings, each bar resolves on the last chord
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # Ab
])

# Sax: Motif continues
# Bb (62), D (67), Eb (62), F (64)
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.375),  # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5),   # F
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm (F, Ab, D, C)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),   # C2
])

# Piano: Open voicings, each bar resolves on the last chord
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D
])

# Sax: Motif ends
# Eb (62), G (67), F (64) (ending on F, leaving it hanging)
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),  # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=4.875),  # F
])

# Add all notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
