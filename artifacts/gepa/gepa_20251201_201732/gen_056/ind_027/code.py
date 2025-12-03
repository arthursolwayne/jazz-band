
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Fm7 (F, Ab, C, Db) - root and fifth with chromatic approach
bass.notes.append(pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875))  # F2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25)) # Gb2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625)) # C3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0))  # Bb3

# Piano: Fm7 - open voicing, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875))  # F4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875))  # Ab4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875))  # C5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875))  # Bb5
piano.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625))  # F4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625))  # Ab4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625))  # C5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625))  # Bb5

# Sax: Start motif (F, Ab, Bb)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75))  # F4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0))  # Ab4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25))  # Bb4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=2.25, end=2.5))  # Ab4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75))  # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=3.0))  # F4

# Drums: Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Bbm7 (Bb, Db, F, Eb) - root and fifth with chromatic approach
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375))  # Bb3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75)) # Db3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125)) # F4
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5))  # Eb4

# Piano: Bbm7 - open voicing, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375))  # Db5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375))  # F6
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375))  # Eb6
piano.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=4.125))  # Db5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125))  # F6
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125))  # Eb6

# Sax: Continue motif (Bb, F, Ab)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25))  # Bb4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5))  # F4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=3.5, end=3.75))  # Ab4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0))  # F4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25))  # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5))  # F4

# Drums: Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D7 (D, F#, A, C) - root and fifth with chromatic approach
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875))  # D4
bass.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25)) # F#4
bass.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625)) # A4
bass.notes.append(pretty_midi.Note(velocity=90, pitch=58, start=5.625, end=6.0))  # G4

# Piano: D7 - open voicing, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875))  # D5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875))  # F#5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875))  # Bb5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875))  # A5
piano.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625))  # D5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625))  # F#5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625))  # Bb5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625))  # A5

# Sax: Complete motif (D, F, Ab, end on rest)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75))  # D5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0))  # F5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=5.0, end=5.25))  # Ab5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5))  # F5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.75))  # G5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0))  # F5

# Drums: Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
