
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm (F, Ab, D, C, F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),  # C2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # Eb5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - start with a motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # Bb4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm (F, Ab, D, C, F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75), # Ab2
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),  # C2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Ab5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # Eb4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm (F, Ab, D, C, F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),  # C2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875),  # Bb4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Resolve the motif, leave space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # F4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
