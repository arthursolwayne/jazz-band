
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drum notes (MIDI note numbers)
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 (0.0 - 1.5s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=1.125, end=1.5))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125))

# Bar 2: Everyone in (1.5 - 3.0s)

# Marcus: Walking bass line in Fm (F, Eb, D, C, Bb, B, C, D)
bass_notes = [53, 51, 50, 48, 45, 46, 48, 50]
for i in range(8):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=bass_notes[i], start=start, end=end))

# Diane: Comping on 2 and 4 (B7 on beat 2, C7 on beat 4)
# Fm7 = F, Ab, C, Eb
# B7 = B, D#, F#, A
# C7 = C, E, Bb, D

# Bar 2: beat 2 = B7 (B, D#, F#, A)
# Bar 2: beat 4 = C7 (C, E, Bb, D)

# Beat 2 (2.25s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625))  # D#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625))  # F#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625))  # A

# Beat 4 (3.75s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125))  # D

# Bar 3: Same structure, but Diane plays a different chord: D7 (D, F#, A, C#)
# D is a chromatic approach to the Fm key, a little dissonant, a little dangerous

# Beat 2 (4.5s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875))  # F#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875))  # C#

# Beat 4 (6.0s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=6.0, end=6.375))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.375))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.375))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.375))  # D

# Bar 3: Add the drum pattern again
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=2.625, end=3.0))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=2.625, end=3.0))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=2.25, end=2.625))

# Bar 4: Same as Bar 3, but now it's your moment

# Your sax motif: short, melodic, with space
# Motif: F (F) — Ab (Ab) — C (C) — (rest)
# Start on beat 1 (1.5s), end on beat 2 (2.25s), rest for a beat, then repeat (end on beat 4)

sax.notes.append(pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=51, start=1.875, end=2.25))  # Ab
sax.notes.append(pretty_midi.Note(velocity=110, pitch=56, start=2.625, end=2.999))  # C
sax.notes.append(pretty_midi.Note(velocity=110, pitch=56, start=3.75, end=4.125))  # C again, with space in between

# Drums again in Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=4.125, end=4.5))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=4.125, end=4.5))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=3.75, end=4.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
