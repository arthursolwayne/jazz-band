
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drum notes: kick=36, snare=38, hihat=42
# Time signatures: 4/4, 160 BPM = 6 seconds for 4 bars

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: 0.0 - 1.5s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))  # Snare on 4

# Bar 2: 1.5 - 3.0s
# Sax takes the melody: D - E - F# - G - A - B♭ - B - A
# Mode: D Dorian (D, E, F#, G, A, Bb, B, C)
# 16th note motif, starts on D, ends on A, leaves it hanging

# D (D4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625))
# E (E4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75))
# F# (F#4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=1.875))
# G (G4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0))
# A (A4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125))
# Bb (Bb4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=2.125, end=2.25))
# B (B4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.375))
# A (A4) - ends on A, leaves it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5))

# Bass line: walking line, chromatic approaches, no repeating notes
# D - Eb - E - F - G - A - Bb - B - C - D
# Bar 2: D - Eb - E - F

# D (D2)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.625))
# Eb (Eb2)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=51, start=1.625, end=1.75))
# E (E2)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=52, start=1.75, end=1.875))
# F (F2)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.0))

# Piano: 7th chords on 2 and 4 (comp), D7, G7, A7
# Bar 2: D7 on beat 2 (1.875s)

# D7: D, F#, A, C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.0))  # F#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0))  # C (D7)

# Bar 3: 3.0 - 4.5s
# Sax: repeat the motif, but vary the rhythm slightly
# D - E - F# - G - A - B♭ - B - A again, but with syncopation

# Syncopated start
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.625))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.625, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=3.875))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.0))

# Bass: G - A - Bb - B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.125))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=3.125, end=3.25))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=58, start=3.25, end=3.375))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.5))   # B

# Piano: G7 on beat 2 (3.375s)
# G7: G, B, D, F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5))  # F (G7)

# Bar 4: 4.5 - 6.0s
# Sax: variation of the motif again, this time ending on B
# D - E - F# - G - A - B♭ - B - C

sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=4.875))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.125))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=5.125, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=5.375, end=5.5))  # C (ending on C, resolving)

# Bass: A - Bb - B - C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.625))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=58, start=4.625, end=4.75))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=59, start=4.75, end=4.875))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.0))   # C

# Piano: A7 on beat 2 (4.875s)
# A7: A, C#, E, G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.0))  # C#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.0))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0))  # G (A7)

# Drums: same pattern for bar 3 and 4

# Bar 3: 3.0 - 4.5s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))  # Snare on 4

# Bar 4: 4.5 - 6.0s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))  # Snare on 4

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
