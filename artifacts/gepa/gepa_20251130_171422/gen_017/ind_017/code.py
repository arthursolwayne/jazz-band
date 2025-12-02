
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth, but with space
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875))  # Snare on 4 (but cut short for space)

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif: Fm7 -> Ab -> Eb -> Gb (Fm scale, resolve to Bb)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0))   # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25))  # Eb
sax.notes.append(pretty_midi.Note(velocity=85, pitch=61, start=2.25, end=2.5))   # Gb (half note)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75))  # F (repeat)
sax.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0))   # Ab

# Bass: Walking line, chromatic approaches, Fm7 -> Ab7 -> Eb7 -> Gm7
bass.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.75))  # F
bass.notes.append(pretty_midi.Note(velocity=75, pitch=35, start=1.75, end=2.0))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=37, start=2.0, end=2.25))  # F
bass.notes.append(pretty_midi.Note(velocity=75, pitch=39, start=2.25, end=2.5))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=2.5, end=2.75))  # Ab
bass.notes.append(pretty_midi.Note(velocity=75, pitch=38, start=2.75, end=3.0))  # G

# Piano: 7th chords, comp on 2 and 4, with emotional shading
# Fm7 on 1, Ab7 on 2, Eb7 on 3, Gm7 on 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0))   # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=60, start=1.5, end=2.0))   # Ab
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=2.0))   # C
piano.notes.append(pretty_midi.Note(velocity=75, pitch=61, start=1.5, end=2.0))   # Db
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.5))   # Ab
piano.notes.append(pretty_midi.Note(velocity=85, pitch=65, start=2.0, end=2.5))   # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.5))   # Eb
piano.notes.append(pretty_midi.Note(velocity=75, pitch=66, start=2.0, end=2.5))   # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=3.0))   # Bb
piano.notes.append(pretty_midi.Note(velocity=85, pitch=66, start=2.5, end=3.0))   # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=3.0))   # F
piano.notes.append(pretty_midi.Note(velocity=75, pitch=63, start=2.5, end=3.0))   # Eb

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone motif: Repeat with slight variation and dynamic change
sax.notes.append(pretty_midi.Note(velocity=105, pitch=64, start=3.0, end=3.25))  # F
sax.notes.append(pretty_midi.Note(velocity=95, pitch=60, start=3.25, end=3.5))   # Ab
sax.notes.append(pretty_midi.Note(velocity=105, pitch=62, start=3.5, end=3.75))  # Eb
sax.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=4.0))   # Gb (half note)
sax.notes.append(pretty_midi.Note(velocity=105, pitch=64, start=4.0, end=4.25))  # F (repeat)
sax.notes.append(pretty_midi.Note(velocity=95, pitch=60, start=4.25, end=4.5))   # Ab

# Bass: Continue walking line, chromatic approaches with a slight shift
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.25))  # Ab
bass.notes.append(pretty_midi.Note(velocity=75, pitch=38, start=3.25, end=3.5))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=3.5, end=3.75))  # Ab
bass.notes.append(pretty_midi.Note(velocity=75, pitch=42, start=3.75, end=4.0))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=4.0, end=4.25))  # B
bass.notes.append(pretty_midi.Note(velocity=75, pitch=42, start=4.25, end=4.5))  # Bb

# Piano: Continue comping, emotional tension
# Ab7 on 1, Eb7 on 2, Gm7 on 3, Fm7 on 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.5))   # Ab
piano.notes.append(pretty_midi.Note(velocity=85, pitch=65, start=3.0, end=3.5))   # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.5))   # Eb
piano.notes.append(pretty_midi.Note(velocity=75, pitch=66, start=3.0, end=3.5))   # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=4.0))   # Bb
piano.notes.append(pretty_midi.Note(velocity=85, pitch=66, start=3.5, end=4.0))   # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.5, end=4.0))   # F
piano.notes.append(pretty_midi.Note(velocity=75, pitch=63, start=3.5, end=4.0))   # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.5))   # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=60, start=4.0, end=4.5))   # Ab
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.5))   # C
piano.notes.append(pretty_midi.Note(velocity=75, pitch=61, start=4.0, end=4.5))   # Db

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone motif: End with a resolution, a slight delay before the final note
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75))  # F
sax.notes.append(pretty_midi.Note(velocity=95, pitch=60, start=4.75, end=5.0))   # Ab
sax.notes.append(pretty_midi.Note(velocity=105, pitch=62, start=5.0, end=5.25))  # Eb
sax.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.75))  # Gb (half note)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0))  # F (repeat)

# Bass: Resolve to a strong root
bass.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.75))  # F
bass.notes.append(pretty_midi.Note(velocity=75, pitch=35, start=4.75, end=5.0))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=5.0, end=5.25))  # F
bass.notes.append(pretty_midi.Note(velocity=75, pitch=38, start=5.25, end=5.5))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=5.5, end=5.75))  # F
bass.notes.append(pretty_midi.Note(velocity=75, pitch=34, start=5.75, end=6.0))  # D

# Piano: Final comp, a strong resolution with emotional weight
# Fm7 on 1, Ab7 on 2, Eb7 on 3, Gm7 on 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=5.0))   # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.0))   # Ab
piano.notes.append(pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=5.0))   # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=5.0))   # Db
piano.notes.append(pretty_midi.Note(velocity=95, pitch=68, start=5.0, end=5.5))   # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.5))   # C
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=5.0, end=5.5))   # Eb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=5.0, end=5.5))   # D
piano.notes.append(pretty_midi.Note(velocity=95, pitch=64, start=5.5, end=6.0))   # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=6.0))   # Ab
piano.notes.append(pretty_midi.Note(velocity=85, pitch=62, start=5.5, end=6.0))   # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=5.5, end=6.0))   # Db

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("waynes_moment.mid")
