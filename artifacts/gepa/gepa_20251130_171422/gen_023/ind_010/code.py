
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Use subtle dynamics, not just loud or soft, but with shading and texture.
# Create rhythmic interest by varying the placement of the kick, snare, and hihat.
# Use rests and space to build tension.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Add variation in dynamics and placement to create interest
drums.notes.append(pretty_midi.Note(velocity=60, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=50, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=36, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875))

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Saxophone motif: concise, emotional, singable, not just a sequence of notes

# Saxophone: D - F# - A - B (motif)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0))

# Bass line: walking with chromatic approaches, melodic not just rhythmic
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=4.125, end=4.5))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=75, start=4.5, end=4.875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=5.625, end=6.0))

# Piano: 7th chords, comp on 2 and 4, with emotion
# D7 on 2 and 4
# D7 = D, F#, A, C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=66, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=75, pitch=60, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=66, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=75, pitch=60, start=3.375, end=3.75))

# Drums: continue with the pattern, adding variation for tension
drums.notes.append(pretty_midi.Note(velocity=60, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=50, pitch=42, start=1.5, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=36, start=2.625, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.25))
drums.notes.append(pretty_midi.Note(velocity=50, pitch=42, start=2.625, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=36, start=3.75, end=4.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.375))
drums.notes.append(pretty_midi.Note(velocity=50, pitch=42, start=3.75, end=4.375))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=36, start=4.875, end=5.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.5))
drums.notes.append(pretty_midi.Note(velocity=50, pitch=42, start=4.875, end=5.5))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=36, start=5.625, end=5.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=6.0, end=6.25))
drums.notes.append(pretty_midi.Note(velocity=50, pitch=42, start=5.625, end=6.25))

# Add a final hi-hat to close the bar
drums.notes.append(pretty_midi.Note(velocity=50, pitch=42, start=6.0, end=6.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
