
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

# Drums - Bar 1
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

# Bass - Bar 2 (F2 - Bb2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25), # Gb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625), # F2 (root)
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # Bb2 (fifth)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 2 (Fm7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # D4
]
for note in piano_notes:
    piano.notes.append(note)

# Drums - Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Sax - Bar 2 (motif A)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - Bar 3 (Ab2 - C2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125), # Ab2
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # Bb2 (fifth)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 3 (Ab7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # Bb4 (double)
]
for note in piano_notes:
    piano.notes.append(note)

# Drums - Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Sax - Bar 3 (motif B)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # Ab4
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass - Bar 4 (Bb2 - F2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # Bb2
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25), # C2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625), # Bb2
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),  # F2 (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 4 (Fm7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # D4
]
for note in piano_notes:
    piano.notes.append(note)

# Drums - Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Sax - Bar 4 (motif A again, finishing it)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # D4
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_midnight_moment.mid")
