
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25))  # C#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0))   # E

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=2.0))   # D7 (D, F#, A, C)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=1.5, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=72, start=2.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=2.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=2.5, end=3.0))

# Sax: Short motif, start with a whisper, build to a cry
sax.notes.append(pretty_midi.Note(velocity=60, pitch=62, start=1.5, end=1.75))    # D (Whisper)
sax.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=1.75, end=2.0))    # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25))   # F#
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.75))  # B (Cry)
sax.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=2.75, end=3.0))    # G

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75)) # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125)) # F#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5))  # G

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.5))   # D7 (D, F#, A, C)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=3.0, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=72, start=3.5, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=3.5, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=3.5, end=4.0))

# Sax: Continue motif with space and dynamics
sax.notes.append(pretty_midi.Note(velocity=75, pitch=64, start=3.0, end=3.25))    # E
sax.notes.append(pretty_midi.Note(velocity=60, pitch=62, start=3.25, end=3.5))    # D (rest)
sax.notes.append(pretty_midi.Note(velocity=95, pitch=69, start=3.5, end=3.75))    # B
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0))   # A
sax.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=4.0, end=4.5))      # B (resolve)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=54, start=4.875, end=5.25)) # F#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625)) # Ab
bass.notes.append(pretty_midi.Note(velocity=90, pitch=58, start=5.625, end=6.0))  # A

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=5.0))   # D7 (D, F#, A, C)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=4.5, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=72, start=5.0, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=5.0, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=5.0, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=5.0, end=5.5))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0))

# Sax: Finish the motif with tension and space
sax.notes.append(pretty_midi.Note(velocity=70, pitch=64, start=4.5, end=4.75))    # E
sax.notes.append(pretty_midi.Note(velocity=50, pitch=62, start=4.75, end=5.0))    # D (rest)
sax.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.25))    # B
sax.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.5))    # A
sax.notes.append(pretty_midi.Note(velocity=75, pitch=69, start=5.5, end=6.0))     # B (hold)

# Add MIDI file
midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro.mid")
