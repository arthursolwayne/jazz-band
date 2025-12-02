
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5))

# Bass line (walking with chromatic tension)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=1.75, end=2.0))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=59, start=2.0, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5))

# Piano chords (7th chords, comp on 2 and 4)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=2.0))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=3.0))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif (variation, ends on a question)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=4.25, end=4.5))

# Bass line (walking with chromatic tension)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.0, end=4.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=4.25, end=4.5))

# Piano chords (7th chords, comp on 2 and 4)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.0))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.25))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.0))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.25))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.5))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif (rest on the last beat)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0))

# Bass line (walking with chromatic tension)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.5))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=5.5, end=5.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=5.75, end=6.0))

# Piano chords (7th chords, comp on 2 and 4)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.5))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.5))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro.mid")
