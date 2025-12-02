
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus
# Walking line with chromatic approaches
bass_notes = [
    (1.5, 48), (1.75, 50), (2.0, 49), (2.25, 51),
    (2.5, 52), (2.75, 50), (3.0, 49), (3.25, 51),
    (3.5, 53), (3.75, 51), (4.0, 50), (4.25, 52),
    (4.5, 53), (4.75, 51), (5.0, 50), (5.25, 52)
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25))

# Piano - Diane
# 7th chords on 2 and 4, comping with aggression
piano_notes = [
    (2.0, 60), (2.0, 64), (2.0, 62), (2.0, 65),
    (2.5, 60), (2.5, 64), (2.5, 62), (2.5, 65),
    (3.0, 60), (3.0, 64), (3.0, 62), (3.0, 65),
    (3.5, 60), (3.5, 64), (3.5, 62), (3.5, 65),
    (4.0, 60), (4.0, 64), (4.0, 62), (4.0, 65),
    (4.5, 60), (4.5, 64), (4.5, 62), (4.5, 65)
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=start, end=start + 0.25))

# Drums - Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=3.0))

# Bar 3: 3.0 - 4.5s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=4.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.5))

# Bar 4: 4.5 - 6.0s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.5, end=6.0))

# Saxophone - Dante
# Simple motif: Fm7 (F, Ab, Bb, D), start on F, play the motif over 3 bars, leave it hanging
sax_notes = [
    (1.5, 66), (1.75, 64), (2.0, 62), (2.25, 67),
    (2.5, 66), (2.75, 64), (3.0, 62), (3.25, 67),
    (3.5, 66), (3.75, 64), (4.0, 62), (4.25, 67),
    (4.5, 66), (4.75, 64), (5.0, 62), (5.25, 67),
    (5.5, 66), (5.75, 64)
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
