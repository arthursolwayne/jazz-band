
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

# Hihat on every eighth
for i in range(0, 4):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i*0.375, end=i*0.375 + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line, chromatic approaches
# F7 chord: F, A, C, E
# Chromatic approach to F on beat 1
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625))  # E
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75))  # F

# Walking line
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0))   # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.375))  # A
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.75)) # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.125)) # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.5))  # F#
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.875))  # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.25)) # A
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.625)) # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=5.0))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.375))  # E
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.375, end=5.75)) # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0))   # G

# Piano - 7th chords, comp on 2 and 4
# F7: F, A, C, E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0))   # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0))   # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=1.75, end=2.0))   # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=1.75, end=2.0))   # E

# D7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.375))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=2.0, end=2.375))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=2.0, end=2.375))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=84, start=2.0, end=2.375))  # C#

# G7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=3.5, end=3.875))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=83, start=3.5, end=3.875))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=85, start=3.5, end=3.875))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=88, start=3.5, end=3.875))  # F#

# C7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.625)) # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=4.25, end=4.625)) # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=4.25, end=4.625)) # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=83, start=4.25, end=4.625)) # B

# F7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.375, end=5.75)) # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=5.375, end=5.75)) # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=5.375, end=5.75)) # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=5.375, end=5.75)) # E

# Sax - short motif, make it sing
# F7: F, A, C, E

# Bar 2: Start with F (beat 1)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75))  # F

# Bar 2: A (beat 2)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.125))  # A

# Bar 2: C (beat 3)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=2.5, end=2.625))  # C

# Bar 2: E (beat 4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.125))  # E

# Bar 3: F (beat 1)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75))  # F

# Bar 3: A (beat 2)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.0, end=4.125))  # A

# Bar 3: C (beat 3)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.625))  # C

# Bar 4: E (beat 4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=5.5, end=5.75))  # E

# Drums: Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.125, end=3.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.25, end=4.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.375, end=5.5))

# Hihat on every eighth
for i in range(4, 16):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i*0.375, end=i*0.375 + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
