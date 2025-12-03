
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: D2 (38) -> G2 (43) -> A2 (45) -> C3 (52) -> B2 (46) -> D2 (38)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar
# Bar 2: Fmaj7 (F, A, C, E) - Root position
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (71)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A (76)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # C (79)
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0),  # E (84)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in F, short and haunting
# Notes: F (71), G (72), Bb (74), F (71)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: D2 (38) -> G2 (43) -> A2 (45) -> C3 (52) -> B2 (46) -> D2 (38)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar
# Bar 3: G7 (G, B, D, F) - Root position
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # G (74)
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=4.5),  # B (79)
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=4.5),  # D (82)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # F (71)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Repeat motif, slightly altered
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: D2 (38) -> G2 (43) -> A2 (45) -> C3 (52) -> B2 (46) -> D2 (38)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=46, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=38, start=6.375, end=6.75),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar
# Bar 4: Cm7 (C, Eb, G, Bb) - Root position
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # C (79)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # Eb (76)
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=6.0),  # G (82)
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=6.0),  # Bb (81)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One last phrase, resolving
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=74, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: 3.0 - 4.5s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: 4.5 - 6.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
