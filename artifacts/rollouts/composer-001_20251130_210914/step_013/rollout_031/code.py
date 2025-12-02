
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

# Hi-hat on every eighth
hihat_start = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
hihat_end = [0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3.0]
for s, e in zip(hihat_start, hihat_end):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=s, end=e))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
# Dmin7 (D F A C)
# Bar 2: D -> Eb -> F -> G
bass_notes = [
    (1.5, 62),  # D
    (1.875, 63),  # Eb
    (2.25, 64),  # F
    (2.625, 65),  # G
    # Bar 3: A -> Bb -> B -> C
    (3.0, 67),  # A
    (3.375, 68),  # Bb
    (3.75, 69),  # B
    (4.125, 70),  # C
    # Bar 4: D -> Eb -> F -> G (repeat)
    (4.5, 62),  # D
    (4.875, 63),  # Eb
    (5.25, 64),  # F
    (5.625, 65)  # G
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Piano: 7th chords, comp on 2 and 4
# Dmin7 (D F A C)
# Bar 2: D F A C on beat 2
piano_notes = [
    # Bar 2, beat 2
    (1.875, 62), (1.875, 65), (1.875, 67), (1.875, 70),
    # Bar 3, beat 4
    (4.125, 62), (4.125, 65), (4.125, 67), (4.125, 70),
    # Bar 4, beat 2
    (4.875, 62), (4.875, 65), (4.875, 67), (4.875, 70)
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=start, end=start + 0.375))

# Sax: One short motif, start it, leave it hanging, come back and finish it
# D -> Eb -> F -> D (motif)
# Bar 2, beat 1: D
# Bar 2, beat 3: F
# Bar 3, beat 1: Eb
# Bar 3, beat 3: D
sax_notes = [
    (1.5, 62),  # D
    (2.25, 64),  # F
    (3.0, 63),  # Eb
    (3.75, 62)   # D
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=start + 0.25))

# Drums continue for bars 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.625, end=4.875))

# Hi-hat on every eighth
hihat_start = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]
hihat_end = [1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625, 6.0]
for s, e in zip(hihat_start, hihat_end):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=s, end=e))

midi.instruments.extend([sax, bass, piano, drums])
