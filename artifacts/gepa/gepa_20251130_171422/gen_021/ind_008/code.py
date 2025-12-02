
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Build tension with subtle rhythms and space

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))

# Bar 2: Everyone in, sax motif starts (1.5 - 3.0s)
# Saxophone motif: F - Bb - Eb - D (Bb - F - Bb - Ab)
sax.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=95, pitch=68, start=1.75, end=2.0))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25)) # Eb
sax.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.5))  # D

# Bass line: walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5))  # G#

# Piano comp: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=85, pitch=64, start=1.75, end=2.0)) # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0)) # A
piano.notes.append(pretty_midi.Note(velocity=75, pitch=69, start=1.75, end=2.0)) # Bb
piano.notes.append(pretty_midi.Note(velocity=85, pitch=72, start=2.25, end=2.5)) # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.5)) # D
piano.notes.append(pretty_midi.Note(velocity=75, pitch=76, start=2.25, end=2.5)) # Eb

# Bar 3: Continue the motif, add variations and space (3.0 - 4.5s)
# Saxophone: repeat the motif with slight variation in dynamics and timing
sax.notes.append(pretty_midi.Note(velocity=95, pitch=68, start=3.0, end=3.25))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5)) # Eb
sax.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=3.5, end=3.75))  # D
sax.notes.append(pretty_midi.Note(velocity=85, pitch=68, start=3.75, end=4.0))  # Bb

# Bass line continues with melodic walking
bass.notes.append(pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.25))  # G#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=3.25, end=3.5))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=55, start=3.5, end=3.75))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.0))  # B

# Piano comp: continue with emotion and space
piano.notes.append(pretty_midi.Note(velocity=85, pitch=64, start=3.25, end=3.5)) # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5)) # A
piano.notes.append(pretty_midi.Note(velocity=75, pitch=69, start=3.25, end=3.5)) # Bb
piano.notes.append(pretty_midi.Note(velocity=85, pitch=72, start=3.75, end=4.0)) # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.0)) # D
piano.notes.append(pretty_midi.Note(velocity=75, pitch=76, start=3.75, end=4.0)) # Eb

# Bar 4: Resolution, tension, and a hint of melody (4.5 - 6.0s)
# Saxophone: finish the motif with a small resolution
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75))  # F
sax.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=4.75, end=5.0))   # D

# Bass line: end with a melodic resolution
bass.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.75))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=55, start=4.75, end=5.0))  # Bb

# Piano comp: resolve with a final 7th chord
piano.notes.append(pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=4.75)) # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75)) # A
piano.notes.append(pretty_midi.Note(velocity=75, pitch=69, start=4.5, end=4.75)) # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=4.75, end=5.0)) # C

# Drums: continue with energy and rhythm
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')
