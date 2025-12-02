
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif starts
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25))  # F#4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # A4

# Bass: walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875))  # D3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.25))  # E3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625))  # C3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=2.625, end=3.0))  # D3

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25))  # D7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=2.25))  # F#7

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: motif continues
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75))  # F#4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125))  # A4

# Bass: walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375))  # D3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75))  # E3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.125))  # C3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=4.125, end=4.5))  # D3

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75))  # D7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.75))  # F#7

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.25, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: motif ends
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25))  # F#4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625))  # G4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0))  # D4

# Bass: walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875))  # D3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25))  # E3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625))  # C3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=5.625, end=6.0))  # D3

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.25))  # D7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=5.25))  # F#7

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.75, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
