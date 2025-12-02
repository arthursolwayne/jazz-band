
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
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 -> F -> Eb -> D
# Bar 2: Dm7 (D F A C) -> F (F A C E)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5))  # C

# Bar 3: Leave it hanging (F -> Eb)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0))  # Eb

# Bar 4: Come back and finish it (D)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0))  # C

# Bass: Walking line, chromatic approaches, never the same note twice.
# Dm7 -> F -> Eb -> D
# Bar 2: D -> C -> B -> A -> G -> F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=1.625, end=1.75))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=59, start=1.75, end=1.875))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=1.875, end=2.0))  # A

# Bar 3: F -> E -> D -> C -> B -> A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.125))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.125, end=2.25))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.375))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=2.375, end=2.5))  # C

# Bar 4: Eb -> D -> C -> B -> A -> G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.625))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=2.75))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=2.875))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=59, start=2.875, end=3.0))  # B

# Piano: 7th chords, comp on 2 and 4.
# Dm7 -> F7 -> Eb7 -> Dm7
# Bar 2: Dm7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0))  # C

# Bar 3: F7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=2.75, end=3.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=3.0))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0))  # E

# Bar 4: Eb7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0))  # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0))  # D

# Drums: Bars 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0))

# Hi-hat on every eighth
for i in range(4, 12):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
