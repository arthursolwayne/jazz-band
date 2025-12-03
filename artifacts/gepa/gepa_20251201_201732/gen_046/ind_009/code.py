
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: One short motif, start it, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.5))  # G4

# Bass: Walking line, roots and fifths with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875))  # D3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25))  # F#3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625)) # F3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0))  # A3

# Piano: Open voicings, different chord each bar, resolve on the last
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0))  # C4 (root)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0))  # E4 (3rd)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0))  # G4 (5th)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0))  # B4 (7th)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif, resolve
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375))  # B4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125))  # G4

# Bass: Walking line
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375))  # A3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75))  # B3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125))  # A3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5))  # D3

# Piano: Different chord, resolve on the last
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5))  # B4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5))  # C#5

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875))  # F#4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625))  # D4

# Bass: Walking line
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875))  # D3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25))  # F#3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625))  # F3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0))  # A3

# Piano: Resolve on the last chord
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0))  # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0))  # E4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0))  # B4

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
