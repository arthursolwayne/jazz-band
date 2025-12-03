
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Fm, walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Gb (chromatic)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # A (fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),   # Bb (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, each bar a different chord
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=85, pitch=60, start=1.5, end=2.25),  # Eb
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=2.25),  # Ab
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=2.25),  # C
]
piano.notes.extend(piano_notes)

# Sax: Haunting motif, incomplete
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # G (above Fm)
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625),  # E (tense)
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # D (suspense)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: Fm, walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Bb (root)
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # C (chromatic)
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125),  # D (fifth)
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),   # Eb (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, each bar a different chord
# Bar 3: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=85, pitch=60, start=3.0, end=3.75),  # Eb
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.75),  # Ab
    pretty_midi.Note(velocity=85, pitch=72, start=3.0, end=3.75),  # C
]
piano.notes.extend(piano_notes)

# Sax: Haunting motif, incomplete
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # E (tense)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # D (suspense)
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),  # G (return)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: Fm, walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),  # Eb (root)
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25),  # F (chromatic)
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625),  # G (fifth)
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),   # Ab (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, each bar a different chord
# Bar 4: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=85, pitch=60, start=4.5, end=5.25),  # Eb
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=5.25),  # Ab
    pretty_midi.Note(velocity=85, pitch=72, start=4.5, end=5.25),  # C
]
piano.notes.extend(piano_notes)

# Sax: Haunting motif, incomplete
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # D (suspense)
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),  # G (return)
    pretty_midi.Note(velocity=100, pitch=63, start=5.625, end=6.0),  # E (tense)
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
