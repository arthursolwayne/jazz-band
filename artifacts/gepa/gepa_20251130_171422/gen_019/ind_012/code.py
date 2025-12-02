
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=80, pitch=61, start=2.75, end=3.0),  # Db
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.75),  # F7
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=51, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.5),   # F7
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif in Fm, melodic but sparse
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.1875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.1875, end=2.375), # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.6875, end=2.875), # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0),   # Eb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=3.25, end=3.5),  # Db
    pretty_midi.Note(velocity=80, pitch=63, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.25),  # F7
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.0),   # F7
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif continues, but with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.6875, end=3.875), # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.1875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.1875, end=4.375), # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.375, end=4.5),   # Eb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.625, end=3.9375), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=3.8125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.9375, end=4.25),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.75),  # Db
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=6.0),  # Eb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.75),  # F7
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=51, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.5),   # F7
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.1875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.1875, end=5.375), # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.6875, end=5.875), # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.875, end=6.0),   # Eb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.125, end=5.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.6875),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
