
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.

# Bar 1: 0.0 - 1.5s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.5 + 0.75))

# Bar 2: 1.5 - 3.0s
# Everyone in. Sax starts the motif.

# Bass line (Marcus): Walking line, chromatic approaches, no repeats
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=2.5, end=2.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0))

# Piano (Diane): 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0)) # D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0))

piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0)) # D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=2.75, end=3.0))

# Drums continue
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.75))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging.
# Motif: D - E - F# - G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.6, end=1.7))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.7, end=1.8))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.8, end=1.9))
# Leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.9, end=2.1))

# Bar 3: 3.0 - 4.5s
# Continue the motif with variation

# Bass line continuation
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=3.0, end=3.25))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.0))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=4.0, end=4.25))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5))

# Piano (Diane): 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5)) # D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.5))

piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5)) # D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=4.25, end=4.5))

# Drums continue
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5))

# Sax continuation
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.1, end=3.2))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.2, end=3.3))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.3, end=3.4))
# End with a question, not a statement
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.4, end=3.6))

# Bar 4: 4.5 - 6.0s
# End with a question

# Bass line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=4.75, end=5.0))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=5.75, end=6.0))

# Piano (Diane): 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0)) # D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0))

piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=6.0)) # D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=5.75, end=6.0))

# Drums continue
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0))

# Sax ends with a question
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.6, end=4.7))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.7, end=4.8))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.8, end=5.0))
# End on silence for tension
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.2))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
