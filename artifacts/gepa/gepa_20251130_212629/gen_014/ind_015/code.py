
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
# Dm7 -> G7 -> Cmaj7 -> F7 (no chord names, just notes)
# D - F - G - A
# G - Bb - B - C
# C - Eb - F - G
# F - Ab - A - Bb

# Bar 2
bass.notes.append(pretty_midi.Note(velocity=60, pitch=62, start=1.5, end=1.75))  # D
bass.notes.append(pretty_midi.Note(velocity=60, pitch=64, start=1.75, end=2.0))  # F
bass.notes.append(pretty_midi.Note(velocity=60, pitch=65, start=2.0, end=2.25))  # G
bass.notes.append(pretty_midi.Note(velocity=60, pitch=67, start=2.25, end=2.5))  # A

# Bar 3
bass.notes.append(pretty_midi.Note(velocity=60, pitch=67, start=2.5, end=2.75))  # G
bass.notes.append(pretty_midi.Note(velocity=60, pitch=69, start=2.75, end=3.0))  # Bb
bass.notes.append(pretty_midi.Note(velocity=60, pitch=71, start=3.0, end=3.25))  # B
bass.notes.append(pretty_midi.Note(velocity=60, pitch=72, start=3.25, end=3.5))  # C

# Bar 4
bass.notes.append(pretty_midi.Note(velocity=60, pitch=72, start=3.5, end=3.75))  # C
bass.notes.append(pretty_midi.Note(velocity=60, pitch=74, start=3.75, end=4.0))  # Eb
bass.notes.append(pretty_midi.Note(velocity=60, pitch=76, start=4.0, end=4.25))  # F
bass.notes.append(pretty_midi.Note(velocity=60, pitch=77, start=4.25, end=4.5))  # G

# Piano: comp on 2 and 4, 7th chords
# Dm7: D, F, A, C
# G7: G, Bb, D, F
# Cmaj7: C, E, G, B
# F7: F, A, C, Eb

# Bar 2 (comp on 2)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0))  # C

# Bar 3 (comp on 2)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=2.75, end=3.0))  # F

# Bar 4 (comp on 2)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.0))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.0))  # B

# Sax: short motif, start it, leave it hanging, finish it
# Dm7: D, F, G, A => D, F, G, rest
# Then G, Bb, rest, rest => end on Bb

# Bar 2
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875))  # G
# Leave A out

# Bar 3
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.625))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.75))  # Bb
# Rest the rest of the bar

# Bar 4
# Rest the first two beats
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.125))  # Bb
# Leave the last two beats open, hanging

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=1.875))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.625, end=1.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0))

# Bar 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=2.5, end=2.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=2.875))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0))

# Bar 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=3.5, end=3.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
