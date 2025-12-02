
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

# Drums - Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2 - Full Quartet (1.5 - 3.0s)

# Drums - Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bass - Bar 2 (Walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # Gb (chromatic)
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # G (3rd)
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # Ab (chromatic)
]
bass.notes.extend(bass_notes)

# Piano - Bar 2 (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # E7 (F7 root)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Bb (7th)
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # G (3rd)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # D (5th)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # Bb (7th)
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # E (root)
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625), # G (3rd)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # D (5th)
]
piano.notes.extend(piano_notes)

# Sax - Bar 2 (Motif: F - Bb - G - Ab)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=73, start=2.25, end=2.5),  # Ab
]
sax.notes.extend(sax_notes)

# Bar 3 - Full Quartet (3.0 - 4.5s)

# Drums - Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bass - Bar 3 (Walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # A (5th)
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125), # B (7th)
    pretty_midi.Note(velocity=100, pitch=51, start=4.125, end=4.5),  # Ab (chromatic)
]
bass.notes.extend(bass_notes)

# Piano - Bar 3 (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # E7 (F7 root)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb (7th)
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # G (3rd)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # D (5th)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # Bb (7th)
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125), # E (root)
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.125), # G (3rd)
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # D (5th)
]
piano.notes.extend(piano_notes)

# Sax - Bar 3 (Motif: F - Bb - G - Ab rest)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=73, start=3.75, end=4.0),  # Ab
]
sax.notes.extend(sax_notes)

# Bar 4 - Full Quartet (4.5 - 6.0s)

# Drums - Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bass - Bar 4 (Walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25), # Gb (chromatic)
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625), # G (3rd)
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),  # Ab (chromatic)
]
bass.notes.extend(bass_notes)

# Piano - Bar 4 (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # E7 (F7 root)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb (7th)
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # G (3rd)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # D (5th)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # Bb (7th)
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625), # E (root)
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.625), # G (3rd)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # D (5th)
]
piano.notes.extend(piano_notes)

# Sax - Bar 4 (Motif: F - Bb - G - Ab (rest) -> complete the motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=73, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=6.0),   # F (resolve)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
