
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - Bar 2 (Walking line: F2, A2, C3, D3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # A2
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # D3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),   # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),   # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 2: Melody
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # G (motif start)
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),  # Bb (end of motif)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums - Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - Bar 3 (Walking line: Eb3, D3, F2, A2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # Eb3
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # D3
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),  # A2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),   # Bb (MIDI 50)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),   # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 3: Melody (repeat motif with slight variation)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125), # A (chromatic approach)
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums - Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass - Bar 4 (Walking line: G2, A2, C3, D3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.625), # C3
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0),  # D3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 4: Fmaj7 (F, A, C, E) with resolution
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),   # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=6.0),   # A
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),   # C
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),   # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 4: Melody (resolve motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # D (resolution)
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # Bb (end of motif)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums - Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
