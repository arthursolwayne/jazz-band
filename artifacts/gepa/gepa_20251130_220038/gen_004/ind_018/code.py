
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=35, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=33, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=80, pitch=34, start=2.625, end=3.0),  # B
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comping on 2 and 4, 7th chords
piano_notes = [
    # Bar 2: 7th chord on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),   # F
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: motif - short, singable, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=35, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=33, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=80, pitch=34, start=4.125, end=4.5),  # B
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comping on 2 and 4, 7th chords
piano_notes = [
    # Bar 3: 7th chord on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),   # F
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: motif continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=35, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=33, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=80, pitch=34, start=5.625, end=6.0),  # B
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comping on 2 and 4, 7th chords
piano_notes = [
    # Bar 4: 7th chord on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),   # F
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: motif completion
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
