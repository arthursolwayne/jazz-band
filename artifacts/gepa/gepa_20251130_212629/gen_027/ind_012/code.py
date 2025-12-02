
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
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

# Bar 2: Full quartet starts (1.5 - 3.0s)

# Bass - walking line in Fm (F, Gb, Ab, A)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.625))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.625, end=1.75))  # Gb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=1.875))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.0))  # A

# Piano - 7th chords on 2 and 4
# Fm7 on beat 2, Ab7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0))  # Db
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0))  # F

piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5))  # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.5))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.5))  # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5))  # G

# Sax - Melody (start with a short motif, leave it hanging)
# F (65) on beat 1, Bb (60) on beat 2, Ab (62) on beat 3, rests on beat 4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=1.875))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.125))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=3.125, end=3.25))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.375))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.5))  # Bb

# Piano - 7th chords on 2 and 4
# Ab7 on beat 2, Cm7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5))  # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=3.25, end=3.5))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=59, start=3.25, end=3.5))  # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5))  # G

piano.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.0))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.0))  # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.0))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.0))  # Bb

# Sax - continuation of melody, open-ended
# C (57) on beat 1, Eb (59) on beat 2, G (62) on beat 3, rest on beat 4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.125))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=3.25, end=3.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass - walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.625))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.625, end=4.75))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=4.875))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.0))  # Bb

# Piano - 7th chords on 2 and 4
# Cm7 on beat 2, Fm7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=4.75, end=5.0))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=4.75, end=5.0))  # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=54, start=4.75, end=5.0))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=59, start=4.75, end=5.0))  # Bb

piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.5))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5))  # Db
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5))  # F

# Sax - rest on beat 1, resolution on beat 3, leave it hanging on beat 4
# F (65) on beat 3, rest on beat 4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=4.875))

# Drums for bar 4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125))

# Hi-hat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro_wayne.mid")
