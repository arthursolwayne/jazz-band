
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
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875)) # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25)) # F#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625)) # E
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0)) # D

# Piano: 7th chords, comp on 2 and 4 (bars 2 and 4)
# Bar 2: Comp on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375)) # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.375))

# Sax: Melody - Bar 2: First phrase
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625)) # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75)) # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=1.875)) # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0)) # D

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums: kick=36, snare=38, hihat=42
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)) # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5))

# Bass: Walking line in Fm, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375)) # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75)) # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125)) # F#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=4.125, end=4.5)) # E

# Piano: 7th chords, comp on beat 2 (bar 3)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.875)) # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=3.875))

# Sax: Melody - Bar 3: Second phrase
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25)) # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375)) # F#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625)) # D

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick=36, snare=38, hihat=42
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)) # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0))

# Bass: Walking line in Fm, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875)) # E
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25)) # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625)) # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0)) # F#

# Piano: 7th chords, comp on beat 2 (bar 4)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.375)) # F7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.375))

# Sax: Melody - Bar 4: Resolve the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625)) # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75)) # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=4.875)) # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0)) # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.125)) # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.125, end=5.25)) # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.375)) # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5)) # D

midi.instruments.extend([sax, bass, piano, drums])

midi.write("4_bar_intro.mid")
