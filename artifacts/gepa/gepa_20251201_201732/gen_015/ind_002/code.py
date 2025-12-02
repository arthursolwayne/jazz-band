
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches (F2 - Bb2, MIDI 38 - 46)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # Bb2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.0),   # A (E4)
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=2.0),   # C (G4)
    pretty_midi.Note(velocity=70, pitch=67, start=1.5, end=2.0),   # E (A4)
]
piano.notes.extend(piano_notes)

# Sax: motif starts here
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # G (B4)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # E (A4)
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # G (B4)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # E (A4)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line (F2 - Bb2, MIDI 38 - 46)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),  # B2
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.5),   # Bb (D4)
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.5),    # D (F4)
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.5),    # F (G4)
    pretty_midi.Note(velocity=70, pitch=51, start=3.0, end=3.5),    # Ab (Bb4)
]
piano.notes.extend(piano_notes)

# Sax: continues motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # G (B4)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # E (A4)
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # G (B4)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # E (A4)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line (F2 - Bb2, MIDI 38 - 46)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),  # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # Bb2
]
bass.notes.extend(bass_notes)

# Piano: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=5.0),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.0),   # A (E4)
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=5.0),   # C (G4)
    pretty_midi.Note(velocity=70, pitch=67, start=4.5, end=5.0),   # E (A4)
]
piano.notes.extend(piano_notes)

# Sax: finishes motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # G (B4)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # E (A4)
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # G (B4)
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # E (A4)
]
sax.notes.extend(sax_notes)

# Drums: fill the bar (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
