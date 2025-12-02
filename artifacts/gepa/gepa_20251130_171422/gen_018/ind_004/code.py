
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
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375))  # Hihat on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125))  # Hihat on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))  # Snare on 4

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75))  # F# (Motif start)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0))  # A (Motif continuation)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25))  # F# (Motif continuation)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5))  # E (Motif continuation)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75))  # F#
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=3.0))  # A

# Bass: Walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=1.5, end=1.75))  # F (root)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=2.0))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.25))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.5))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=2.5, end=2.75))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=3.0))  # F#

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75))  # C#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.75))  # A (7th)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5))  # C#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.5))  # A (7th)

# Drums: Full bar
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875))  # Hihat on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.5))   # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.5))   # Hihat on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.875)) # Hihat on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.25))   # Snare on 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.25))   # Hihat on 4

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif with variation
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25))  # F# (Motif start)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5))  # A (Motif continuation)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75))  # F# (Motif continuation)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0))  # E (Motif continuation)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25))  # F#
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5))  # A

# Bass: Walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.25))  # F (root)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.5))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=3.5, end=3.75))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.0))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=4.0, end=4.25))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.5))  # F#

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25))  # C#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.25))  # A (7th)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0))  # C#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0))  # A (7th)

# Drums: Full bar
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375))  # Hihat on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.0))   # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.0))   # Hihat on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.375)) # Hihat on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.75))   # Snare on 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.75))   # Hihat on 4

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with resolution
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75))  # F# (Motif start)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0))  # A (Motif continuation)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25))  # F# (Motif continuation)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5))  # E (Motif continuation)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75))  # F#
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0))  # A

# Bass: Walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.75))  # F (root)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=5.0))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=5.0, end=5.25))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.5))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=5.5, end=5.75))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=6.0))  # F#

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75))  # C#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.75))  # A (7th)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5))  # C#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.5))  # A (7th)

# Drums: Full bar
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875))  # Hihat on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.5))   # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.5))   # Hihat on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.875)) # Hihat on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.25))   # Snare on 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.25))   # Hihat on 4

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
