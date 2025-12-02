
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in Fm, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=1.75, end=2.0))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=2.0, end=2.25))  # Gb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.5))  # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=2.75))  # Ab
bass.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=2.75, end=3.0))  # Bb

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.75))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75))  # Db

piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.5))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.5))  # Db

# Sax: Motif, start it, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.75))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=2.5, end=2.75))  # Bb

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: walking line in Fm, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.25))  # Bb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=45, start=3.25, end=3.5))  # B
bass.notes.append(pretty_midi.Note(velocity=100, pitch=46, start=3.5, end=3.75))  # C
bass.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.0))  # C#
bass.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=4.0, end=4.25))  # Db
bass.notes.append(pretty_midi.Note(velocity=100, pitch=49, start=4.25, end=4.5))  # D

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.25))  # Db

piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.0))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.0))  # Db

# Sax: Motif continuation, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25))  # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5))  # D

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375))

# Bass line: walking line in Fm, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.75))  # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=51, start=4.75, end=5.0))  # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=52, start=5.0, end=5.25))  # E
bass.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.5))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=54, start=5.5, end=5.75))  # F#
bass.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=5.75, end=6.0))  # G

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.75))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.75))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75))  # Db

piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.5))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.5))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.5))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.5))  # Db

# Sax: Motif continuation, end with a question
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0))  # C

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
