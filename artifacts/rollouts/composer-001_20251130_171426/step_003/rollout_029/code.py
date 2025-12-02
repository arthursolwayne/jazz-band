
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)) # Snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)) # Hihat on every 8th

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Fm walking line
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=1.875)) # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25)) # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625)) # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0))  # F

# Piano: F7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=2.25)) # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=2.25)) # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=2.25)) # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=2.25)) # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=2.25)) # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=2.25)) # Eb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.375)) # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=3.375)) # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=3.375)) # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.375)) # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.375)) # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.375)) # Eb

# Drums: Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)) # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)) # Snare on 4

# Sax: Motif (start on bar 2)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)) # Gm7
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25)) # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625)) # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0))  # F

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Fm walking line
bass.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375)) # Bb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)) # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125)) # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5))  # Eb

# Piano: F7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.75)) # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.75)) # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.75)) # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.75)) # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.75)) # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.75)) # Eb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.875)) # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.875)) # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.875)) # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.875)) # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.875)) # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.875)) # Eb

# Drums: Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)) # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)) # Snare on 4

# Sax: Motif (Bar 3)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75)) # Gm7
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125)) # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5))  # G

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Fm walking line
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875)) # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=4.875, end=5.25)) # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)) # C
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0))  # F

# Piano: F7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=5.25)) # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=5.25)) # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=5.25)) # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=5.25)) # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=5.25)) # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=5.25)) # Eb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.375)) # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=5.625, end=6.375)) # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=6.375)) # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.375)) # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.375)) # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.375)) # Eb

# Drums: Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)) # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)) # Snare on 4

# Sax: Motif (Bar 4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25)) # Gm7
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625)) # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0))  # G

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
