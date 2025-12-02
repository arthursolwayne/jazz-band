
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
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
# Dm7 -> G7 -> Cmaj7 -> F7
# D F# A C -> G B D F -> C E G B -> F A C E

# Bar 2: Dm7 (1.5s)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.625))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=1.625, end=1.75))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=55, start=1.75, end=1.875))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=52, start=1.875, end=2.0))  # C

# Bar 3: G7 (2.0s)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.125))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=2.125, end=2.25))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.375))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.375, end=2.5))  # F

# Bar 4: Cmaj7 (2.5s)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.625))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=2.75))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=2.75, end=2.875))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=2.875, end=3.0))  # B

# Piano: 7th chords on 2 and 4
# Bar 2: Dm7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0))  # C

# Bar 3: G7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.5))  # F

# Bar 4: Cmaj7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=3.0))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=3.0))  # B

# Sax: Short motif, start it, leave it hanging, come back and finish it
# D F# G A -> (rest) -> D F# G A

# Bar 2: D F# G A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875))  # F#
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.125))  # A

# Bar 4: Return and finish it
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.875))  # F#
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.875, end=3.0))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.125))  # A

# Drums: continuation of kick, snare, and hihat for bars 2-4
# Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.375, end=2.5))  # Snare on 2
for i in range(0, 4):
    start = 2.0 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.75, end=3.125))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.125, end=3.25))  # Snare on 2
for i in range(0, 4):
    start = 2.75 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.875, end=4.0))  # Snare on 2
for i in range(0, 4):
    start = 3.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
