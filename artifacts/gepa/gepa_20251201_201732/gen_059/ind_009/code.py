
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Drums - Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - Bar 2: Root and fifth with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 2: Open voicing, unresolved chord
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 2: Haunting, incomplete motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - Bar 3: Root and fifth with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 3: Open voicing, unresolved chord with shift
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.5),  # A
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 3: Haunting, incomplete motif (continuation)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums - Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bass - Bar 4: Root and fifth with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 4: Open voicing, unresolved chord with shift
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=6.0),  # A
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 4: Haunting, incomplete motif (final phrases)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
