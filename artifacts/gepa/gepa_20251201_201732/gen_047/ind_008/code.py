
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),    # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),   # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),   # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),    # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),    # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: walking bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # D (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # F (flat 3)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # A (5th)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: piano comp, open voicings
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.0),  # Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=2.0),

    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.5),  # Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.5),

    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=59, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=52, start=2.5, end=3.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: sax melody, one motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D (sax in Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: walking bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # F (flat 3)
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # A (5th)
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: piano comp, open voicings
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.5),  # Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.5),

    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.0),  # Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=58, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=4.0),

    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.5),  # C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=59, start=4.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=57, start=4.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=52, start=4.0, end=4.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: sax melody, finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: walking bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0),  # A (5th)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: piano comp, open voicings
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=5.0),  # Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=5.0),

    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.5),  # Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=58, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=55, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=50, start=5.0, end=5.5),

    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=6.0),  # C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=59, start=5.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=57, start=5.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=52, start=5.5, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: sax melody, resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),    # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),   # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),   # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),    # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),    # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
