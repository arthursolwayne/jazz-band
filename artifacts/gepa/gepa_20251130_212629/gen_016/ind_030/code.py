
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.875))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: 4 notes, slight syncopation, ends on a rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.625, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0))

# Bass: walking line, chromatic approach
bass.notes.append(pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=1.625, end=1.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.0))

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=59, start=1.5, end=1.625))  # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.625))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=63, start=1.5, end=1.625))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.625))

piano.notes.append(pretty_midi.Note(velocity=95, pitch=59, start=2.25, end=2.375))  # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.375))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=63, start=2.25, end=2.375))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.375))

# Drums: continue with kick, snare, hihat
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation of motif, but with a rest in between
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.125))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.5))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.625, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=3.875, end=4.0))

# Bass: walking line with chromatic approach
bass.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.125))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=3.125, end=3.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.5))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=3.5, end=3.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=3.625, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=3.875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=3.875, end=4.0))

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=59, start=3.0, end=3.125))  # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=63, start=3.0, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.125))

piano.notes.append(pretty_midi.Note(velocity=95, pitch=59, start=3.75, end=3.875))  # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=63, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=3.875))

# Drums: continue with kick, snare, hihat
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.75))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: end on a rest, question mark
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.625, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=63, start=4.875, end=5.0))

# Bass: chromatic walking line
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=56, start=4.625, end=4.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=4.75, end=4.875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.0))

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=59, start=4.5, end=4.625))  # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=63, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.625))

piano.notes.append(pretty_midi.Note(velocity=95, pitch=59, start=5.25, end=5.375))  # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.375))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=63, start=5.25, end=5.375))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.375))

# Drums: continue with kick, snare, hihat
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.25))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("intro.mid")
