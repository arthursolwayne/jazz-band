
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
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax: Start the motif
# F7 -> Bb7 -> D7 -> F7 (sax line)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.6875))  # F7
sax.notes.append(pretty_midi.Note(velocity=100, pitch=80, start=1.6875, end=1.875))  # Bb7
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.0625))  # D7
sax.notes.append(pretty_midi.Note(velocity=100, pitch=87, start=2.0625, end=2.25))  # F7

# Bass: Walking line in F
# F -> G -> Ab -> A -> Bb -> C -> Db -> D -> E -> F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=78, start=1.5, end=1.625))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=81, start=1.625, end=1.75))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=79, start=1.75, end=1.875))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=82, start=1.875, end=2.0))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=83, start=2.0, end=2.125))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=84, start=2.125, end=2.25))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=2.25, end=2.375))  # Db
bass.notes.append(pretty_midi.Note(velocity=80, pitch=85, start=2.375, end=2.5))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=87, start=2.5, end=2.625))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=78, start=2.625, end=2.75))  # F

# Piano: 7th chords on 2 and 4
# F7 on 2 (1.5-1.75s), Bb7 on 4 (2.0-2.25s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=87, start=1.5, end=1.75))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=1.5, end=1.75))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=84, start=1.5, end=1.75))  # C7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.75))  # E7

piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=2.0, end=2.25))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=2.0, end=2.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.25))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=2.0, end=2.25))  # Ab7

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: Repeat motif with variation
sax.notes.append(pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.1875))  # F7
sax.notes.append(pretty_midi.Note(velocity=100, pitch=80, start=3.1875, end=3.375))  # Bb7
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.5625))  # D7
sax.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=3.5625, end=3.75))  # E7

# Bass: Walking line in F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=78, start=3.0, end=3.125))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=81, start=3.125, end=3.25))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=79, start=3.25, end=3.375))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=82, start=3.375, end=3.5))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=83, start=3.5, end=3.625))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=84, start=3.625, end=3.75))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=3.75, end=3.875))  # Db
bass.notes.append(pretty_midi.Note(velocity=80, pitch=85, start=3.875, end=4.0))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=87, start=4.0, end=4.125))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=78, start=4.125, end=4.25))  # F

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=87, start=3.0, end=3.25))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=3.0, end=3.25))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=84, start=3.0, end=3.25))  # C7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.25))  # E7

piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=3.5, end=3.75))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=3.5, end=3.75))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=3.5, end=3.75))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=3.75))  # Ab7

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax: Resolve the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.6875))  # F7
sax.notes.append(pretty_midi.Note(velocity=100, pitch=80, start=4.6875, end=4.875))  # Bb7
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.0625))  # D7
sax.notes.append(pretty_midi.Note(velocity=100, pitch=87, start=5.0625, end=5.25))  # F7

# Bass: Walking line in F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=78, start=4.5, end=4.625))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=81, start=4.625, end=4.75))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=79, start=4.75, end=4.875))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=82, start=4.875, end=5.0))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=83, start=5.0, end=5.125))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=84, start=5.125, end=5.25))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=5.25, end=5.375))  # Db
bass.notes.append(pretty_midi.Note(velocity=80, pitch=85, start=5.375, end=5.5))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=87, start=5.5, end=5.625))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=78, start=5.625, end=5.75))  # F

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=87, start=4.5, end=4.75))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=4.5, end=4.75))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=84, start=4.5, end=4.75))  # C7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.75))  # E7

piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=5.0, end=5.25))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=5.0, end=5.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=5.0, end=5.25))  # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=5.0, end=5.25))  # Ab7

# Drums: Bar 4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0))

# Hihat on every eighth
for i in range(0, 4):
    start = 4.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('intro_wayne.mid')
