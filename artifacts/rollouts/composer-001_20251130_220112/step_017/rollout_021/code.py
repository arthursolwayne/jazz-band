
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

# Sax melody: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=105, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=105, pitch=69, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=105, pitch=67, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=105, pitch=64, start=2.75, end=3.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: Walking in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=51, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=49, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=2.75, end=3.0),  # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # Db
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # Db
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=105, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=105, pitch=69, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=105, pitch=67, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=105, pitch=64, start=4.25, end=4.5),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: Continue walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=80, pitch=47, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=80, pitch=48, start=4.25, end=4.5),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Continue comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # Db
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=105, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=105, pitch=69, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=105, pitch=71, start=5.5, end=5.75),  # Db
    pretty_midi.Note(velocity=105, pitch=69, start=5.75, end=6.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: Finish walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=53, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=80, pitch=47, start=5.75, end=6.0),  # B
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Resolve on 1 and 3
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # Db
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Continue the pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
