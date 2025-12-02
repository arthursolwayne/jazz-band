
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
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=2.25))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (F2, G2, A2, B2, C3, D3, E3, F3)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=1.5, end=1.875))  # F2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=79, start=1.875, end=2.25))  # G2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=81, start=2.25, end=2.625))  # A2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=83, start=2.625, end=3.0))  # B2

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=89, start=1.5, end=3.0))

# Sax: Motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875))  # F4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.25))  # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.625))  # A4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0))   # F4 (hanging)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=84, start=3.0, end=3.375))  # C3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=86, start=3.375, end=3.75))  # D3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=88, start=3.75, end=4.125))  # E3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=4.125, end=4.5))   # F2

# Piano: Different chord, C7 (C, E, G, Bb)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=89, start=3.0, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=92, start=3.0, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=4.5))

# Sax: Motif again (variation)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375))  # F4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75))  # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=76, start=3.75, end=4.125))  # A4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.5))   # F4 (hanging)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=79, start=4.5, end=4.875))  # G2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=81, start=4.875, end=5.25))  # A2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=83, start=5.25, end=5.625))  # B2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=84, start=5.625, end=6.0))   # C3

# Piano: Different chord, Gm7 (G, Bb, D, F)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0))

# Sax: Finish the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875))  # F4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25))  # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.625))  # A4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=77, start=5.625, end=6.0))   # Bb4 (resolve)

# Drums: Continue pattern
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
