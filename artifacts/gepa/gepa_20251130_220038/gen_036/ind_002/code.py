
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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

# Bass line: Chromatic walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),   # G#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E♭)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=2.25),  # B♭
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=2.25),  # E♭
    # Bar 3: B♭7 (B♭, D, F, A)
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=3.0),  # B♭
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=3.0),  # B♭
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=3.0),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif (F, G, A, B♭)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),   # B♭
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: Chromatic walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=80, pitch=54, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),   # B#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: F7 (F, A, C, E♭)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.75),  # B♭
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.75),  # E♭
    # Bar 4: C7 (C, E, G, B♭)
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=3.75, end=4.5),  # E
    pretty_midi.Note(velocity=90, pitch=81, start=3.75, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=3.75, end=4.5),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue with motif and resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),  # E♭
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125),  # B♭
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: Chromatic walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=56, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=80, pitch=58, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0),   # D#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 (F, A, C, E♭)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=5.25),  # B♭
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=5.25),  # E♭
    # Bar 4 (end): A7 (A, C#, E, G)
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=81, start=5.25, end=6.0),  # C#
    pretty_midi.Note(velocity=90, pitch=83, start=5.25, end=6.0),  # E
    pretty_midi.Note(velocity=90, pitch=81, start=5.25, end=6.0),  # C#
    pretty_midi.Note(velocity=90, pitch=83, start=5.25, end=6.0),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Return to motif and resolve with a cry
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=81, start=5.25, end=5.625),  # E♭
    pretty_midi.Note(velocity=100, pitch=84, start=5.625, end=6.0),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo.mid")
