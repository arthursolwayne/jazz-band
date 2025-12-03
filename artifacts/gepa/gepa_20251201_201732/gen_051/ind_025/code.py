
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet starts (1.5 - 3.0s)

# Marcus: Walking bass line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D -> C# -> E -> D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # C#3
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # E3
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: D7 (G4, A4, D5, F#4)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F#4

    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F#4
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif starts on 1, leaves it hanging, returns on 3
# D (D4), F# (F#4), G (G4), C (C4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),  # C4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: (3.0 - 4.5s)

# Marcus: B -> A -> C -> B
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # B3
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75),  # A3
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # B3
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Cmaj7 (E4, G4, C5, E4)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # E4

    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # C5
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # E4
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif repeats with variation
# D (D4), C (C4), B (B4), D (D4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75),  # C4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # B4
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: (4.5 - 6.0s)

# Marcus: D -> C# -> E -> D again, but with a half-step chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # C#3
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.625),  # C#3
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: D7 (G4, A4, D5, F#4) again, with a slight tension in the last chord
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # F#4

    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),  # D5
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # G4
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Repeat motif with a slight resolution
# D (D4), F# (F#4), G (G4), C (C4) again but with a minor delay on last note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),  # C4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Final fill
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
