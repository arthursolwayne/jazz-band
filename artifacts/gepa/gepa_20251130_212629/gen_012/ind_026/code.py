
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

# Bar 1: Kick at 0.0, 0.75
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125))

# Snare at 0.375, 1.125
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))

# Hihat on every eighth
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * 0.375, end=i * 0.375 + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D, chromatic approaches, no repeated notes
# Bar 2: D - C# - E - F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0))

# Bar 3: F# - G - A - Bb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5))

# Bar 4: Bb - A - G - F#
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0))

# Piano: 7th chords, comp on 2 and 4
# Bar 2: D7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625))  # F#

# Bar 3: D7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75))  # F#

# Bar 4: D7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25))  # F#

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))

# Hihat on every eighth
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i * 0.375, end=1.5 + i * 0.375 + 0.1875))

# Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))

# Hihat on every eighth
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0 + i * 0.375, end=3.0 + i * 0.375 + 0.1875))

# Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875))  # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625))  # D

# Bar 3: Leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375))  # E

# Bar 4: Come back and finish it
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625))  # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0))   # D

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
