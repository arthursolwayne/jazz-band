
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in F (F2, C3, G3, Bb3, A3, G3, F3, E3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=81, start=1.875, end=2.25), # C3
    pretty_midi.Note(velocity=100, pitch=84, start=2.25, end=2.625), # G3
    pretty_midi.Note(velocity=100, pitch=83, start=2.625, end=3.0),  # Bb3
]
bass.notes.extend(bass_notes)

# Piano: F7, Bb7, C7, F7 (open voicings, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=2.25),  # F7
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=83, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=84, start=2.25, end=3.0),   # Bb7
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif starts on F4 (bar 2)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=82, start=1.875, end=2.25), # A4
    pretty_midi.Note(velocity=110, pitch=83, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=110, pitch=84, start=2.625, end=3.0),  # C5
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2, D3, A3, C4, B3, A3, G3, F3
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=83, start=3.375, end=3.75), # D3
    pretty_midi.Note(velocity=100, pitch=86, start=3.75, end=4.125), # A3
    pretty_midi.Note(velocity=100, pitch=88, start=4.125, end=4.5),  # C4
]
bass.notes.extend(bass_notes)

# Piano: C7, F7, G7, C7 (open voicings, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.75),   # C7
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=85, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=84, start=3.75, end=4.5),   # F7
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Motif continues (bar 3)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=82, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=110, pitch=80, start=3.375, end=3.75), # G4
    pretty_midi.Note(velocity=110, pitch=82, start=3.75, end=4.125), # A4
    pretty_midi.Note(velocity=110, pitch=84, start=4.125, end=4.5),  # C5
]
sax.notes.extend(sax_notes)

# Drums: kick on 1, snare on 2, hihat on 3, kick on 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: C2, G2, C3, E3, D3, C3, B2, A2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # C2
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=100, pitch=81, start=5.25, end=5.625), # C3
    pretty_midi.Note(velocity=100, pitch=85, start=5.625, end=6.0),  # E3
]
bass.notes.extend(bass_notes)

# Piano: G7, C7, D7, G7 (open voicings, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=85, start=4.5, end=5.25),   # G7
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=83, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=81, start=5.25, end=6.0),   # C7
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif resolves (bar 4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=82, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=110, pitch=84, start=4.875, end=5.25), # C5
    pretty_midi.Note(velocity=110, pitch=82, start=5.25, end=5.625), # A4
    pretty_midi.Note(velocity=110, pitch=80, start=5.625, end=6.0),  # G4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1, snare on 2, hihat on 3, kick on 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
