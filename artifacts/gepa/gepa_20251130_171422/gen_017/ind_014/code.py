
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-hats on every eighth
for i in range(0, 4):
    start = i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dorian mode, start with a motif that ends on a suspension

# Sax: F, G, Ab, Bb (F7sus4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75))   # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=2.0))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25))  # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5))  # F (suspension)

# Bass: Walking line with chromatic approaches
# F -> Gb -> G -> Ab -> Bb -> B -> C -> Db -> D -> Eb -> F

bass_notes = [77, 76, 78, 79, 81, 82, 84, 83, 85, 87, 77]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Bar 2: F7 on 2 (F, A, C, Eb)
# Bar 3: Bb7 on 4 (Bb, D, F, Ab)

# Bar 2 (1.5 - 3.0s) - F7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.125))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.125))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=2.0, end=2.125))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=2.0, end=2.125))  # Eb

# Bar 3 (3.0 - 4.5s) - Bb7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=3.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=3.875))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=3.875))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=3.875))  # Ab

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation of the motif, resolving the suspension

sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.25))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=3.25, end=3.5))   # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75))   # B
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0))   # A

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Develop the motif, introducing a chromatic line

sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0))   # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.25))   # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5))   # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=5.5, end=5.75))   # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=5.75, end=6.0))   # Bb

# Bass: Continue the walking line
bass_notes = [79, 80, 82, 84, 85, 87, 89, 88, 90, 92, 93]
for i, note in enumerate(bass_notes):
    start = 3.0 + i * 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375))

# Piano: 7th chords on 2 and 4
# Bar 4: F7 on 2 (F, A, C, Eb)
# Bar 4: Bb7 on 4 (Bb, D, F, Ab)

# Bar 4 (4.5 - 6.0s) - F7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.125))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=5.0, end=5.125))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=5.0, end=5.125))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=5.0, end=5.125))  # Eb

# Bar 4 (4.5 - 6.0s) - Bb7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=5.75, end=5.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=5.75, end=5.875))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=79, start=5.75, end=5.875))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=5.75, end=5.875))  # Ab

# Drums: Bar 3 (3.0 - 4.5s)
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))

# Hi-hats on every eighth
for i in range(0, 4):
    start = 3.0 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.125))

# Drums: Bar 4 (4.5 - 6.0s)
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375))  # Out of range

# Hi-hats on every eighth
for i in range(0, 4):
    start = 4.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
