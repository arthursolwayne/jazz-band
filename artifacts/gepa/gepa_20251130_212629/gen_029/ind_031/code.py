
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

# Drums in Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),    # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=38, start=1.375, end=1.5),    # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),   # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (walking, chromatic)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.75),    # F
    pretty_midi.Note(velocity=80, pitch=45, start=1.75, end=2.0),    # F#
    pretty_midi.Note(velocity=80, pitch=46, start=2.0, end=2.25),    # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),    # A
    pretty_midi.Note(velocity=80, pitch=46, start=2.5, end=2.75),    # G
    pretty_midi.Note(velocity=80, pitch=44, start=2.75, end=3.0),    # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp (7th chords on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),    # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),    # C
    pretty_midi.Note(velocity=90, pitch=76, start=1.75, end=2.0),    # E
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),    # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),    # C
    pretty_midi.Note(velocity=90, pitch=76, start=2.75, end=3.0),    # E
]

for note in piano_notes:
    piano.notes.append(note)

# Drums in Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),  # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.5),    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.25),  # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.25),    # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone motif (variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),   # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),   # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (walking, chromatic)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.25),    # F
    pretty_midi.Note(velocity=80, pitch=45, start=3.25, end=3.5),    # F#
    pretty_midi.Note(velocity=80, pitch=46, start=3.5, end=3.75),    # G
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.0),    # A
    pretty_midi.Note(velocity=80, pitch=46, start=4.0, end=4.25),    # G
    pretty_midi.Note(velocity=80, pitch=44, start=4.25, end=4.5),    # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp (7th chords on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),    # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),    # C
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5),    # E
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),    # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),    # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.25, end=4.5),    # E
]

for note in piano_notes:
    piano.notes.append(note)

# Drums in Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.0),    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.375),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.75),  # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.75),    # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone motif (variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),   # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (walking, chromatic)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.75),    # F
    pretty_midi.Note(velocity=80, pitch=45, start=4.75, end=5.0),    # F#
    pretty_midi.Note(velocity=80, pitch=46, start=5.0, end=5.25),    # G
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.5),    # A
    pretty_midi.Note(velocity=80, pitch=46, start=5.5, end=5.75),    # G
    pretty_midi.Note(velocity=80, pitch=44, start=5.75, end=6.0),    # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp (7th chords on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),    # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),    # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.75, end=5.0),    # E
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),    # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),    # C
    pretty_midi.Note(velocity=90, pitch=76, start=5.75, end=6.0),    # E
]

for note in piano_notes:
    piano.notes.append(note)

# Drums in Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.5),    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.5, end=5.875),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.875, end=6.25),  # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=38, start=6.0, end=6.25),    # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
