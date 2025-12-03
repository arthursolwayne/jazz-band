
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass (Marcus): D2 (38) -> F2 (41) with chromatic approach from E2 (40)
# D2 = 38, F2 = 41
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=41, start=2.125, end=2.5),
    pretty_midi.Note(velocity=90, pitch=38, start=2.5, end=2.875),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Dm7 (D-F-A-C) -> Gm7 (G-Bb-D-F) -> Cm7 (C-Eb-G-Bb) -> F7 (F-A-C-E)
# Open voicings, resolve on 4
piano_notes = [
    # Bar 2: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # C4
    # Bar 3: Gm7 (G-Bb-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.5),  # F4
    # Bar 4: Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=3.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # Bb4
]
for note in piano_notes:
    piano.notes.append(note)

# Drums (Bar 2): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.125),
    pretty_midi.Note(velocity=100, pitch=36, start=2.125, end=2.5),
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.5)
]
for note in drum_notes:
    drums.notes.append(note)

# Sax (Bar 2): Motif (D4 - F4 - D4 - rest), then on Bar 3: (F4 - A4 - rest), Bar 4: (C4 - D4 - rest)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),   # F4
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.25),  # C4
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass (Marcus): D2 (38) -> E2 (40) with chromatic approach from Eb2 (39)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=39, start=3.375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=40, start=3.625, end=4.0),
    pretty_midi.Note(velocity=90, pitch=38, start=4.0, end=4.375),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Dm7 (D-F-A-C) -> Gm7 (G-Bb-D-F) -> Cm7 (C-Eb-G-Bb) -> F7 (F-A-C-E)
# Open voicings, resolve on 4
piano_notes = [
    # Bar 3: Gm7 (G-Bb-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),  # F4
    # Bar 4: F7 (F-A-C-E)
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=4.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # C4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0),  # E4
]
for note in piano_notes:
    piano.notes.append(note)

# Drums (Bar 3): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5)
]
for note in drum_notes:
    drums.notes.append(note)

# Sax (Bar 3 and 4): Motif continuation, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
