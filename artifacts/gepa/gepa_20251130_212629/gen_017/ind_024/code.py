
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

# Hi-hats on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (1.5, 45), (1.75, 46), (2.0, 48), (2.25, 47),
    (2.5, 50), (2.75, 51), (3.0, 48), (3.25, 47),
    (3.5, 50), (3.75, 51), (4.0, 52), (4.25, 51),
    (4.5, 53), (4.75, 51), (5.0, 48), (5.25, 47)
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (2.0, 64), (2.0, 67), (2.0, 71), (2.0, 69),
    (3.0, 64), (3.0, 67), (3.0, 71), (3.0, 69),
    (4.0, 64), (4.0, 67), (4.0, 71), (4.0, 69)
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Sax: One short motif, start it, leave it hanging. Come back and finish it.
# Melody: F - A - Bb - rest (bar 2), Bb - A - rest - F (bar 3), rest - F - A - Bb (bar 4)
sax_notes = [
    (2.0, 65), (2.125, 68), (2.25, 67), (2.375, 69), # F - A - Bb - rest
    (3.0, 67), (3.125, 68), (3.25, 69), (3.375, 65), # Bb - A - rest - F
    (4.0, 65), (4.125, 68), (4.25, 67), (4.375, 69)  # F - A - Bb - rest
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125))

# Add drum fills on bars 2 and 3
# Bar 2 fill: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.125, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0))

# Bar 3 fill: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.25, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
