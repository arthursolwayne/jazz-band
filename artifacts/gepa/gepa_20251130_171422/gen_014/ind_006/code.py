
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0))  # C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=2.0, end=2.25))  # D#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0))  # A

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.75))  # G7
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=1.75))  # B
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=1.5, end=1.75))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=1.5, end=1.75))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.5))  # B
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=2.25, end=2.5))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=2.25, end=2.5))  # F

# Sax: Motif, start it, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25))  # G#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75))  # G#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0))  # A

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25))  # B
bass.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5))  # C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.75))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0))  # E
bass.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=4.0, end=4.25))  # F#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=79, start=4.25, end=4.5))  # A

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.25))  # B7
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=3.0, end=3.25))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=3.0, end=3.25))  # E
piano.notes.append(pretty_midi.Note(velocity=85, pitch=79, start=3.0, end=3.25))  # G
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=3.75, end=4.0))  # B
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=3.75, end=4.0))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=3.75, end=4.0))  # E
piano.notes.append(pretty_midi.Note(velocity=85, pitch=79, start=3.75, end=4.0))  # G

# Sax: Motif, continue and finish it
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25))  # B
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75))  # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.0))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=4.0, end=4.25))  # F#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=4.25, end=4.5))  # A

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375))

# Bass: walking line, chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.75))  # A
bass.notes.append(pretty_midi.Note(velocity=90, pitch=81, start=4.75, end=5.0))  # B
bass.notes.append(pretty_midi.Note(velocity=90, pitch=83, start=5.0, end=5.25))  # C#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=85, start=5.25, end=5.5))  # D#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=87, start=5.5, end=5.75))  # E#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=89, start=5.75, end=6.0))  # F#

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=85, pitch=79, start=4.5, end=4.75))  # A7
piano.notes.append(pretty_midi.Note(velocity=85, pitch=82, start=4.5, end=4.75))  # C
piano.notes.append(pretty_midi.Note(velocity=85, pitch=84, start=4.5, end=4.75))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=87, start=4.5, end=4.75))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=79, start=5.25, end=5.5))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=82, start=5.25, end=5.5))  # C
piano.notes.append(pretty_midi.Note(velocity=85, pitch=84, start=5.25, end=5.5))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=87, start=5.25, end=5.5))  # F

# Sax: Motif, finish it with a rest and a final note
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.75))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=4.75, end=5.0))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=84, start=5.0, end=5.25))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=87, start=5.25, end=5.5))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=89, start=5.5, end=5.75))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=84, start=5.75, end=6.0))  # D

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
