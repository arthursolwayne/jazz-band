
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# Dmin7 = D, F, A, C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [
    (1.5, 62),  # D
    (1.75, 63),  # Eb
    (2.0, 64),  # F
    (2.25, 65),  # G
    (2.5, 67),  # A
    (2.75, 68),  # Bb
    (3.0, 69),  # B
    (3.25, 71),  # C
    (3.5, 62),  # D
    (3.75, 63),  # Eb
    (4.0, 64),  # F
    (4.25, 65),  # G
    (4.5, 67),  # A
    (4.75, 68),  # Bb
    (5.0, 69),  # B
    (5.25, 71),  # C
    (5.5, 62),  # D
    (5.75, 63),  # Eb
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25))

# Diane: 7th chords, comp on 2 and 4
# Dmin7 = D, F, A, C
# Dmin7 = D, F, A, C
# Dmin7 = D, F, A, C
# Dmin7 = D, F, A, C
# Dmin7 = D, F, A, C
# Dmin7 = D, F, A, C

# Bar 2 (1.5 - 2.0s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0))

# Bar 3 (2.5 - 3.0s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=3.0))

# Bar 4 (3.5 - 4.0s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=4.0))

# You: This is your moment. One short motif, make it sing.
# Dmin7 = D, F, A, C
# Motif: D -> A -> C -> F (one bar), then repeat with variation

# Bar 2 (1.5 - 2.0s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0))

# Bar 3 (2.5 - 3.0s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=2.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=2.875, end=3.0))

# Bar 4 (3.5 - 4.0s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=3.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.875, end=4.0))

# Add more fills in bar 4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.125))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.375))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=4.375, end=4.5))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.625, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0))

# Drums: continue in bar 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.25, end=4.625))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))

# Hihat on every eighth
for i in range(4, 12):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Add more hihats in bar 4
for i in range(12, 16):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
