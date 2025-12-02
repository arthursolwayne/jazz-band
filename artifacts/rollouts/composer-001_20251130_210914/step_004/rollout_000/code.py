
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# SAX: Motif starts
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F5
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # G5
    pretty_midi.Note(velocity=100, pitch=61, start=2.0, end=2.25),  # E5
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F5
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # A5
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # G5
]

for note in sax_notes:
    sax.notes.append(note)

# BASS: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.75),  # F3
    pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=2.0),  # Gb3
    pretty_midi.Note(velocity=80, pitch=48, start=2.0, end=2.25),  # G3
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.5),  # Ab3
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),  # A3
    pretty_midi.Note(velocity=80, pitch=51, start=2.75, end=3.0),  # Bb3
]

for note in bass_notes:
    bass.notes.append(note)

# PIANO: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.75),  # C5
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),  # E5
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.5),  # D5
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.5),  # F5
    pretty_midi.Note(velocity=90, pitch=56, start=2.25, end=2.5),  # Ab5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# SAX: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F5
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # G5
    pretty_midi.Note(velocity=100, pitch=61, start=3.5, end=3.75),  # E5
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # F5
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),  # A5
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # G5
]

for note in sax_notes:
    sax.notes.append(note)

# BASS: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.25),  # Bb3
    pretty_midi.Note(velocity=80, pitch=53, start=3.25, end=3.5),  # B3
    pretty_midi.Note(velocity=80, pitch=54, start=3.5, end=3.75),  # C4
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.0),  # Db4
    pretty_midi.Note(velocity=80, pitch=56, start=4.0, end=4.25),  # D4
    pretty_midi.Note(velocity=80, pitch=57, start=4.25, end=4.5),  # Eb4
]

for note in bass_notes:
    bass.notes.append(note)

# PIANO: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.25),  # C5
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # E5
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # B4
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.0),  # D5
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.0),  # F5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# SAX: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F5
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # G5
    pretty_midi.Note(velocity=100, pitch=61, start=5.0, end=5.25),  # E5
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F5
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),  # A5
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # G5
]

for note in sax_notes:
    sax.notes.append(note)

# BASS: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=80, pitch=59, start=4.75, end=5.0),  # Gb4
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.5),  # Ab4
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),  # A4
    pretty_midi.Note(velocity=80, pitch=63, start=5.75, end=6.0),  # Bb4
]

for note in bass_notes:
    bass.notes.append(note)

# PIANO: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.75),  # F5
    # Bar 4: D7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.5),  # F4
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.5),  # A4
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.5),  # C5
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
