
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D
# D -> C# -> B -> A -> G -> F# -> E -> D -> C# -> B -> A -> G -> F# -> E -> D -> C#
bass_notes = [
    (1.5, 62),  # D
    (1.75, 61),  # C#
    (2.0, 60),  # B
    (2.25, 59),  # A
    (2.5, 57),  # G
    (2.75, 56),  # F#
    (3.0, 55),  # E
    (3.25, 62),  # D
    (3.5, 61),  # C#
    (3.75, 60),  # B
    (4.0, 59),  # A
    (4.25, 57),  # G
    (4.5, 56),  # F#
    (4.75, 55),  # E
    (5.0, 62),  # D
    (5.25, 61),  # C#
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Diane: 7th chords on 2 and 4
# D7 (D F# A C) on 2 and 4

# Bar 2: 2 and 4 at 1.75 and 2.25
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0))

piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5))

# Bar 3: 2 and 4 at 3.25 and 3.75
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5))

piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0))

# Bar 4: 2 and 4 at 4.75 and 5.25
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0))

piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5))

# Dante: Your motif
# Start on D, move to F#, then B, back to D
# D (62), F# (64), B (67), D (62)

# Bar 2
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5))

# Bar 3
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5))

# Bar 4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=6.25, end=6.5))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
