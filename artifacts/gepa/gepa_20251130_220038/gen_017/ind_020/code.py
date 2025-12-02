
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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
# Sax: melody starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line starting on F (4th fret of E string)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 (F, A, C#, E)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.25),  # C#
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.25),  # E
    # Bar 3: G7 (Bb, D, F, A)
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0),  # A
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat the motif with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=51, start=4.125, end=4.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: D7 (F, A, C#, E)
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.75),  # C#
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.75),  # E
    # Bar 4: Bb7 (D, F, Ab, C)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.5),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Bb7 (D, F, Ab, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=5.25),  # C
    # Bar 4: resolution to F7 (A, C, Eb, G)
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=6.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=6.0),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.375, end=4.625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.625, end=4.75),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
