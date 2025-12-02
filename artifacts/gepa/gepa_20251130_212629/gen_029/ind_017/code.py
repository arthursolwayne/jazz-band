
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

# Hihat on every eighth note
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line, chromatic approaches
# D Dorian: D, E, F#, G, A, B, C
# Walking bass line: D F# G A | D F# G B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=1.625, end=1.75))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=1.875))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.125))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=2.125, end=2.25))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.375))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=2.375, end=2.5))  # B

# Diane: 7th chords, comp on 2 and 4
# D7: D, F#, A, C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.75))  # F#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75))  # C

# Diane: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.5))  # F#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5))  # C

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125))  # Snare on 4
for i in range(4, 8):
    start = (i * 0.375) + 1.5
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D as root, 7th chord, maybe a triplet or something that feels unfinished

# Bar 2: Melody starts
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75))  # A (D7)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875))  # B
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0))  # A

# Bar 3: Rest
# Bar 4: Repeat motif, but altered slightly
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.375))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5))  # A

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line, chromatic approaches
# D F# G A | D F# G B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.125))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=3.125, end=3.25))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.375))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.625))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=3.625, end=3.75))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=3.875))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.875, end=4.0))  # B

# Diane: 7th chords, comp on 2 and 4
# D7: D, F#, A, C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.25))  # F#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25))  # C

# Diane: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.0))  # F#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0))  # C

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3: 3.0 - 4.5s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625))  # Snare on 4
for i in range(8, 12):
    start = (i * 0.375) + 3.0
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
