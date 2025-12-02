
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

# Hihat on every eighth note
for i in range(8):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus (bass): walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.75))    # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=39, start=1.75, end=2.0))    # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=2.0, end=2.25))    # Gb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.5))    # Ab

# Diane (piano): 7th chords on 2 and 4
# Bar 2: 2nd beat - Bb7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=1.75, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=1.75, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=79, start=1.75, end=2.0))  # Ab

# Bar 2: 4th beat - Eb7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.5))  # Eb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5))  # G
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5))  # D

# Dante (sax): motif on bar 2
# Motif: F, Ab, Bb, rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75))   # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0))   # Ab
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25))   # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5))   # F

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus (bass): walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.25))    # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=3.25, end=3.5))    # Gb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=3.5, end=3.75))    # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=39, start=3.75, end=4.0))    # Eb

# Diane (piano): 7th chords on 2 and 4
# Bar 3: 2nd beat - Ab7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=3.25, end=3.5))  # Ab
piano.notes.append(pretty_midi.Note(velocity=80, pitch=79, start=3.25, end=3.5))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=81, start=3.25, end=3.5))  # Db
piano.notes.append(pretty_midi.Note(velocity=80, pitch=83, start=3.25, end=3.5))  # Eb

# Bar 3: 4th beat - Gb7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.0))  # Gb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.0))  # F

# Dante (sax): motif variation on bar 3
# Motif: Ab, Bb, F, rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=3.25))   # Ab
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5))   # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75))   # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0))   # F

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus (bass): walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.75))    # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=4.75, end=5.0))    # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=39, start=5.0, end=5.25))    # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.5))    # Gb

# Diane (piano): 7th chords on 2 and 4
# Bar 4: 2nd beat - Bb7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=4.75, end=5.0))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=4.75, end=5.0))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=79, start=4.75, end=5.0))  # Ab

# Bar 4: 4th beat - Eb7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5))  # Eb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5))  # G
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5))  # D

# Dante (sax): motif variation on bar 4
# Motif: Bb, rest, F, Ab
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75))   # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0))   # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=5.25, end=5.5))   # Ab

# Drums: kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125))

# Hihat on every eighth note
for i in range(8):
    start = 4.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
