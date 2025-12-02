
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Dm7 walking line with chromatic approaches
# D - C - Eb - F - D - C - Eb - F (bar 2)
# F - E - G - A - F - E - G - A (bar 3)
# A - G - Bb - B - A - G - Bb - B (bar 4)

# Bar 2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=1.625, end=1.75))  # C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=1.875))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0))   # F

# Bar 3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.125))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=2.125, end=2.25))  # E
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.375, end=2.5))   # A

# Bar 4
bass.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.625))  # A
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=2.875))  # Bb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=2.875, end=3.0))   # B

# Piano: Dm7 chords on 2 and 4
# Dm7: D - F - A - C
# Bar 2 (1.5 - 2.0s)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0))  # C

# Bar 3 (2.0 - 2.5s)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5))  # C

# Bar 4 (2.5 - 3.0s)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0))  # C

# Saxophone: Dm7 melody, one short motif, make it sing
# D - F - A - C (bar 2)
# D - F - A - C (bar 3)
# D - F - A - C (bar 4)

# Bar 2
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.0))   # C

# Bar 3
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.125))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=2.125, end=2.25))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.375))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=2.375, end=2.5))   # C

# Bar 4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.625))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=2.875))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=2.875, end=3.0))   # C

# Add the drums to the MIDI
# Bars 2-4: Drums continue with same pattern
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.875, end=4.0))

# Hi-hat on every eighth
for i in range(4, 8):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
