
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))   # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.375, end=1.75)) # Snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))  # Hihat on every 8th

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (Fm root)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875)) # F2 on 1
# Piano: Fm7 (F, Ab, C, Eb)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75)) # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75)) # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75)) # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75)) # Eb
# Sax: Motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)) # G (Fm3)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25)) # E (Fm7)
# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=2.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=3.125)) # Snare on 4

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Ab2 (Fm b7)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=3.375)) # Ab2 on 1
# Piano: Bb7 (Bb, D, F, Ab)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.25)) # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25)) # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25)) # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25)) # Ab
# Sax: Motif continuation
sax.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375)) # F (Fm root)
# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.625)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.375, end=4.75)) # Snare on 4

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: C2 (Fm 5)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875)) # C2 on 1
# Piano: Dm7 (D, F, Ab, C)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75)) # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75)) # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75)) # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.75)) # C
# Sax: Motif resolution
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)) # G (Fm3)
# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=5.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.25)) # Snare on 4

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
