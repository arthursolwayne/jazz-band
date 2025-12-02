
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

# Hi-hat on every eighth note
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
# Fm7 -> Ab -> G -> F (chromatic approach to F)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875))  # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0))  # F

# Diane on piano: 7th chords, comp on 2 and 4
# F7 on beat 1, Ab7 on beat 2, G7 on beat 3, F7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.625))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.625))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625))  # Eb

piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875))  # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=1.875))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=1.875))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=1.875))  # Bb

piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.125))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=2.0, end=2.125))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.125))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.125))  # D

piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375))  # Eb

# Dante on sax: short motif, make it sing, leave it hanging
# C -> Bb -> F -> (rest)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=2.0))   # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25))  # F

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass: walking line
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=3.125, end=3.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375))  # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5))  # F

# Diane on piano: 7th chords, comp on 2 and 4
# F7 on beat 1, Ab7 on beat 2, G7 on beat 3, F7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.125))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.125))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.125))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125))  # Eb

piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375))  # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.375))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.375))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.375))  # Bb

piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.625))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=3.625))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.625))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=3.5, end=3.625))  # D

piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.875))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.875))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875))  # Eb

# Dante on sax: return and finish the motif
# C -> Bb -> F -> C (resolve)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.5))   # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0))  # C

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus on bass: walking line
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=4.625, end=4.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875))  # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0))  # F

# Diane on piano: 7th chords, comp on 2 and 4
# F7 on beat 1, Ab7 on beat 2, G7 on beat 3, F7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.625))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.625))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.625))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.625))  # Eb

piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=4.875))  # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=4.875))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=4.875))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=4.875))  # Bb

piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.125))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=5.0, end=5.125))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=5.0, end=5.125))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=5.0, end=5.125))  # D

piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.375))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.375))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.375))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.375))  # Eb

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.625))

for i in range(12, 16):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
