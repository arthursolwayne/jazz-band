
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Little Ray alone
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))

# Bar 2 (1.5 - 3.0s): Full quartet enters
# Bass: Walking line with chromatic approach
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=1.5, end=1.875))  # Fm root
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25)) # b9
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)) # 7
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0))  # b13

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875))  # Db
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625)) # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625)) # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625)) # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625)) # Db

# Sax: Motif, start it, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25)) # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0))  # G

# Bar 3 (3.0 - 4.5s): Continue with tension and release
# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5))

# Bass: Walking line with chromatic approach
bass.notes.append(pretty_midi.Note(velocity=100, pitch=37, start=3.0, end=3.375))  # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)) # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)) # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=4.125, end=4.5))  # F

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375))  # Db
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125)) # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125)) # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125)) # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125)) # Db

# Sax: Continue motif, build tension
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75)) # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5))  # G

# Bar 4 (4.5 - 6.0s): End with a question, not a statement
# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))    # Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0))

# Bass: Walking line with chromatic approach
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875))  # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=4.875, end=5.25)) # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)) # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=37, start=5.625, end=6.0))  # D

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875))  # Db
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625)) # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625)) # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625)) # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625)) # Db

# Sax: End with a question, not a statement
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25)) # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0))  # G (with a slight rest before the last note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("4_bar_intro.mid")
