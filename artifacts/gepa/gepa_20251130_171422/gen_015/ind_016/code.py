
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75))  # Hihat on 1 & 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5))   # Hihat on 2 & 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))  # Kick on 3

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax starts the melody, with space and tension
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75))  # Fm7 - F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0))  # Eb
sax.notes.append(pretty_midi.Note(velocity=105, pitch=60, start=2.0, end=2.25))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75))  # G
sax.notes.append(pretty_midi.Note(velocity=105, pitch=64, start=2.75, end=3.0))  # F

# Bass line (walking line, chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.75))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=1.75, end=2.0))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.25))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.5))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=2.5, end=2.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=2.75, end=3.0))  # D

# Piano comping (7th chords, on 2 and 4)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0))  # F7 - F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=1.75, end=2.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0))  # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=2.75, end=3.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0))  # Eb

# Drums continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 4):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i * 1.5, end=1.5 + i * 1.5 + 0.375))  # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5 + i * 1.5 + 0.75, end=1.5 + i * 1.5 + 1.125))  # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i * 1.5 + 1.125, end=1.5 + i * 1.5 + 1.5))  # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5 + i * 1.5, end=1.5 + i * 1.5 + 1.5))  # Hihat on 1 & 2 & 3 & 4

# Bar 3: Continue with tension and space (3.0 - 4.5s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5))  # Eb
sax.notes.append(pretty_midi.Note(velocity=105, pitch=60, start=3.5, end=3.75))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25))  # G
sax.notes.append(pretty_midi.Note(velocity=105, pitch=64, start=4.25, end=4.5))  # F

# Bass line (walking line, chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.25))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=3.25, end=3.5))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.75))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.0))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=4.0, end=4.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=4.25, end=4.5))  # D

# Piano comping (7th chords, on 2 and 4)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5))  # F7 - F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=3.25, end=3.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5))  # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=4.25, end=4.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5))  # Eb

# Bar 4: Full resolution (4.5 - 6.0s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25))  # F
sax.notes.append(pretty_midi.Note(velocity=105, pitch=62, start=5.25, end=5.5))  # Eb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=5.75, end=6.0))  # G

# Bass line (walking line, chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.75))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=4.75, end=5.0))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.25))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.5))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=5.5, end=5.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=5.75, end=6.0))  # D

# Piano comping (7th chords, on 2 and 4)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0))  # F7 - F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=4.75, end=5.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0))  # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=5.75, end=6.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=6.0))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=6.0))  # Eb

# Final drum fill
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.75))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.75, end=6.0))    # Snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0))  # Hihat on 3 & 4

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
