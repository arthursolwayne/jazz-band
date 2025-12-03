
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
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.5 + 0.375 * 4))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: F2 (D#) - G2 (F) - Ab2 (G#) - A2 (A), with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875))  # D#2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.25))  # F2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625))  # G#2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=39, start=2.625, end=3.0))  # A2

# Diane on piano: Fm7 (F, Ab, C, Eb) -> Bb7 (Bb, D, F, Ab) -> E7 (E, G#, B, D) -> Am7 (A, C, E, G)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875))  # F4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875))  # Ab4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.875))  # C4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875))  # Eb4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625))  # D4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625))  # F4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625))  # Ab4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0))  # E4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0))  # G#4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0))  # B4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0))  # D4

# Dante on sax: Motif - start with a short phrase, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75))  # F5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0))  # G5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25))  # A5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5))  # F5

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass: Ab2 (G#) - A2 (A) - Bb2 (A#) - Bb2 (A#), with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375))  # G#2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=39, start=3.375, end=3.75))  # A2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125))  # A#2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5))  # A#2

# Diane on piano: Bb7 (Bb, D, F, Ab) -> E7 (E, G#, B, D) -> Am7 (A, C, E, G) -> D7 (D, F#, A, C)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375))  # D4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375))  # F4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375))  # Ab4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75))  # E4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75))  # G#4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75))  # B4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75))  # D4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125))  # A4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125))  # C4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125))  # E4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125))  # G4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5))  # D4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=59, start=4.125, end=4.5))  # F#4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5))  # A4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5))  # C4

# Dante on sax: Motif continuation and resolution
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25))  # F5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5))  # G5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75))  # A5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0))  # C6
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25))  # A5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5))  # G5

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus on bass: F2 (D#) - G2 (F) - Ab2 (G#) - A2 (A), with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875))  # D#2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=37, start=4.875, end=5.25))  # F2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625))  # G#2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=39, start=5.625, end=6.0))  # A2

# Diane on piano: Fm7 (F, Ab, C, Eb) -> Bb7 (Bb, D, F, Ab) -> E7 (E, G#, B, D) -> Am7 (A, C, E, G)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875))  # F4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875))  # Ab4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875))  # C4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875))  # Eb4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625))  # D4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625))  # F4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625))  # Ab4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0))  # E4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0))  # G#4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0))  # B4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0))  # D4

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.0 + 0.375 * 4))

# Dante on sax: Motif resolution
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75))  # F5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0))  # G5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25))  # A5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5))  # F5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75))  # G5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0))  # A5

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
