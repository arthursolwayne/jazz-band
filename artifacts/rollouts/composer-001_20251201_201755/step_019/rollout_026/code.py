
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

# Drums in Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass in Bar 2: Walking line, roots and fifths, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Ab (E2)
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625), # G (D#2)
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # C (F2)
]
bass.notes.extend(bass_notes)

# Piano in Bar 2: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax in Bar 2: Motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # G (A4)
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25), # Bb (B4)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # G (A4)
]
sax.notes.extend(sax_notes)

# Drums in Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)  # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass in Bar 3: Walking line, roots and fifths, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # C (F2)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # Bb (E2)
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125), # Ab (D#2)
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # F (D2)
]
bass.notes.extend(bass_notes)

# Piano in Bar 3: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax in Bar 3: Motif, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G (A4)
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75), # Bb (B4)
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125), # G (A4)
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),  # F (G4)
]
sax.notes.extend(sax_notes)

# Drums in Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)  # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass in Bar 4: Walking line, roots and fifths, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F (D2)
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # Ab (E2)
    pretty_midi.Note(velocity=100, pitch=39, start=5.25, end=5.625), # G (D#2)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # C (F2)
]
bass.notes.extend(bass_notes)

# Piano in Bar 4: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax in Bar 4: Motif, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # G (A4)
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25), # Bb (B4)
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # G (A4)
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # F (G4)
]
sax.notes.extend(sax_notes)

# Drums in Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)  # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
