
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

# Drums: Bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5))     # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Bar 2 (D2-G2, MIDI 38-43)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875)) # D2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25)) # G2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=37, start=2.25, end=2.625)) # D2-1 semitone down
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0)) # G2

# Piano: Bar 2 - Open voicing on D7sus4 (D, G, C, F#)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0)) # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0)) # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0)) # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=3.0)) # F#4

# Sax: Bar 2 - Haunting melody (D4, F#4, C4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)) # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0)) # F#4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25)) # C4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5)) # D4 (rest from 2.5 to 3.0)

# Drums: Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)) # Snare on 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0))     # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Bar 3 - Chromatic approach on G2 (F#2 to G2)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375)) # F#2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75)) # D2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125)) # G2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5)) # G2

# Piano: Bar 3 - Open voicing on G7sus4 (G, C, D, F#)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5)) # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5)) # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5)) # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5)) # F#4

# Sax: Bar 3 - Haunting melody (G4, Bb4, D4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25)) # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5)) # Bb4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75)) # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0)) # G4 (rest from 4.0 to 4.5)

# Drums: Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)) # Snare on 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5))     # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Bar 4 - D2 again, with a chromatic approach (C#2 to D2)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=35, start=4.5, end=4.875)) # C#2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25)) # D2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625)) # D2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0)) # D2

# Piano: Bar 4 - Open voicing on D7sus4, but resolving on D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0)) # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0)) # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0)) # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=6.0)) # F#4

# Sax: Bar 4 - Haunting melody (D4, F#4, rest)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75)) # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0)) # F#4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25)) # D4 (rest from 5.25 to 6.0)

# Drums: Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)) # Snare on 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0))     # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
